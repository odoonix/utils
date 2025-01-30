"""Loads basics of the workspace

Resources:
- .otoolbox

"""
from otoolbox import env
from otoolbox import utils










###################################################################
# init
###################################################################
def init():
    """Init the resources for the workspace
    """
    (env
        .add_resource(
            priority=100,
            path=".otoolbox",
            title="Workspace configuration directory",
            description="All configuration related to current workspace are located in this folder",
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
    )