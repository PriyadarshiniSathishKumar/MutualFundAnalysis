# Mutual Fund Investment Analyzer

Mutual Fund Investment Analyzer is a Python-based Streamlit web application that provides users with tools to analyze mutual fund performance using live NAV data fetched directly from the AMFI (Association of Mutual Funds in India) website. It also includes calculators to estimate future returns for SIP (Systematic Investment Plan) and lump sum investments.

## Features

- 📈 Fetches real-time mutual fund NAV data from AMFI
- 🔍 Displays mutual fund data in a clean, searchable table
- 📊 Visualizes NAV trends over time using interactive Plotly line charts
- 💸 Calculates future value for SIP and lump sum investments
- 🖥️ User-friendly and responsive web interface using Streamlit

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Requests

## How to Run

1. Clone the repository:
   git clone https://github.com/your-username/mutual-fund-analyzer.git

2. Navigate to the project directory:
   cd mutual-fund-analyzer

3. Install required dependencies:
   pip install -r requirements.txt

4. Run the application:
   streamlit run app.py

## Project Structure

- `app.py` – Main Streamlit app interface
- `fetch_data.py` – Module to fetch and clean mutual fund NAV data from AMFI
- `sip_calculator.py` – Contains functions for SIP and lump sum calculations
- `requirements.txt` – List of required Python libraries

## Sample Calculations

- SIP Future Value
- Lump Sum Investment Growth

## Acknowledgements

- AMFI India for providing mutual fund NAV data

---


https://github.com/user-attachments/assets/1e46967d-0128-4da5-872d-48a1bc74207e


