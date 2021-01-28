def create():
    settings_file_text = "cutting start command" + "\n"
    settings_file_text += "M07" + "\n" + "\n"
    settings_file_text += "cutting end command" + "\n"
    settings_file_text += "M08" + "\n" + "\n"
    settings_file_text += "gcode file extension" + "\n"
    settings_file_text += ".CNC" + "\n" + "\n"
    settings_file_text += "table size X (mm)" + "\n"
    settings_file_text += "2700" + "\n" + "\n"
    settings_file_text += "table size Y (mm)" + "\n"
    settings_file_text += "6300" + "\n" + "\n"
    settings_file_text += "show line numbers (0-no, 1-yes)" + "\n"
    settings_file_text += "0" + "\n" + "\n"
    settings_file_text += "show feed speed (0-no, 1-yes)" + "\n"
    settings_file_text += "0" + "\n" + "\n"
    settings_file_text += "show positioning speed (0-no, 1-yes)" + "\n"
    settings_file_text += "0" + "\n" + "\n"
    settings_file_text += "positioning speed" + "\n"
    settings_file_text += "2700" + "\n" + "\n"
    settings_file_text += "default save folder Linux" + "\n"
    settings_file_text += "/media/a/OXICORTE" + "\n" + "\n"
    settings_file_text += "default save folder Windows" + "\n"
    settings_file_text += "" + "\n" + "\n"
    #print(settings_file_text);
    settings_file = open("settings.ini", "w")
    settings_file.write(settings_file_text)
    settings_file.close()
