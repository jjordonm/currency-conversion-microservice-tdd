from typing import Optional, Mapping

def validate_conversion_request(args: Mapping) -> Optional[str]:
    """
    Validate the query parameters for the currency conversion request.
    Returns an error message string if validation fails, otherwise None.
    """
    required = ['source_currency', 'target_currency', 'amount']
    for param in required:
        if param not in args:
            return f"Missing required parameter: {param}"
    # Check for empty or invalid currency codes
    for param in ['source_currency', 'target_currency']:
        value = args.get(param, "")
        if value == "":
            return f"Invalid currency code: {param}"
        if not value.isalpha() or len(value) != 3:
            return f"Invalid currency code: {param}"
    try:
        float(args.get('amount'))
    except (ValueError, TypeError):
        return "Invalid value for amount; must be a number."
    return None
