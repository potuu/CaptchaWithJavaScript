import os

def rename_photos(folder_path, prefix):
    # Get files from folder
    files = os.listdir(folder_path)
    # Choose only .jpg files
    jpg_files = [f for f in files if f.endswith('.jpg')]
    
    for i, filename in enumerate(sorted(jpg_files), start=1):
        # Creating new file name
        new_name = f"{prefix}{i}.jpg"
        # Creating old and new file paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        # Renaming file
        os.rename(old_file, new_file)
        print(f"Renamed: {old_file} to {new_file}")

# Setting the folder paths
bird_folder = r'E:\birdanddrone\captcha\images\bird'
drone_folder = r'E:\birdanddrone\captcha\images\drone'
other_folder = r'E:\birdanddrone\captcha\images\other'

# Rename photos
rename_photos(bird_folder, 'bird')
rename_photos(drone_folder, 'drone')
rename_photos(other_folder, 'other')
