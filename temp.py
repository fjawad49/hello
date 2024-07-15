
def calculate_moving_average(stock_prices, window_size):
    """
    Calculates the moving average of a list of stock prices.

    A moving average is a statistical measure that smooths out price data by calculating the average of a specified number of recent price values.
    It helps analysts identify trends, volatility, and short-term price movements in the stock.

    Parameters:
    stock_prices (list): A list of numerical stock prices representing the closing prices of a stock over time.
    window_size (int, optional): The size of the moving average window. Defaults to 10.

    Returns:
    list: A list of moving average values corresponding to the input stock prices.

    Raises:
    TypeError: If the input stock_prices is not a list.
    ValueError: If the window_size is less than or equal to 0.
    """

    # Check if the input is a list
    if not isinstance(stock_prices, list):
        raise TypeError("Input stock prices should be a list.")

    # Check if the window size is positive
    if window_size <= 0:
        raise ValueError("Window size should be a positive integer.")

    # Initialize an empty list to store the moving average values
    moving_averages = []

    # Calculate the moving average using a loop
    for i in range(len(stock_prices)):
        # Calculate the sum of the last window_size prices
        sum_of_window = sum(stock_prices[i-window_size:i+1])
        print(stock_prices[i-window_size:i+1])
        # Calculate the moving average by dividing the sum by window_size
        moving_average = sum_of_window / window_size

        # Append the moving average value to the list
        moving_averages.append(moving_average)

    return moving_averages


#Example usage:
if __name__ == "__main__":
    #Example stock prices
    stock_prices = [100, 120, 110, 90, 80, 95, 105, 115, 125, 108]

    #Calculate the moving average with a window size of 3
    window_size = 3
    moving_avg = calculate_moving_average(stock_prices, window_size)
    print("Moving Average with window size of 3: ", moving_avg)

 
                  

