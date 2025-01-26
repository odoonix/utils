"""Envirnement fo the sysetm"""

import pkg_resources
import os
import sys
from otoolbox import base

VERSION = "0.0.0"
context = {
    'resources': {}
}




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

def get_workspace_path(path):
    """Gets subfolder/file with in workspace"""
    return os.path.join(get_workspace(), path)



#################################################################################
# Resource
#################################################################################
def add_resource(resource:base.WorkspaceResource):
    group = context['resources'].get(resource.path, None)
    if not group:
        group = base.WorkspaceResourceGroup()
    group.append(resource)
    return sys.modules[__name__]

def constructor_copy_resource(path):
    """Create a constructor to copy resource with path"""
    def copy_resource(resource:base.WorkspaceResource):
        resource_stream = resource_stream(path)
        # Open the output file in write-binary mode
        with open(resource.path, 'wb') as out_file:
            # Read from the resource stream and write to the output file
            out_file.write(resource_stream.read())
    return copy_resource