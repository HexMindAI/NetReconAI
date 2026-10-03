import socket


def scan_common_ports(domain):
    ports = {
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-ALT"
    }

    results = {}

    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror:
        return results

    for port, service in ports.items():

        try:
            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(1)

            result = sock.connect_ex(
                (ip_address, port)
            )

            sock.close()

            results[port] = {
                "service": service,
                "open": result == 0
            }

        except Exception:
            results[port] = {
                "service": service,
                "open": False
            }

    return results