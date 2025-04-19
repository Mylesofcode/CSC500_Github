def main():
    # Get number of books purchased
    books = int(input("Enter the number of books purchased this month: "))
    
    # Input validation
    while books < 0:
        print("Number of books cannot be negative.")
        books = int(input("Enter the number of books purchased this month: "))
    
    # Calculate points based on books purchased
    if books == 0:
        points = 0
    elif books <= 1:  # Not specified in requirements, assuming 0
        points = 0
    elif books <= 3:  # For 2-3 books
        points = 5
    elif books <= 5:  # For 4-5 books
        points = 15
    elif books <= 7:  # For 6-7 books
        points = 30
    else:  # 8 or more books
        points = 60
    
    # Display results
    print(f"Points awarded: {points}")

if __name__ == "__main__":
    main()