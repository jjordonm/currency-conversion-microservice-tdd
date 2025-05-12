import unittest
from currency import convert_currency, supported_currency_codes

input_output_pairs = [
    {"input": {"amount": 100, "source": "USD", "target": "EUR"}, "expected_output": 92.0},
    {"input": {"amount": 0, "source": "USD", "target": "EUR"}, "expected_output": "Validation error: amount must be greater than zero"},
    {"input": {"amount": -50, "source": "USD", "target": "EUR"}, "expected_output": "Validation error: amount must be greater than zero"},
    {"input": {"amount": 1_000_000_000, "source": "USD", "target": "EUR"}, "expected_output": 920_000_000.0},
    {"input": {"amount": 100, "source": "USD", "target": "USD"}, "expected_output": 100.0},
    {"input": {"amount": 100, "source": "USD", "target": "XYZ"}, "expected_output": "Error: unsupported currency code 'XYZ'"},
    {"input": {"amount": 100, "source": "USDD", "target": "EUR"}, "expected_output": "Error: unsupported currency code 'USDD'"},
    {"input": {"source": "USD", "target": "EUR"}, "expected_output": "Validation error: amount is required"},
    {"input": {"amount": "abc", "source": "USD", "target": "EUR"}, "expected_output": "Validation error: amount must be a number"},
    {"input": {"amount": 100, "source": "USD", "target": "EUR", "simulate_error": True}, "expected_output": "Error: service unavailable"},
    {"input": {"amount": 1e13, "source": "USD", "target": "EUR"}, "expected_output": "Validation error: amount is too large"},
    {"input": {"amount": 1e-7, "source": "USD", "target": "EUR"}, "expected_output": "Validation error: amount is too small"},
    {"input": {"amount": 1.333333, "source": "USD", "target": "EUR"}, "expected_output": 1.226666},
]

class TestCurrencyConversion(unittest.TestCase):
    def test_cases(self):
        for io in input_output_pairs:
            inp = io["input"]
            expected = io["expected_output"]
            amount = inp.get("amount")
            source = inp.get("source")
            target = inp.get("target")
            simulate_error = inp.get("simulate_error", False)
            rates = supported_currency_codes
            result = convert_currency(amount, source, target, rates, simulate_error)
            print(f"Input: {inp}\nExpected Output: {expected}\nActual Output: {result}\n---")
            self.assertEqual(result, expected, f"Failed for input: {inp}")

if __name__ == "__main__":
    print("Running automated tests...")
    unittest.main()
