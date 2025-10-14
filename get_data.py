import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt



class analytics_functions:
    def __init__(self, tickers):
        self.tickers = tickers
        self.data = None

    def fetch_live_data(self, period="1d", interval="1d"):
        """
        Fetch live data and return dataframe.
        """
        all_data = []

        for ticker in self.tickers:
            df = yf.download(ticker, period=period, interval=interval)
            df["Ticker"] = ticker
            all_data.append(df)
        self.data = pd.concat(all_data)
        print(f"Fetched data for {len(self.tickers)} tickers.")
        return self.data



    def clean_data(self):
        """
        Fill rate, transformations.
        """
        if self.data is None:
            raise ValueError("No data fetched as of yet. Run fetch_live_data() first.")
        self.data = self.data \
            .dropna() \
            .reset_index() 
        self.data.columns = [col.lower().replace(" ", "_") for col in self.data.columns]
        print("Data Cleaned")
        return self.data

    def to_sql(self):
        """
        Creates a SQL database if database does not exist, else update.
        """

    def ETL(self):
        """
        Extract, Transform Load using previous functions in order.
        """




price = analytics_functions(["AAPL", "SPY", "GLD"])
price = price.fetch_live_data()
print(price)

"""        
plt.plot(price, color='r')
plt.legend()
plt.grid()
plt.show()
"""
