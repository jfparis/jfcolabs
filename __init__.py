from __future__ import print_function
from google.colab import drive
import os, os.path


DEFAULT_PATH = '/content/gdrive'
NOTEBOOK_DIR = "Colab Notebooks"
DRIVE_DIR = "My Drive"
MODEL_DIR = "TFModels"


def get_drive_root(path=DEFAULT_PATH):
    return os.path.join(path, "%s" % DRIVE_DIR)


def is_drive_mounted(path=DEFAULT_PATH):
    return os.path.isdir(get_drive_root(path)) and \
           os.path.isdir(os.path.join(get_drive_root(path), NOTEBOOK_DIR))


def mount_drive(path=DEFAULT_PATH):
    if not is_drive_mounted(path):
        drive.mount(path)


def get_model_path(project_name, create=False):
    path = os.path.join(DEFAULT_PATH, DRIVE_DIR, MODEL_DIR, project_name)
    if create:
        if not os.path.exists(path):
            os.mkdir(path)
    return path


def custom_progress_text(message):
  import progressbar
  from string import Formatter

  message_ = message.replace('(', '{')
  message_ = message_.replace(')', '}')

  keys = [key[1] for key in Formatter().parse(message_)]

  ids = {}
  for key in keys:
    if key is not None:
      ids[key] = float('nan')

  msg = progressbar.FormatCustomText(message, ids)
  return msg


def create_progress_bar(text=None):
  import progressbar
  if text is None:
    text = progressbar.FormatCustomText('')
  bar = progressbar.ProgressBar(widgets=[
      progressbar.Percentage(),
      progressbar.Bar(),
      progressbar.AdaptiveETA(), '  ',
      text,
  ])
  return bar