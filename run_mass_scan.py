import numpy as np
import os
import subprocess
import sys

# === config  ===
mg5_executable = "./bin/mg5_aMC"
process_folder = "dm_bb" # need to check and change the process
masses = np.logspace(np.log10(5.0), np.log10(1000.0), 100)
nevents = 100000
# ===================

for i, mass in enumerate(masses):
    run_name = f"run_m{mass:.2f}"
    
    print(f"[{i+1}/100] Processing Mass: {mass:.2f} GeV ...")
    
    commands = f"""
set nb_core 16                  
set automatic_html_opening False
launch {process_folder} -n {run_name}
shower=Pythia8
set run_card nevents {nevents}
set use_syst False
set lpp1 0
set lpp2 0
set mpsi {mass}
set ebeam1 {mass + 0.1}
set ebeam2 {mass + 0.1}
set mh2 {mass / 2}
set width 38 Auto
set pythia8_card Main:numberOfEvents {nevents}
0
quit
"""
    
    with open("temp_cmd.txt", "w") as f:
        f.write(commands)
        
    try:
        subprocess.run(
            f"{mg5_executable} temp_cmd.txt", 
            shell=True, 
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"  -> {run_name} finished!")
        
    except subprocess.CalledProcessError as e:
        print(f"\n🚨 Called Error ({run_name})")
        print(f"log check: {process_folder}/{run_name}_tag_1_debug.log")
        print(f"MadGraph Error tail:\n{e.stderr[-500:]}")
        sys.exit(1)

print("\n All Simulation Done.")
