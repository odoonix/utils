import sys


# from . import administrator
# from . import developer
# from . import maintainer


# if sys.version_info[:2] >= (3, 8):
#     # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
#     from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
# else:
#     from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

# try:
#     # Change here if project is renamed and does not equal the package name
#     dist_name = "utils"
#     __version__ = version(dist_name)
# except PackageNotFoundError:  # pragma: no cover
#     __version__ = "unknown"
# finally:
#     del version, PackageNotFoundError


def run():
    print("Running utils v" + "__version__")


if __name__ == '__main__':
    run()
