#!/usr/bin/env python3 
#Shebang, tells the operating system to run the script with Python

import yfinance as yf # Yahoo Finance data.
import pandas as pd # Pandas library
import os
import datetime as dt
import matplotlib.pyplot as plt



def get_data(): #Defining function

    tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']

    stocks_data = {}
    #List with the five stock tickers
    
    # Looping through tickers
    for ticker in tickers:

        
        
        # Fetching data with custom interval, hourly data, previous five days
        df = yf.download(ticker, period='5d', interval='1h', auto_adjust = False)
       # print(df) checking how data if printed

        # Converting datetime from an index to a column, for better visualization
        df.reset_index(inplace=True)
        #print(df) checking how data is printed after setting datetime to a column


        stocks_data[ticker] = df
                 
    # Current time
    now = dt.datetime.now()

    all_data = pd.concat(stocks_data.values(), axis=1)
    # Creting CSV file with required naming format and current time
    all_data.to_csv("data/" + now.strftime("%Y%m%d-%H%M%S") + ".csv", index=False) 
    
def plot_data():

    path = "data"

    # Find all .csv files in the folder
    csv_files = [x for x in os.listdir(path) if x.endswith(".csv")]

    # Find the most recent CSV file by modification time
    recent_csv = max(csv_files, key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    
    #Joining folder and file to create the full file path for functions
    latest_path = os.path.join(path, recent_csv)

    # Reading CSV and converting to Dataframe, header has two rows for plotting reference
    df = pd.read_csv(latest_path, header=[0, 1])

    #Converting first column with dates to Datetime
    datetime_column = df.columns[0]
    df[datetime_column] = pd.to_datetime(df[datetime_column])
    
    #Defining tickers to be plotted
    tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']

    plt.figure(figsize=(14, 6)) # making plot wider for better visualization

    # Plot Close prices for each ticker, looping through each ticker 
    for ticker in tickers:
        plt.plot(df[datetime_column], df[('Close', ticker)], label=ticker)
        
    # Defining lables and title to plot
    plt.xlabel("Datetime")
    plt.ylabel("Close Price")
    plt.title('Close prices')
    plt.legend()

      # Saving plot to 'plots' folder
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    save_path = os.path.join("plots", f"{timestamp}.png")
    plt.savefig(save_path)
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