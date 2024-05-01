from CSVDataReader import CSVDataReader

def test_read_data():
    file_path = 'test_data.csv'
    data_reader = CSVDataReader()
    data = data_reader.read_data(file_path)
    assert len(data) == 3
