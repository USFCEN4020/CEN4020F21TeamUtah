import os
import sys

# add source files to path
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../src")

import main
import main_menu
import links_menu
import profile_menu
import db.db as db
import friends
