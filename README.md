# computer_infrastructure

# Computer Infrastructure Assessment

## Table of Contents
 - [Project Purpose](#project-purpose)
 - [Setup Instructions](#setup-instructions)
 - [Install Dependencies](#install-dependencies)
 - [Implementations](#implementations)
    - [Problem 1](#problem-1-data-from-yfinance)
    - [Problem 2](#problem-2-plotting-data)
    - [Problem 3](#problem-3-script) & [script](faang.py)
    - [Problem 4](#problem-4-automation)


## Project Purpose
This repository contains my submissions for the Computer Infrastructure class assessment completed as part of the Higher Diploma in Science in Computing in Data Analytics at ATU.
The assessment requires building Python code to interact with financial data from [yfinance](https://ranaroussi.github.io/yfinance/). Including:

 - Downloading stock market data for five FAANG stocks (Facebook, Apple, 
Amazon, Netflix and Google) for a determined period, process and visualize the results in timestamped CSV.

- Plotting stock prices also in timestamped PNG.

- Creating an executable script to run the entire process from a terminal

- Scheduling automatic executions using GitHub Actions

- To visualize the code, explanations and outputs: problems.ipynb


## Install Dependencies

All required libraries are listed in requirements.txt  


## Setup Instructions

Clone this GitHub repository:
<pre> git clone https://github.com/vanelyraa/computer_infrastructure.git </pre>

Navigate the project directory:
<pre> cd https://github.com/vanelyraa/computer_infrastructure.git </pre>

Create a virtual environment (optional):
<pre> python3 -m venv venv </pre>

Activate virtual environment (optional):  
For windows: <pre> source venv/bin/activate </pre> 
For MacOS: <pre> source venv/bin/activate  </pre> 

Install required dependencies:
<pre> pip install -r requirements.txt </pre>


## Implementations

#### Problem 1: Data from yfinance

In this exercise, we are required to create a function 'get_data()' to retrieve data from yfinance for five technology companies:Meta, Apple, Amazon, Netflix, and Google and save the data in a timestamped CSV file and save into a folder called 'data'.
The companies tickers are stored in a variable called 'tickers'.

The function initializes a dictionary called 'stocks_data', to store all fetched data for each stock. 
The function loops through each ticker and downloads their hourly data for the previous five days and stores it in a dataframe. The downloaded data includes datetime, open, high, low, close, and volume data.

For easier analysis and visualization, the datetime is converted into a regular column using 'reset_index()'. Each ticker’s DataFrame is then saved in the 'stocks_data' dictionary.

To create a timestamped CSV filename, the current date and time are retrieved using 'dt.datetime.now()' and the filename format required is stored as a variable called 'filename'.

Using 'os.path.exists', function checks if the data folder exists, if not 'os.makedirs' creates the folder in the root of the repository.
All five stock DataFrames are concatenated side by side to a single DataFrame using 'pandas.concat()', 'axis=1' joins columns horizontally left to right.

Finally, the combined data is saved in a  CSV file in the data folder using the defined timestamped filename. 

#### Problem 2: Plotting Data

In problem 2 we are required to write a function called 'plot_data()' to find the latest CSV file from the data folder and plot the 'Close' prices for each stock. Save timestamped plots in PNG into a folder called 'plots'. The 'plot_data()' function starts by saving the data folder path into a variable called 'path'. After that, it checks if folder plots exist and creates it if not. All CSV files are listed in variable 'csv_files' using a 'for' loop and 'os.listdir'. The filenames are then sorted using '.sort()' function, so the latest timestamped filename is positioned in index 0, the filename in index zero is saved to variable 'recent_csv'.

The full file path is constructed using os.path concatenating variables path and 'recent_csv'. The file is read into DataFrame using 'pd.read_csv()', 'header=[0,1]' tells Python the header a two-row header, enabling multi-level column indexing. 

The first column, index 0, contains the datetime and it is converted to datetime using 'pd.to_datetime()' to ensure correct plotting.

A for loop iterates through each ticker and plots its corresponding close price against time. A title, a legend and axis labels are added to the plot.

The plot is saved as a PNG file in plots folder using the same timestamp as the CSV using 'replace' to replace CSV to PNG in filename. 'Savefig()' saves the file with determined filename and path, with a higher resolution of 300 dpi.

#### Problem 3: Script

For problem 3, a Python script named 'faang.py' was created so any user could run the code from a terminal. A shebang was added to allow the script to be executed using Python 3. Required libraries were imported.

The functions from problems 1 and 2 were added to the script, get_data() and plot_data() and a main() function was written to call the functions in order.

The script execution is controlled using the if __name__ == "__main__": block to ensure it runs only when executed, not imported. File permissions were updated using 'chmod 777' to allow other users to run the script.

#### Problem 4: Automation

In problem 4, we are required to automate the script execution using GitHub Actions workflow. The workflow runs automatically every Saturday at 9:00am using cron.

The workflow runs on an Linux environment. It first checks out the repository, sets up Python, installs dependencies, the script is executed to download and plot stocks data. The updates are automatically committed and pushed to the repository.


** End **

