from api_autoresbot import ApiAutoresbot

# Initialize the API client
api = ApiAutoresbot(api_key="your_api_key_here")

# Example GET request
try:
    response = api.get("/some-endpoint", params={"param1": "value1"})
    print(response)
except Exception as e:
    print(f"Error: {e}")

# Example POST request
try:
    response = api.post("/some-endpoint", data={"key": "value"})
    print(response)
except Exception as e:
    print(f"Error: {e}")

# Example file upload
try:
    response = api.tmp_upload("path/to/file.pdf")
    print(response)
except Exception as e:
    print(f"Error: {e}")
