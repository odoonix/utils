import sys
import argparse
import importlib
import chevron


from otoolbox import args
from otoolbox import env


if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "otoolbox"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError


def init_cli():
    """Initialize the command-line interface for the Odoo Toolbox."""
    arg_parser = argparse.ArgumentParser(
        prog='odoo-util',
        description="""
            Odoonix Toolbox is a comprehensive suite of tools designed to streamline 
            the workflows of developers and maintainers working with Odoo. It 
            simplifies tasks such as tracking changes in addons, cloning 
            repositories, managing databases, and configuring development 
            environments. With its user-friendly interface and automation 
            features, Odoonix Toolbox enables teams to maintain consistency, 
            reduce manual effort, and speed up development cycles. By integrating 
            essential functionalities into one cohesive package, it empowers 
            developers to focus on creating and maintaining high-quality Odoo 
            solutions efficiently.
        """,
        epilog='Developer toolbox'
    )

    arg_parser.add_argument(
        "--path",
        help="""The workspace directory, default is current directory""",
        action="store",
        dest="path",
        required=False,
        default=".")

    arg_parser.add_argument(
        "--verbose",
        help="""The workspace directory, default is current directory""",
        action="count",
        dest="verbose",
        required=False,
        default=0)

    arg_parser.add_argument(
        "--silent",
        help="""Do not print extra information""",
        action="count",
        dest="silent",
        required=False,
        default=0)

    return arg_parser, arg_parser.add_subparsers()


def load_resources(*args):
    def call_init(package_name):
        # Import the package dynamically
        package = importlib.import_module(package_name)

        # Check if the package has an __init__ method and call it if it exists
        if hasattr(package, 'init'):
            package.init()

    # Example usage
    for path in args:
        call_init(path)


if __name__ == '__main__':
    # Init resources
    load_resources(
        'otoolbox.help',
        'otoolbox.workspace',
        'otoolbox.ubuntu',
        'otoolbox.vscode',
        'otoolbox.repositories'
    )

    # Init arguments
    parser, parent_parser = init_cli()
    args.workspace.init_cli(parent_parser)
    args.developer.init_cli(parent_parser)
    args.maintainer.init_cli(parent_parser)

    args = parser.parse_args()
    env.context.update(args.__dict__)
    if not env.context.get('silent', 0):
        print(chevron.render(
            template=env.resource_string("data/banner.txt"),
            data=env.context
        ))
    args.func()
