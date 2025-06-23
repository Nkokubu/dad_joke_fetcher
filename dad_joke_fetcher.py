import requests

# Send a GET request with header for plain text
response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "text/plain"})

# Print the joke
print("Here's a dad joke for you:")
print(response.text.strip())
