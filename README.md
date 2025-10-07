# Currency Conversion Microservice

## Purpose

This repository demonstrates a test-driven development (TDD) approach for building a Python-based microservice that performs real-time currency conversion. The service exposes a REST API using Flask, accepts query parameters for `source_currency`, `target_currency`, and `amount`, and returns the converted amount as JSON. It fetches exchange rates from an external API (exchangerate.host) and includes robust error handling and fallback behavior.

## Features

- REST API endpoint for currency conversion (`/convert`)
- Real-time exchange rate fetching with fallback to static rates
- Modular code structure (API, validation, external integration)
- Comprehensive test suite using `pytest` and `requests-mock`
- Clean code practices and robust error handling

## How to Use

1. **Install dependencies:**

   ```powershell
   pip install -r src/requirements.txt
   ```

2. **Run the Flask app:**

   ```powershell
   python src/app.py
   ```

   The app will start on [http://127.0.0.1:5000](http://127.0.0.1:5000) by default.

3. **Run the test suite:**

   ```powershell
   python -m pytest src
   ```

   > **Note:** The tests require `pytest` and `requests-mock` (both included in `requirements.txt`).

### Example API Usage

**Request:**

```text
GET /convert?source_currency=USD&target_currency=EUR&amount=100
```

**Response:**

```json
{
  "source_currency": "USD",
  "target_currency": "EUR",
  "amount": 100,
  "converted_amount": 92.34,
  "rate": 0.9234
}
```

## Project Structure

- `src/app.py` - Flask application and API endpoint
- `src/exchange.py` - External API integration and fallback logic
- `src/validation.py` - Request validation logic
- `src/test_app.py` - Test suite for the microservice
- `src/requirements.txt` - Python dependencies
- `notes/` - TDD plans, best practices, and documentation

## TDD and Clean Code

This project was developed using TDD principles, with phases for planning, test writing, minimal implementation, and refactoring. The codebase emphasizes modularity, maintainability, and robust error handling.

See `notes/tdd-best-practices-notes.md` and `notes/currency-microservice-tdd-plan.md` for detailed TDD process, prompting examples, and best practices.

## Collaboration and Hyper Velocity Engineering

This project was developed in close collaboration with GitHub Copilot, leveraging AI-assisted coding to:

- Rapidly prototype and iterate on requirements, tests, and implementation
- Apply test-driven development (TDD) at every stage
- Refactor and modularize code for maintainability and clarity
- Accelerate feedback cycles by automating test writing and validation

By integrating Copilot into the workflow, I was able to:

- Break down features and tasks into actionable TDD phases
- Use Copilot to generate, review, and refine both tests and production code
- Quickly adapt to changes and resolve issues with AI-powered suggestions

This approach embodies hyper velocity engineering practices—emphasizing automation, rapid iteration, and continuous improvement—resulting in a robust, well-tested, and maintainable microservice.
