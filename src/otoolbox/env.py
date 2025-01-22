"""Envirnement fo the sysetm"""

import pkg_resources

VERSION = "0.0.0"
context = {}


def load_text_banner():
    """Load texu"""
    data = resource_string("banner.txt")
    return data.format(version=VERSION)


def resource_string(resource_name, encoding="utf-8"):
    """Load resource"""
    return pkg_resources.resource_string("otoolbox", resource_name).decode(encoding)


def resource_stream(resource_name):
    """Load resource"""
    return pkg_resources.resource_stream("otoolbox", resource_name)


def get_workspace():
    """Get the workspace"""
    return context.get("path", ".")
