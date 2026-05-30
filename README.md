# ThreatLens

ThreatLens is a Python-based threat intelligence tool that analyzes the reputation of URLs and IP addresses using the VirusTotal API. The project combines external threat intelligence with custom reputation scoring to help identify potentially malicious indicators of compromise (IOCs).

## Features

### URL Reputation Scanning

* Scan URLs using the VirusTotal API
* Retrieve malicious, suspicious, harmless, and undetected verdicts
* Generate a custom URL reputation score based on phishing indicators
* Detect suspicious keywords commonly used in phishing attacks
* Detect URL shortening services
* Identify insecure HTTP connections
* Flag unusually long URLs

### IP Reputation Scanning

* Check IP reputation using VirusTotal
* Identify malicious or suspicious IP addresses
* View detection statistics from multiple security vendors

### Threat Intelligence Integration

* VirusTotal API integration
* Real-time scan status monitoring
* Automated result retrieval
* Basic error handling and timeout protection

## Technologies Used

* Python 3
* Requests Library
* VirusTotal API

## Installation

Clone the repository:

```bash
git clone https://github.com/Kluuuz/ThreatLens.git
cd threatlens
```

Install dependencies:

```bash
pip install requests
```

## Configuration

Obtain a free API key from VirusTotal.

Store your API key in the script:

```python
API = "YOUR_API_KEY"
```

For better security, use environment variables instead of hardcoding your API key.

## Usage

Run the scanner:

```bash
python scanner.py
```

Menu:

```text
OPTIONS:
1. Scan URL
2. Scan IP reputation
```

Example:

```text
Enter URL: http://example.com

===== URL Reputation =====
Risk Score: 45
⚠ MEDIUM RISK (Suspicious)

===== RESULTS =====
Malicious : 2
Suspicious: 1
Harmless  : 78
Undetected: 11
```

## How It Works

1. User submits a URL or IP address.
2. ThreatLens sends the indicator to VirusTotal.
3. VirusTotal analyzes the indicator using multiple security vendors.
4. ThreatLens retrieves the completed analysis.
5. Detection statistics and reputation scores are displayed to the user.

## Future Improvements

* IOC logging
* JSON and CSV report generation
* Domain reputation analysis
* WHOIS integration
* Threat scoring improvements
* Batch scanning
* Dashboard interface
* SIEM integration

## Disclaimer

This project is intended for educational purposes, cybersecurity research, and threat intelligence learning. Always follow applicable laws, organizational policies, and VirusTotal's terms of service when using this tool.
