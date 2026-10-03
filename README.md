# NetReconAI

AI-Assisted Domain Security & Network Reconnaissance Tool built with Python.

NetReconAI is a defensive cybersecurity project designed to collect basic domain, DNS, web security, and common port information for authorized security testing and educational purposes.

## Features

* Domain IP address lookup
* DNS A record analysis
* DNS MX record analysis
* DNS NS record analysis
* HTTP/HTTPS status checking
* Security header detection
* Common TCP port checking
* Basic risk assessment
* JSON report generation
* Modular Python architecture

## Project Structure

```text
NetReconAI/
│
├── src/
│   ├── main.py
│   ├── dns_scanner.py
│   ├── web_scanner.py
│   ├── port_scanner.py
│   ├── risk_analyzer.py
│   └── report_generator.py
│
├── reports/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Requirements

* Python 3.x
* dnspython
* requests

## Installation

Clone the repository:

```bash
git clone https://github.com/HexMindAI/NetReconAI.git
cd NetReconAI
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run NetReconAI:

```bash
python src/main.py
```

When prompted, enter a domain that you own or are authorized to test:

```text
Enter a domain you own or are authorized to test:
```

The tool performs:

* DNS analysis
* Website security checks
* Security header detection
* Common TCP port checks
* Basic security risk analysis
* JSON report generation

## JSON Reports

NetReconAI automatically generates a JSON report after a successful scan.

Example:

```text
reports/
└── example.com_report.json
```

Generated reports are excluded from Git tracking through `.gitignore`.

## Security Note

NetReconAI is intended for educational purposes and authorized defensive security testing only.

Only scan domains and systems that you own or have explicit permission to test.

Do not use this tool to access, disrupt, attack, or interfere with systems without authorization.

## Risk Analysis

NetReconAI currently uses a basic heuristic to identify security findings.

The risk score is based on checks such as:

* Missing security headers
* Selected open network ports

The reported risk level is an indication from the project's current checks and should not be considered a complete vulnerability assessment or guaranteed security rating.

## Current Status

Version: 1.0

Implemented:

* DNS analysis
* HTTP/HTTPS analysis
* Security header checks
* Common port scanning
* Basic risk analysis
* JSON reporting

## Future Improvements

Planned improvements include:

* AI-assisted security explanations
* Additional DNS record types
* Improved risk analysis
* Command-line arguments
* HTML security reports
* Additional defensive security checks
* Better error handling
* Scan history

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

## Author

**HexMindAI**

Cybersecurity & AI Enthusiast | Python Developer
