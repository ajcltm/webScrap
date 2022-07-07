from typing import Protocol
from pathlib import Path
import os


class IWorkedList(Protocol):

    def get_worked_list():
        ...

class WorkedList:

    def get_worked_list(self, workedFilePath:Path):
        return os.listdir(workedFilePath)