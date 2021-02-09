import os

def change_python_cwd():
    snap_cwd = os.getcwd()+"/snap/gisoplox/"
    if os.path.exists(snap_cwd):
        x = 10000
        while x >= 1:
            snap_cwdx = snap_cwd+str(x)
            if os.path.exists(snap_cwdx):
                os.chdir(snap_cwdx)
            x -= 1
