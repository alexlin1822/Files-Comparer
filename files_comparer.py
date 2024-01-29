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


# def compare_files(file1, file2):
#     # Open the files for reading

#     folder1=get_md5_array(file1)
#     folder2 = get_md5_array(file2)

#     # with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
#     #     # Read the contents of the files
#     #     content1 = f1.read()
#     #     content2 = f2.read()

#     #     if len(content1) != len(content2):
#     #         return False

#     #     # Compare the contents byte by byte
#     #     for byte1, byte2 in zip(content1, content2):
#     #         if byte1 != byte2:
#     #             return False

#     #     return True


def compare_folders(folder1, folder2, replace_older_files):
    identical_old_files = []
    # different_old_files = []
    print("Checking files in ", folder1)
    old_folder_array = get_md5_array(folder1)
    print("Checking files in ", folder1)
    new_folder_array = get_md5_array(folder2)

    for old_file_array in old_folder_array:
        if np.any(new_folder_array[:, 0] == old_file_array[0]):
            # print(f"File {old_file_array[1]}  is duplicated!")
            identical_old_files.append(old_file_array[1])
        # else:
        #     # print(f"File {old_file_array[1]}  is unqiue!")
        #     different_old_files.append(old_file_array[1])
    # return True

    # Get the list of files in each folder
    # files1 = os.listdir(folder1)
    # files2 = os.listdir(folder2)

    # # Sort the lists of files to ensure proper comparison
    # files1.sort()
    # files2.sort()
    # i = 0

    # for file1, file2 in zip(files1, files2):
    #     file1_path = os.path.join(folder1, file1)
    #     file2_path = os.path.join(folder2, file2)

    #     file1_md5 = calculate_md5(file1_path)
    #     file2_md5 = calculate_md5(file2_path)

    #     if file1_md5 == file2_md5:
    #         #         identical_old_files.append(file1_path)
    #         print(f"Files {file1} and {file2} are identical.")
    #     else:
    #         #         different_old_files.append(file1_path)
    #         print(f"Files {file1} and {file2} are different.")

    # # Check if both files exist and are regular files
    # if os.path.isfile(file1_path) and os.path.isfile(file2_path):
    #     i += 1
    #     if compare_files(file1_path, file2_path):
    #         identical_old_files.append(file1_path)
    #         # print(f"Files {file1} and {file2} are identical.")
    #     else:
    #         different_old_files.append(file1_path)
    #         # print(f"Files {file1} and {file2} are different.")
    #     if i % 100 == 0:
    #         print("checked: ", i)
    # else:
    #     print(f"Skipping comparison for {file1} and {file2}.")

    # # Iterate through files in both folders and compare
    # for file1, file2 in zip(files1, files2):
    #     file1_path = os.path.join(folder1, file1)
    #     file2_path = os.path.join(folder2, file2)
    #     # Check if both files exist and are regular files
    #     if os.path.isfile(file1_path) and os.path.isfile(file2_path):
    #         i += 1
    #         if compare_files(file1_path, file2_path):
    #             identical_old_files.append(file1_path)
    #             # print(f"Files {file1} and {file2} are identical.")
    #         else:
    #             different_old_files.append(file1_path)
    #             # print(f"Files {file1} and {file2} are different.")
    #         if i % 100 == 0:
    #             print("checked: ", i)
    #     else:
    #         print(f"Skipping comparison for {file1} and {file2}.")

    # for different_old_file in different_old_files:
    #     file2_path = os.path.join(folder2, file2)

    #     # Check if both files exist and are regular files
    #     if os.path.isfile(different_old_file) and os.path.isfile(file2_path):
    #         if compare_files(file1_path, file2_path):
    #             identical_old_files.append(file1_path)
    #             # print(f"Files {file1} and {file2} are identical.")
    #         else:
    #             different_old_files.append(file1_path)
    #             # print(f"Files {file1} and {file2} are different.")
    #     else:
    #         print(f"Skipping comparison for {file1} and {file2}.")

    # Print the results
    if replace_older_files:
        # Replace the older files with the newer ones
        for file_path in identical_old_files:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted.")
            else:
                print(f"File '{file_path}' does not exist.")

    else:
        print(f"Identical files: {identical_old_files}")


if __name__ == '__main__':

    # Example usage:
    old_folder_path = 'D:\\PhonePhoto\\2023-09-03'
    new_folder_path = 'D:\\PhonePhoto\\2023-11-24\\DCIM\\Camera'

    # old_folder_path = 'D:\\PhonePhoto\\a'
    # new_folder_path = 'D:\\PhonePhoto\\b'
    replace_older_files = True

    compare_folders(old_folder_path, new_folder_path, replace_older_files)

    # compare_files('D:\\PhonePhoto\\2023-09-03\\IMG_20230521_131653.jpg',
    #   'D:\\PhonePhoto\\2023-09-03\\IMG_20230521_131655.jpg')
