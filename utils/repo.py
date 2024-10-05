import os
import json
import subprocess
from . import linux
from .addons_model import AddonsModel
import re


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
    directory = get_workspace()
    configs = {}
    with open(directory+'/utils/config.json') as config_file:
        configs = json.load(config_file)

    result = configs['repositories']
    if filter_workspace:
        result = [repo for repo in configs['repositories']
                  if repo['workspace'] in filter_workspace]
    return result

###########
def get_workspace_module(url:str) -> str:
    workspace = ''
    match = re.search(r'https://github\.com/([^/]+)/', url)
    if match:
        workspace = match.group(1)
    else:
        print("No workspace found.")
    return workspace

def get_versions_module(result) -> list[str]:
         versions=[]
         output = result.stdout
         lines = output.splitlines()
         numbers = [line.split('/')[-1].strip() for line in lines if line.strip()]
         versions = [item for item in numbers if item == "16.0" or item == "17.0"]
         return versions

def get_name_module(url:str) -> str:
    name = ''
    match = re.search(r'https://github\.com/([^/]+)/([^/]+)', url)
    if match:
        name = match.group(2).rstrip('.git')
    else:
        print("No name found.")
    return name


def get_addons_module(repo_path_list:str) -> list[AddonsModel]:
    result_version:AddonsModel = []
    
    for repo_path in repo_path_list:
            result = linux.get_addons_version(repo_path)
            if result:
                verson_list = get_versions_module(result)
                name_module = get_name_module(repo_path)
                workspace_module = get_workspace_module(repo_path)
                if verson_list and workspace_module and name_module:
                    addons = AddonsModel(workspace=workspace_module, description='Successfully loaded!',name=name_module, versions_odoons=verson_list)
                    addons.status = 1
                    result_version.append(addons)
                else:
                    addons = AddonsModel(workspace=workspace_module, description='.No matching version found.',name=name_module, versions_odoons=['', ''], status=2)
                    result_version.append(addons)                
    return result_version



def get_branch():
    # To update repositories
    directory = get_workspace()
    configs = {}
    with open(directory+'/utils/config.json') as config_file:
        configs = json.load(config_file)
    return configs['version']


def get_workspace():
    return os.path.dirname(os.path.abspath(__file__)) + '/../..'




    