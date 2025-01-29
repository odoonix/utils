import os
import json

from otoolbox import env
from otoolbox.repositories import linux


class ModuleList(list):
    def __rich__(self):
        return '\n'.join(self)

    def difference(self, other):
        new_list = ModuleList()
        for item in self:
            if item not in other:
                new_list.append(item)
        return new_list


def is_addons(name, dir):
    new_path = os.path.join(name, dir)
    for file_name in os.listdir(new_path):
        if file_name == '__manifest__.py':
            return True
    return False


def get_addons_list(name, *args, **kargs):
    addons_list = ModuleList()
    if not os.path.exists(name) \
            or os.path.isfile(name):
        return addons_list

    for dir in os.listdir(name):
        new_path = os.path.join(name, dir)
        if os.path.isdir(new_path) \
                and is_addons(name, dir):
            addons_list.append(dir)

    return addons_list


def git_update(workspace, project, branch_name=None, depth='1'):
    if not branch_name:
        branch_name = get_branch()

    cwd = "{}/{}".format(workspace, project)
    # Replace old scafolding with new one
    if project != 'odoo' and os.path.exists(project):
        linux.run([
            ['mkdir', '-p', 'tmp'],
            ['mv', project, 'tmp'],

            ['mkdir', '-p', workspace],
            ['mv', "tmp/{}".format(project), workspace],

            ['rm', 'tmp']
        ])

    if os.path.exists(cwd):
        linux.call_safe(['git', 'pull'], cwd=cwd)
        state = 'Created'
    else:
        linux.run([
            ['mkdir', '-p', workspace],
        ])
        result = linux.call_safe([
            'git',
            'clone',
            '--branch', branch_name,
            '--depth', depth,
            'git@github.com:' + workspace + '/' + project + '.git'
        ], cwd=workspace)
        if result == 0:
            state = 'Updated'
        else:
            state = 'Fail'
    return state


def get_list(filter_workspace=False):
    # To update repositories
    configs = json.loads(env.resource_string('config.json'))
    result = configs['repositories']
    if filter_workspace:
        result = [repo for repo in configs['repositories']
                  if repo['workspace'] in filter_workspace]
    return result


def get_branch():
    # To update repositories
    configs = json.loads(env.resource_string('config.json'))
    return configs['version']


def get_workspace():
    return env.get_workspace()
