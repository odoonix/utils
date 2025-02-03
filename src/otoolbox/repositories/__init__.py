"""Adds resources to manage repositories

Resources:
- .otoolbox/repositoires.json

"""
import os
import json

from otoolbox import env
from otoolbox import utils

from otoolbox.repositories import git


REPOSITORIES_PATH = ".otoolbox/repositoires.json"
RESOURCE_REPOSITORIES_PATH = "data/repositories.json"
###################################################################
# init
###################################################################

# Load repositories as resources
# If no repository found, then default list will be loaded


def _load_repositories():
    reposiotires_path = env.get_workspace_path(REPOSITORIES_PATH)
    data = False
    if os.path.isfile(reposiotires_path):
        with open(reposiotires_path, 'r', encoding="utf8") as f:
            data = f.read()

    if not data:
        data = env.resource_string(RESOURCE_REPOSITORIES_PATH)
    repo_list = json.loads(data)
    workspaces = []
    for item in repo_list:
        env.add_resource(
            path="{}/{}".format(item["workspace"], item["name"]),
            title="Git repository: {}/{}".format(item["workspace"], item["name"]),
            description="""Automaticaly added resources from git.""",
            constructors=[
                git.git_clone
            ],
            destructors=[],
            validators=[]
        )
        if item["workspace"] not in workspaces:
            workspaces.append(item["workspace"])

    for workspace in workspaces:
        env.add_resource(
            priority=11,
            path="{}".format(workspace),
            title="Git workspace: {}".format(workspace),
            description="""Automaticaly added resources from git workspace.""",
            constructors=[
                utils.makedir
            ],
            destructors=[
                utils.delete_dir
            ],
            validators=[
                utils.is_dir,
                utils.is_readable
            ]
        )


def init():
    """Init the resources for the workspace
    """
    (env
        .add_resource(
            priority=100,
            path=REPOSITORIES_PATH,
            title="List of managed repositories",
            description="Adding, removing, and updating repositories in the workspace is done through this file",
            constructors=[
                utils.constructor_copy_resource(RESOURCE_REPOSITORIES_PATH)
            ],
            destructors=[
                utils.delete_file
            ],
            validators=[
                utils.is_file,
                utils.is_readable
            ]
        )
     )
    _load_repositories()
