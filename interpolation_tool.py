import os
import glob
import numpy as np
import pandas as pd
import scipy.interpolate as interp
import matplotlib.pyplot as plt
import pickle
import sys

# ==========================================================
# === 🛠️ CONFIGURATION START ===
# ==========================================================
INPUT_DATA_FOLDER = "Spectra_Data_sfdm_2b2tau_r0.1"   # 데이터 폴더
CHANNEL_NAME = "2b2tau"                     # 채널 이름

# 1. 한 번에 처리할 입자 목록
PARTICLE_TYPES = ["photon", "positron", "antiproton"]

# 2. 보간 범위 확장
# x = E / m_DM. 1 TeV DM의 1e-9는 1 keV 수준이므로 충분히 넓습니다.
X_MIN = 1e-10 
X_MAX = 1.0
X_POINTS = 5000  # 그리드 포인트 수

# ==========================================================
# === 🛠️ CONFIGURATION END ===
# ==========================================================

class SpectrumInterpolator:
    def __init__(self, data_folder, particle, channel, x_min=1e-5, x_max=1.0, n_points=500):
        self.data_folder = data_folder
        self.particle = particle
        self.channel = channel
        self.masses = []
        self.spectrum_matrix = []
        
        # [수정] 공통 x축 범위 확장 설정 적용
        self.common_x = np.logspace(np.log10(x_min), np.log10(x_max), n_points)
        
        self._load_data()
        self._build_interpolator()

    def _get_mass_from_filename(self, fname):
        try:
            basename = os.path.basename(fname)
            start = basename.find('mpsi') + 4
            end = basename.find('GeV')
            return float(basename[start:end])
        except:
            return None

    def _load_data(self):
        file_pattern = os.path.join(self.data_folder, f"*{self.channel}_{self.particle}.csv")
        files = glob.glob(file_pattern)
        
        if not files:
            # 해당 입자의 데이터가 아예 없으면 에러 대신 빈 상태로 둠 (처리 로직에서 스킵)
            print(f"⚠️ 경고: '{self.particle}' 데이터가 없습니다. 스킵합니다.")
            return

        files.sort(key=self._get_mass_from_filename)
        
        temp_masses = []
        temp_spectra = []

        print(f"  🔄 데이터 로딩 중... ({len(files)} files)")

        for f in files:
            mass = self._get_mass_from_filename(f)
            if mass is None: continue
            
            df = pd.read_csv(f)
            
            # 유효 데이터 필터링
            mask = (df['x'] > 0) & (df['dNdx'] > 0)
            x_data = df.loc[mask, 'x'].values
            y_data = df.loc[mask, 'dNdx'].values
            
            if len(x_data) < 5: continue 

            # 1차 보간 (Log-Log)
            # fill_value="extrapolate" 덕분에 범위 밖도 데이터 경향 따라 확장됨
            f_interp = interp.interp1d(np.log10(x_data), np.log10(y_data), 
                                       kind='linear', fill_value="extrapolate")
            
            y_interp = 10 ** f_interp(np.log10(self.common_x))
            y_interp = np.nan_to_num(y_interp, nan=1e-30) 

            temp_masses.append(mass)
            temp_spectra.append(y_interp)

        if not temp_masses:
            print(f"⚠️ 경고: 유효한 데이터가 하나도 없습니다.")
            return

        self.masses = np.array(temp_masses)
        self.spectrum_matrix = np.array(temp_spectra)
        print(f"  ✅ 로드 완료: {len(self.masses)} masses loaded.")

    def _build_interpolator(self):
        if len(self.masses) == 0: return

        log_spectrum = np.log10(np.maximum(self.spectrum_matrix, 1e-30))
        self.interp_func = interp.RectBivariateSpline(
            np.log10(self.masses), 
            np.log10(self.common_x), 
            log_spectrum,
            kx=1, ky=1
        )

    def get_spectrum(self, mass, x_array=None):
        if len(self.masses) == 0: return None

        if x_array is None:
            x_array = self.common_x
            
        # 범위 경고 (너무 과도한 외삽 방지)
        if mass < self.masses.min() or mass > self.masses.max():
            print(f"    ⚠️ 질량 범위 외삽: {mass:.1f} GeV")

        log_m = np.log10(mass)
        log_x = np.log10(x_array)
        log_y_pred = self.interp_func(log_m, log_x)[0] 
        return 10 ** log_y_pred


