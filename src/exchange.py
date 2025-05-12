import requests
from typing import Optional, Tuple

EXTERNAL_API_URL = "https://api.exchangerate.host/convert"

FALLBACK_RATES = {
    ("USD", "EUR"): 0.9,
    ("EUR", "USD"): 1.1,
    ("USD", "USD"): 1.0,
    ("EUR", "EUR"): 1.0,
}

RATE_LIMITED = False  # Simulate rate limiting for testing


def fetch_conversion_rate(
    source_currency: str, target_currency: str
) -> Tuple[Optional[float], Optional[str]]:
    """
    Fetch the conversion rate from source_currency to target_currency using an external API.
    Returns a tuple of (rate, error_message). Uses fallback rates if the API fails.
    """
    if RATE_LIMITED:
        return None, "Rate limit exceeded"
    params = {
        "from": source_currency,
        "to": target_currency,
    }
    try:
        response = requests.get(EXTERNAL_API_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("success") and "result" in data:
            return data["result"], None
        raise Exception("API did not return success")
    except Exception as e:
        rate = FALLBACK_RATES.get((source_currency, target_currency))
        if rate is not None:
            return rate, f"External API failed, using fallback rate: {str(e)}"
        return None, f"External API failed and no fallback available: {str(e)}"
