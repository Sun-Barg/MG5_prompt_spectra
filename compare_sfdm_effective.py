import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pickle
import scipy.interpolate as interp

# ==========================================================
# === 🛠️ USER CONFIGURATION  ===
# ==========================================================

CHANNEL = "4b"           # 4b, 4tau, 2b2tau
PARTICLE = "antiproton"  # photon, positron, antiproton

DIR_SFDM = "Spectra_Data_sfdm_4b"   # SFDM
DIR_EFF  = "Spectra_Data_4b"    # Effective

LABEL_SFDM = "SFDM"
LABEL_EFF  = "Effective"

TARGET_MASSES = [100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0]

OUTPUT_DIR = "Comparison_SFDM_vs_Effective"

# ==========================================================
# === 🏗️ CLASS DEFINITION ===
# ==========================================================
class SpectrumInterpolator:
    def __init__(self, data_folder, particle, channel, x_min=1e-5, x_max=1.0, n_points=500):
        self.data_folder = data_folder
        self.particle = particle
        self.channel = channel
        self.masses = []
        self.spectrum_matrix = []
        self.common_x = np.logspace(np.log10(x_min), np.log10(x_max), n_points)
        
    def get_spectrum(self, mass, x_array=None):
        if x_array is None: x_array = self.common_x
        if mass < self.masses.min() or mass > self.masses.max():
            return None 
            
        log_m = np.log10(mass)
        log_x = np.log10(x_array)
        log_y_pred = self.interp_func(log_m, log_x)[0] 
        return 10 ** log_y_pred

# ==========================================================
# === 🚀 MAIN LOGIC ===
# ==========================================================

def load_interpolator(folder, channel, particle):
    filename = f"interpolator_{channel}_{particle}.pkl"
    path = os.path.join(folder, filename)
    
    if not os.path.exists(path):
        print(f"❌ The interpolation file cannot be found : {path}")
        print(f"   (run the interpolation_tool to generate a .pkl file.)")
        return None
    
    print(f"🔄 loading : {filename} from {folder}")
    with open(path, "rb") as f:
        return pickle.load(f)

def plot_comparison(mass, interp_sfdm, interp_eff):
    x = np.logspace(-5, 0, 200)
    
    y_sfdm = interp_sfdm.get_spectrum(mass, x)
    y_eff  = interp_eff.get_spectrum(mass, x)
    
    if y_sfdm is None or y_eff is None:
        print(f"⚠️ Mass {mass} GeV data is skipped as it falls outside the interpolation range.")
        return

    fig = plt.figure(figsize=(10, 8))
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
    
    ax0 = plt.subplot(gs[0])
    ax0.plot(x, y_eff,  'k--', lw=2, label=LABEL_EFF, alpha=0.8) 
    ax0.plot(x, y_sfdm, 'r-',  lw=2, label=LABEL_SFDM, alpha=0.8) 
    
    ax0.set_xscale('log')
    ax0.set_yscale('log')
    ax0.set_ylabel(r'$dN / dx$', fontsize=14)
    ax0.set_title(f'Model Comparison: {CHANNEL} channel, {PARTICLE}\n$m_{{\chi}} = {mass:.1f}$ GeV', fontsize=16)
    ax0.legend(fontsize=12)
    ax0.grid(True, which='both', ls='--', alpha=0.4)
    ax0.set_xlim(1e-4, 1.0)
    
    y_valid = np.concatenate([y_sfdm[x > 1e-4], y_eff[x > 1e-4]])
    if len(y_valid) > 0:
        ax0.set_ylim(max(1e-5, y_valid.min() * 0.5), y_valid.max() * 5.0)

    ax1 = plt.subplot(gs[1], sharex=ax0)
    
    with np.errstate(divide='ignore', invalid='ignore'):
        ratio = y_sfdm / y_eff
        
    ax1.plot(x, ratio, 'b-', lw=1.5)
    
    ax1.set_xlabel(r'$x = E / m_{\chi}$', fontsize=14)
    ax1.set_ylabel('Ratio\n(SFDM / Eff)', fontsize=10)
    ax1.axhline(1.0, color='gray', linestyle='--', linewidth=1.5)
    ax1.grid(True, which='both', ls='--', alpha=0.4)
    ax1.set_ylim(0.0, 4.0) 
    
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.05)
    
    save_filename = f"Compare_{CHANNEL}_{PARTICLE}_m{mass:.0f}.png"
    save_path = os.path.join(OUTPUT_DIR, save_filename)
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  ✅ Graph save done : {save_filename}")

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print(f"🚀 SFDM vs Effective compare start")
    print(f"   Channel: {CHANNEL}, Particle: {PARTICLE}")
    
    interp_sfdm = load_interpolator(DIR_SFDM, CHANNEL, PARTICLE)
    interp_eff  = load_interpolator(DIR_EFF,  CHANNEL, PARTICLE)
    
    if interp_sfdm and interp_eff:
        print(f"\n📊 Performs a comparison on mass points {len(TARGET_MASSES)}...")
        
        for mass in TARGET_MASSES:
            plot_comparison(mass, interp_sfdm, interp_eff)
            
        print(f"\n🎉 All tasks completed! Check the ‘{OUTPUT_DIR}’ folder.")
    else:
        print("\n❌ Interpolator loading failed. Please check the path and filename.")
