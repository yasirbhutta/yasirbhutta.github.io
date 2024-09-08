# Python: Facebook Graph API

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaeGV0517En4iyZGWn2P) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

## How to Publish a Facebook Page Post Using the Facebook Graph API in Python

### Overview of Facebook Graph API
- **Facebook Graph API:** Allows developers to interact with Facebook’s platform using code.

**resources:**

1. [https://developers.facebook.com/tools/explorer/](https://developers.facebook.com/tools/explorer/)

```python
import requests  # Import the requests library to handle HTTP requests

def get_page_access_token(page_id, user_access_token):
    """
    Function to retrieve the Page Access Token using the user access token and page ID.
    """

    # Define the Graph API version and construct the API URL to request the Page Access Token
    version = 'v20.0'
    api_url_token = f'https://graph.facebook.com/{version}/{page_id}?fields=access_token&access_token={user_access_token}'
    
    try:
        # Make a GET request to the Facebook Graph API to fetch the Page Access Token
        response = requests.get(api_url_token)
        response.raise_for_status()  # Raise an exception if the request returns an HTTP error

        # Parse the response as JSON and return the access token
        data = response.json()
        return data['access_token']
    except requests.exceptions.RequestException as e:
        # Handle any exceptions (e.g., network issues, API errors) and print the error
        print("Error:", e)
        return None  # Return None if the access token retrieval fails

def post_fb(page_id, page_access_token):
    """
    Function to publish a post to the Facebook Page using the Page Access Token.
    """
    
    message = 'Hello, World'  # The message that will be posted to the Facebook Page
    
    # Construct the URL for the POST request to the page's feed
    url = f'https://graph.facebook.com/v20.0/{page_id}/feed'
    
    # Define the payload (message and access token) that will be sent in the POST request
    payload = {
        'message': message,
        'access_token': page_access_token
    }
    
    # Make the POST request to the Facebook Graph API to publish the post
    response = requests.post(url, data=payload)
    
    # Check the response status and print a success or failure message accordingly
    if response.status_code == 200:
        print("Post successfully published!")
    else:
        print(f"Failed to post: {response.status_code}")
        print(response.json())  # Print the error details from the API response

# User access token (replace with your actual user access token)
user_access_token = 'your_access_token_here'

# Facebook Page ID (replace with your actual page ID)
page_id = 'your_page_id_here'

# Retrieve the Page Access Token using the user access token and page ID
page_access_token = get_page_access_token(page_id, user_access_token)

# If the Page Access Token was successfully retrieved, publish the post
if page_access_token:
    post_fb(page_id, page_access_token)
else:
    print("Failed to obtain Page Access Token.")  # Print an error if the token retrieval fails
```

### Explanation:
- **get_page_access_token:** This function requests the Page Access Token from Facebook's Graph API using a user access token and page ID. The function handles errors and returns the token if successful.
  
- **post_fb:** This function uses the Page Access Token to publish a post to the specified Facebook Page by making a POST request to the Graph API's feed endpoint.

- **Main Script:** After fetching the Page Access Token, the script attempts to post a message to the page. If the token retrieval fails, an error message is displayed.