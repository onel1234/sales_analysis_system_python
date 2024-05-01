
class DataProcessor:
    @staticmethod
    def process_data(data):
        sales_data = {}
        for transaction in data:
            product_id = transaction['product_id']
            amount = float(transaction['amount'])
            if product_id in sales_data:
                sales_data[product_id] += amount
            else:
                sales_data[product_id] = amount
        return sales_data

# Main.py (Continued)
from DataProcessor import DataProcessor

def main():
    file_path = 'sales_data.csv'
    data_reader = CSVDataReader()
    sales_data = data_reader.read_data(file_path)
    processed_data = DataProcessor.process_data(sales_data)
    print(processed_data)

if __name__ == "__main__":
    main()
