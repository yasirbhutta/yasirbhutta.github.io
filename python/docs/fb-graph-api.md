---
layout: page
title: Python- Facebook Graph API
description: Learn Python variables with this beginner-friendly guide. Understand variable naming rules, assignments, and operations with examples and exercises. Perfect for students and professionals starting their Python journey.  
keywords: Python variables, Python variable examples, Python variable exercises, Python variable naming rules, Python variable assignment, Python beginner tutorials, Python programming basics, learn Python variables, Python coding exercises
toc: toc/python.html
---

## How to Publish a Facebook Page Post Using the Facebook Graph API in Python

<div class="yt-video">
<iframe src="https://www.youtube.com/embed/oSIFwDkBWB4?si=TBpex89UMzdI-P0X" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## Overview of Facebook Graph API

- **Facebook Graph API:** Allows developers to interact with Facebook’s platform using code.

**resources:**

1. [https://developers.facebook.com/apps/](https://developers.facebook.com/apps/)
2. [https://developers.facebook.com/tools/explorer/](https://developers.facebook.com/tools/explorer/)
3. [Facebook Graph API: Access Token Debugger](https://developers.facebook.com/tools/debug/accesstoken/)

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

## Explanation:

- **get_page_access_token:** This function requests the Page Access Token from Facebook's Graph API using a user access token and page ID. The function handles errors and returns the token if successful.
  
- **post_fb:** This function uses the Page Access Token to publish a post to the specified Facebook Page by making a POST request to the Graph API's feed endpoint.

- **Main Script:** After fetching the Page Access Token, the script attempts to post a message to the page. If the token retrieval fails, an error message is displayed.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<!-- display square -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="9845543342"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>