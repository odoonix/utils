"""The **Maintainer** Python package offers CLI tools for automating package updates, 
repository tracking, database management, and backups.

The **Maintainer** Python package is a powerful CLI utility designed to simplify the 
workflows of software maintainers. It provides commands for automating essential 
maintenance tasks, such as updating packages, tracking changes in repositories, 
managing and inspecting databases, and creating backups. This tool helps ensure systems 
remain up-to-date, secure, and efficient, while reducing manual overhead. Whether 
managing single projects or complex multi-repository environments, the Maintainer 
package offers a reliable and streamlined solution for maintenance operations.
"""
import typer



from otoolbox import env
# from otoolbox.repositories import admin


app = typer.Typer()


def _filter_resources():
    resources = (
        env.context
            .get('resources')
            .filter(lambda resource: resource.has_tag('git'))
    )
    return resources;

@app.command()
def info():
    """Display information about the workspace"""
    pass

@app.command()
def init():
    """Initialize all resources from addons into the current workspace"""
    return _filter_resources().build()

@app.command()
def update():
    """Updates current workspace to the latest version"""
    return _filter_resources().update()




# def add_repo_list_filter(parser):
#     parser.add_argument(
#         '--oca',
#         default=False,
#         action='store_true')
#     parser.add_argument(
#         '--no-oca',
#         dest='python',
#         action='store_false')

#     parser.add_argument(
#         '--viraweb123',
#         default=False,
#         action='store_true')
#     parser.add_argument(
#         '--no-viraweb123',
#         dest='python',
#         action='store_false')

#     parser.add_argument(
#         '--moonsunsoft',
#         default=False,
#         action='store_true')
#     parser.add_argument(
#         '--no-moonsunsoft',
#         dest='python',
#         action='store_false')
    
# def init_cli(parent_parser):
#     """Init CLI to support maintainer tools
#     """
#     admin_parseer = parent_parser.add_parser('admin',)
#     admin_subparser = admin_parseer.add_subparsers(
#         title="Administrator Tools",
#         description="""
#             Tools and Utilites to help administrators. It makes simple to 
#             keep dev repositories up to date.
#         """)

#     # dev update
#     dev_update = admin_subparser.add_parser(
#         'update',
#         description="Update packages")
#     dev_update.set_defaults(func=admin.update_repositories)
#     common.add_repo_list_filter(dev_update)

#     # admin info
#     dev_info = admin_subparser.add_parser(
#         'info',
#         description="List packages")
#     dev_info.set_defaults(func=admin.show_repositories)
#     common.add_repo_list_filter(dev_info)

#     return admin_parseer
