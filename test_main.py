import pytest
from main import parse_file, sort_by_area, sort_by_population

@pytest.fixture
def sample_data():
    return [
        {'country': 'Ukraine', 'area': 603628, 'population': 40000000},
        {'country': 'Monaco', 'area': 2, 'population': 38000},
        {'country': 'USA', 'area': 9833517, 'population': 331000000}
    ]