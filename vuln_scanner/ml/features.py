def extract_features(request):
    """
    Extract features from an HTTP request for ML processing.
    
    Args:
        request: Dictionary containing 'url', 'params', and 'method'
    
    Returns:
        Dictionary of extracted features
    """
    features = {}
    features['url_length'] = len(request['url'])
    features['num_params'] = len(request['params'].split('&')) if request['params'] else 0
    features['has_sql'] = 1 if 'sql' in request['params'].lower() else 0
    features['has_script'] = 1 if 'script' in request['params'].lower() else 0
    features['method'] = request['method']
    return features