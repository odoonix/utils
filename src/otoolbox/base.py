import os
import logging

_logger = logging.getLogger(__name__)

class WorkspaceResource():
    def __init__(
            self,
            path,
            title = None, 
            description = None,  
            constructors = None,
            destructors = None, 
            validators = None 
        ):
        self.path = path
        self.title = title
        self.description = description if description else []
        self.constructors = constructors if constructors else []
        self.destructors = destructors if destructors else []
        self.validators = validators if validators else []

        # internals
        self.validation_errors = []
        self.is_valied = False


class WorkspaceResourceGroup():
    def __init__(self):
        self.resources = []

    def append(self, resource:WorkspaceResource):
        self.resources.append(resource)
###################################################################
# constructors
###################################################################
def makedir(context):
    pass



###################################################################
# validators
###################################################################
def is_readable(context):
    pass

def is_dir(context):
    pass

def is_file(context:WorkspaceResource):
    pass



###################################################################
# destructors
###################################################################

