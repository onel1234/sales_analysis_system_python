from sale import Sale
import analysis
from branch import Branch
from data_input import input_data
from analysis import monthly_sales_analysis, price_analysis, weekly_sales_analysis, product_preference_analysis, sales_distribution_analysis,calculate_total_sales


def main():
    # Input data
    input_data()

    # Perform analysis based on user input
    choice = int(input("Choose an analysis option:\n1. Monthly Sales Analysis\n2. Price Analysis\n3. Weekly Sales Analysis\n4. Product Preference Analysis\n5. Sales Distribution Analysis\nEnter your choice: "))

    if choice == 1:
        branch_name = input("Enter branch name: ")
        month = input("Enter month (e.g., January): ")
        # Call monthly sales analysis function
        monthly_sales_analysis(branch_name, month)
    elif choice == 2:
        # Call price analysis function
        price_analysis()
    elif choice == 3:
        # Call weekly sales analysis function
        weekly_sales_analysis()
    elif choice == 4:
        # Call product preference analysis function
        product_preference_analysis()
    elif choice == 5:
        # Call sales distribution analysis function
        sales_distribution_analysis()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
