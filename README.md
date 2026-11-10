# .SA Domain Checker

A Python-based domain availability checker that automatically generates and checks short `.sa` domain names using an API.

Built to explore **Python automation, HTTP requests, API integration, and data collection**, with a focus on Saudi Arabian domains.

## Overview

Finding short, memorable domain names can be challenging, especially when most common combinations are already registered.

**SA Domain Checker** automates the process by generating combinations of letters and numbers, checking their availability, and storing the results in a CSV file for further analysis.

The project focuses on the `.sa` country-code top-level domain (ccTLD) for Saudi Arabia.

## Features

- **Automated domain generation:** Generates combinations of lowercase letters and digits.
- **Short domain scanning:** Checks one-, two-, and three-character `.sa` domains.
- **API integration:** Sends HTTP requests to a domain availability service.
- **CSV export:** Saves domain names and their reported availability.
- **Real-time output:** Prints results to the terminal as each domain is checked.
- **Incremental storage:** Appends results to an existing CSV file.

## How It Works

The script generates domain names using the following character set:

```python
abcdefghijklmnopqrstuvwxyz0123456789
```

This provides 36 possible characters for each position.

### Domain Combinations

| Length | Combinations | Example |
|---|---:|---|
| 1 character | 36 | `a.sa` |
| 2 characters | 1,296 | `ab.sa` |
| 3 characters | 46,656 | `abc.sa` |
| **Total** | **47,988** | |

The script also includes `ax.sa` as an additional explicit entry, resulting in 47,989 checks, including one duplicate.

### Availability Checking

For each generated domain, the script sends a POST request to the domain availability API.

```text
https://api-domains.solutions.com.sa/v1/open/domains/search?checkVariant=true
```

The request includes the domain name in JSON format:

```json
{
  "domainName": "abc.sa"
}
```

The script reads the `isAvailable` field from the API response and records the result.

### Output

Results are saved to:

```text
available_domains.csv
```

Example CSV structure:

```csv
domain,isAvailable
abc.sa,False
xyz.sa,True
123.sa,False
```

These are illustrative results, not verified availability statuses.

## Getting Started

### Requirements

- Python 3
- pip
- Internet connection
- `requests` library

### 1. Clone the Repository

```bash
git clone https://github.com/Fai707/sa-domain-checker.git
cd sa-domain-checker
```

### 2. Install Dependencies

```bash
pip install requests
```

### 3. Run the Script

```bash
python main.py
```

The script begins generating domain combinations and checking their availability.

Results are printed to the terminal and appended to `available_domains.csv`.

## Repository Structure

```text
sa-domain-checker/
├── main.py                 # Domain generation and API requests
├── README.md               # Project documentation
└── available_domains.csv   # Generated output (after execution)
```

## Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | HTTP API communication |
| CSV | Result storage |
| REST API | Domain availability lookup |

## Limitations

The current implementation is a simple automation script with several limitations:

- Generates only one-, two-, and three-character domains.
- Makes requests sequentially.
- Does not implement rate limiting or retry handling.
- Does not resume from the last checked domain.
- Does not handle network errors or unexpected API responses.
- Appends results to the CSV file, which can produce duplicate records across runs.
- Relies on a third-party API whose availability and behavior may change.

**Important:** A domain reported as available by an API is not necessarily eligible for registration. Saudi domain registration requirements and naming restrictions still apply.

## Future Improvements

Potential improvements include:

- Configurable minimum and maximum domain lengths.
- Command-line arguments for custom scans.
- Automatic retry handling and request timeouts.
- Rate limiting to respect API usage policies.
- Resume functionality for interrupted scans.
- Filtering results to show only available domains.
- Progress tracking and estimated completion time.
- Improved error handling and logging.

## What I Learned

This project provided practical experience with:

- Python scripting and automation.
- Generating combinations using nested loops.
- Working with HTTP POST requests.
- Processing JSON API responses.
- Reading and writing CSV files.
- Automating repetitive tasks.
- Understanding domain availability lookup systems.

## Responsible Usage

This project is intended for educational purposes and legitimate domain research.

Users should respect the API provider's terms of service, request limits, and applicable domain registration policies.

Avoid excessive automated requests that could negatively affect third-party services.

## Author

**Fai707**

GitHub: [github.com/Fai707](https://github.com/Fai707)
