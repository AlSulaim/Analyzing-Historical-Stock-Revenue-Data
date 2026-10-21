Tesla and GameStop Stock Analysis 📈
Overview

This project analyzes the historical stock prices and revenue of Tesla (TSLA) and GameStop (GME) using Python. It retrieves historical stock data, extracts revenue data from web pages, and visualizes both datasets using interactive charts.

The project allows users to select a company and view its historical share price and revenue in a two-panel graph.

Features
Stock Data Retrieval: Fetches historical stock prices using the yfinance library.
Web Scraping: Extracts historical revenue data using BeautifulSoup, requests, and pandas.
Data Cleaning: Removes currency symbols, commas, and empty revenue values.
Interactive Visualization: Creates charts using Plotly to display historical share prices and revenue.
Company Selection: Allows users to choose between Tesla and GameStop through a command-line menu.
HTML Export: Saves the generated interactive chart as an HTML file.
Technologies Used
Python
yfinance
BeautifulSoup
pandas
requests
Plotly
Kaleido
Project Structure
.
├── main.py
├── gme_graph.html
└── README.md

main.py: Contains the stock analysis, web scraping, data cleaning, and visualization functions.
gme_graph.html: An example of the exported interactive stock analysis chart. The generated filename is the same for both companies.
README.md: Project documentation.
Installation
1. Clone the Repository
git clone <repository-url>
cd <repository-folder>


Replace the placeholders with your repository URL and folder name.

2. Install Dependencies

Make sure Python is installed, then run:

pip install yfinance beautifulsoup4 pandas requests plotly kaleido lxml

How to Run

Run the Python script from your terminal:

python main.py


Choose a stock when prompted:

Choose Stock to analyze :
 [1] Tesla
 [2] GME

Enter 1 to analyze Tesla (TSLA).
Enter 2 to analyze GameStop (GME).

The program retrieves the relevant data, displays sample records in the terminal, generates an interactive chart, and saves the chart as an HTML file.

Visualization

The generated chart contains two subplots:

Historical Share Price: Displays the historical closing price of the selected stock.
Historical Revenue: Displays the company's reported revenue over time.

The chart uses date-based x-axes and includes an interactive range slider for exploring historical stock prices.

The visualization is configured to display stock prices through June 14, 2021, and revenue data through April 30, 2021.

Main Functions
Function	Description
make_graph()	Creates and exports the stock price and revenue charts.
tesla_analyze()	Retrieves Tesla stock data and extracts its revenue data.
gme_analyze()	Retrieves GameStop stock data and extracts its revenue data.
Data Sources
Stock Prices: Retrieved using Yahoo Finance through yfinance.
Tesla Revenue: Extracted from the IBM Skills Network educational dataset.
GameStop Revenue: Extracted from the IBM Skills Network educational dataset.
Notes and Limitations
An active internet connection is required to retrieve stock and revenue data.
The revenue data comes from educational datasets and may not reflect the latest financial reports.
The chart filters the data to specific historical dates, so it does not display the entire available history.
Both analyses save their output to gme_graph.html. Running one analysis after the other will overwrite the previous HTML file.
The script depends on the availability and structure of the source web pages and external data services.
Future Improvements
Add support for more companies.
Allow users to select custom date ranges.
Save separate HTML files for Tesla and GameStop.
Improve error handling for network failures and missing data.
Add additional financial metrics and comparisons.
License

This project is intended for educational purposes. Add a license file if you plan to distribute the project publicly.
