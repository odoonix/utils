#!/usr/bin/env python3
import argparse

from utils import develop
from utils import admin
from utils import repo
from utils import po_manage

def add_repo_list_filter(parser):
    parser.add_argument(
        '--oca',
        default=False,
        action='store_true')
    parser.add_argument(
        '--no-oca',
        dest='python',
        action='store_false')

    parser.add_argument(
        '--viraweb123',
        default=False,
        action='store_true')
    parser.add_argument(
        '--no-viraweb123',
        dest='python',
        action='store_false')

    parser.add_argument(
        '--moonsunsoft',
        default=False,
        action='store_true')
    parser.add_argument(
        '--no-moonsunsoft',
        dest='python',
        action='store_false')


parser = argparse.ArgumentParser(
    prog='odoo-util',
    description='ViraWeb123 Odoo Utility',
    epilog='Text at the bottom of help')
parser.add_argument(
    '-v',
    '--verbose',
    action='count',
    default=0)
parser.add_argument(
    '-P',
    '--proxy',
    default=None)
_dev = parser.add_subparsers(
    title='ViraWeb123 Odoo Tools',
    description="""
        Tools and Utilites to help developers and administrators. It makes simple to 
        keep dev environment up to date.
    """)

#####################################################################
#                      Developer Toolse                             #
#####################################################################
_dev_parseer = _dev.add_parser('dev')
dev = _dev_parseer.add_subparsers(
    title='Developer Tools',
    description="""
        Tools and Utilites to help developer. It makes simple to 
        keep dev environment up to date.
    """)

# dev init
dev_init = dev.add_parser(
    'init',
    description='Initialize the development environment')
add_repo_list_filter(dev_init)

dev_init.add_argument(
    '--ubuntu',
    help="""Install all required tools for Ubuntu""",
    action='store_true',
    default=False)
dev_init.add_argument(
    '--no-ubuntu',
    dest='ubuntu',
    action='store_false')

dev_init.add_argument(
    '--vscode',
    default=False,
    action='store_true')
dev_init.add_argument(
    '--no-vscode',
    dest='vscode',
    action='store_false')

dev_init.add_argument(
    '--docker',
    default=False,
    action='store_true')
dev_init.add_argument(
    '--no-docker',
    dest='docker',
    action='store_false')

dev_init.add_argument(
    '--repo',
    default=False,
    action='store_true')
dev_init.add_argument(
    '--no-repo',
    dest='repo',
    action='store_false')

dev_init.add_argument(
    '--python',
    default=False,
    action='store_true')
dev_init.add_argument(
    '--no-python',
    dest='python',
    action='store_false')



dev_init.set_defaults(func=develop.init)


# dev update
dev_update = dev.add_parser(
    'update',
    description="Update packages")
dev_update.set_defaults(func=develop.update)
add_repo_list_filter(dev_update)

#####################################################################
#                          Admin Toolse                             #
#####################################################################
admin_parseer = _dev.add_parser('admin',)
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
add_repo_list_filter(dev_update)

# admin info
dev_info = admin_subparser.add_parser(
    'info',
    description="List packages")
dev_info.set_defaults(func=admin.show_repositories)
add_repo_list_filter(dev_info)

# odoo module information
dev_module_info = admin_subparser.add_parser('status', description='Odoo modules information')
dev_module_info.add_argument(
    '--odoo',
    type = int,
    action='append',
    dest='version',
)
dev_module_info.add_argument(
    '--workspace',
    action ='append',
    dest ='workspace',
)
dev_module_info.add_argument(
    '--addons=all',
    dest ='addons',
    action='store_false'
)
dev_module_info.set_defaults(func=admin.supported_addons)

#####################################################################
#                       Translate po module                         #
#####################################################################
localization_parser = _dev.add_parser('localization')
localization_subparser = localization_parser.add_subparsers(
    title="Localization",
    description="This is localization"
)

dev_translate = localization_subparser.add_parser(
    'translate',
    description="Translate packages"
)

dev_translate.add_argument(
    '--input',
    dest='address', 
    type=str,  
    help="Input string for address"
)

dev_translate.add_argument(
    '--language',
    dest='language', 
    type=str,  
    help="Input string for Language"
)

dev_translate.add_argument(
    '--apikey',
    dest='apikey', 
    type=str,  
    help="Input Access token from OpenAI"
)
dev_translate.set_defaults(func=po_manage.process_po_file) 


 
if __name__ == '__main__':
    args = parser.parse_args()
    if args.verbose:
        print("Odoo version :{}".format(repo.get_branch()))
    args.func(**args.__dict__)
