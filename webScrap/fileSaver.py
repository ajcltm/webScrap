from typing import Protocol
from pathlib import Path
import pickle

class IFileSaver(Protocol):

    def save_file(self, data:any, file_name:str):
        ...


class PickleSaver:

    def __init__(self, filePath:Path):
        self.filePath = filePath

    def save_file(self, data:any, file_name:str) -> None:
        save_path = self.filePath.joinpath(f'{file_name}.pickle')
        with open(save_path, 'wb') as fw:
            pickle.dump(data, fw, protocol=pickle.HIGHEST_PROTOCOL)