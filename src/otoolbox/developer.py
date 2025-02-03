"""The **Developer** module in Odoonix Toolbox streamlines DevOps processes for Odoo 
developers by automating tasks, managing environments, and simplifying workflows.

The **Developer** module in the Odoonix Toolbox is a specialized tool designed to 
streamline the DevOps processes for Odoo developers. It provides utilities for 
automating repetitive tasks, managing development environments, and simplifying 
workflows. With features such as addon management, environment configuration, 
database handling, and integration tools, the Developer module empowers developers 
to focus on coding and innovation rather than setup and maintenance. This module 
bridges the gap between development and operations, enhancing productivity and 
ensuring a seamless development experience in Odoo projects.
"""
import typer

# from otoolbox.args import common
# from otoolbox.repositories import develop

app = typer.Typer()



@app.command()
def update():
    # # 1- load all repositories
    # admin.update_repositories(**kargs)

    # # TODO: check if need to update settings
    pass



# def init_cli(parent_parser):
#     """ Init parser and adds developer options
#     """

#     developer_cli_parser = parent_parser.add_parser('dev')
#     dev = developer_cli_parser.add_subparsers(
#         title='Developer Tools',
#         description="""
#             Tools and Utilites to help developer. It makes simple to 
#             keep dev environment up to date.""")

#     # dev init
#     dev_init = dev.add_parser(
#         'init',
#         description='Initialize the development environment')
#     common.add_repo_list_filter(dev_init)

#     dev_init.add_argument(
#         '--ubuntu',
#         help="""Install all required tools for Ubuntu""",
#         action='store_true',
#         default=False)
#     dev_init.add_argument(
#         '--no-ubuntu',
#         dest='ubuntu',
#         action='store_false')

#     dev_init.add_argument(
#         '--vscode',
#         default=False,
#         action='store_true')
#     dev_init.add_argument(
#         '--no-vscode',
#         dest='vscode',
#         action='store_false')

#     dev_init.add_argument(
#         '--docker',
#         default=False,
#         action='store_true')
#     dev_init.add_argument(
#         '--no-docker',
#         dest='docker',
#         action='store_false')

#     dev_init.add_argument(
#         '--repo',
#         default=False,
#         action='store_true')
#     dev_init.add_argument(
#         '--no-repo',
#         dest='repo',
#         action='store_false')

#     dev_init.add_argument(
#         '--python',
#         default=False,
#         action='store_true')
#     dev_init.add_argument(
#         '--no-python',
#         dest='python',
#         action='store_false')

#     # dev_init.set_defaults(func=develop.init)

#     # dev update
#     dev_update = dev.add_parser(
#         'update',
#         description="Update packages")
#     dev_update.set_defaults(func=develop.update)
#     common.add_repo_list_filter(dev_update)

#     return developer_cli_parser
