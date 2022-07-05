import sys
from pathlib import Path
sys.path.append(Path.cwd().joinpath('webScap'))
from work import IWork
from typing import Protocol, List

class IWorkingList(Protocol):

    def get_working_list(self)->List[IWork]:
        ...