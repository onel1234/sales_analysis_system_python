from DataProcessor import DataProcessor

def test_process_data():
    data = [{'product_id': '1', 'amount': '100.0'}, {'product_id': '2', 'amount': '150.0'}]
    processed_data = DataProcessor.process_data(data)
    assert processed_data == {'1': 100.0, '2': 150.0}