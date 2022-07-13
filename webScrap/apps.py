from webScrap.workingList import IWorkingList
from webScrap.workedList import IWorkedList, WorkedList
from webScrap.workingListFilter import IWorkingListFilter, WorkingListFilter
from webScrap.requester import IRequester
from webScrap.fileSaver import IFileSaver, PickleSaver
from tqdm import tqdm
from pathlib import Path


class SScraper:

    def __init__(self, IWorkingList:IWorkingList, IWorkedList:IWorkedList, IWorkingListFilter:IWorkingListFilter, IRequester:IRequester, IFileSaver:IFileSaver) -> None:
        self.wkngl = IWorkingList
        self.wkedl = IWorkedList
        self.wlf = IWorkingListFilter
        self.r = IRequester
        self.fs = IFileSaver

    def execute(self):
        working_list = self.wkngl.get_working_list()
        worked_list = self.wkedl.get_worked_list()
        notYetWorkedList = self.wlf.filt_working_list(workedList=worked_list, workingList=working_list)
    
        for iwork in tqdm(notYetWorkedList):
            try:
                data = self.r.request(iwork.get_request_key())
            except :
                data = None
                print(f'fail to get data : {iwork}')
            if data:
                self.fs.save_file(data, iwork.get_file_name())

class FSScraper:

    def __init__(self, IWorkingList:IWorkingList, IRequester:IRequester, save_path:Path) -> None:
        self.wkngl = IWorkingList
        self.wkedl = WorkedList(save_path)
        self.wlf = WorkingListFilter()
        self.r = IRequester
        self.fs = PickleSaver(save_path)

    def get_sscraper(self):
        return SScraper(IWorkingList=self.wkngl, IWorkedList=self.wkedl, IWorkingListFilter=self.wlf, IRequester=self.r, IFileSaver=self.fs)
        
    def execute(self):
        sscraper = self.get_sscraper()
        sscraper.execute()
        
        
