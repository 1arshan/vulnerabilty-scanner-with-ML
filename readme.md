# Vulnerability Scanner with ML-Driven Anomaly Detection

This project is a modular, extensible tool designed to scan web applications for common vulnerabilities and detect anomalies using machine learning. By combining traditional scanning techniques with AI-driven insights, it aims to provide a comprehensive security assessment for web applications. The project is currently under active development, with a focus on creating a flexible architecture that supports future enhancements.

## Features
### Current Features
- **Basic Web Vulnerability Scanning**: Checks for common issues such as missing security headers (e.g., X-Frame-Options, Strict-Transport-Security) and server version disclosure.
- **Simple Machine Learning Model**: Uses an Isolation Forest algorithm to detect anomalies in HTTP requests, helping identify potential security threats.
- **Command-Line Interface (CLI)**: Allows users to run scans directly from the terminal.
- **Modular Architecture**: Designed with separate modules for scanning, machine learning, and interfaces, making it easy to extend and maintain.

### Planned Features
- **Advanced Vulnerability Detection**: Implement checks for SQL injection, cross-site scripting (XSS), CSRF, and other common web vulnerabilities.
- **Enhanced Machine Learning Models**: Develop more sophisticated models (e.g., deep learning) to improve anomaly detection accuracy and adapt to new threats.
- **User-Friendly Web Interface**: Expand the current basic Flask-based UI to include scan management, result visualization, and detailed reporting.
- **API and Network Scanning**: Extend scanning capabilities to include RESTful APIs and network-level vulnerabilities.
- **CI/CD Integration**: Enable automated security checks within continuous integration and deployment pipelines.

## Architecture
The project follows a modular design to ensure scalability, maintainability, and ease of development:

- **Scanner Module (`vuln_scanner/scanner/`)**: Contains all scanning logic, including web vulnerability checks. Future extensions (e.g., network or API scanning) can be added here without affecting other components.
- **ML Module (`vuln_scanner/ml/`)**: Manages machine learning tasks such as model training, anomaly prediction, and feature extraction. This separation allows for easy experimentation with different algorithms.
- **Web Interface (`web/`)**: A Flask-based UI that provides a user-friendly way to interact with the scanner. It is kept separate from the core logic to allow for alternative interfaces (e.g., REST API) in the future.
- **CLI (`vuln_scanner/cli.py`)**: A command-line interface for users who prefer terminal-based operations. It leverages the same core modules as the web interface.

This architecture ensures that each component can be developed, tested, and extended independently, promoting a clean and organized codebase.

## Technology Stack
- **Backend**: Python 3.x