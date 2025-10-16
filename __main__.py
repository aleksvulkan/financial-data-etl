"""
Market Data Pipeline: 

Step 1: Ingest data from API. 
    - Download daily price data.


Step 2: Clean data 
    - Clean the data, fillrate, nullrate, transformation etc etc

Step 3
    - Store into MySQL


"""
from get_data import analytics_functions

def main():
    tickers_input = input("Enter tickers separated by commas (e.g. AAPL,SPY,GLD): ")
    db_name = input("Enter database name (default: market_data.db): ").strip() or "market_data.db"
    table_name = input("Enter SQL table name (default: tickers_data): ").strip() or "tickers_data"

    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]
    if not tickers:
        print("No valid tickers entered. Exiting.")
        return

    analytics = analytics_functions(tickers, db_name=db_name)
    analytics.ETL(period="1mo", interval="1d", table_name=table_name)


if __name__ == "__main__":
    main()



