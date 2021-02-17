import os
import shutil


def change_python_cwd():
    snap_cwd = os.getcwd() + "/snap/gisoplox/"
    if os.path.exists(snap_cwd):
        x = 10000
        while x >= 1:
            current_snap_folder = snap_cwd + str(x)
            old_snap_folder = snap_cwd + str(x - 1)
            # print(old_snap_folder)
            print(current_snap_folder)
            if os.path.exists(old_snap_folder) and os.path.exists(current_snap_folder):
                os.mkdir(current_snap_folder + str("/.gisoplox"))
                os.mkdir(current_snap_folder + str("/Gisoplox_output"))
                old_file = old_snap_folder + "/.gisoplox/history.gisoplox"
                new_file = current_snap_folder + "/.gisoplox/history.gisoplox"
                shutil.copy(old_file, new_file)
                old_file = old_snap_folder + "/.gisoplox/history_sheet.csv"
                new_file = current_snap_folder + "/.gisoplox/history_sheet.csv"
                shutil.copy(old_file, new_file)
                old_file = old_snap_folder + "/.gisoplox/metrics.gisoplox"
                new_file = current_snap_folder + "/.gisoplox/metrics.gisoplox"
                shutil.copy(old_file, new_file)
                old_file = old_snap_folder + "/.gisoplox/oxyfuel_cutting_width.gisoplox"
                new_file = current_snap_folder + "/.gisoplox/oxyfuel_cutting_width.gisoplox"
                shutil.copy(old_file, new_file)
                old_file = old_snap_folder + "/.gisoplox/plasma_cutting_width.gisoplox"
                new_file = current_snap_folder + "/.gisoplox/plasma_cutting_width.gisoplox"
                shutil.copy(old_file, new_file)
                old_file = old_snap_folder + "/.gisoplox/settings.ini"
                new_file = current_snap_folder + "/.gisoplox/settings.ini"
                shutil.copy(old_file, new_file)
                x = 0
            if os.path.exists(current_snap_folder):
                os.chdir(current_snap_folder)
                x = 0
            x -= 1
