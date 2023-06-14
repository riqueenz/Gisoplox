import os
import shutil
import local_data_files


def find_snap_folders():
    current_snap_folder = ""
    old_snap_folder = ""
    snap_cwd = os.getcwd() + "/snap/gisoplox/"
    if os.path.exists(snap_cwd):
        x = 10000
        while x >= 1:
            current_snap_folder = snap_cwd + str(x)
            if os.path.exists(current_snap_folder):
                x -= 1
                while x >= 1:
                    old_snap_folder = snap_cwd + str(x)
                    if os.path.exists(old_snap_folder):
                        x = 0
                    x -= 1
            x -= 1
        return old_snap_folder, current_snap_folder


def copy_files(old_snap_folder, current_snap_folder):
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


def change_settings_file(old_snap_folder, current_snap_folder):
    settings_file_name = current_snap_folder + '/.gisoplox/settings.ini'
    settings_file = open(settings_file_name, 'r')
    file_content = settings_file.read()
    file_content = file_content.replace(old_snap_folder, current_snap_folder)
    settings_file = open(settings_file_name, 'w')
    settings_file.write(file_content)
    settings_file.close()


def change_python_cwd():
    old_snap_folder, current_snap_folder = find_snap_folders()
    if os.path.exists(current_snap_folder):
        os.chdir(current_snap_folder)
        local_data_files.create_data_folders()
    settings_file = current_snap_folder + '/.gisoplox/settings.ini'
    if not os.path.exists(settings_file):
        if os.path.exists(old_snap_folder):
            copy_files(old_snap_folder, current_snap_folder)
            change_settings_file(old_snap_folder, current_snap_folder)
        else:
            local_data_files.create()


