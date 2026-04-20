import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os
import pickle
import sys
from interpolation_tool import SpectrumInterpolator

# ==========================================================
# === 🛠️ USER CONFIGURATION ===
# ==========================================================
CHANNEL = "bb"           # "bb", "tautau", "ww", "mumu" 등
PARTICLE = "antiproton"      # "photon", "positron", "antiproton"
TARGET_MASS = 50.0      # GeV
SCALE_FACTOR = 2.0       # Ratio 보정용 (필요시 2.0 등)
DATA_DIR_PATTERN = f"Spectra_Data_{CHANNEL}"

# ==========================================================
# === ⚙️ SYSTEM CONFIGURATION (EW Corrections Included) ===
# ==========================================================

PPPC_FILES = {
    "photon": "/home/haebarg/ipynb/AtProduction_gammas.dat",
    "positron": "/home/haebarg/ipynb/AtProduction_positrons.dat",
    "antiproton": "/home/haebarg/ipynb/AtProduction_antiprotons.dat",
}

PPPC_COLS = {
    "ee": 4,       # e+ e- (Total)
    "mumu": 7,     # mu+ mu- (Total)
    "tautau": 10,  # tau+ tau- (Total)
    "qq": 11,      # u, d, s quarks
    "cc": 12,      # c c~
    "bb": 13,      # b b~  <-- [확인 완료]
    "tt": 14,      # t t~
    "ww": 17,      # W+ W- (Total)
    "zz": 20,      # Z Z (Total)
    "gg": 21,      # gluons
    "gammagamma": 22, # gamma gamma
    "hh": 23,      # h h
    "nue": 24,     # nu_e nu_e~
    "numu": 25,    # nu_mu nu_mu~
    "nutau": 26    # nu_tau nu_tau~
}

# ==========================================================
# === 🚀 MAIN LOGIC ===
# ==========================================================

def get_paths_and_config():
    """설정에 따른 파일 경로와 컬럼 인덱스 자동 생성"""
    pkl_filename = f"interpolator_{CHANNEL}_{PARTICLE}.pkl"
    pkl_path = os.path.join(DATA_DIR_PATTERN, pkl_filename)
    
    if PARTICLE not in PPPC_FILES:
        print(f"❌ 지원하지 않는 입자입니다: {PARTICLE}")
        sys.exit()
    pppc_path = PPPC_FILES[PARTICLE]
    
    if CHANNEL not in PPPC_COLS:
        print(f"⚠️ 경고: '{CHANNEL}' 채널에 대한 PPPC 매핑 정보가 없습니다.")
        sys.exit()
    pppc_col = PPPC_COLS[CHANNEL]
    
    return pkl_path, pppc_path, pppc_col

def load_pppc_data(filepath, mass, col_idx):
    """PPPC 데이터 로드 및 변환"""
    try:
        # dtype=str로 읽어서 안전하게 변환
        df = pd.read_csv(filepath, sep=r'\s+', header=None, comment='#', dtype=str)
        df = df.apply(pd.to_numeric, errors='coerce').dropna()

        # 질량 매칭
        df_mass = df[np.isclose(df[0], mass, atol=1e-1)]
        if df_mass.empty:
            print(f"⚠️ PPPC 데이터에 질량 {mass} GeV가 없습니다.")
            return None, None
            
        log10x = df_mass[1].values
        dNdlog10x = df_mass[col_idx].values
        
        x = 10**log10x
        dNdx = dNdlog10x / (x * np.log(10))
        
        return x, dNdx
    except Exception as e:
        print(f"❌ PPPC 로드 에러: {e}")
        return None, None

def plot_comparison():
    pkl_path, pppc_path, pppc_col_idx = get_paths_and_config()
    
    # 1. Interpolator 로드
    if not os.path.exists(pkl_path):
        print(f"❌ 내 데이터 파일을 찾을 수 없습니다:\n   {pkl_path}")
        return
    
    print(f"🔄 Loading My Data: {pkl_path}")
    with open(pkl_path, "rb") as f:
        interpolator = pickle.load(f)

    # 2. PPPC 데이터 로드
    if not os.path.exists(pppc_path):
        print(f"❌ PPPC 파일을 찾을 수 없습니다 (다운로드 필요):\n   {pppc_path}")
        return

    print(f"🔄 Loading PPPC Data: {pppc_path} (Column {pppc_col_idx})")
    x_pppc, y_pppc = load_pppc_data(pppc_path, TARGET_MASS, pppc_col_idx)
    if x_pppc is None: return

    # 3. 내 데이터 보간 (PPPC x축 기준)
    valid_mask = x_pppc < 1.0
    x_common = x_pppc[valid_mask]
    y_pppc = y_pppc[valid_mask]
    
    # [Scale Factor 적용]
    y_my = interpolator.get_spectrum(TARGET_MASS, x_common) * SCALE_FACTOR

    # 4. 플롯 그리기
    fig = plt.figure(figsize=(10, 8))
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
    
    # [상단] 스펙트럼
    ax0 = plt.subplot(gs[0])
    ax0.plot(x_common, y_pppc, 'k-', lw=2, label='PPPC4DMID (Standard, EW incl.)')
    
    my_label = f'My Simulation (MG5+Pythia8)'
    if SCALE_FACTOR != 1.0:
        my_label += f' x {SCALE_FACTOR}'
        
    ax0.plot(x_common, y_my, 'r--', lw=2, label=my_label)
    
    ax0.set_xscale('log')
    ax0.set_yscale('log')
    ax0.set_ylabel(r'$dN / dx$', fontsize=14)
    
    title_str = f"Spectrum Comparison: {CHANNEL} channel, {PARTICLE}\n"
    title_str += f"$m_{{\chi}} = {TARGET_MASS:.1f}$ GeV"
    ax0.set_title(title_str, fontsize=16)
    
    ax0.legend(fontsize=12)
    ax0.grid(True, which='both', ls='--', alpha=0.4)
    ax0.set_xlim(1e-4, 1.0)
    ax0.set_ylim(1e-2, 1e4)

    # [하단] 비율
    ax1 = plt.subplot(gs[1], sharex=ax0)
    
    with np.errstate(divide='ignore', invalid='ignore'):
        ratio = y_my / y_pppc
    
    ax1.plot(x_common, ratio, 'b-', lw=1.5)
    
    ax1.set_xlabel(r'$x = E / m_{\chi}$', fontsize=14)
    ax1.set_ylabel('Ratio\n(Mine / PPPC)', fontsize=10)
    ax1.axhline(1.0, color='gray', linestyle='--', linewidth=1.5)
    ax1.grid(True, which='both', ls='--', alpha=0.4)
    ax1.set_ylim(0.0, 2.0)
    
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.05)
    
    save_filename = f"compare_{CHANNEL}_{PARTICLE}_m{TARGET_MASS:.0f}_EW.png"
    save_path = os.path.join(DATA_DIR_PATTERN, save_filename)
    plt.savefig(save_path, dpi=300)
    print(f"🎉 그래프 저장 완료: {save_path}")

if __name__ == "__main__":
    plot_comparison()
