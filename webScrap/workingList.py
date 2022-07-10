from webScrap.work import IWork
from typing import Protocol, List

class IWorkingList(Protocol):

    def get_working_list(self)->List[IWork]:
        ...