# **How to Embed YouTube Shorts in Your HTML Web Page**

To embed a YouTube Short in an HTML page, follow these steps:  

1. Go to the YouTube Short you want to embed.  
2. Click on the `Share` button and select `Embed.`  
3. Copy the provided iframe code.  
4. Paste it into your HTML file.  

Here's an example of how it looks in HTML:  

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Embed YouTube Short</title>
</head>
<body>
    <h1>Watch This YouTube Short</h1>
    <iframe 
        width="360" 
        height="640" 
        src="https://www.youtube.com/embed/SHORT_VIDEO_ID" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
    </iframe>
</body>
</html>
```

✅ Replace `SHORT_VIDEO_ID` with the actual ID from the YouTube Short's URL. For example, if the URL is `https://youtube.com/shorts/abc123`, use `abc123` in the iframe.