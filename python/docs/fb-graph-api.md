# Python: Facebook Graph API

## How to Publish a Facebook Page Post Using the Facebook Graph API in Python

### Overview of Facebook Graph API
- **Facebook Graph API:** Allows developers to interact with Facebook’s platform using code.

**resources:**

1. [https://developers.facebook.com/tools/explorer/](https://developers.facebook.com/tools/explorer/)

```python
import requests

def get_page_access_token(page_id, user_access_token):

    version ='v20.0'
    api_url_token = f'https://graph.facebook.com/{version}/{page_id}?fields=access_token&access_token={user_access_token}'
    try:
        response = requests.get(api_url_token)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        return data['access_token']
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def post_fb(page_id,page_access_token):
    message = 'Hello, World'
    # URL to post to a page
    url = f'https://graph.facebook.com/v20.0/{page_id}/feed'
    # Data for the post
    payload = {
        'message': message,
        'access_token': page_access_token
    }
    # Make the POST request to the Facebook Graph API
    response = requests.post(url, data=payload)
    # Check the response
    if response.status_code == 200:
        print("Post successfully published!")
    else:
        print(f"Failed to post: {response.status_code}")
        print(response.json())


# user access token
user_access_token = 'your_access_token_here'
page_id = 'your_page_id here'

page_access_token = get_page_access_token(page_id, user_access_token)

if page_access_token:
    post_fb(page_id,page_access_token)
else:
    print("Failed to obtain Page Access Token.")
```