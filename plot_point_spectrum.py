import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# === 사용자 설정 ===
input_folder = "Spectra_Data_4tau"   
particle_name = "antiproton"          
channel_name = "4tau"                
# ===================

def get_mass_from_filename(fname):
    """파일명에서 질량(GeV) 추출"""
    try:
        basename = os.path.basename(fname)
        start = basename.find('mpsi') + 4
        end = basename.find('GeV')
        return float(basename[start:end])
    except:
        return 0.0

file_pattern = os.path.join(input_folder, f"*{particle_name}.csv")
files = glob.glob(file_pattern)

if not files:
    print(f"❌ '{input_folder}' 폴더에 '{particle_name}' 데이터가 없습니다.")
else:
    files.sort(key=get_mass_from_filename)
    
    plt.figure(figsize=(12, 8))
    
    cmap = plt.get_cmap('viridis')
    norm = mcolors.LogNorm(vmin=get_mass_from_filename(files[0]), 
                           vmax=get_mass_from_filename(files[-1]))
    
    print(f"📈 총 {len(files)}개의 데이터 파일을 플롯합니다...")

    for file_path in files:
        try:
            df = pd.read_csv(file_path)
            mass = get_mass_from_filename(file_path)
            
            color = cmap(norm(mass))
            
            mask = df['dNdx'] > 0
            
            plt.plot(df.loc[mask, 'x'], df.loc[mask, 'dNdx'], 
                     color=color, linestyle='None', marker='.', alpha=0.7)
            
        except Exception as e:
            print(f"  ⚠️ 읽기 실패: {file_path} ({e})")

    plt.xscale('log')
    plt.yscale('log')
    
    # plt.xlim(1e-4, 1.0)
    # plt.ylim(1e-1, 1e4)
    
    plt.xlabel(r'$x = E / m_{\chi}$', fontsize=14)
    plt.ylabel(r'$dN / dx$', fontsize=14)
    plt.title(f'Dark Matter Annihilation Spectrum ($\chi\chi \\to {channel_name}$, {particle_name})', fontsize=16)
    
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=plt.gca(), label=r'Dark Matter Mass ($m_{\chi}$) [GeV]')
    
    plt.grid(True, which="both", ls="--", alpha=0.4)
    plt.tight_layout()
    
    save_name = f"point_spectrum_{channel_name}_{particle_name}.png"
    plt.savefig(save_name, dpi=300)
    print(f"🎉 그래프 저장 완료: {save_name}")
    # plt.show() # 서버 환경(GUI 없음)에서는 이 줄을 주석 처리하거나 무시됩니다.
