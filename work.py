from typing import Protocol, Dict
from dataclasses import dataclass

class IWork(Protocol):

    def get_request_key(self):
        ...
    
    def get_file_name(self):
        ...

@dataclass
class Work:
    work : dict

    def get_request_key(self)->Dict:
        return self.work
    
    def get_file_name(self)->str:
        key_part = '_'.join(s for s in list(self.work.keys()))
        value_part = '_'.join(s for s in list(self.work.values()))
        return f'{key_part}_{value_part}'