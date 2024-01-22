import os
import json

from . import linux


def git_update(workspace, project, branch_name='16.0', depth='1'):
    state = 'Not Found'
    # SOURCE_PATH="./odoo-utils"
    # GIT_OPTIONS=" --branch 16.0  --depth 1"
    # git clone $GIT_OPTIONS git@github.com:viraweb123/odoo-utils.git
    if os.path.exists(project):
        linux.call_safe(['git', 'pull'], cwd=project)
        state = 'Created'
    else:
        result = linux.call_safe([
            'git',
            'clone',
            '--branch', branch_name,
            '--depth', depth,
            'git@github.com:' + workspace + '/' + project + '.git'
        ])
        if result == 0:
            state = 'Updated'
        else:
            state = 'Fail'
    return state


def get_list():
    # To update repositories
    directory = os.path.dirname(os.path.realpath(__file__)) + '/..'
    configs = {}
    with open(directory+'/config.json') as config_file:
        configs = json.load(config_file)
    return configs['repositories']
