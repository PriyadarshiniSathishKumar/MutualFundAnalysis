def calculate_sip(amount, rate, years):
    """Calculates expected returns for an SIP investment"""
    rate = rate / 100 / 12  # Monthly interest rate
    months = years * 12
    future_value = amount * (((1 + rate) ** months - 1) / rate) * (1 + rate)
    return round(future_value, 2)

def calculate_lump_sum(amount, rate, years):
    """Calculates expected returns for a lump sum investment"""
    future_value = amount * ((1 + (rate / 100)) ** years)
    return round(future_value, 2)
