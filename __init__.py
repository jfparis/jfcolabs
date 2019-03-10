from __future__ import print_function
from google.colab import drive
import os.path


DEFAULT_PATH = '/content/gdrive'
NOTEBOOK_DIR = "Colab Notebooks"
DRIVE_DIR = "My Drive"
MODEL_DIR = "Models"


def get_drive_root(path=DEFAULT_PATH):
    return os.path.join(path, "%s" % DRIVE_DIR)


def is_drive_mounted(path=DEFAULT_PATH):
    return os.path.isdir(get_drive_root(path)) and \
           os.path.isdir(os.path.join(get_drive_root(path), NOTEBOOK_DIR))


def mount_drive(path=DEFAULT_PATH):
    if not is_drive_mounted(path):
        drive.mount(path)


def get_model_path(project_name):
    return os.path.join(DEFAULT_PATH, DRIVE_DIR, MODEL_DIR, project_name)

