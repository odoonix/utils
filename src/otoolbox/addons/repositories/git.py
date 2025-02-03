
import os

from otoolbox import env
from otoolbox import utils


def git_clone(context):
    """Clone the git repository from github
    """
    branch_name = env.context.get("odoo_version", "18.0")
    cwd = env.get_workspace_path(context.parent)
    depth = env.context.get("depth", "1")

    result = utils.call_process_safe([
        'git',
        'clone',
        '--branch', branch_name,
        '--depth', depth,
        f"git@github.com:{context.path}.git"
    ], cwd=cwd)

    if result != 0:
        raise AssertionError("Fail to update the repository")



def git_pull(context):
    """Pull the git repository from github
    """
    cwd = os.path.dirname(context.path)
    result = utils.call_process_safe([
        'git',
        'pull',
        f"git@github.com:{context.path}.git"
    ], cwd=cwd)

    if result != 0:
        raise AssertionError("Fail to update the repository")
