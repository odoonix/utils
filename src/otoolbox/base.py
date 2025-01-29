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
            validators = None,
            priority=10,
        ):
        self.path = path
        self.title = title
        self.description = description if description else []
        self.constructors = constructors if constructors else []
        self.destructors = destructors if destructors else []
        self.validators = validators if validators else []
        self.priority = priority

        # internals
        self.validation_errors = []
        self.is_valied = False

    def build(self, **kargs):
        for constructor in self.constructors:
            constructor(context=self, **kargs)

    def destroy(self, **kargs):
        for destructor in self.destructors:
            destructor(context=self, **kargs)

    def verify(self, **kargs):
        for validator in self.validators:
            validator(context=self, **kargs)

class WorkspaceResourceGroup(WorkspaceResource):
    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.resources = kargs.get('resources', [])

    def append(self, resource:WorkspaceResource):
        self.resources.append(resource)
        self.resources = sorted(self.resources, key=lambda x: x.priority, reverse=True)

    def build(self, **kargs):
        for resource in self.resources:
            resource.build(**kargs)
        super().build(**kargs)

    def destroy(self, **kargs):
        for resource in self.resources:
            resource.destroy(**kargs)
        super().destroy(**kargs)

    def verify(self, **kargs):
        for resource in self.resources:
            resource.verify(**kargs)
        super().verify(**kargs)

    def get(self, path, default=False, **kargs):
        for resource in self.resources:
            if resource.path == path:
                return resource
        return default
            
        
