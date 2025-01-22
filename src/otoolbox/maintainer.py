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

from otoolbox import common
from otoolbox.utils import admin


def init_cli(parent_parser):
    """Init CLI to support maintainer tools
    """
    admin_parseer = parent_parser.add_parser('admin',)
    admin_subparser = admin_parseer.add_subparsers(
        title="Administrator Tools",
        description="""
            Tools and Utilites to help administrators. It makes simple to 
            keep dev repositories up to date.
        """)

    # dev update
    dev_update = admin_subparser.add_parser(
        'update',
        description="Update packages")
    dev_update.set_defaults(func=admin.update_repositories)
    common.add_repo_list_filter(dev_update)

    # admin info
    dev_info = admin_subparser.add_parser(
        'info',
        description="List packages")
    dev_info.set_defaults(func=admin.show_repositories)
    common.add_repo_list_filter(dev_info)

    return admin_parseer
