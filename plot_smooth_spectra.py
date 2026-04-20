import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from scipy.ndimage import gaussian_filter1d  # 스무딩을 위한 핵심 라이브러리

# === 사용자 설정 ===
input_folder = "Spectra_Data_sfdm_4tau"   # 데이터 폴더
particle_name = "antiproton"         # 데이터가 적은 입자
channel_name = "4tau"

# 스무딩 강도 (0: 안 함, 1~3: 적당함, 5 이상: 매우 뭉갬)
SMOOTHING_SIGMA = 2.0 
# ===================

def get_mass_from_filename(fname):
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
    print(f"❌ 데이터가 없습니다.")
else:
    files.sort(key=get_mass_from_filename)
    
    plt.figure(figsize=(10, 7))
    
    cmap = plt.get_cmap('viridis')
    norm = mcolors.LogNorm(vmin=get_mass_from_filename(files[0]), 
                           vmax=get_mass_from_filename(files[-1]))
    
    print(f"📈 총 {len(files)}개의 데이터 파일을 플롯합니다... (Smoothing: {SMOOTHING_SIGMA})")

    for file_path in files:
        try:
            df = pd.read_csv(file_path)
            mass = get_mass_from_filename(file_path)
            color = cmap(norm(mass))
            
            # 0이 아닌 데이터만 선택 (로그 스케일 위해)
            # 하지만 스무딩을 위해서는 0인 구간도 포함해서 흐름을 보는 게 좋을 수도 있습니다.
            # 여기서는 데이터가 있는 구간만 가져와서 스무딩합니다.
            df = df.sort_values('x') # x축 기준 정렬 필수
            
            x_data = df['x'].values
            y_data = df['dNdx'].values
            
            # [핵심] 가우시안 스무딩 적용
            if SMOOTHING_SIGMA > 0:
                y_plot = gaussian_filter1d(y_data, sigma=SMOOTHING_SIGMA)
            else:
                y_plot = y_data

            # 값이 너무 작은 노이즈(0 근처)는 그래프를 지저분하게 하므로 컷
            mask = y_plot > 1e-10 
            
            plt.plot(x_data[mask], y_plot[mask], 
                     color=color, linewidth=1.5, alpha=0.8)
            
        except Exception as e:
            pass

    plt.xscale('log')
    plt.yscale('log')
    
    #plt.xlim(8e-4, 1.0)
    # y축 범위를 데이터에 맞게 조절 (너무 낮은 값은 안 보이게)
    #plt.ylim(1e-4, 3e2) 
    
    plt.xlabel(r'$x = E / m_{\chi}$', fontsize=14)
    plt.ylabel(r'$dN / dx$ (Smoothed)', fontsize=14)
    plt.title(f'Smoothed Spectrum: $\chi\chi \\to {channel_name}$, {particle_name}\n(Gaussian Sigma = {SMOOTHING_SIGMA})', fontsize=15)
    
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ax=plt.gca(), label=r'Dark Matter Mass ($m_{\chi}$) [GeV]')
    
    plt.grid(True, which="both", ls="--", alpha=0.3)
    plt.tight_layout()
    
    save_name = f"plot_smooth_{channel_name}_{particle_name}.png"
    plt.savefig(save_name, dpi=300)
    print(f"🎉 그래프 저장 완료: {save_name}")
