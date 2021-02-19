import os
from settings import oxyfuel_cutting_width_file
from settings import plasma_cutting_width_file
from settings import settings_file
from settings import metrics_file
from settings import history_file


def create_data_folders():
    if not os.path.exists(".gisoplox"):
        os.mkdir(".gisoplox")
    if not os.path.exists("Gisoplox_output"):
        os.mkdir("Gisoplox_output")


def create():
    create_data_folders()
    settings_file.create()
    oxyfuel_cutting_width_file.create()
    plasma_cutting_width_file.create()
    metrics_file.create()
    history_file.create()
