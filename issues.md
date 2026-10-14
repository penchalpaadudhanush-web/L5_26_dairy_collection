# Lab 5: Static Code Analysis — Issues Found

| Issue | Type | Original Line(s) | Description | Fix Applied |
|---|---|---:|---|---|
| SQL injection risk | Security | 11 | SQL query used string formatting with user input. | Used parameterized SQL queries. |
| Weak MD5 hashing | Security | 16 | MD5 is considered weak for security-sensitive use. | Replaced MD5 with SHA-256. |
| Shell command execution | Security | 31 | `os.system()` executed a shell command. | Replaced shell execution with Python's `print()`. |
| Unused import | Code quality | 2 | The `json` module was imported but not used. | Removed the unused import. |
| Long lines | Code style | 7, 11, 20, 25 | Some lines exceeded the length limit. | Split long statements across multiple lines. |
| Unclear variable name | Code style | 26 | The variable `l` was difficult to understand. | Renamed it to `top`. |
| Incorrect None comparison | Code quality | 36 | The code used `fat == None`. | Changed it to `fat is None`. |
| Missing documentation and naming issues | Code quality | Multiple | Functions lacked docstrings and used inconsistent naming. | Added docstrings and used snake_case names. |

## Verification

After fixing the issues, I ran Pylint, Bandit, and Flake8 again on the corrected Python program. Pylint reported 10.00/10, Bandit reported no detected issues, and Flake8 produced no violations.
