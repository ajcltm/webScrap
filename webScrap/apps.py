from webScrap.workingList import IWorkingList
from webScrap.workedList import IWorkedList
from webScrap.workingListFilter import IWorkingListFilter
from webScrap.requester import IRequester
from webScrap.fileSaver import IFileSaver
from tqdm import tqdm

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
            r = self.r.get_request_r(iwork.get_request_key())
            try:
                data = r.json()
            except :
                data = None
                print(f'fail to get data : {r.status_code}')
            if data:
                self.fs.save_file(data, iwork.get_file_name())


        
