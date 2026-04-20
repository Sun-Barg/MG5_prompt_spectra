import os
import numpy as np
import pyhepmc
import pandas as pd # 데이터를 다루기 쉽게 pandas 사용

# === 사용자 설정 ===
base_path = "/home/haebarg/MG5_aMC_v3_5_12/dm_bb/Events"
output_csv_name = "DM_bb_spectra_full.csv"

# 질량 범위 재계산 (폴더명 매칭용)
target_masses = np.logspace(np.log10(5.0), np.log10(1000.0), 100)

# ===================

def get_spectrum(file_path, mass, bins=50):
    """(이전과 동일한 로직) 파일에서 스펙트럼 추출"""
    try:
        # 압축된 파일(.gz)과 안 된 파일 모두 대응
        open_func = pyhepmc.open
        if file_path.endswith('.gz'):
            import gzip
            open_func = lambda f: pyhepmc.open(gzip.open(f, "rb"))

        photons = []
        n_events = 0
        
        with pyhepmc.open(file_path) as f:
            for event in f:
                n_events += 1
                for p in event.particles:
                    if p.pid == 22 and p.status == 1:
                        photons.append(p.momentum.e)
                        
        if n_events == 0: return None, None

        # 로그 빈 생성 (x = E/m_DM 기준 10^-5 ~ 1)
        # 실제 에너지 빈 = mass * x_bin
        x_min, x_max = 1e-5, 1.0
        bin_edges = np.logspace(np.log10(x_min * mass), np.log10(x_max * mass), bins + 1)
        
        hist, _ = np.histogram(photons, bins=bin_edges)
        bin_widths = np.diff(bin_edges)
        dNdE = hist / (n_events * bin_widths)
        centers = np.sqrt(bin_edges[:-1] * bin_edges[1:])
        
        return centers, dNdE
        
    except Exception as e:
        print(f"  Error reading {file_path}: {e}")
        return None, None

# 데이터 수집 루프
all_data = []

for mass in target_masses:
    run_name = f"run_m{mass:.2f}" # 폴더명 형식
    # 파일 찾기 (hepmc 또는 hepmc.gz)
    folder_path = os.path.join(base_path, run_name)
    
    # 파일명 추측 (tag_1_pythia8_events.hepmc 또는 .gz)
    # 실제로는 tag 번호가 바뀔 수 있으니 os.listdir로 찾는 게 안전합니다.
    target_file = None
    if os.path.exists(folder_path):
        for f in os.listdir(folder_path):
            if "pythia8_events.hepmc" in f:
                target_file = os.path.join(folder_path, f)
                break
    
    if target_file:
        print(f"Analyzing {mass:.2f} GeV...")
        energy, dNdE = get_spectrum(target_file, mass)
        
        if energy is not None:
            # 데이터프레임용 리스트에 추가
            for e, val in zip(energy, dNdE):
                all_data.append({
                    "Mass_GeV": mass,
                    "Energy_GeV": e,
                    "x": e/mass,
                    "dNdE": val,
                    "dNdx": val * mass # 스케일링된 값
                })
    else:
        print(f"Skipping {mass:.2f} GeV (File not found)")

# CSV 저장
if all_data:
    df = pd.DataFrame(all_data)
    df.to_csv(output_csv_name, index=False)
    print(f"\n✅ 저장 완료: {output_csv_name}")
    print(df.head())
else:
    print("\n❌ 저장할 데이터가 없습니다.")
