#!/usr/bin/env python3
from . import linux
from . import admin
import os


def update(**kargs):
    # 1- load all repositories
    admin.update_repositories(**kargs)

    # TODO: check if need to update settings


def init(
        repo=False,
        vscode=False,
        docker=False,
        ubuntu=False,
        python=False,
        **kargs):

    if repo:
        # 1- load all repositories
        admin.update_repositories(**kargs)

    if python:
        print("Installing and Updating python3 virtual environment")
        linux.run([
            ['python', '-m', 'venv', '.venv'],
            ['.venv/bin/pip', 'install', '-r', 'odoo/requirements.txt']
        ])

    if vscode:
        print("VSCode configs")
        linux.run([
            ['mkdir', '-p', '.vscode'],
            # echo "Try to load new VS configuraiton"
            ["cp", "-i", os.path.dirname(os.path.realpath(__file__)) + "/../data/template-tasks.json", os.getcwd() + "/.vscode/task.json","-y"],
            ["cp", "-i", os.path.dirname(os.path.realpath(__file__)) + "/../data/template-launch.json", os.getcwd() + "/.vscode/launch.json","-y"],
            ["cp", "-i", os.path.dirname(os.path.realpath(__file__)) + "/../data/template-settings.json", os.getcwd() + "/.vscode/settings.json","-y"],
            # # TODO: update project list based on project list
            # # TODO: update project list based on project list
            ['code', '.'],
        ])
