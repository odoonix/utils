#!/usr/bin/env python3

import os
import platform
import subprocess
import logging
import json


def call_safe(command, shell=False, cwd='.'):
    try:
        with open("app.logs", "a") as log:
            ret = subprocess.call(command, shell=shell,
                                  cwd=cwd, stdout=log, stderr=log)
            if ret != 0:
                if ret < 0:
                    print("Killed by signal")
                else:
                    print("Command failed with return code")
                exit(2)
    except Exception as e:
        logging.error('Failed to execute command: %s', e)
        exit(2)


def git_update(workspace, project):
    branch_name = '16.0'
    depth = '1'
    # SOURCE_PATH="./odoo-utils"
    # GIT_OPTIONS=" --branch 16.0  --depth 1"
    # git clone $GIT_OPTIONS git@github.com:viraweb123/odoo-utils.git
    if os.path.exists(project):
        call_safe(['git', 'pull'], cwd=project)
    else:
        call_safe(['git', 'clone', 
                   '--branch', branch_name, 
                   '--depth', depth, 
                   'git@github.com:' + workspace + '/' + project + '.git'])


def progressBar(iterable, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function

    def printProgressBar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                         (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()


# To update repositories
directory = os.path.dirname(os.path.realpath(__file__))
configs = {}
with open(directory+'/config.json') as config_file:
    configs = json.load(config_file)


print("Clone&Update Repositories")
for repo in progressBar(
        configs['repositories'],
        prefix='Progress:',
        suffix='Complete',
        length=50):
    git_update(repo['workspace'], repo['name'])

# Make venv
call_safe(['python', '-m', 'venv', '.venv'])

# To install requirenment
call_safe(['.venv/bin/pip', 'install', '-r', 'odoo/requirements.txt'])

# Make workspace
call_safe(['mkdir', '-p', '.vscode'])

# echo "Try to load new VS configuraiton"
# cp -i "${SOURCE_PATH}/data/template-tasks.json"       ".vscode/task.json"
# cp -i "${SOURCE_PATH}/data/template-settings.json"    ".vscode/settings.json"
# cp -i "${SOURCE_PATH}/data/template-launch.json"      ".vscode/launch.json"
# # TODO: update project list based on project list


# Open code editor
call_safe(['code', '.'])
