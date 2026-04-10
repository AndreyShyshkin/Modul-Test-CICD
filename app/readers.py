from abc import ABC, abstractmethod
from typing import List
from app.models import Country


class DataReader(ABC):
    @abstractmethod
    def read(self, source: str) -> List[Country]:
        pass


class TxtFileReader(DataReader):
    def read(self, source: str) -> List[Country]:
        countries = []
        with open(source, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    countries.append(Country(
                        name=parts[0].strip(),
                        area=float(parts[1].strip()),
                        population=int(parts[2].strip())
                    ))
        return countries
