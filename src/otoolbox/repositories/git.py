
import os

from otoolbox import env
from otoolbox import utils


def git_clone(context):
    """Clone the git repository from github
    """
    branch_name = env.context.get("odoo_version", "18.0")
    cwd = os.path.dirname(context.path)
    depth = env.context.get("depth", "1")

    result = utils.call_process_safe([
        'git',
        'clone',
        '--branch', branch_name,
        '--depth', depth,
        f"git@github.com:{context.path}.git"
    ], cwd=cwd)

    if result != 0:
        raise Exception("Fail to update the repository")
