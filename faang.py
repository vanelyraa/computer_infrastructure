#!/usr/bin/env python3 
#Shebang, tells the operating system to run the script with Python

import yfinance as yf # Yahoo Finance data.
import pandas as pd # Pandas library
import os
import datetime as dt
import matplotlib.pyplot as plt

# List tickers 
tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]

# Defining function
def get_data(): 

    # Dictionary to store stock data
    stocks_data = {}
        
    # Looping through tickers
    for ticker in tickers:  
        
        # Fetching data with custom interval, hourly data, previous five days
        df = yf.download(ticker, period="5d", interval="1h", auto_adjust = False)
       
        # print(df) checking how data if printed (debugging)

        # Converting datetime from an index to a column, for better visualization and analysis
        df.reset_index(inplace=True)

        #print(df) checking how data is printed after setting datetime to a column (debugging)

        # Storing each stock's DataFrame in a dictionary using the ticker name
        stocks_data[ticker] = df
                 
    # Fetching current time
    now = dt.datetime.now()

    # Storing csv naming format and current time to a variable
    filename = now.strftime("%Y%m%d-%H%M%S") + ".csv"

    # Creating data folder if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")  

    # Concatenate all stocks data side by side in one table
    # stocks_data.values() fetch all DF saved in dictionary
    # axis = 1: join columns horizontally left to right
    all_data = pd.concat(stocks_data.values(), axis=1)

    # Creating CSV file with required naming format and current time
    all_data.to_csv("data/" + filename, index=False) 
    
   
def plot_data():

    # Storing path - data folder - into a variable to be reused multiple times without the need of typing folder path, or in case path changes
    # it only need to be updated once in the function
    path = "data"

    # Creating plots folder if it doesn't exist
    if not os.path.exists("plots"):
        os.makedirs("plots")

    # Find all CSV files in the folder
    csv_files = [x for x in os.listdir(path) if x.endswith(".csv")]

    # Sorting CSV files by filename showing newest first, inspiration from lecture
    csv_files.sort(reverse=True)

    # Latest file, inspiration from lecture
    recent_csv = csv_files[0]

    # Joining folder and file to create the full file path for functions
    latest_path = os.path.join(path, recent_csv)

    # Reading CSV and converting to Dataframe, header has two rows for plotting reference (multi level indexing)
    df = pd.read_csv(latest_path, header=[0, 1])

    # Converting first column with dates to Datetime
    datetime_column = df.columns[0]
    df[datetime_column] = pd.to_datetime(df[datetime_column])
    
    # Making plot wider for better visualization
    plt.figure(figsize=(14, 6)) 

    # Plot Close prices for each ticker, looping through each ticker 
    for ticker in tickers:
        plt.plot(df[datetime_column], df[('Close', ticker)], label=ticker)
        
    # Defining lables and title to plot
    plt.xlabel("Datetime")
    plt.ylabel("Close Price")
    plt.title('Close prices')
    plt.legend()

      # Saving plot to 'plots' folder, ensuring CSV and PNG files have the same timestamp
    plot_filename = recent_csv.replace('.csv', '.png')
    save_path = os.path.join("plots", plot_filename)
    plt.savefig(save_path, dpi=300)
    plt.close()
    
def main():
    #Calling functions to be executed
    get_data()
    plot_data()

if __name__ == "__main__": #this function make sure the code is executed if the file is run as a script not when its imported
    main()

# https://realpython.com/python-shebang/ Python 3 shebang and calling functions
# https://dev.to/devasservice/execute-python-with-shebang-make-your-scripts-executable-17f2 #Running script
# https://www.geeksforgeeks.org/python/run-function-from-the-command-line-in-python/ #Calling functions in script
# https://realpython.com/if-name-main-python/  #If name function
# https://phoenixnap.com/kb/chmod-755 User permissions