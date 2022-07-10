import sys
from pathlib import Path
# sys.path.append(str(Path.cwd()))
import unittest
from core import fileSaver
from core import work
import pickle
import os
import requester

class TestFileSaver(unittest.TestCase):

    def tearDown(self) -> None:
        os.remove(self.saved_file_path)

    def test_valid_data_saver(self):
        work_data = {'complexNo':"20220709", 'ptp':'a_type'}
        data = {'complexNo':"20220709", 'ptp':'a_type', 'price': 50000}
        w = work.Work(work=work_data)
        file_path = Path.cwd()
        fs = fileSaver.PickleSaver(filePath=file_path)
        fs.save_file(data, w.get_file_name())
        self.saved_file_path = f'{file_path.joinpath(w.get_file_name())}.pickle'
        with open(self.saved_file_path, mode='rb') as fr:
            load_data = pickle.load(fr)

        self.assertEqual(data, load_data)

if __name__ == '__main__':
    unittest.main()