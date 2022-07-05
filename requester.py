from typing import Protocol, Dict

class IRequester(Protocol):

    def get_request_r(self, key:Dict):
        ...