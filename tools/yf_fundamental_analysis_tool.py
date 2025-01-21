import yfinance as yf

def perform_fundamental_analysis(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        info = stock.info

        if not info or 'regularMarketPrice' not in info:
            return f"No data available for {stock_symbol}. Please check the symbol."

        return {
            "Company Name": info.get("longName", "N/A"),
            "Sector": info.get("sector", "N/A"),
            "Industry": info.get("industry", "N/A"),
            "Market Cap": info.get("marketCap", "N/A"),
            "P/E Ratio": info.get("trailingPE", "N/A"),
            "Debt to Equity Ratio": info.get("debtToEquity", "N/A"),
            "Revenue Growth": info.get("revenueGrowth", "N/A"),
        }
    except Exception as e:
        return f"Error fetching fundamental data: {str(e)}"
