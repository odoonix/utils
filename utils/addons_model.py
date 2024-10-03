
class AddonsModel:
    def __init__(self, workspace:str, name:str, description:str, versions_odoons:str=[], is_private=False, status:int=0, *args, **kwargs) -> None:
        self._workspace = workspace
        self._name = name
        self._versions_odoons = versions_odoons
        self._is_private = is_private
        self._status = status
        self._description = description
    

    @property
    def workspace(self):
        return self._workspace

    @workspace.setter
    def workspace(self, value):
        self._workspace = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def versions_odoons(self):
        return self._versions_odoons

    @versions_odoons.setter
    def versions_odoons(self, value):
        self._versions_odoons = value

    @property
    def is_private(self):
        return self._is_private

    @is_private.setter
    def is_private(self, value):
        self._is_private = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value



    def __str__(self) -> str:
        return self._workspace+"  "+self._name+"  "+self._versions_odoons+"  "+self._is_private        

