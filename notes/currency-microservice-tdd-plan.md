# TDD Implementation Plan: Python Currency Conversion Microservice

## Overview

This plan outlines a test-driven development (TDD) approach for building a Python-based microservice that exposes a REST API for currency conversion using real-time exchange rates. The service will use Flask, fetch rates from an external API (e.g., exchangerate.host), and include robust error handling and fallback behavior.

## Task List for TDD Implementation

### Phase 1: API Endpoint Skeleton
- [ ] Create a minimal Flask app with a `/convert` endpoint.
- [ ] Write pytest unit tests for:
    - Valid request returns 200 status.
    - Missing parameters return 400 with helpful message.
    - Invalid parameter values return 400.
- [ ] Implement basic request parsing and validation to pass tests.
- [ ] Refactor: Move validation logic to a separate function/module.

### Phase 2: Integrate Real-Time Exchange Rate Fetching
- [ ] Write pytest unit tests for:
    - Valid conversion returns correct amount (mock external API).
    - Graceful handling of external API failures (mocked).
    - Edge cases: unsupported currency, large/small amounts, same currency.
- [ ] Implement logic to fetch rates from exchangerate.host using requests.
- [ ] Use mocking for all external API calls in tests.
- [ ] Refactor: Abstract external API calls into a separate module/class.

### Phase 3: Error Handling and Fallback Behavior
- [ ] Write pytest unit tests for:
    - Fallback response when external API is down.
    - Clear and consistent error messages.
    - Rate limiting or timeout scenarios.
- [ ] Implement fallback logic and improve error handling.
- [ ] Ensure all error responses are JSON and consistent.
- [ ] Refactor: Centralize error handling and response formatting; consider Flask blueprints and custom error handlers.

### Phase 4: Code Quality, Refactoring, and Documentation
- [ ] Write pytest unit tests for:
    - Code coverage and additional edge cases.
    - Input validation edge cases (empty strings, special characters).
- [ ] Refactor for readability, maintainability, and add type hints/docstrings.
- [ ] Modularize code into separate files for API, business logic, and integrations.
- [ ] Review for DRY and SRP principles.

---

## General Recommendations
- Use pytest for all testing.
- Use mocking for all external API calls in tests.
- Emphasize clean code, modular design, and robust error handling throughout development.
