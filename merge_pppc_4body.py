import pandas as pd
import numpy as np
import pickle
import os
import sys

# ==========================================================
# === 🛠️ USER CONFIGURATION ===
# ==========================================================
Spectrum = "photon" # photon(gammas), positron(s), antiproton(s)
Ratio = 0.1

PPPC_FILE = f"AtProduction_{Spectrum}.dat" 
#OUTPUT_FILE = f"AtProduction_{Spectrum}_sfdm_4body_extended.dat"
OUTPUT_FILE = f"AtProduction_{Spectrum}_sfdm_4body_extended_r{Ratio}.dat" # ratio version

# Interpolator 경로 : sfdm_4b,4tau,2b2tau_r0.1,0.3,0.5,0.7,1.0
INTERPOLATOR_PATHS = {
    "4b":     f"Spectra_Data_sfdm_4b_r{Ratio}/interpolator_4b_{Spectrum}.pkl",
    "4tau":   f"Spectra_Data_sfdm_4tau_r{Ratio}/interpolator_4tau_{Spectrum}.pkl",
    "2b2tau": f"Spectra_Data_sfdm_2b2tau_r{Ratio}/interpolator_2b2tau_{Spectrum}.pkl"
}

# ==========================================================
# === 🏗️ CLASS DEFINITION ===
# ==========================================================
class SpectrumInterpolator:
    def __init__(self, data_folder, particle, channel, x_min=1e-5, x_max=1.0, n_points=500):
        self.data_folder = data_folder
        self.particle = particle
        self.channel = channel
        self.masses = []
        self.spectrum_matrix = []
        self.common_x = np.logspace(np.log10(x_min), np.log10(x_max), n_points)
        
    def get_spectrum(self, mass, x_array=None):
        is_scalar = False
        if x_array is None:
            x_array = self.common_x
        elif np.isscalar(x_array):
            is_scalar = True
            x_array = np.array([x_array])

        if hasattr(self, 'masses') and len(self.masses) > 0:
            if mass < self.masses.min() or mass > self.masses.max():
                return 0.0 if is_scalar else np.zeros_like(x_array)

        log_m = np.log10(mass)
        log_x = np.log10(x_array)
        
        try:
            log_y_pred = self.interp_func(log_m, log_x)
            if log_y_pred.ndim > 1:
                log_y_pred = log_y_pred[0][0]
            elif log_y_pred.ndim == 1:
                log_y_pred = log_y_pred[0]
            res = 10 ** log_y_pred
            return float(res) if is_scalar else res
        except Exception:
            return 0.0 if is_scalar else np.zeros_like(x_array)

# ==========================================================
# === 🚀 MAIN LOGIC ===
# ==========================================================

def main():
    print(f"🔄 PPPC 파일 로딩 및 정리 중: {PPPC_FILE}")
    
    try:
        # 1. 일단 모든 데이터를 문자열(dtype=str)로 읽어서 포맷 오류 방지
        df_raw = pd.read_csv(PPPC_FILE, sep=r'\s+', header=None, dtype=str)
        
        # 2. 'mDM'이라는 글자가 포함된 행을 찾아서 헤더로 설정
        # (첫 번째 열[0]에서 'mDM'을 찾음)
        header_mask = df_raw[0].str.contains('mDM', case=False, na=False)
        
        if header_mask.any():
            # 헤더 행의 인덱스 찾기
            header_idx = header_mask.idxmax()
            print(f"   ℹ️ 헤더 발견 (Line {header_idx})")
            
            # 컬럼 이름 설정
            df_raw.columns = df_raw.iloc[header_idx]
            
            # 헤더 행과 그 위의 잡다한 행들 제거, 순수 데이터만 남김
            df_data = df_raw.iloc[header_idx+1:].copy()
        else:
            print("   ⚠️ 헤더('mDM')를 찾을 수 없습니다. 첫 줄부터 데이터로 간주합니다.")
            df_data = df_raw.copy()
            # 컬럼 이름이 없으므로 임의 지정 (나중에 저장 시 문제될 수 있음)
            df_data.columns = ["mDM", "Log[10,x]"] + [f"Col_{i}" for i in range(2, df_data.shape[1])]

        # 3. 데이터 프레임을 숫자로 변환 (에러 발생 시 NaN 처리 후 제거)
        # 이 과정에서 'mDM' 같은 문자가 섞여 있어도 안전하게 걸러집니다.
        df_data = df_data.apply(pd.to_numeric, errors='coerce')
        
        # NaN이 있는 행(숫자가 아닌 행) 삭제
        original_len = len(df_data)
        df_data = df_data.dropna(subset=[df_data.columns[0], df_data.columns[1]])
        
        if len(df_data) < original_len:
            print(f"   🧹 숫자가 아닌 행 {original_len - len(df_data)}개 제거됨 (헤더 또는 빈 줄)")
        
        print(f"✅ 데이터 정리 완료: {len(df_data)} rows")

    except Exception as e:
        print(f"❌ 파일 읽기 실패: {e}")
        return

    # mDM, Log10x 값 추출 (이제 무조건 float임이 보장됨)
    masses = df_data.iloc[:, 0].values
    log10x = df_data.iloc[:, 1].values
    x_vals = 10 ** log10x

    # 4. 채널별 데이터 병합
    for channel_name, pkl_path in INTERPOLATOR_PATHS.items():
        print(f"🧩 Processing channel: {channel_name} ...")
        
        if not os.path.exists(pkl_path):
            print(f"   ⚠️ Warning: {pkl_path} 없음. (0.0으로 채움)")
            df_data[channel_name] = 0.0
            continue

        with open(pkl_path, "rb") as f:
            interp_obj = pickle.load(f)

        new_values = []
        
        for m, x in zip(masses, x_vals):
            # dN/dx 값 얻기
            val = interp_obj.get_spectrum(m, x)
            
            # 스칼라 변환 (float 강제)
            if isinstance(val, (np.ndarray, list)):
                val = float(val.item()) if hasattr(val, 'item') else float(val[0])
            else:
                val = float(val)

            # 단위 변환: dN/dlog10x
            final_val = val * x * np.log(10)
            
            new_values.append(final_val)

        df_data[channel_name] = new_values

    # 5. 파일 저장
    print(f"💾 결과 저장 중: {OUTPUT_FILE}")
    
    # PPPC 포맷 유지 (헤더 포함, 공백 구분, 지수 표기법)
    df_data.to_csv(OUTPUT_FILE, sep=' ', index=False, float_format='%.8e')
    print("🎉 모든 작업 완료! 에러 없이 파일이 생성되었습니다.")

if __name__ == "__main__":
    main()
