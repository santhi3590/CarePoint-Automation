import os


def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)