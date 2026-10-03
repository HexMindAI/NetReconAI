import json
import os
from datetime import datetime


def generate_report(domain, dns_results, web_results, port_results, risk_results):

    report = {
        "target": domain,
        "scan_time": datetime.now().isoformat(),
        "dns": dns_results,
        "website": web_results,
        "ports": port_results,
        "security": risk_results
    }

    os.makedirs("reports", exist_ok=True)

    safe_domain = domain.replace("/", "_").replace(":", "_")

    filename = f"reports/{safe_domain}_report.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            indent=4
        )

    return filename