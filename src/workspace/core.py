import abc
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

    @abc.abstractmethod
    def flatten(self):
        pass
    
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

    def flatten(self):
        for cp in self.path().iterdir():
            if cp.is_file():
                yield (self.path().name, cp.name), cp
            elif cp.is_dir():
                for fcp in self.subspace(cp.name).flatten():
                    _cp, _p = fcp
                    yield (self.path().name, *_cp), _p

