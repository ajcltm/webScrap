from typing import Protocol, List
import os
from pathlib import Path
from work import IWork

class IWorkingListFilter(Protocol):

    def filt_working_list(self, workingList:List[IWork]) -> List[IWork] :
        ...


class WorkingListFilter:

    def __init__(self,workedFilePath:Path)->None:
        self.workedFilePath = workedFilePath

    def filt_working_list(self, workedList:List, workingList:List[IWork]) -> List[IWork]:
        if not workedList:
            return workingList
        suffix = os.path.splitext(str(self.workedFilePath.joinpath(workedList[0])))[-1]
        notYetWorkedList = [i for i in workingList if not f'{i.get_file_name()}{suffix}' in workedList]                
        return notYetWorkedList