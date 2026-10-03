def generate_security_explanation(risk_results):
    """
    Generate human-readable security explanations
    from NetReconAI's existing risk findings.

    This is a local rule-based analysis layer.
    It does not connect to an external AI service.
    """

    risk_level = risk_results.get("risk_level", "UNKNOWN")
    risk_score = risk_results.get("risk_score", 0)
    findings = risk_results.get("findings", [])

    explanations = []

    for finding in findings:

        if "Missing security header" in finding:
            header = finding.split(": ", 1)[-1]

            explanations.append({
                "finding": finding,
                "explanation": (
                    f"The {header} security header was not detected. "
                    "Security headers can help reduce certain browser-based "
                    "security risks."
                ),
                "recommendation": (
                    f"Review the web server configuration and consider "
                    f"implementing {header} where appropriate."
                )
            })

        elif "Open port detected" in finding:
            parts = finding.split(":", 1)[-1].strip()

            explanations.append({
                "finding": finding,
                "explanation": (
                    f"The service associated with {parts} is reachable "
                    "on the scanned host."
                ),
                "recommendation": (
                    "Verify that the service is required and restrict "
                    "network exposure when it is not needed."
                )
            })

        else:
            explanations.append({
                "finding": finding,
                "explanation": "The scanner identified a security-related finding.",
                "recommendation": (
                    "Review this finding and verify the related configuration."
                )
            })

    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "explanations": explanations
    }