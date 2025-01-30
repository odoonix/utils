"""Envirnement fo the sysetm"""

import pkg_resources
import os
import sys
from otoolbox.base import (
    WorkspaceResource,
    WorkspaceResourceGroup
)

VERSION = "0.1.0"
context = {
    'version': VERSION,
    'author': "Odoonix",
    'email': "info@odoonix.com",
    'website': "https://odoonix.com",
    'github': "https://githubs.com/odoonix",
    'resources': WorkspaceResourceGroup(
        path='virtual://',
        title="Root Resource"
    )
}


def resource_string(resource_name, encoding="utf-8"):
    """Load resource"""
    return pkg_resources.resource_string("otoolbox", resource_name).decode(encoding)


def resource_stream(resource_name):
    """Load resource"""
    return pkg_resources.resource_stream("otoolbox", resource_name)


def get_workspace():
    """Get the workspace"""
    return context.get("path", ".")


def get_workspace_path(path):
    """Gets subfolder/file with in workspace"""
    return os.path.join(get_workspace(), path)


#################################################################################
# Resource
#################################################################################
def add_resource(**kargs):
    resource = WorkspaceResource(**kargs)
    path = kargs.get('path')
    group = context['resources'].get(path)
    if not group:
        group = WorkspaceResourceGroup(path=path)
    group.append(resource)
    context['resources'].append(group)
    return sys.modules[__name__]
