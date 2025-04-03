# How to make embedded youtube video responsive

## **Step 1:** Embed a video or playlist

1. On a computer, go to the YouTube video or playlist you want to embed.
2. Click `SHARE` .
3. From the list of Share options, click `Embed`.
4. From the box that appears, copy the HTML code.
5. Paste the code into your website HTML.

## **Step 2: Make YouTube Video Embeds Responsive**  

When embedding YouTube videos, it’s important to ensure they adjust seamlessly to different screen sizes. Here are two methods to make your video embeds responsive:  

---

### ✅ **Method 1: Quick Inline Approach**  

Set the `width` attribute of the `<iframe>` to `100%` to make it responsive.  

```html
<iframe width="100%" height="315" src="https://www.youtube.com/embed/66N2Kmca21U?si=bl8EQbReO-w1kuQP" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen>
</iframe>
```

---

### ✅ **Method 2: Using a CSS Class**  

This approach provides better control, especially when you need to reuse styles across multiple videos.  

1. **Create a generic class in your CSS file:**  

```css
.yt-video {
    width: 100%;
    height: 315px;
    max-width: 100%;
    text-align: center;
}
```

2. **Apply the class to your iframe:**  

```html
<iframe class="yt-video" src="https://www.youtube.com/embed/rcVVfyeJfLk?si=xM8iE8vU0g9J66qY" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen>
</iframe>
```

---

Both methods will make your YouTube embeds adapt smoothly to different screen sizes. For consistent styling, Method 2 is recommended.