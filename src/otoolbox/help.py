from otoolbox import env
from otoolbox import base
from otoolbox.base import WorkspaceResource








###################################################################
# init
###################################################################
(env
    .add_resource(WorkspaceResource(
        path=env.get_workspace_path("README.md"),
        name="Workspace README",
        description="A readme that shows parts of the workspace",
        constructors=[
            env.constructor_copy_resource("data/WORKSPACE_README.md")
        ],
        destructors=[
            base.delete_file
        ],
        validators=[
            base.is_file, 
            base.is_readable
        ]
    ))
)