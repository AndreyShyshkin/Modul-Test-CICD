from typing import List
from app.models import Country


class CountrySorter:
    def __init__(self, countries: List[Country]):
        self._countries = countries

    def by_area(self) -> List[Country]:
        return sorted(self._countries, key=lambda c: c.area, reverse=True)

    def by_population(self) -> List[Country]:
        return sorted(self._countries, key=lambda c: c.population, reverse=True)
