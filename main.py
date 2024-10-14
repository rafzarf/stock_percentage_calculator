def calculate_percentage_return(opening_price, closing_price):
    """
    Calculate the percentage return given opening and closing stock prices.
    """
    return (closing_price - opening_price) / opening_price * 100


def validate_input(price):
    """
    Validate the user's input to ensure it's a positive number.
    """
    try:
        value = float(price)
        if value <= 0:
            raise ValueError("Price must be a positive number.")
        return value
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


def main():
    print("Stock Percentage Return Calculator")

    # Input and validation for opening price
    while True:
        opening_price = input("Enter the opening price of the stock: ")
        validated_opening = validate_input(opening_price)
        if validated_opening is not None:
            break

    # Input and validation for closing price
    while True:
        closing_price = input("Enter the closing price of the stock: ")
        validated_closing = validate_input(closing_price)
        if validated_closing is not None:
            break

    # Calculate and display the percentage return
    result = calculate_percentage_return(validated_opening, validated_closing)
    print(f"The stock’s percentage return is {result:.2f}%")


if __name__ == "__main__":
    main()
