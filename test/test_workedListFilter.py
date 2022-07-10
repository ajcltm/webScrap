import sys
from pathlib import Path
path = str(Path.cwd().joinpath('webScrap'))
print(path)
sys.path.append(path)
import workingListFilter
import core.work as work

import unittest

class TestWorkedList(unittest.TestCase):

    def setUp(self) -> None:
        dataList = [{'complexNo':'apartment1', 'ptp':'a_type'}, {'complexNo':'apartment2', 'ptp':'b_type'}]
        self.workingList = [work.Work(work=i) for i in dataList]

    def test_none_worked_list(self) -> None:
        workedList = None        
        workedPath = Path.cwd().joinpath('webScrap', 'test')
        wlf = workingListFilter.WorkingListFilter(workedFilePath=workedPath)
        return_value = wlf.filt_working_list(workedList=workedList, workingList=self.workingList)
        self.assertEqual(return_value, self.workingList)

    def test_worked_list(self) -> None:
        workedList_ = [i.get_file_name() for i in self.workingList]
        workedList = [f'{i}.pickle' for i in workedList_][:1]
        print(workedList)
        workedPath = Path.cwd().joinpath('webScrap', 'test')
        wlf = workingListFilter.WorkingListFilter(workedFilePath=workedPath)
        return_value = wlf.filt_working_list(workedList=workedList, workingList=self.workingList)
        self.assertEqual(return_value, self.workingList[-1:])



if __name__ == '__main__':
    unittest.main()