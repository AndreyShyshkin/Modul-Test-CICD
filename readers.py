from abc import ABC, abstractmethod
from typing import List
from models import Country

class DataReader(ABC):
    @abstractmethod
    def read(self, source: str) -> List[Country]:
        pass