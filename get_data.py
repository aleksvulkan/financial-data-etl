import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt



class analytics_functions:
    def __init__(self, tickers, db_name = "market_data.db"):
        self.tickers = tickers
        self.data = None
        self.db_name = db_name

    def fetch_live_data(self, period="3mo", interval="1d"):
        """
        Fetch live data and return dataframe.
        """
        all_data = []

        for ticker in self.tickers:
            df = yf.download(ticker, period=period, interval=interval)
            if df.empty:
                print(f"Warning: No data returned for {ticker}. Skipping.")
                continue
            df["Ticker"] = ticker
            all_data.append(df)

        self.data = pd.concat(all_data, axis=1, keys=self.tickers)
        self.data.reset_index(inplace=True)

        self.data.columns = [
            f"{col[0].lower().replace(' ', '_')}_{col[1]}" if isinstance(col, tuple) else str(col).lower().replace(" ", "_")
            for col in self.data.columns
            ]
        # print(f"Fetched data for {len(self.tickers)} tickers.")


        return self.data



    def clean_data(self):
        """
        Fill rate, transformations.
        """
        if self.data is None:
            raise ValueError("No data fetched as of yet. Run fetch_live_data() first.")
        
        missing_counts = self.data \
            .isna() \
            .sum()

        total_rows = len(self.data)
        fill_rates = 1 - (
            missing_counts / total_rows
        )
        print("=== Fill Rates ===")
        print(fill_rates)

        self.data = self.data \
            .dropna() \
            .ffill() \
            .bfill()
        
        print("Data Cleaned")
        print("\n=== Data Summary ===")
        print(self.data.describe())

        return self.data

    def to_sql(self, table_name="ticker_table"):
        """
        Creates a SQL database if database does not exist, else update.
        """
        from sqlalchemy import create_engine

        if self.data is None:
            raise ValueError("No data to save. Run clean_data() first.")
        
        engine = create_engine(f"sqlite:///{self.db_name}")
        self.data.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Data written to {self.db_name} in table '{table_name}'.")

    def ETL(self, period="1mo", interval="1d", table_name="tickers_data"):
        """
        Extract, Transform Load using previous functions in order.
        """
        print("\n Starting ETL process...")
        self.fetch_live_data(period=period, interval=interval)
        self.clean_data()
        self.to_sql(table_name=table_name)
        print("ETL process completed successfully.")


"""
tickers = ["AAPL", "SPY", "GLD"]
af = analytics_functions(tickers)

# Fetch one month of daily data for testing
af.fetch_live_data()
af.clean_data()
af.to_sql()
"""