def main():
    # Initialize variables
    total_months = 0
    total_rainfall = 0.0
    
    # Get the number of years
    years = int(input("Enter the number of years: "))
    
    # Input validation for years
    while years < 1:
        print("Years must be at least 1.")
        years = int(input("Enter the number of years: "))
    
    # Nested loops to get rainfall for each month of each year
    for i in range(1, years + 1):
        for j in range(1, 13):
            # Get rainfall for current month
            rainfall = float(input(f"Enter rainfall for Year {i} Month {j}: "))
            
            # Input validation for rainfall
            while rainfall < 0:
                print("Rainfall cannot be negative.")
                rainfall = float(input(f"Enter rainfall for Year {i} Month {j}: "))
            
            # Add to totals
            total_rainfall += rainfall
            total_months += 1
    
    # Calculate average
    average_rainfall = total_rainfall / total_months
    
    # Display results
    print(f"\nNumber of months: {total_months}")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

if __name__ == "__main__":
    main()