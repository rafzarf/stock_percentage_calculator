# **Stock Percentage Return Calculator**

## **Project Overview**
The **Stock Percentage Return Calculator** is a Python tool designed to calculate the percentage return of a stock based on the provided opening and closing prices. This tool is simple to use, with input validation to ensure the user provides valid, positive numeric values.

Additionally, the project includes unit tests to verify the correctness of both the percentage return calculation and the input validation functions.

## **Features**
- **Percentage Return Calculation**:
  Calculate the percentage return of a stock using the formula:
  $$
  \text{Percentage Return} = \frac{\text{Closing Price} - \text{Opening Price}}{\text{Opening Price}} \times 100
  $$

- **Input Validation**:
  Ensure that both the opening and closing prices are valid, positive numbers. If the input is invalid, the user is prompted to re-enter the value.

- **Unit Testing**:
  The project includes a set of unit tests to ensure that the main functions behave as expected.

## **Getting Started**

### **Prerequisites**
To run the calculator, you will need:
- **Python 3.x**

### **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/stock-return-calculator.git
   cd stock-return-calculator
   ```

2. **Install Dependencies**:
   This project does not have any external dependencies beyond core Python.

### **Running the Calculator**

1. Run the `main.py` file:
   ```bash
   python main.py
   ```

2. Follow the prompts:
   - Enter the **opening price** and **closing price** of the stock.
   - The calculator will validate the inputs and compute the percentage return.

3. **Example Input/Output**:
   ```
   Stock Percentage Return Calculator
   Enter the opening price of the stock: 100
   Enter the closing price of the stock: 120
   The stock’s percentage return is 20.00%
   ```

## **Running Unit Tests**

To ensure that the calculator is functioning as expected, run the provided unit tests.

1. **Run the tests**:
   ```bash
   python -m unittest discover
   ```

2. **Example Output**:
   ```
   ----------------------------------------------------------------------
   Ran 2 tests in 0.001s

   OK
   ```

### **Test Coverage**
The project includes tests for:
1. **Percentage Return Calculation**:
   - Ensures that the formula produces correct results.
   - Example test: `calculate_percentage_return(100, 120)` should return `20.0`.

2. **Input Validation**:
   - Ensures that only positive numeric inputs are accepted.
   - Example tests: 
     - `validate_input("-50")` should return `False`.
     - `validate_input("100")` should return `100.0`.

## **File Structure**

```
stock-return-calculator/
├── main.py           # The main Python script for the calculator
├── tests.py      # Unit test file for testing functions
└── README.md         # Project documentation
```

## **Project Details**

### **Input Validation**
The `validate_input()` function ensures that users provide valid, positive numbers for both the opening and closing prices. If an invalid input is detected, the user is prompted to re-enter a valid value.

### **Percentage Return Calculation**
The `calculate_percentage_return()` function uses the provided opening and closing prices to compute the percentage return. The result is rounded to two decimal places and displayed in a clear and readable format.




