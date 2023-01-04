import os
import re
from time import sleep


def get_folder_scripts():
    dir = os.getcwd()
    return os.listdir(dir)

def get_old_folder():
    return os.getcwd()

def open_folder_scripts():
    folder_scripts = get_folder_scripts()
    list_dirs = list()
    for folder in folder_scripts:
        if os.path.isdir(folder) and folder != 'JSON':
            open_folder_script = os.path.join(os.getcwd(), folder)
            old_folder = os.getcwd()
            os.chdir(open_folder_script)
            list_dirs.append(open_folder_script)
            os.chdir(old_folder)
    
    return list_dirs


def run_scripts(dirs, name_script, old_dir):
    for dir in os.listdir(dirs):
        if '.py' in dir and name_script in dir and 'headers' not in dir:
            os.chdir(dirs)
            print(f'executando o script {dir}')
            os.system(f'python3 {dir}')
            os.chdir(old_dir)


def start():
    old_dir = os.getcwd()
    while True:
        folders_scripts = open_folder_scripts()
        for scripts in folders_scripts:
            name_script = re.search('', scripts)
            name_script = scripts.split('\\')[7]
            run_scripts(scripts, name_script, old_dir)
        os.system('python3 lerjson.py')
        sleep(420)

start()