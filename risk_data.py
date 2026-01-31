import pandas as pd

def get_financial_profile():
    """
    Returns a dictionary-based dataframe representing a 
    simulated company financial profile (High-Risk Scenario).
    """
    data = {
        "Metric": [
            "Debt-to-Equity Ratio",
            "Current Ratio (Liquidity)",
            "Revenue Growth (YoY %)",
            "Net Profit Margin (%)",
            "Corporate Credit Score",
            "Market Volatility Index (1-10)"
        ],
        "Value": [
            2.8,   # High Risk (> 2.0 is usually bad)
            0.95,  # High Risk (< 1.0 means they can't pay short-term debts)
            -5.0,  # Negative Growth
            3.2,   # Low Margin
            620,   # Subprime/Risk category
            8      # High Volatility
        ]
    }
    
    return pd.DataFrame(data)