# --- 메인 실행 루프 (일괄 처리) ---
if __name__ == "__main__":
    print(f"🚀 일괄 보간 작업 시작: {CHANNEL_NAME} 채널")
    print(f"   입자 목록: {PARTICLE_TYPES}")
    print(f"   보간 범위: x = {X_MIN} ~ {X_MAX}\n")

    for p_type in PARTICLE_TYPES:
        print(f"==========================================")
        print(f"🧩 처리 중: [{p_type.upper()}]")
        
        # 1. 보간기 생성
        try:
            interpolator = SpectrumInterpolator(INPUT_DATA_FOLDER, p_type, CHANNEL_NAME, 
                                                x_min=X_MIN, x_max=X_MAX, n_points=X_POINTS)
        except Exception as e:
            print(f"❌ 에러 발생 ({p_type}): {e}")
            continue

        # 데이터가 없으면 다음 입자로 넘어감
        if len(interpolator.masses) == 0:
            print(f"❌ {p_type} 데이터가 없어 건너뜁니다.")
            continue

        # 2. Pickle 저장
        pkl_filename = f"interpolator_{CHANNEL_NAME}_{p_type}.pkl"
        pkl_save_path = os.path.join(INPUT_DATA_FOLDER, pkl_filename)
        
        with open(pkl_save_path, "wb") as f:
            pickle.dump(interpolator, f)
        print(f"  💾 객체 저장됨: {pkl_filename}")

        # 3. 검증 그래프 그리기
        # 테스트 질량 (데이터 범위 내)
        test_mass = interpolator.masses.max() * 0.9
        if test_mass > interpolator.masses.max(): test_mass = interpolator.masses.max()
        
        test_x = np.logspace(np.log10(X_MIN), 0, 100)
        pred_y = interpolator.get_spectrum(test_mass, test_x)
        
        # 실제 데이터 비교
        closest_idx = np.argmin(np.abs(interpolator.masses - test_mass))
        closest_mass = interpolator.masses[closest_idx]
        raw_file = os.path.join(INPUT_DATA_FOLDER, f"MM_mpsi{closest_mass:.2f}GeV_{CHANNEL_NAME}_{p_type}.csv")
        
        plt.figure(figsize=(10, 6))
        plt.plot(test_x, pred_y, 'b--', lw=2, label=f'Interpolated ($m={test_mass:.1f}$)')
        
        if os.path.exists(raw_file):
            df_raw = pd.read_csv(raw_file)
            mask = df_raw['x'] > 0
            # Raw Data 점 찍기
            plt.plot(df_raw.loc[mask, 'x'], df_raw.loc[mask, 'dNdx'], 'k.', markersize=4, alpha=0.5,
                     label=f'Raw Data ($m={closest_mass:.1f}$)')

        plt.xscale('log')
        plt.yscale('log')
        plt.xlim(X_MIN, 1.0) # 확장된 범위 적용
        #plt.ylim(1e-2, 1e5)
        plt.xlabel(r'$x = E/m_{\chi}$', fontsize=12)
        plt.ylabel(r'$dN/dx$', fontsize=12)
        plt.title(f"Interpolation Check: {CHANNEL_NAME} - {p_type}")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        png_filename = f"interpolation_test_{CHANNEL_NAME}_{p_type}.png"
        png_path = os.path.join(INPUT_DATA_FOLDER, png_filename)
        plt.savefig(png_path, dpi=100)
        plt.close()
        print(f"  📊 그래프 저장됨: {png_filename}")

    print("\n🎉 모든 작업이 완료되었습니다!")
