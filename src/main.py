from dns_scanner import scan_dns
from web_scanner import scan_website
from port_scanner import scan_common_ports
from risk_analyzer import analyze_risk
from report_generator import generate_report


def print_results(domain, dns_results, web_results, port_results, risk_results):

    print("\n" + "=" * 60)
    print("                 NETRECONAI")
    print("          DOMAIN SECURITY ANALYZER")
    print("=" * 60)

    print(f"\nTarget: {domain}")

    # IP Address
    print("\n[IP ADDRESS]")

    if dns_results["ip_address"]:
        print(f"  [+] {dns_results['ip_address']}")
    else:
        print("  [-] Could not resolve IP address.")

    # DNS A Records
    print("\n[DNS A RECORDS]")

    if dns_results["a_records"]:
        for record in dns_results["a_records"]:
            print(f"  [+] {record}")
    else:
        print("  [-] No A records found.")

    # DNS MX Records
    print("\n[DNS MX RECORDS]")

    if dns_results["mx_records"]:
        for record in dns_results["mx_records"]:
            print(f"  [+] {record}")
    else:
        print("  [-] No MX records found.")

    # DNS NS Records
    print("\n[DNS NS RECORDS]")

    if dns_results["ns_records"]:
        for record in dns_results["ns_records"]:
            print(f"  [+] {record}")
    else:
        print("  [-] No NS records found.")

    # Website
    print("\n[HTTP/HTTPS SECURITY CHECK]")

    if web_results["https_status"]:
        print(f"  [+] HTTPS Status: {web_results['https_status']}")
        print(f"  [+] Final URL: {web_results['final_url']}")
    else:
        print("  [-] HTTPS connection failed.")

    # Security Headers
    print("\n[SECURITY HEADERS]")

    for header, present in web_results["security_headers"].items():

        if present:
            print(f"  [+] {header}: Present")
        else:
            print(f"  [-] {header}: Missing")

    # Ports
    print("\n[COMMON PORT SCAN]")

    for port, information in port_results.items():

        if information["open"]:
            print(
                f"  [+] Port {port:<5} OPEN   "
                f"{information['service']}"
            )
        else:
            print(
                f"  [-] Port {port:<5} CLOSED "
                f"{information['service']}"
            )

    # Risk
    print("\n[SECURITY RISK ANALYSIS]")

    print(
        f"  Risk Score: {risk_results['risk_score']}"
    )

    print(
        f"  Risk Level: {risk_results['risk_level']}"
    )

    print("\n[SECURITY FINDINGS]")

    if risk_results["findings"]:

        for finding in risk_results["findings"]:
            print(f"  [!] {finding}")

    else:
        print("  [+] No findings from current checks.")

    print("\n" + "=" * 60)
    print("             Analysis completed.")
    print("=" * 60)


def main():

    print("\nWelcome to NetReconAI")

    domain = input(
        "\nEnter a domain you own or are authorized to test: "
    ).strip()

    # Clean input
    domain = domain.replace("https://", "")
    domain = domain.replace("http://", "")
    domain = domain.rstrip("/")

    if not domain:
        print("Please enter a domain.")
        return

    print("\nScanning...")
    print("Please wait...\n")

    # DNS Scan
    dns_results = scan_dns(domain)

    # Website Scan
    web_results = scan_website(domain)

    # Port Scan
    port_results = scan_common_ports(domain)

    # Risk Analysis
    risk_results = analyze_risk(
        web_results,
        port_results
    )

    # Display results
    print_results(
        domain,
        dns_results,
        web_results,
        port_results,
        risk_results
    )

    # Generate JSON report
    report_file = generate_report(
        domain,
        dns_results,
        web_results,
        port_results,
        risk_results
    )

    print(f"\n[+] JSON report saved to: {report_file}")


if __name__ == "__main__":
    main()