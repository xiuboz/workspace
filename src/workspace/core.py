import abc
import os
from pathlib import Path

class AbstractWorkspace(abc.ABC):

    def __init__(
        self,
        path: str,
        parent: 'AbstractWorkspace' = None,
    ):
        # print(path, parent.path() if parent else None)
        self._parent: 'AbstractWorkspace' = parent
        self._path: Path = Path(path) if self._parent is None else self._parent.subpath(path)
        self._path.mkdir(parents=True, exist_ok=True)  # make sure our _path exists; creat it otherwise.
        pass
    
    def subpath(self, name: str) -> Path:
        return self._path.joinpath(name)

    @abc.abstractmethod
    def subspace(
        self, 
        name: str
    ) -> 'AbstractWorkspace' :
        pass

    def path(self) -> Path:
        return self._path
    
    def __str__(self) -> str:
        return str(self.path())


class Workspace(AbstractWorkspace):

    def __init__(
        self,
        path: str,
        parent: AbstractWorkspace = None,
    ): 
        super().__init__(path, parent)
        
    
    def subspace(
        self, 
        name: str
    ) -> AbstractWorkspace:
        return Workspace(name, self)

    

    
