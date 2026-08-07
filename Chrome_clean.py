import os
import shutil
import subprocess

def close_chrome():
    print("Closing Google Chrome to release file locks...")
    # Safely tells Windows to terminate any running Chrome instances
    subprocess.run("taskkill /f /im chrome.exe", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def cleanup_chrome_cache():
    # Path to Chrome's user data on Windows
    local_app_data = os.getenv('LOCALAPPDATA')
    chrome_cache_path = os.path.join(local_app_data, r"Google\Chrome\User Data\Default\Cache\Cache_Data")
    
    if not os.path.exists(chrome_cache_path):
        print("Chrome cache directory not found. It might be in a different profile or already clean.")
        return

    print(f"Cleaning cache at: {chrome_cache_path}")
    
    success_count = 0
    fail_count = 0

    # Iterate and delete files inside the Cache_Data folder
    for filename in os.listdir(chrome_cache_path):
        file_path = os.path.join(chrome_cache_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            success_count += 1
        except Exception as e:
            # Some files might still be locked by background system processes
            fail_count += 1

    print(f"Cleanup complete. Successfully removed {success_count} cache items.")
    if fail_count > 0:
        print(f"Skipped {fail_count} items (currently locked or inaccessible).")

if __name__ == "__main__":
    # Make sure to save your work in Chrome before running this!
    close_chrome()
    cleanup_chrome_cache()