
import os
import glob
import sys

# ==========================================================
# === 🛠️ CONFIGURATION ===
# ==========================================================

# [중요] 수정할 파일들이 있는 디렉토리 목록을 정의합니다.
# 사용자가 원하는 채널에 맞게 이 리스트를 수정하세요.
TARGET_DIRECTORIES = [
#    "Spectra_Data_4b_off",    # 4b 채널 off-shell 데이터
#    "Spectra_Data_4tau_off",  # 4tau 채널 off-shell 데이터
    "Spectra_Data_2b2tau_off" # 2b2tau 채널 off-shell 데이터
]

# 파일명에서 제거할 문자열
REMOVE_STRING = "_off"

# ==========================================================
# === 🚀 MAIN FUNCTION ===
# ==========================================================

def rename_off_suffix(directory, remove_str):
    """지정된 디렉토리 내의 모든 .csv 파일명에서 특정 문자열을 제거합니다."""

    # 디렉토리 존재 여부 확인
    if not os.path.isdir(directory):
        print(f"❌ 오류: 디렉토리가 존재하지 않거나 찾을 수 없습니다: {directory}")
        return

    print(f"\n🔄 디렉토리 [{directory}] 내 파일명 수정 시작...")

    # .csv 파일 목록 가져오기
    search_pattern = os.path.join(directory, "*.csv")
    files_to_rename = glob.glob(search_pattern)

    if not files_to_rename:
        print("  ✅ 수정할 CSV 파일이 없습니다.")
        return

    count = 0
    for old_path in files_to_rename:
        # 파일 이름만 추출 (예: MM_mpsi9.50GeV_4b_off_antiproton.csv)
        old_filename = os.path.basename(old_path)

        # 제거할 문자열 포함 확인
        if remove_str in old_filename:
            # 새 파일 이름 생성 (일괄 치환)
            new_filename = old_filename.replace(remove_str, "")
            new_path = os.path.join(directory, new_filename)

            # 파일명 수정 수행
            try:
                os.rename(old_path, new_path)
                print(f"  [수정] '{old_filename}' -> '{new_filename}'")
                count += 1
            except OSError as e:
                print(f"❌ 파일 수정 실패 ({old_filename}): {e}")

    print(f"\n✅ {directory} 작업 완료. 총 {count}개의 파일이 수정되었습니다.")

if __name__ == "__main__":

    print("=" * 40)
    print(f" 파일명 일괄 수정 도구 ({REMOVE_STRING} 제거)")
    print("=" * 40)

    for target_dir in TARGET_DIRECTORIES:
        rename_off_suffix(target_dir, REMOVE_STRING)

    print("\n🎉 모든 디렉토리 작업이 완료되었습니다!")
