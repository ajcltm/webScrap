from typing import Protocol
import requests

class IRequester(Protocol):

    def execute(self):
        ...


class GetReqester:

    def __init__(self, url:str, params:dict) -> None :
        self.url = url
        self.params = params

    def execute(self):
        return requests.get(url=self.url, params=self.params)

class PostRequester:

    def __init__(self, url:str, params=None, dataForms=None):
        self.url = url
        self.params = params
        self.dataForms = dataForms

    def execute(self):
        if not self.params:
            return requests.post(url=self.url, data=self.dataForms)
        
        elif not self.dataForms:
            return requests.post(url=self.url, params=self.params)
        
        else:
            return requests.post(url=self.url, params=self.params, data=self.dataForms)