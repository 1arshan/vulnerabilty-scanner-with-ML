from flask import Flask, request, render_template
from vuln_scanner.scanner.web_scan import scan_url
from vuln_scanner.ml.predict import predict_anomaly

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handle GET and POST requests for the main page.
    - GET: Display the URL input form.
    - POST: Scan the URL and display results.
    """
    if request.method == 'POST':
        url = request.form['url']
        vulns = scan_url(url)
        # Sample request for anomaly prediction
        sample_request = {'url': url, 'params': '', 'method': 'GET'}
        anomaly_result = predict_anomaly(sample_request)
        return render_template('results.html', vulns=vulns, anomaly=anomaly_result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)