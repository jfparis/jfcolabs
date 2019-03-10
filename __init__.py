from google.colab import drive
import os.path


DEFAULT_PATH = '/content/gdrive'


def get_drive_root(path=DEFAULT_PATH):
    return os.path.join(path, "My Drive")


def is_drive_mounted(path=DEFAULT_PATH):
    return os.path.isdir(get_drive_root(path)) and \
           os.path.isdir(os.path.join(get_drive_root(path), "Colab Notebooks"))


def mount_drive(path=DEFAULT_PATH):
    drive.mount(path)
