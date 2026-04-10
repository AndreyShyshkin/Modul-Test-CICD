from readers import TxtFileReader
from sorters import CountrySorter


def main():
    file_name = 'data.txt'
    reader = TxtFileReader()

    try:
        data = reader.read(file_name)
        sorter = CountrySorter(data)

        print("Сортування за площею:")
        for country in sorter.by_area():
            print(f"{country.name} - {country.area}")

        print("\nСортування за населенням:")
        for country in sorter.by_population():
            print(f"{country.name} - {country.population}")

    except FileNotFoundError:
        print(f"Помилка: Файл '{file_name}' не знайдено.")


if __name__ == "__main__":
    main()