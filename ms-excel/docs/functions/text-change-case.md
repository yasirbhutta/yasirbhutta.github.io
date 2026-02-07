---
layout: page
title: "How to Change Text Case in Excel | Excel Text Functions"
description: Learn how to use Excel’s text case functions like UPPER, LOWER, and PROPER. Easily change text case for efficient data formatting and analysis.
keywords: excel change text case, excel UPPER function, excel LOWER function, excel PROPER function, excel text functions, excel text formatting, MS excel tips, excel function guide, excel tutorial, text case conversion in excel
author: Muhammad Yasir Bhutta
course: ms-excel
topic: functions
toc: toc/ms-excel-toc.html
prev: /ms-excel/docs/functions/date-time.html
next: /ms-excel/docs/functions/len-lenb.html
breadcrumb: 
- title: Functions
url: /ms-excel/docs/functions.html
---

[Download PDF](/downloads/ms-excel/functions/text-change-case.pdf)

## Change the case of Text

**LOWER function:** Converts all uppercase letters in a text string to lowercase.

**Syntax:**

```excel
LOWER(text)
```

The LOWER function syntax has the following arguments:

Text Required. The text you want to convert to lowercase. LOWER does not change characters in text that are not letters.

**UPPER function:** Converts text to uppercase.

**Syntax:**

```excel
UPPER(text)
```

The UPPER function syntax has the following arguments:

Text Required. The text you want converted to uppercase. Text can be a reference or text string.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1602443888929206"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-1602443888929206"
     data-ad-slot="6296238623"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

**PROPER function:**

- [Video Tutorial: Change the case of text in excel](https://youtu.be/X38NcRn0PhM?si=pCO7K-DuBJKz5G9b)

**See also:**

- [LOWER function - Microsoft Support](https://support.microsoft.com/en-us/office/lower-function-3f21df02-a80c-44b2-afaf-81358f9fdeb4#:~:text=The%20LOWER%20function%20syntax%20has,text%20that%20are%20not%20letters.)
- [UPPER function - Microsoft Support](https://support.microsoft.com/en-gb/office/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6)
- [Change the case of text - Microsoft Support](https://support.microsoft.com/en-gb/office/change-the-case-of-text-01481046-0fa7-4f3b-a693-496795a7a44d)

**Exercise :** Lowercase Conversion

1. Create a new worksheet.
2. In cell A1, type "PYTHON PROGRAMMING IS FUN."
3. In cell B1, use the LOWER function to convert the text in cell A1 to lgowercase. The formula should look like this: =LOWER(A1). B1 should display "python programming is fun."

**Exercise :** Proper Case Conversion

1. Open a new Excel worksheet.
2. In cell A1, type "muhammad ahmad."
3. In cell B1, use the PROPER function to convert the text in cell A1 to proper case. The formula should look like this: =PROPER(A1). B1 should display "Muhammad Ahmad."

**Exercise :** Change the following text to uppercase.

```excel
This is a sample text.
```

**Exercise:** Change the following text to lowercase.

```excel
THIS IS A SAMPLE TEXT.
```

**Exercise :** Change the following text to title case.

```excel
this is a sample text.
```

**Exercise :** Create a new column called "Title Case" and use the PROPER function to convert the text in Column A to title case.

Sample Data:

| **Good Habits**|
| ------------ |
| regular exercise|
| healthy eating       |
| adequate sleep      |
| time management|
| mindfulness and meditation|
