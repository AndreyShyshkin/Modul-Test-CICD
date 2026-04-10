def parse_file(file_path: str) -> list:
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 3:
                data.append({
                    'country': parts[0].strip(),
                    'area': float(parts[1].strip()),
                    'population': int(parts[2].strip())
                })
    return data

def sort_by_area(data: list) -> list:
    return sorted(data, key=lambda x: x['area'], reverse=True)

def sort_by_population(data: list) -> list:
    return sorted(data, key=lambda x: x['population'], reverse=True)

if __name__ == "__main__":
    file_name = 'data.txt'