sample_currency_rates = {
    ("USD", "EUR"): 0.92,
    ("EUR", "USD"): 1.09,
    ("USD", "JPY"): 150.0,
    ("JPY", "USD"): 0.0067,
    ("USD", "USD"): 1.0,
    ("EUR", "EUR"): 1.0,
}

supported_currency_codes = ["USD", "EUR", "JPY"]

def convert_currency(amount, source, target, rates=supported_currency_codes, simulate_error=False):
    if simulate_error:
        return "Error: service unavailable"
    if amount is None:
        return "Validation error: amount is required"
    try:
        if isinstance(amount, str):
            amount = float(amount)
    except Exception:
        return "Validation error: amount must be a number"
    if not isinstance(amount, (int, float)):
        return "Validation error: amount must be a number"
    if amount <= 0:
        return "Validation error: amount must be greater than zero"
    # Edge case: extremely large values
    if isinstance(amount, (int, float)) and abs(amount) > 1e12:
        return "Validation error: amount is too large"
    # Edge case: extremely small positive values (but not zero)
    if isinstance(amount, (int, float)) and 0 < abs(amount) < 1e-6:
        return "Validation error: amount is too small"
    # Edge case: floating-point rounding
    if (source, target) in sample_currency_rates:
        rate = sample_currency_rates[(source, target)]
        result = round(amount * rate, 6)  # Increased precision for edge case
        return result
    if source not in rates or target not in rates:
        return f"Error: unsupported currency code '{source if source not in rates else target}'"
    if (source, target) not in sample_currency_rates:
        return f"Error: unsupported currency code '{target}'"
    rate = sample_currency_rates[(source, target)]
    return round(amount * rate, 2)
