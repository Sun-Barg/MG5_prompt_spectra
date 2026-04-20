import numpy as np
import os
import subprocess
import sys
import random
import time

# ==========================================================
# === 🛠️ CONFIGURATION START ===
# ==========================================================

PROCESS_FOLDER = "4b_repeat_test" 

MASSES = np.logspace(np.log10(5.0), np.log10(1000.0), 100)
NEVENTS = 10000
N_REPEATS = 50
NB_CORE = 16 

# ==========================================================
# === 🛠️ CONFIGURATION END ===
# ==========================================================

madevent_exe = os.path.join(PROCESS_FOLDER, "bin", "madevent")

if not os.path.exists(madevent_exe):
    print(f"❌ 오류: '{madevent_exe}'를 찾을 수 없습니다.")
    sys.exit(1)

print(f"🚀 순차적 반복 모드 시작: {PROCESS_FOLDER}")
print(f"   총 {N_REPEATS}회 반복 (Cycle), 각 Cycle 당 {len(MASSES)}개 질량 포인트")

for rep in range(1, N_REPEATS + 1):
    print(f"\n" + "="*50)
    print(f" 🔄 Cycle [{rep} / {N_REPEATS}] 시작")
    print(f"="*50)
    
    for i, mass in enumerate(MASSES):
        run_name = f"run_m{mass:.2f}_rep{rep}"
        
        print(f"[{i+1}/{len(MASSES)}] Mass: {mass:.2f} GeV (Rep {rep}) running...")

        seed = random.randint(1, 100000000)
        
        ebeam = mass * 1.01
        mh2 = mass 

        # ---------------------------------------------------------
        # 📝 명령어 파일 생성
        # ---------------------------------------------------------
        cmd_content = f"""
generate_events {run_name}
shower=Pythia8
done
set run_card nevents {NEVENTS}
set run_card iseed {seed}
set run_card use_syst False
set run_card lpp1 0
set run_card lpp2 0
set run_card ebeam1 {ebeam}
set run_card ebeam2 {ebeam}
set param_card mpsi {mass}
set param_card mh2 {mh2}
set param_card width 38 Auto
set pythia8_card Main:numberOfEvents {NEVENTS}
set pythia8_card PartonLevel:MPI off
set pythia8_card Print:quiet on
done
"""
        cmd_filename = f"cmd_{PROCESS_FOLDER}_{run_name}.txt"
        with open(cmd_filename, "w") as f:
            f.write(cmd_content)

        # ---------------------------------------------------------
        # 🏃 Madevent 실행
        # ---------------------------------------------------------
        try:
            subprocess.run(
                f"{madevent_exe} {cmd_filename}", 
                shell=True, 
                check=True,
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.PIPE,
                text=True
            )
            print(f"  ✅ {run_name} 완료")
            
        except subprocess.CalledProcessError as e:
            print(f"  ❌ {run_name} 실패")

        finally:
            if os.path.exists(cmd_filename):
                os.remove(cmd_filename)

print("\n🎉 모든 시뮬레이션 종료.")
