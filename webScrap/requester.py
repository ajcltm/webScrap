from typing import Protocol, Dict

class IRequester(Protocol):

    def request(self, key:Dict):
        ...