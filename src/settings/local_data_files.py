import os
import settings_file
import oxyfuel_cutting_width_file
def create():
    os.mkdir(".gisoplox")
    settings_file.create()
    oxyfuel_cutting_width_file.create()
