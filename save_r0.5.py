import os
import numpy as np
import pyhepmc
import pandas as pd 
import glob
import re  # 정규표현식 사용 (질량 추출용)

# ==========================================================
# === 🛠️ CONFIGURATION ===
# ==========================================================
TARGET_RATIO = 0.5  # 처리할 비율

base_path = "/home/haebarg/MG5_aMC_v3_5_12/sfdm_2b2tau_r0.5/Events"
output_folder = f"Spectra_Data_sfdm_2b2tau_r{TARGET_RATIO}"  
channel_name = "2b2tau"

particles_to_analyze = {
    "photon": 22,
    "positron": -11,
    "antiproton": -2212
}
# ==========================================================

os.makedirs(output_folder, exist_ok=True)
print(f"📂 결과 저장 경로: {os.path.abspath(output_folder)}")
print(f"🎯 타겟 비율 (Ratio): {TARGET_RATIO}")

def get_raw_energies(file_path, pid):
    energies = []
    n_events = 0
    try:
        if os.path.getsize(file_path) == 0: return [], 0
        with pyhepmc.open(file_path) as f:
            for event in f:
                n_events += 1
                for p in event.particles:
                    if p.pid == pid and p.status == 1:
                        energies.append(p.momentum.e)
        return energies, n_events
    except Exception as e:
        print(f"    ⚠️ 파일 에러: {e}")
        return [], 0

# --- 1. 폴더 스캔 및 질량 자동 감지 ---
print("🔍 폴더 스캔 중...")

# 해당 비율(Ratio)을 가진 모든 폴더 찾기
folder_pattern = os.path.join(base_path, f"run_m*_r{TARGET_RATIO}_rep*")
all_folders = glob.glob(folder_pattern)

# 폴더명에서 질량 추출 (중복 제거)
detected_masses = set()
for folder in all_folders:
    folder_name = os.path.basename(folder)
    # 정규표현식으로 'm' 뒤의 숫자 추출 (예: run_m100.00_r...)
    match = re.search(r"run_m([\d\.]+)_r", folder_name)
    if match:
        detected_masses.add(float(match.group(1)))

# 질량 정렬
sorted_masses = sorted(list(detected_masses))

if not sorted_masses:
    print("❌ 해당 Ratio의 데이터 폴더를 하나도 찾지 못했습니다!")
    exit()

print(f"✅ 총 {len(sorted_masses)}개의 질량 포인트 감지됨: {sorted_masses[0]:.2f} ~ {sorted_masses[-1]:.2f} GeV")

# --- 2. 데이터 처리 루프 ---
count = 0
for mass_idx, mass in enumerate(sorted_masses):
    print(f"[{mass_idx+1}/{len(sorted_masses)}] Processing {mass:.2f} GeV...", end="\r")
    
    # 해당 질량의 모든 반복(rep) 폴더 찾기
    run_pattern = f"run_m{mass:.2f}_r{TARGET_RATIO}_rep*"
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
            bin_centers = np.sqrt(bin_edges[:-1] * bin_edges[1:])
            
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
                count += 1

print(f"\n🎉 작업 완료! 총 {count}개의 CSV 파일이 생성되었습니다.")
