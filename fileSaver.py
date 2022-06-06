from typing import Protocol
from pathlib import Path
import pickle

class FileSaver(Protocol):

    def execute(self, data:any):
        ...


class PickleSaver:

    def __init__(self, filePath:Path):
        self.filePath = filePath

    def execute(self, data:any) -> None:
        with open(self.filePath, 'wb') as fw:
            pickle.dump(data, fw, protocol=pickle.HIGHEST_PROTOCOL)


class FFileSaver:

    def __init__(self, code, mainPath):
        self.code = code
        self.filePath = mainPath.joinpath(f'{self.code}.pickle')

    def get_fileSaver(self):
        return PickleSaver(self.filePath)