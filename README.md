# NetReconAI

AI-Assisted Domain Security & Network Reconnaissance Tool built with Python.

NetReconAI is a defensive cybersecurity project designed to collect basic domain, DNS, web security, and common port information for authorized security testing and educational purposes.

## Features

- Domain IP address lookup
- DNS A record analysis
- DNS MX record analysis
- DNS NS record analysis
- HTTP/HTTPS status checking
- Security header detection
- Common TCP port checking
- Basic risk assessment
- JSON report generation
- Modular Python architecture

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
└── .gitignore