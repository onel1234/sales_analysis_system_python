def monthly_sales_analysis(branch, month):
    # Calculate and display monthly sales analysis for the given branch and month
    pass

def price_analysis(products):
    # Calculate and display price analysis for each product
    pass

def weekly_sales_analysis():
    # Calculate and display weekly sales analysis for the Sampath supermarket network
    pass

def product_preference_analysis():
    # Analyze and display product preference analysis
    pass

def sales_distribution_analysis():
    # Analyze and display distribution of total sales amount of purchases
    pass
def calculate_total_sales(data):
    total_sales = {}  # Dictionary to store total sales for each product
    for sale in data:
        product = sale.product
        amount = sale.amount
        if product in total_sales:
            total_sales[product] += amount
        else:
            total_sales[product] = amount
    return total_sales
