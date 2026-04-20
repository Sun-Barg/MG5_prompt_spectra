import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# === 사용자 설정 ===
input_folder = "Spectra_Data_sfdm_2b2tau_r0.1"
channel_name = "2b2tau"                
# ===================

particles = ["photon", "positron", "antiproton"]

def get_mass_from_filename(fname):
    """파일명에서 질량(GeV) 추출"""
    try:
        basename = os.path.basename(fname)
        start = basename.find('mpsi') + 4
        end = basename.find('GeV')
        return float(basename[start:end])
    except:
        return 0.0

def plot_single_mode(files, particle, mode):
    """
    단일 모드(Scaled 또는 Energy)에 대한 그래프 생성 및 저장
    mode: 'scaled' (x=E/m, y=dN/dx) 또는 'energy' (x=E, y=dN/dE)
    """
    files.sort(key=get_mass_from_filename)
    
    plt.figure(figsize=(12, 8))
    
    cmap = plt.get_cmap('viridis')
    try:
        min_mass = get_mass_from_filename(files[0])
        max_mass = get_mass_from_filename(files[-1])
    except:
        return # 파일이 비어있거나 문제 발생 시 패스

    norm = mcolors.LogNorm(vmin=min_mass, vmax=max_mass)
    
    for file_path in files:
        try:
            df = pd.read_csv(file_path)
            mass = get_mass_from_filename(file_path)
            color = cmap(norm(mass))
            
            if mode == 'scaled':
                # x = E/m, y = dN/dx
                mask = df['dNdx'] > 0
                x_data = df.loc[mask, 'x']
                y_data = df.loc[mask, 'dNdx']
                
            elif mode == 'energy':
                # x = E, y = dN/dE
                mask = df['dNdE'] > 0
                x_data = df.loc[mask, 'Energy_GeV']
                y_data = df.loc[mask, 'dNdE']
            
            plt.plot(x_data, y_data, color=color, linewidth=1.5, alpha=0.7)
            
        except Exception as e:
            print(f"    ⚠️ 읽기 실패: {os.path.basename(file_path)}")

    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.4)
    
    if mode == 'scaled':
       # plt.xlim(1e-4, 1.0)
       # plt.ylim(1e-1, 1e4)
        plt.xlabel(r'$x = E / m_{\chi}$', fontsize=14)
        plt.ylabel(r'$dN / dx$', fontsize=14)
        title_suffix = "(Scaled)"
    else:
        # plt.xlim(1e-3, 1200) # 1 MeV ~ 1.2 TeV
        # plt.ylim(1e-7, 1e2)
        plt.xlabel(r'Energy ($E$) [GeV]', fontsize=14)
        plt.ylabel(r'$dN / dE$ [GeV$^{-1}$]', fontsize=14)
        title_suffix = "(Absolute Energy)"

    plt.title(f'Dark Matter Annihilation Spectrum ($\chi\chi \\to {channel_name}$, {particle}) {title_suffix}', fontsize=16)

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ax=plt.gca(), label=r'Dark Matter Mass ($m_{\chi}$) [GeV]')
    
    plt.tight_layout()
    
    save_name = f"plot_{channel_name}_{particle}_{mode}.png"
    plt.savefig(save_name, dpi=300)
    plt.close() # 메모리 해제를 위해 닫기
    print(f"  ✅ 저장 완료: {save_name}")

print(f"🚀 통합 플롯팅 시작... (입자 3종 x 모드 2종 = 총 6개)")

for p_name in particles:
    file_pattern = os.path.join(input_folder, f"*{p_name}.csv")
    files = glob.glob(file_pattern)
    
    if not files:
        print(f"❌ {p_name}: 데이터 파일이 없습니다. 건너뜁니다.")
        continue
        
    print(f"\n[{p_name.upper()}] 처리 중...")
    
    # 1. Scaled Mode (x=E/m)
    plot_single_mode(files, p_name, 'scaled')
    
    # 2. Energy Mode (x=E)
    plot_single_mode(files, p_name, 'energy')

print("\n🎉 모든 그래프 저장이 완료되었습니다!")
