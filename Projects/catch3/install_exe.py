import os

def install_exe(pyfile):
    cmd = 'pyinstaller -F %s' % pyfile
    os.system(cmd)

if __name__ == "__main__":
    install_exe('catch2.py')
