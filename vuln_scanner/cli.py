import argparse
from vuln_scanner.scanner.web_scan import scan_url
from vuln_scanner.ml.predict import predict_anomaly

def main():
    """
    Command-line interface for the Vulnerability Scanner.
    """
    parser = argparse.ArgumentParser(description="Vulnerability Scanner CLI")
    parser.add_argument("command", choices=["scan"], help="Command to execute")
    parser.add_argument("url", help="URL to scan")
    args = parser.parse_args()
    
    if args.command == "scan":
        vulns = scan_url(args.url)
        print("Vulnerabilities found:")
        for v in vulns:
            print(f"- {v}")
        
        # Sample request for anomaly prediction
        sample_request = {'url': args.url, 'params': '', 'method': 'GET'}
        anomaly_result = predict_anomaly(sample_request)
        print(f"Anomaly Detection: {anomaly_result}")

if __name__ == "__main__":
    main()