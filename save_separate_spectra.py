import os
import numpy as np
import pyhepmc
import pandas as pd 
import gzip

base_path = "/home/haebarg/MG5_aMC_v3_5_12/dm_4tau/Events"  
output_folder = "Spectra_Data_4tau"  
channel_name = "4tau"               # ex: bb, 4b, 4tau

particles_to_analyze = {
    "photon": 22,
    "positron": -11,
    "antiproton": -2212
}

target_masses = np.logspace(np.log10(5.0), np.log10(1000.0), 100)
# ===================

os.makedirs(output_folder, exist_ok=True)
print(f"📂 result directory generated: {os.path.abspath(output_folder)}")

def get_spectrum(file_path, mass, pid, bins=50):
    """특정 PID를 가진 입자의 스펙트럼 추출"""
    try:
        energies = []
        n_events = 0
        opener = gzip.open if file_path.endswith('.gz') else open
        
        with pyhepmc.open(file_path) as f:
            for event in f:
                n_events += 1
                for p in event.particles:
                    if p.pid == pid and p.status == 1:
                        energies.append(p.momentum.e)
                        
        if n_events == 0: return None, None

        x_min, x_max = 1e-5, 1.0
        bin_edges = np.logspace(np.log10(x_min * mass), np.log10(x_max * mass), bins + 1)
        
        hist, _ = np.histogram(energies, bins=bin_edges)
        bin_widths = np.diff(bin_edges)
        dNdE = hist / (n_events * bin_widths)
        centers = np.sqrt(bin_edges[:-1] * bin_edges[1:])
        
        return centers, dNdE
        
    except Exception as e:
        print(f"  ⚠️ Error reading {file_path}: {e}")
        return None, None

# --- main loop ---
print(f"🚀 데이터 추출 시작...")

count = 0
for mass in target_masses:
    run_name = f"run_m{mass:.2f}"
    folder_path = os.path.join(base_path, run_name)
    
    target_file = None
    if os.path.exists(folder_path):
        for f in os.listdir(folder_path):
            if "pythia8_events.hepmc.gz" in f:
                target_file = os.path.join(folder_path, f)
                break
    
    if target_file:
        print(f"Processing {mass:.2f} GeV...", end="\r")
        
        for p_name, p_pid in particles_to_analyze.items():
            energy, dNdE = get_spectrum(target_file, mass, p_pid)
            
            if energy is not None:
                data_list = []
                for e, val in zip(energy, dNdE):
                    if val > 0: # 0값 제외
                        data_list.append({
                            "Energy_GeV": e,
                            "x": e/mass,
                            "dNdE": val,
                            "dNdx": val * mass
                        })
                
                if data_list:
                    df = pd.DataFrame(data_list)
                    
                    filename = f"MM_mpsi{mass:.2f}GeV_{channel_name}_{p_name}.csv"
                    save_path = os.path.join(output_folder, filename)
                    
                    df.to_csv(save_path, index=False)
                    count += 1

print(f"\n✅ 모든 작업 완료! 총 {count}개의 파일이 '{output_folder}' 폴더에 저장되었습니다.")
