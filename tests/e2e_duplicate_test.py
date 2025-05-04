import requests

base_url = "http://localhost:8000"

# First guess should succeed
r1 = requests.post(f"{base_url}/guess", json={"guess": "Paper"})
print(r1.json())

# Duplicate guess should fail
r2 = requests.post(f"{base_url}/guess", json={"guess": "Paper"})
print(r2.json())
