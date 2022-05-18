import sys
parentPath='c:/Users/ajcltm/PycharmProjects/webScrap' # parent 경로
sys.path.append(parentPath) # 경로 추가

from dataRequests import IRequester
from fileSaver import FileSaver

class JsonDataScraper:

    def __init__(self, requester:IRequester, fileSaver:FileSaver):
        self.requester = requester
        self.fileSaver = fileSaver

    def execute(self):
        r = self.requester.execute()
        try:
             data = r.json()
        except :
            data = None
            print(r.status_code)

        if data:
            self.fileSaver.execute(data)
