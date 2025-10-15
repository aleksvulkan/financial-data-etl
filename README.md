### Overview
This project is a daily **ETL (Extract, Transform, Load)** pipeline that automatically fetches live financial data for selected tickers, cleans it, and stores it in a SQL database.  
Built using **Python, yfinance, pandas, and SQLAlchemy**.

---

### Features
- Fetches daily stock data from Yahoo Finance  
- Cleans and standardizes the data for SQL storage  
- Saves data into a SQLite database (`market_data.db`)  
- Designed for daily automated updates via scheduler or cron  
- Easy to extend for additional tickers or data sources  

---

### Tech Stack
- **Python 3.10+**
- `pandas`
- `yfinance`
- `sqlalchemy`
- `schedule` (for automation)

---

### Usage
```bash
# Clone the repo
git clone https://github.com/<your-username>/financial-data-etl.git
cd financial-data-etl

# Install dependencies
pip install -r requirements.txt

