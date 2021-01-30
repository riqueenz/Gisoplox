import os
from settings import oxyfuel_cutting_width_file
from settings import plasma_cutting_width_file
from settings import settings_file
from settings import metrics_file
def create():
    os.mkdir(".gisoplox")
    settings_file.create()
    oxyfuel_cutting_width_file.create()
    plasma_cutting_width_file.create()
    metrics_file.create()
