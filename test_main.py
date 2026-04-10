import pytest
from main import parse_file, sort_by_area, sort_by_population

@pytest.fixture
def sample_data():
    return [
        {'country': 'Ukraine', 'area': 603628, 'population': 40000000},
        {'country': 'Monaco', 'area': 2, 'population': 38000},
        {'country': 'USA', 'area': 9833517, 'population': 331000000}
    ]

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test_data.txt"
    file.write_text("Ukraine, 603628, 40000000\nMonaco, 2, 38000\nUSA, 9833517, 331000000")
    return str(file)

def test_parse_file(temp_file):
    result = parse_file(temp_file)
    assert len(result) == 3
    assert result[0]['country'] == 'Ukraine'