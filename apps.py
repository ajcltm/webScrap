import sys
from pathlib import Path
sys.path.append(str(Path.cwd().joinpath('webScrap')))
import fileSaver
import os
from tqdm import tqdm


class SScraper:

    def __init__(self, FReqeuster, working_list, main_path):
        self.fr = FReqeuster
        self.wl = working_list
        self.mp = main_path

    def execute(self):
        start_point = self.get_start_point()
        if start_point == None:
            exit()
        list_to_work = self.wl[start_point:]
        for i in tqdm(list_to_work):
            r = self.fr(i).get_requester()
            try:
                data = r.json()
            except :
                data = None
                print(f'fail to get data : {r.status_code}')
            if data:
                fileSaver.FFileSaver(i, self.mp).get_fileSaver().execute(data)

    def get_start_point(self):
        worked_lst = os.listdir(self.mp)
        if not worked_lst: 
            return 0
        for i in self.wl:
            if not f'{i}.pickle' in worked_lst:
                return self.wl.index(i)
        return None
