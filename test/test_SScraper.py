import unittest
from unittest.mock import Mock
from pathlib import Path
from webScrap import work, workingListFilter, fileSaver, apps

class TestSScraper(unittest.TestCase):

    def test_valid_sscraper(self):
        work_data = [{'key': '1234'}, {'key': '2345'}]

        wkngl = Mock()
        wkngl.get_working_list.return_value = [work.Work(work=i) for i in work_data]
        
        wkedl = Mock()
        wkedl.get_worked_list.return_value = [f'{work.Work(work=work_data[0]).get_file_name()}.pickle']

        request = Mock()
        r = Mock()
        r.json.return_value = {'data_key' : 'data_value'}
        request.get_request_r.return_value = r

        file_path = Path.cwd().joinpath('test')
        print(file_path)
        fs = fileSaver.PickleSaver(file_path)

        ss = apps.SScraper(IWorkingList=wkngl, IWorkedList=wkedl, IWorkingListFilter=workingListFilter.WorkingListFilter(), IRequester=request, IFileSaver=fs)
        ss.execute()
    
if __name__ == '__main__':
    unittest.main()

