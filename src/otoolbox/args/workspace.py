"""Supports basic operation related to workspase"""

from otoolbox import env


def _init_resources(**kargs):
    resources = env.context.get('resources')
    resources.build()

def _delete_resources(**kargs):
    resources = env.context.get('resources')
    resources.destroy()

def init_cli(parent_parser):
    """Init CLI to support maintainer tools
    """
    init_parseer = parent_parser.add_parser(
        'init',
        description="""
            Tools and Utilites to help developers and maintainers. It makes simple to 
            keep dev repositories up to date.
        """)
    init_parseer.set_defaults(func=_init_resources)
    
    init_parseer.add_argument(
        '--odoo',
        dest='odoo_version',
        action='store',
        required=False
    )

    delete_parseer = parent_parser.add_parser(
        'delete',
        description="""
            Delete resources.
        """)
    delete_parseer.set_defaults(func=_delete_resources)
    

    return parent_parser
