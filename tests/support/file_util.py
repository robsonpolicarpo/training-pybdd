import os
import zipfile


def zip_csv(filepath: str):
    zip_name = zipfile.ZipFile(filepath.replace('.csv', '.zip'), mode='w')
    filename_in_zip = filepath[filepath.rfind('/') + 1:]
    zip_name.write(filepath, arcname=filename_in_zip)
    zip_name.close()


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
