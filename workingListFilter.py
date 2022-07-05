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

    def filt_working_list(self, workingList:List[IWork]) -> List[IWork]:
        workedLst = os.listdir(self.workedFilePath)
        if not workedLst:
            return workingList
        suffix = os.path.splitext(str(self.mp.joinpath(workedLst[0])))[-1]
        notYetWorkedList = [i for i in workingList if not f'{i.get_file_name()}.{suffix}' in workedLst]                
        return notYetWorkedList