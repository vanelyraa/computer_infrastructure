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
 - [Bibliografy](#bibliografy)


## Project Purpose
This repository contains my submissions for the Computer Infrastructure class assessment completed as part of the Higher Diploma in Science in Computing in Data Analytics at ATU.
The assesment requires building Python code to interact with financial data from [yfinance](https://ranaroussi.github.io/yfinance/). Including:

 - Downloading stock market data for five FAANG stocks (Facebook, Apple, 
Amazon, Netflix and Google) for a determined period, process and visualize the results in timeframed .csv

- Plotting stock prices also in timeframed .png

- Creating an executable script to run the entire process from a terminal

- Scheduling automatic executions using GitHub Actions

To visualize the code, explanations and outputs: problems.ipynb
To run the project full workflow:

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

The get_data() function is responsible for downloading stock data for five major tecnology companies:Facebook, Apple, Amazon, Netflix and Google from yfincance, store the data in a timestamped .csv file 

A list called 'tickers' is defined with the tickers from the five companies to be analysed. A ticker is an abbreviation  that uniquely identifies a company.
A dictionary called 'stocks_data' is created and used to store data fetched for each ticker.

The function loops through each of the tickers and downloads it's hourly stock data, from the previous 5 days from Yahoo Finance

The data is stored in a [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) columns containing close, high, low, open and volume values and rows each timestamp

The datetime is converted into a column as they are stored as in index in YFinance, the conversion is done for easy data manipulation.

#### Problem 2: Plotting Data
#### Problem 3: Script
#### Problem 4: Automation

## Bibliografy


** End **

