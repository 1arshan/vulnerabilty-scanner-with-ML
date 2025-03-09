import requests

def check_vulnerabilities(response):
    """
    Check HTTP response headers for common security vulnerabilities.
    
    Args:
        response: HTTP response object from requests library
    
    Returns:
        List of vulnerability messages
    """
    vulnerabilities = []
    if 'X-Frame-Options' not in response.headers:
        vulnerabilities.append("Missing X-Frame-Options header")
    if 'Strict-Transport-Security' not in response.headers:
        vulnerabilities.append("Missing Strict-Transport-Security header")
    if 'Server' in response.headers:
        vulnerabilities.append(f"Server header discloses version: {response.headers['Server']}")
    return vulnerabilities

def scan_url(url):
    """
    Scan a given URL for vulnerabilities by sending an HTTP GET request.
    
    Args:
        url: String representing the URL to scan
    
    Returns:
        List of vulnerability messages or error message
    """
    try:
        response = requests.get(url)
        vulns = check_vulnerabilities(response)
        return vulns
    except requests.exceptions.RequestException as e:
        return [f"Error: {e}"]