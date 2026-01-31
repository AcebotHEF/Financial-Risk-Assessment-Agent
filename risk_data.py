import pandas as pd

def get_financial_profile():
    data = {
        "Metric": [
            "Debt-to-Equity Ratio",
            "Liquidity Ratio",
            "Revenue Growth (YoY)",
            "Net Margin",
            "Credit Score",
            "Market Volatility (1–10)"
        ],
        "Value": [2.8, 0.95, -5.0, 3.2, 620, 8]
    }
    return pd.DataFrame(data)