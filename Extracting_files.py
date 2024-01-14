import os
import shutil

def extract_and_remove_empty_folders():
    current_directory = os.getcwd()

    for root, dirs, files in os.walk(current_directory):
        for file in files:
            file_path = os.path.join(root, file)
            dest_path = os.path.join(current_directory, file)

            # Check if the destination file already exists
            count = 1
            while os.path.exists(dest_path):
                file_name, file_extension = os.path.splitext(file)
                dest_path = os.path.join(current_directory, f"{file_name}_{count}{file_extension}")
                count += 1

            shutil.move(file_path, dest_path)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
            except OSError:
                pass  # Ignore if the directory is not empty

if __name__ == "__main__":
    extract_and_remove_empty_folders()
