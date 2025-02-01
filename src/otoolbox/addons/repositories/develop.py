#!/usr/bin/env python3
from . import linux
from . import admin

def init(
        repo=False,
        vscode=False,
        docker=False,
        ubuntu=False,
        python=False,
        **kargs):

    # 0- Basics
    linux.run([
        ['mkdir', '-p', '.vw'],
    ])

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
            ['cp', 
                '-i', 
                'odoonix/utils/data/template-workspace.json',
                'odoo.code-workspace'],
            # # TODO: update project list based on project list
            # # TODO: update project list based on project list
            ['code', 'odoo.code-workspace'],
        ])
