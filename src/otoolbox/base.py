import os
import logging

_logger = logging.getLogger(__name__)


class WorkspaceResource():
    def __init__(
        self,
        path,
        title=None,
        description=None,
        constructors=None,
        destructors=None,
        validators=None,
        updates=None,
        tags=None,
        priority=10,
    ):
        self.path = path
        self.title = title
        self.description = description if description else []
        self.constructors = constructors if constructors else []
        self.destructors = destructors if destructors else []
        self.validators = validators if validators else []
        self.tags = tags if tags else []
        self.updates = updates if updates else []
        self.priority = priority

        # internals
        self.validation_errors = []
        self.is_valied = False

    def build(self, **kargs):
        """Launch all build function"""
        for constructor in self.constructors:
            constructor(context=self, **kargs)

    def destroy(self, **kargs):
        """Launch all destroy function"""
        for destructor in self.destructors:
            destructor(context=self, **kargs)

    def verify(self, **kargs):
        """Launch all verifiy function"""
        for validator in self.validators:
            validator(context=self, **kargs)

    def update(self, **kargs):
        """Launch all updates function"""
        for udpdate in self.updates:
            udpdate(context=self, **kargs)


class WorkspaceResourceGroup(WorkspaceResource):
    """Group of resources

    If there are many resources that are related to each other, it is possible to group them in a group.
    """

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.resources = kargs.get('resources', [])

    def append(self, resource: WorkspaceResource):
        """Appends new resource to the group"""
        self.resources.append(resource)
        self.resources = sorted(self.resources, key=lambda x: x.priority, reverse=True)
        self.priority = self.resources[0].priority
        self.title = self.resources[0].title
        self.description = self.resources[0].description

    def get(self, path, default=False, **kargs):
        """Gets resources"""
        for resource in self.resources:
            if resource.path == path:
                return resource
        return default

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
