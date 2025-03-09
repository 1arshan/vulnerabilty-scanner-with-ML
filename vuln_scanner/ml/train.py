import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OneHotEncoder
import joblib
from .features import extract_features

# Mock data for training (replace with real data in practice)
data = [
    {'url': 'http://example.com', 'params': '', 'method': 'GET'},
    {'url': 'http://example.com/login', 'params': 'user=admin&pass=123', 'method': 'POST'},
    {'url': 'http://example.com/search', 'params': 'q=test', 'method': 'GET'},
    {'url': 'http://example.com/search', 'params': 'q=<script>alert(1)</script>', 'method': 'GET'},
]

# Extract features and create a DataFrame
df = pd.DataFrame([extract_features(req) for req in data])

# One-hot encode the 'method' column
encoder = OneHotEncoder(sparse_output=False)
method_encoded = encoder.fit_transform(df[['method']])
method_df = pd.DataFrame(method_encoded, columns=encoder.get_feature_names_out())

# Combine numeric features with encoded method
features_df = pd.concat([df.drop('method', axis=1), method_df], axis=1)

# Train the Isolation Forest model
model = IsolationForest(contamination=0.1)
model.fit(features_df)

# Save the trained model and encoder
joblib.dump(model, 'isolation_forest_model.pkl')
joblib.dump(encoder, 'method_encoder.pkl')