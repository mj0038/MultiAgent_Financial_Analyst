import yfinance as yf

def perform_technical_analysis(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        history = stock.history(period="1y")

        if history.empty:
            return f"No data available for {stock_symbol}. Please check the symbol."

        # Example technical indicators
        moving_avg_50 = history['Close'].rolling(window=50).mean().iloc[-1]
        moving_avg_200 = history['Close'].rolling(window=200).mean().iloc[-1]
        latest_close = history['Close'].iloc[-1]
        rsi = (history['Close'].diff().gt(0).sum() / len(history)) * 100

        return {
            "Latest Close": latest_close,
            "50-Day Moving Average": moving_avg_50,
            "200-Day Moving Average": moving_avg_200,
            "RSI": rsi
        }
    except Exception as e:
        return f"Error fetching technical data: {str(e)}"
