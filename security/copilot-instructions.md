<!--
  Copilot Instructions: These guidelines are for GitHub Copilot (or other AI agents) to help generate a comprehensive security plan using the template and folder structure provided.

  ## Input:
  - Template file: `security/security-template.md`
  - Diagrams output folder: `security/diagrams/`

  ## General Workflow:
  1. Understand the project context by inspecting the repository structure, README, and source code.
  2. Use this context to complete or generate content in `security/security-template.md` following the sections below.

  ## 1. Project and Metadata Initialization:
  - Prompt the user for the project name and replace every instance of `Project Name` in the template.
  - Ensure the preamble remains intact and accurate.
  - Remove any placeholder text (e.g., `<insert image here>`, `<insert notable threats...>`) once replacements are added.

  ## 2. Diagram Generation:
  - Use Mermaid to generate diagrams directly inside markdown when applicable.
  - Output all image-based diagrams (if any) to the `security/diagrams/` folder.
  - Generate and insert both diagrams in the corresponding markdown image sections using the following approach:

    ### Architecture Diagram
    - If the architecture is inferable from the project structure or source code, generate a high-level Mermaid `graph TD` diagram showing components like clients, APIs, services, databases, storage, monitoring, identity, etc.
    - Save the rendered PNG version to `security/diagrams/architecture.png`.
    - Replace the placeholder with: `![Architecture Diagram](diagrams/architecture.png)`

    ### Data Flow Diagram
    - Generate a `graph LR` Mermaid diagram that shows labeled data flows between services.
    - Ensure all data flow edges are numbered (`1`, `2`, ...) and correspond to entries in the Data Flow Attributes table.
    - Save the rendered PNG version to `security/diagrams/data-flow.png`.
    - Replace the placeholder with: `![Data Flow Diagram](diagrams/data-flow.png)`

  ## 3. Data Flow Attributes Table:
  - For each numbered flow in the data flow diagram, add a row in the table.
  - Use real values from the architecture if available; otherwise, insert TODOs for human review.
  - Use these default headers unless project-specific headers are defined:
    | # | Transport Protocol | Data Classification | Authentication | Authorization | Notes |

  ## 4. Threats and Mitigations:
  - Analyze the repository for common threats (e.g., public endpoints, secrets in code, exposed ports, misconfigured roles).
  - Use knowledge of OWASP Top 10, Defender for Cloud findings, or ISE Security Threats guidance.
  - For each threat, document:
    - Title of the threat
    - Description of the threat context
    - Mitigation strategy (e.g., secure headers, token validation, RBAC)
  - Format as a bulleted list or table if appropriate.

  ## 5. Secrets Inventory:
  - Scan for `.env`, Key Vault references, GitHub Actions secrets, Terraform variables, etc.
  - For each secret, attempt to populate:
    | Name | What is its purpose? | Where does it live? | How was it generated? | Rotation strategy | Distribution method | Lifespan |
  - If values cannot be determined, insert TODO comments for developer review.

  ## 6. Code Markers and Collaboration:
  - Use `TODO:` or `FIXME:` inline to flag sections that require manual completion or confirmation.
  - Do not delete the preamble or ISE disclaimer.
  - Avoid duplicating content that can be referenced via URLs or project documentation.

  ## 7. Output:
  - Save the updated document as `security/security-plan.md` (or overwrite `security/security-template.md` if configured).
  - Ensure all generated diagrams are saved in `security/diagrams/`.

  ## 8. Keep Current:
  - Suggest a review of this file during PRs when architectural or security-affecting changes are made.
  - Encourage syncing diagram or inventory changes with customer conversations.

  Do not include these Copilot instructions in the final rendered document.
-->
