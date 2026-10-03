def analyze_risk(web_results, port_results):
    risk_score = 0
    findings = []

    # Check security headers
    headers = web_results.get("security_headers", {})

    for header, present in headers.items():
        if not present:
            risk_score += 1
            findings.append(
                f"Missing security header: {header}"
            )

    # Check open ports
    for port, information in port_results.items():
        if information["open"]:
            if port in [21, 22, 25, 3306, 8080]:
                risk_score += 1
                findings.append(
                    f"Open port detected: {port} "
                    f"({information['service']})"
                )

    # Determine risk level
    if risk_score >= 6:
        risk_level = "HIGH"
    elif risk_score >= 3:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "findings": findings
    }