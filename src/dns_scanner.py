import socket
import dns.resolver


def get_ip_address(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None


def get_dns_records(domain, record_type):
    records = []

    try:
        answers = dns.resolver.resolve(domain, record_type)

        for answer in answers:
            records.append(str(answer))

    except Exception:
        pass

    return records


def scan_dns(domain):
    results = {
        "ip_address": get_ip_address(domain),
        "a_records": get_dns_records(domain, "A"),
        "mx_records": get_dns_records(domain, "MX"),
        "ns_records": get_dns_records(domain, "NS")
    }

    return results