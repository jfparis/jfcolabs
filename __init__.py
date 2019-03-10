from google.colab import drive
import os.path


DEFAULT_PATH='/content/gdrive'


def is_drive_mounted(path=DEFAULT_PATH):
    return os.path.isdir(path) and os.path.isdir(os.path.join(path, "Colab Notebooks"))


def mount_drive(path=DEFAULT_PATH):
    drive.mount(path)
