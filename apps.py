import sys
from pathlib import Path
sys.path.append(str(Path.cwd().joinpath('webScrap')))
from workingList import IWorkingList
from workingListFilter import IWorkingListFilter
from requester import IRequester
from fileSaver import IFileSaver
from tqdm import tqdm

class SScraper:

    def __init__(self, workingList:IWorkingList, workingListFilter:IWorkingListFilter, requester:IRequester, fileSaver:IFileSaver) -> None:
        self.wl = workingList
        self.wlf = workingListFilter
        self.r = requester
        self.fs = fileSaver

    def execute(self):
        working_list = self.wl.get_working_list()
        notYetWorkedList = self.wlf.filt_working_list(working_list)

        for iwork in tqdm(notYetWorkedList):
            r = self.r.get_request_r(iwork.get_request_key())
            try:
                data = r.json()
            except :
                data = None
                print(f'fail to get data : {r.status_code}')
            if data:
                self.fs.save_file(data, iwork.get_file_name())


        
