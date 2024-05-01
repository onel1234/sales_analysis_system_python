
class ReportGenerator:
    @staticmethod
    def generate_report(sales_data):
        print("Sales Report:")
        for product_id, amount in sales_data.items():
            print(f"Product ID: {product_id}, Total Sales Amount: {amount}")

# Main.py (Continued)
from ReportGenerator import ReportGenerator

def main():
    file_path = 'sales_data.csv'
    data_reader = CSVDataReader()
    sales_data = data_reader.read_data(file_path)
    processed_data = DataProcessor.process_data(sales_data)
    ReportGenerator.generate_report(processed_data)

if __name__ == "__main__":
    main()
