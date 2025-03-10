import random
import pandas as pd

def generate_normal_request():
    """Generate a single normal HTTP request."""
    urls = [
        'http://example.com/',
        'http://example.com/login',
        'http://example.com/search',
        'http://example.com/profile',
        'http://example.com/contact'
    ]
    url = random.choice(urls)
    if url == 'http://example.com/':
        params = ''
    elif url == 'http://example.com/login':
        user = random.choice(['admin', 'user1', 'user2', 'user3'])
        passw = random.choice(['123', 'password', 'qwerty', 'letmein'])
        params = f'user={user}&pass={passw}'
    elif url == 'http://example.com/search':
        query = random.choice(['python', 'java', 'machine learning', 'web development', 'data science'])
        params = f'q={query}'
    elif url == 'http://example.com/profile':
        id = random.randint(1, 100)
        params = f'id={id}'
    elif url == 'http://example.com/contact':
        name = random.choice(['John', 'Alice', 'Bob', 'Charlie'])
        email = f'{name.lower()}@example.com'
        message = random.choice(['Hello', 'Hi', 'Contact me', 'Question'])
        params = f'name={name}&email={email}&message={message}'
    return {'url': url, 'method': 'GET', 'params': params}

def generate_anomalous_request():
    """Generate a single anomalous HTTP request."""
    urls = [
        'http://example.com/login',
        'http://example.com/search'
    ]
    anomalous_patterns = [
        "' OR 1=1 --",
        "UNION SELECT * FROM users",
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "sqlmap",
        "admin' --",
        "DROP TABLE users",
        "SELECT * FROM information_schema.tables"
    ]
    url = random.choice(urls)
    if url == 'http://example.com/login':
        user = random.choice(anomalous_patterns)
        passw = '123'
        params = f'user={user}&pass={passw}'
    elif url == 'http://example.com/search':
        query = random.choice(anomalous_patterns)
        params = f'q={query}'
    return {'url': url, 'method': 'GET', 'params': params}

def generate_dataset(num_normal, num_anomalous):
    """Generate a dataset with specified numbers of normal and anomalous requests."""
    dataset = []
    # Generate normal requests
    for _ in range(num_normal):
        dataset.append(generate_normal_request())
    # Generate anomalous requests
    for _ in range(num_anomalous):
        dataset.append(generate_anomalous_request())
    # Shuffle the dataset to mix normal and anomalous requests
    random.shuffle(dataset)
    return dataset

if __name__ == "__main__":
    # Set the number of requests
    num_normal = 900
    num_anomalous = 100
    # Generate the dataset
    dataset = generate_dataset(num_normal, num_anomalous)
    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(dataset)
    df.to_csv('raw/http_requests.csv', index=False)
    print(f"Generated {len(dataset)} requests and saved to data/raw/http_requests.csv")