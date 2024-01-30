import os
import hashlib
import numpy as np


def calculate_md5(file_path):
    """Calculate the MD5 hash of a file."""
    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Create an MD5 hash object
        md5_hash = hashlib.md5()

        # Read and update the hash string value in blocks of 4K
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)

    # Return the hexadecimal representation of the MD5 hash
    return md5_hash.hexdigest()


def get_md5_array(folder_path):
    """Calculate the MD5 hash of a file."""
    # Open the file in binary mode
    md5_array = []
    i = 0
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        md5_array.append([calculate_md5(file_path), file_path])
        i += 1
        if i % 100 == 0:
            print("checked: ", i)

    md5_array = sorted(md5_array, key=lambda x: x[0])
    np_md5_array = np.array(md5_array)
    # Return the hexadecimal representation of the MD5 hash
    return np_md5_array


def compare_folders(folder1, folder2, replace_older_files):
    """Compare two folders and print the results."""
    """If replace_older_files is True, then delete the older files in older folder"""
    """else, print the identical files in older folder"""

    identical_old_files = []
    # different_old_files = []
    print("Checking files in ", folder1)
    old_folder_array = get_md5_array(folder1)
    print("Checking files in ", folder1)
    new_folder_array = get_md5_array(folder2)

    print("Comparing files...")
    for old_file_array in old_folder_array:
        if np.any(new_folder_array[:, 0] == old_file_array[0]):
            identical_old_files.append(old_file_array[1])
        # else:
        #     different_old_files.append(old_file_array[1])

    # Print the results
    if replace_older_files:
        print("Deleteing files...")
        i = 0
        j = 0
        # Replace the older files with the newer ones
        for file_path in identical_old_files:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted.")
                i += 1
            else:
                print(f"File '{file_path}' does not exist.")
                j += 1
        print(f'Deleted {i} files! {j} files do not exist!')

    else:

        print(f"=============================================")
        print(f"Identical files:")
        for file_path in identical_old_files:
            print(f"  {file_path}")
        print(f"=============================================")


if __name__ == '__main__':
    # Example usage:
    old_folder_path = 'G:\\DELL\\D\\PhonePhoto\\2023.02.04\\Camera'
    new_folder_path = 'G:\\DELL\\D\\PhonePhoto\\2023-11-24\\DCIM\\Camera'

    # old_folder_path = 'D:\\PhonePhoto\\a'
    # new_folder_path = 'D:\\PhonePhoto\\b'
    replace_older_files = True
    # replace_older_files = False

    compare_folders(old_folder_path, new_folder_path, replace_older_files)
