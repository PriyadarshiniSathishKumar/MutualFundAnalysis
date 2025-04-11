import requests
import pandas as pd

def fetch_amfi_data():
    """Fetches mutual fund NAV data from AMFI India"""
    url = "https://www.amfiindia.com/spages/NAVAll.txt"
    response = requests.get(url)
    
    data = response.text.split("\n")
    funds = []
    
    for row in data[1:]:  # Skip header
        values = row.split(";")
        if len(values) > 4:
            funds.append({
                "Scheme Code": values[0],
                "Scheme Name": values[3],
                "NAV": values[4],
                "Date": values[5]
            })
    
    return pd.DataFrame(funds)

# Test function
if __name__ == "__main__":
    df = fetch_amfi_data()
    print(df.head())
