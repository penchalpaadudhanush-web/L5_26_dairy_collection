# Lab 5: Reflection

### 1. What did you learn from static code analysis?

I learned that static code analysis helps identify code quality, style, and security issues without executing the program. Pylint, Bandit, and Flake8 help detect different types of problems.

### 2. What issues did you find in the original program?

The original program contained an SQL injection risk, weak MD5 hashing, shell command execution, an unused import, long lines, unclear variable naming, and an incorrect comparison with None. It also needed better documentation and consistent naming conventions.

### 3. How did you fix the identified issues?

I used parameterized SQL queries, replaced MD5 with SHA-256, removed shell command execution and the unused import, shortened long lines, improved variable names, used `is None`, added docstrings, and followed the snake_case naming convention.

### 4. Why is static code analysis important?

Static code analysis helps improve code readability, maintainability, and security. It identifies potential problems early and helps developers fix them before deployment. Running the tools again after making corrections helps verify the improvements.
