
import csv

class CSVDataReader:
    @staticmethod
    def read_data(file_path):
        data = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

# Main.py
from CSVDataReader import CSVDataReader

def main():
    file_path = 'sales_data.csv'
    data_reader = CSVDataReader()
    sales_data = data_reader.read_data(file_path)
    print(sales_data)

if __name__ == "__main__":
    main()
