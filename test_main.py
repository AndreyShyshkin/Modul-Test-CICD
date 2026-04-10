import pytest
from models import Country
from readers import TxtFileReader
from sorters import CountrySorter

@pytest.fixture
def sample_data():
    return [
        Country("Ukraine", 603628.0, 40000000),
        Country("Monaco", 2.0, 38000),
        Country("USA", 9833517.0, 331000000)
    ]

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test_data.txt"
    file.write_text("Ukraine, 603628, 40000000\nMonaco, 2, 38000\nUSA, 9833517, 331000000")
    return str(file)

def test_txt_file_reader(temp_file):
    reader = TxtFileReader()
    result = reader.read(temp_file)
    assert len(result) == 3
    assert result[0].name == 'Ukraine'

@pytest.mark.parametrize("index, expected_country", [
    (0, 'USA'),
    (1, 'Ukraine'),
    (2, 'Monaco')
])
def test_sorter_by_area(sample_data, index, expected_country):
    sorter = CountrySorter(sample_data)
    assert sorter.by_area()[index].name == expected_country

@pytest.mark.parametrize("index, expected_country", [
    (0, 'USA'),
    (1, 'Ukraine'),
    (2, 'Monaco')
])
def test_sorter_by_population(sample_data, index, expected_country):
    sorter = CountrySorter(sample_data)
    assert sorter.by_population()[index].name == expected_country