---
layout: page
title: Finding Your Public IP Address: Techniques Using Command Line, PowerShell, and Python
description: To find your public IP address, you can use several methods. Here are a few tasks you can perform to achieve that: 1. Open Command Prompt. 2. Run the...
keywords: address, public, opendns, your, com
---
# Finding Your Public IP Address: Techniques Using Command Line, PowerShell, and Python

To find your public IP address, you can use several methods. Here are a few tasks you can perform to achieve that:

### Using Command Prompt (Windows)
1. Open Command Prompt.
2. Run the following command:

    ```cmd
    nslookup myip.opendns.com resolver1.opendns.com
    ```

This will show your public IP address by querying OpenDNS.

The command `nslookup myip.opendns.com resolver1.opendns.com` is used to find your public IP address by querying the OpenDNS servers. Here's a breakdown of how to use it and what to expect:

### How to Use the Command

1. **Open Command Prompt**:
   - Press `Win + R`, type `cmd`, and hit `Enter`.

2. **Run the Command**:
   - Type the following command and press `Enter`:

     ```cmd
     nslookup myip.opendns.com resolver1.opendns.com
     ```

### Expected Output

You should see output similar to this:

```
Server:  resolver1.opendns.com
Address:  208.67.222.222

Non-authoritative answer:
Name:    myip.opendns.com
Address: <Your Public IP Address>
```

- In this output, `<Your Public IP Address>` will be replaced by your actual public IP address.

### Explanation of the Command
- **`nslookup`**: This command queries the Domain Name System (DNS) to obtain domain name or IP address mapping.
- **`myip.opendns.com`**: This is a special domain provided by OpenDNS that returns the public IP address of the client making the request.
- **`resolver1.opendns.com`**: This specifies the DNS server to use for the query, in this case, one of OpenDNS's resolvers.

This command is a quick and efficient way to retrieve your public IP address from the command line.

### Using PowerShell
1. Open PowerShell.
2. Run the following command:

    ```powershell
    (Invoke-WebRequest -Uri "http://ifconfig.me/ip").Content.Trim()
    ```

This will make a web request and display your public IP address.

### Using Python Script
1. Create a Python script (e.g., `find_public_ip.py`).
2. Use the following code:

    ```python
    import requests

    response = requests.get("https://api.ipify.org")
    if response.status_code == 200:
        print("Your public IP address is:", response.text)
    else:
        print("Unable to fetch public IP address.")
    ```

3. Run the script to display your public IP address.

### Using Online Tools
1. Open a web browser.
2. Visit a website like [https://whatismyipaddress.com](https://whatismyipaddress.com) or [https://ifconfig.me](https://ifconfig.me) or [https://www.whatismyip.com/](https://www.whatismyip.com/)
3. Your public IP address will be displayed on the page.