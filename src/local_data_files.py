import os
import oxyfuel_cutting_width_file
import plasma_cutting_width_file
import settings_file
import metrics_file
import history_file


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
