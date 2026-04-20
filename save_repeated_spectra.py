import os
import numpy as np
import pyhepmc
import pandas as pd 
import gzip
import glob

# ==========================================================
# === 🛠️ CONFIGURATION ===
# ==========================================================
base_path = "/home/haebarg/MG5_aMC_v3_5_12/4b_repeat_test/Events"  
output_folder = "re_Spectra_Data_4b"                          
channel_name = "4b"                                        # ex: bb, 4b, 4tau

particles_to_analyze = {
    "photon": 22,
    "positron": -11,
    "antiproton": -2212
}

target_masses = np.logspace(np.log10(5.0), np.log10(1000.0), 100)
# ==========================================================

os.makedirs(output_folder, exist_ok=True)
print(f"📂 결과 저장 경로: {os.path.abspath(output_folder)}")

def get_raw_energies(file_path, pid):
    """파일에서 에너지 리스트와 이벤트 수만 추출 (히스토그램 생성 전 단계)"""
    energies = []
    n_events = 0
    
    try:
        if os.path.getsize(file_path) == 0:
            return [], 0
            
        with pyhepmc.open(file_path) as f:
            for event in f:
                n_events += 1
                for p in event.particles:
                    if p.pid == pid and p.status == 1:
                        energies.append(p.momentum.e)
        return energies, n_events
        
    except Exception as e:
        print(f"    ⚠️ 파일 읽기 에러 ({os.path.basename(file_path)}): {e}")
        return [], 0

# --- Main Loop ---
print(f"🚀 데이터 병합 및 추출 시작...")

for mass_idx, mass in enumerate(target_masses):
    print(f"[{mass_idx+1}/{len(target_masses)}] Processing {mass:.2f} GeV...", end="\r")
    
    run_pattern = f"run_m{mass:.2f}_rep*"
    search_path = os.path.join(base_path, run_pattern)
    rep_folders = glob.glob(search_path)
    
    for p_name, p_pid in particles_to_analyze.items():
        total_energies = []
        total_events = 0
        
        for folder in rep_folders:
            hepmc_files = glob.glob(os.path.join(folder, "*pythia8_events.hepmc*"))
            if not hepmc_files: continue
            
            target_file = hepmc_files[0]
            e_list, n_evt = get_raw_energies(target_file, p_pid)
            total_energies.extend(e_list)
            total_events += n_evt
            
        if total_events > 0 and total_energies:
            bins = np.logspace(np.log10(1e-5), np.log10(mass), 60) 
            hist, bin_edges = np.histogram(total_energies, bins=bins)
            bin_widths = np.diff(bin_edges)
            bin_centers = np.sqrt(bin_edges[:-1] * bin_edges[1:]) # 기하 평균
            dNdE = hist / total_events / bin_widths
            
            data_list = []
            for e, val in zip(bin_centers, dNdE):
                if val > 0:
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

print(f"\n🎉 모든 데이터 추출 및 병합 완료!")
