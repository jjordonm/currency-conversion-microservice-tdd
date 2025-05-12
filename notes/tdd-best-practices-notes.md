# TDD Best Practices

## Summary of Discussion

- **Test-First Development**: Write tests before production code to clarify requirements and expected behavior.
- **Small, Focused Tests**: Each test should cover a single behavior or scenario for clarity and maintainability.
- **Descriptive Test Names**: Use clear, descriptive names for tests to communicate intent.
- **Automated Test Execution**: Integrate tests into CI/CD pipelines to ensure they run consistently.
- **Refactor with Confidence**: Use tests as a safety net for safe refactoring.
- **Team Collaboration**: Involve developers, testers, and product owners in defining test cases.
- **Meaningful Test Coverage**: Aim for high coverage, but prioritize meaningful tests over arbitrary metrics.
- **Regular Test Review**: Review and update tests as the codebase evolves.

## Prompting Examples for TDD Implementation

- "Write a failing test for a function that converts temperatures from Celsius to Fahrenheit."
- "Generate test cases for a login API, including both valid and invalid credentials."
- "Refactor the code to pass the following test: [describe test]."
- "Suggest edge case tests for a function that calculates the total price with discounts."
- "Write tests for a microservice that handles currency conversion, including error handling."
- "Show how to use parameterized tests for a function that validates email addresses."
- "Add a test to ensure that an exception is raised when an invalid input is provided."
- "Demonstrate the red-green-refactor cycle for a new feature in a shopping cart module."

## Link to Plan

[Currency Microservice TDD Plan](./currency-microservice-tdd-plan.md)
