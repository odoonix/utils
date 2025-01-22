import sys
import argparse


from otoolbox import administrator
from otoolbox import developer
from otoolbox import maintainer
from otoolbox import env


if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "utils"
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

    return arg_parser, arg_parser.add_subparsers()


if __name__ == '__main__':
    parser, parent_parser = init_cli()
    administrator_parser = administrator.init_cli(parent_parser)
    developer_parser = developer.init_cli(parent_parser)
    maintainer_parser = maintainer.init_cli(parent_parser)

    args = parser.parse_args()
    env.context.update(args.__dict__)
    print(env.load_text_banner())
    args.func()
