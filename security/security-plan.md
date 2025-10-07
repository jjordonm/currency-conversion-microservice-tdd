# Security Plan – Currency Conversion Microservice

## Preamble

*Important to note:* ISE cannot certify/attest to the security of an architecture nor code. This document is intended to help produce backlog items specific to the customer engagement and to document the relevant security design decisions made by the team during build. Please direct your customer to work with their account team or preferred security vendor to seek an audit or pen-test from a security vendor if required/desired.

## Overview

Please find the Security Plan for the Currency Conversion Microservice below. This document shows the architecture and data flow diagram of the application. These artifacts were constructed based on documentation and source code from the project itself and are subject to change as the architecture and codebase evolves. Each of the labeled entities in the figures below are accompanied by meta-information which describes the threats, describes the data in scope, and recommendations for security controls.

## Diagrams

### Architecture Diagram

![Architecture Diagram](diagrams/architecture.png)

### Data Flow Diagram

![Data Flow Diagram](diagrams/data-flow.png)

For help getting started, please see our [Security Plan Guidelines](https://aka.ms/ISESecurityPlanInstructions) and [Microsoft Threat Modeling Security Fundamentals](https://learn.microsoft.com/en-us/training/paths/tm-threat-modeling-fundamentals/).

### Data Flow Attributes
  
| # | Transport Protocol | Data Classification | Authentication | Authorization | Notes|
|---|--------------------|---------------------|----------------|---------------|------|
| 1 | HTTPS | Public/PII (amount, currency codes) | None (public endpoint) | None (public endpoint) | Client to API: REST request for conversion |
| 2 | Internal (function call) | N/A | N/A | N/A | API to Validation: parameter validation |
| 3 | Internal (function call) | N/A | N/A | N/A | API to Exchange: fetch rate |
| 4 | HTTPS | Public | None (API key not required) | N/A | Exchange to External API: fetch rate |
| 5 | Internal (function call) | N/A | N/A | N/A | Exchange to Fallback: use static rates |
| 6 | HTTPS | Public/PII (converted amount) | None | None | API to Client: JSON response |

## Threats and Mitigations

- **Public API Exposure**
  - *Threat*: The `/convert` endpoint is publicly accessible and could be abused (e.g., DoS, scraping).
  - *Mitigation*: Implement rate limiting (Flask-Limiter or similar), monitor logs for abuse, and consider API keys or authentication for production.

- **Input Validation**
  - *Threat*: Malicious or malformed input could cause errors or exploit vulnerabilities.
  - *Mitigation*: Strict input validation is implemented in `validation.py`. Ensure continued coverage for all parameters and types.

- **External API Dependency**
  - *Threat*: Reliance on `exchangerate.host` could result in service disruption or data tampering if the API is compromised.
  - *Mitigation*: Fallback to static rates is implemented. Consider monitoring for API changes and validating responses.

- **Lack of Authentication/Authorization**
  - *Threat*: Anyone can access the API and perform conversions.
  - *Mitigation*: For public demo, this is acceptable. For production, add authentication (OAuth, API keys) and RBAC as needed.

- **Secrets Management**
  - *Threat*: If future enhancements require API keys or secrets, improper storage could lead to leaks.
  - *Mitigation*: Use environment variables or Azure Key Vault for secret storage. Never commit secrets to source control.

- **Error Handling and Information Disclosure**
  - *Threat*: Unhandled exceptions could leak stack traces or sensitive info.
  - *Mitigation*: Centralized error handling is implemented. Review error messages for sensitive data before returning to clients.

- **Transport Security**
  - *Threat*: Data in transit could be intercepted if not using HTTPS.
  - *Mitigation*: Enforce HTTPS in production deployments.

- **Dependency Vulnerabilities**
  - *Threat*: Vulnerabilities in Flask, requests, or other dependencies.
  - *Mitigation*: Regularly update dependencies and use tools like Dependabot or `pip-audit`.

## Secrets Inventory

An ideal architecture would contain *zero secrets*. Credential-less options like managed identities should be used wherever possible. Where secrets are required, it’s important to track them for operational purposes. Please see our [Example Secrets Inventory](https://eng.ms/docs/microsoft-customer-partner-solutions-mcaps/industry-and-partner-sales/industry-solutions-engineering-ise/industry-solutions-engineering-ise/centraloperations/security/securityplanguidelines#example-secrets-inventory) to help you get started.

| Name | What is its purpose? | Where does it live? | How was it generated? | What's the rotation strategy? Does it cause downtime? | How does the secret get distributed to consumers? | What’s the secret’s lifespan? |
| ---- | ----------- | ------------------- | --------------------- | ----------------------------------------------------- | ------------------------------------------------- | ----------------------------- |
| (none) | N/A | N/A | N/A | N/A | N/A | N/A |

<!--
TODO: Review this file during PRs for architectural or security-affecting changes.
TODO: Sync diagram or inventory changes with customer conversations.
TODO: If secrets are added in the future, update the inventory table above.
-->
