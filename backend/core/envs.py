""" Define paths across project """
from os.path import join
import datetime

# Path to project root should be defined manually or add environment variable
# ROOT_DIR = /path/to/project/project-TT

# relative directories related to project
BACKEND_DIR = 'backend'

# relative directories related to data
DATA_DIR = 'data'
IMAGE_DIR = join(DATA_DIR, 'images')
THUMBNAIL_DIR = join(DATA_DIR, 'thumbnails')

# start time used by instagram
START_TIME = datetime.datetime(1970, 1, 1)
