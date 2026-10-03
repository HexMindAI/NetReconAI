import requests


def scan_website(domain):
    result = {
        "https_status": None,
        "final_url": None,
        "security_headers": {},
        "error": None
    }

    url = "https://" + domain

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        result["https_status"] = response.status_code
        result["final_url"] = response.url

        security_headers = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Referrer-Policy",
            "Permissions-Policy"
        ]

        for header in security_headers:
            result["security_headers"][header] = (
                header in response.headers
            )

    except requests.RequestException as error:
        result["error"] = str(error)

    return result