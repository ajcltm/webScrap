from typing import Protocol, List
import os
from webScrap.work import IWork

class IWorkingListFilter(Protocol):

    # def filt_working_list(self, workedList:List, workingList:List[IWork]) -> List[IWork] :
        # ...
    def filt_working_list() :
        ...


class WorkingListFilter:

    def filt_working_list(self, workedList:List, workingList:List[IWork]) -> List[IWork]:
        if not workedList:
            return workingList
        suffix = os.path.splitext(workedList[0])[-1]
        notYetWorkedList = [i for i in workingList if not f'{i.get_file_name()}{suffix}' in workedList]                
        return notYetWorkedList