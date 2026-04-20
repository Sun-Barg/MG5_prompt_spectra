import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pickle
import scipy.interpolate as interp

# ==========================================================
# === 🛠️ USER CONFIGURATION ===
# ==========================================================

# 1. 채널 및 입자 설정
CHANNEL = "2b2tau"           # 기본 채널명 (예: "4b", "4tau")
PARTICLE = "antiproton"  # 입자명 (예: "photon", "positron", "antiproton")

# 2. 데이터 폴더 경로 설정 (자동으로 _off가 붙는다고 가정)
DIR_ON = f"Spectra_Data_{CHANNEL}"
DIR_OFF = f"Spectra_Data_{CHANNEL}_off"

# 3. 비교하고 싶은 질량 목록 (GeV)
# 두 시뮬레이션의 질량 범위 내에 있는 값들을 자유롭게 적으세요.
TARGET_MASSES = [100.0, 500.0, 1000.0]

# 4. 결과 저장 폴더
OUTPUT_DIR = "Comparison_Results"

# ==========================================================
# === 🏗️ CLASS DEFINITION (Pickle 로드를 위해 필수) ===
# ==========================================================
# 이 클래스 정의는 저장할 때 사용된 코드와 동일해야 합니다.
class SpectrumInterpolator:
    def __init__(self, data_folder, particle, channel, x_min=1e-5, x_max=1.0, n_points=500):
        self.data_folder = data_folder
        self.particle = particle
        self.channel = channel
        self.masses = []
        self.spectrum_matrix = []
        self.common_x = np.logspace(np.log10(x_min), np.log10(x_max), n_points)
        
    def get_spectrum(self, mass, x_array=None):
        if x_array is None: x_array = self.common_x
        log_m = np.log10(mass)
        log_x = np.log10(x_array)
        log_y_pred = self.interp_func(log_m, log_x)[0] 
        return 10 ** log_y_pred

# ==========================================================
# === 🚀 MAIN LOGIC ===
# ==========================================================

def load_interpolator(folder, filename):
    path = os.path.join(folder, filename)
    if not os.path.exists(path):
        print(f"❌ 파일을 찾을 수 없습니다: {path}")
        return None
    
    print(f"🔄 로딩 중: {path}")
    with open(path, "rb") as f:
        return pickle.load(f)

def plot_comparison(mass, interp_on, interp_off):
    # 공통 x축 (1e-5 ~ 1.0)
    x = np.logspace(-5, 0, 200)
    
    # 각 보간기에서 스펙트럼 추출
    y_on = interp_on.get_spectrum(mass, x)
    y_off = interp_off.get_spectrum(mass, x)
    
    # 그래프 그리기
    fig = plt.figure(figsize=(10, 8))
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
    
    # [상단] 스펙트럼
    ax0 = plt.subplot(gs[0])
    ax0.plot(x, y_on, 'b-', lw=2, label=f'On-shell ({CHANNEL})', alpha=0.8)
    ax0.plot(x, y_off, 'r--', lw=2, label=f'Off-shell ({CHANNEL}_off)', alpha=0.8)
    
    ax0.set_xscale('log')
    ax0.set_yscale('log')
    ax0.set_ylabel(r'$dN / dx$', fontsize=14)
    ax0.set_title(f'On-shell vs Off-shell: {CHANNEL} channel, {PARTICLE}\n$m_{{\chi}} = {mass:.1f}$ GeV', fontsize=16)
    ax0.legend(fontsize=12)
    ax0.grid(True, which='both', ls='--', alpha=0.4)
    #ax0.set_xlim(1e-4, 1.0)
    #ax0.set_ylim(1e-4, 1e4) # y축 범위는 상황에 맞게 조절

    # [하단] 비율 (Ratio = Off / On)
    ax1 = plt.subplot(gs[1], sharex=ax0)
    
    # 0으로 나누기 방지
    with np.errstate(divide='ignore', invalid='ignore'):
        ratio = y_off / y_on
        
    ax1.plot(x, ratio, 'k-', lw=1.5)
    
    ax1.set_xlabel(r'$x = E / m_{\chi}$', fontsize=14)
    ax1.set_ylabel('Ratio\n(Off / On)', fontsize=10)
    ax1.axhline(1.0, color='gray', linestyle='--', linewidth=1.5)
    ax1.grid(True, which='both', ls='--', alpha=0.4)
    ax1.set_ylim(0.0, 3.0) # 비율 범위
    
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.05)
    
    # 저장
    save_filename = f"Compare_{CHANNEL}_OnOff_{PARTICLE}_m{mass:.0f}.png"
    save_path = os.path.join(OUTPUT_DIR, save_filename)
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  ✅ 그래프 저장 완료: {save_filename}")

if __name__ == "__main__":
    # 0. 저장 폴더 생성
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 1. 파일명 규칙 정의 (사용자 요청 반영)
    # On-shell: interpolator_4b_antiproton.pkl
    pkl_name_on = f"interpolator_{CHANNEL}_{PARTICLE}.pkl"
    
    # Off-shell: interpolator_4b_off_antiproton.pkl
    pkl_name_off = f"interpolator_{CHANNEL}_off_{PARTICLE}.pkl"
    
    # 2. Interpolator 로드
    interp_on = load_interpolator(DIR_ON, pkl_name_on)
    interp_off = load_interpolator(DIR_OFF, pkl_name_off)
    
    if interp_on and interp_off:
        print(f"\n🚀 비교 분석 시작 ({len(TARGET_MASSES)} masses)...")
        
        # 3. 질량별 비교 수행
        for mass in TARGET_MASSES:
            # 보간 범위 체크
            min_mass = max(interp_on.masses.min(), interp_off.masses.min())
            max_mass = min(interp_on.masses.max(), interp_off.masses.max())
            
            if mass < min_mass or mass > max_mass:
                print(f"⚠️ Skip {mass} GeV: 데이터 범위({min_mass:.1f}~{max_mass:.1f}) 밖입니다.")
                continue
                
            plot_comparison(mass, interp_on, interp_off)
            
        print("\n🎉 모든 작업 완료!")
    else:
        print("\n❌ Interpolator 로드에 실패하여 작업을 중단합니다.")
        print("   이전 단계에서 .pkl 파일이 생성되었는지 확인해주세요.")
