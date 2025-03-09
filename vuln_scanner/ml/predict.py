import pandas as pd
import joblib
from .features import extract_features

def predict_anomaly(request):
    """
    Predict whether an HTTP request is anomalous using the trained model.
    
    Args:
        request: Dictionary containing 'url', 'params', and 'method'
    
    Returns:
        String indicating if the request is an anomaly or normal
    """
    # Load the trained model and encoder
    model = joblib.load('isolation_forest_model.pkl')
    encoder = joblib.load('method_encoder.pkl')
    
    # Extract features and encode the method
    features = extract_features(request)
    method_encoded = encoder.transform([[features['method']]])
    features_list = [features['url_length'], features['num_params'], features['has_sql'], features['has_script']] + list(method_encoded[0])
    features_df = pd.DataFrame([features_list], columns=['url_length', 'num_params', 'has_sql', 'has_script'] + list(encoder.get_feature_names_out()))
    
    # Make prediction
    prediction = model.predict(features_df)[0]
    return "Anomaly detected" if prediction == -1 else "Normal request"