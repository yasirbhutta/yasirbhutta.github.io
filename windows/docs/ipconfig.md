---
layout: page
title: Window Networking Commands: ipconfig
description: Connect with me: Youtube \| LinkedIn \| WhatsApp Channel \| Web \| Facebook \| Twitter - Download PDF - To access the updated handouts, please click o...
keywords: address, ipconfig, dns, command, your
---
# Window Networking Commands: ipconfig

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/windows/docs/ipconfig.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/windows/docs/ipconfig.html](https://yasirbhutta.github.io/windows/docs/ipconfig.html)

Here are some practical tasks to help you get hands-on experience with the ipconfig command:

1. Check Your IP Configuration

Task: Display the IP configuration for all network adapters on your machine.

Command:

```cmd
ipconfig
```

Goal: Identify your computer’s IP address, subnet mask, and default gateway.


2. View Detailed IP Information

Task: Display detailed information for all network interfaces, including DNS, DHCP, and MAC addresses.

Command:

```cmd
ipconfig /all
```

Goal: Record the MAC address and DNS server details.


3. Release Your Current IP Address

Task: Release the current IP address assigned to your machine.

Command:

```cmd
ipconfig /release
```

Goal: Verify that the IP address is no longer assigned by checking the configuration again with ipconfig.


4. Renew Your IP Address

Task: Renew the IP address after releasing it.

Command:

```cmd
ipconfig /renew
```cmd

Goal: Check if a new IP address has been assigned after running the command.

5. Display DNS Cache

Task: View the current DNS resolver cache entries.

Command:

```cmd
ipconfig /displaydns
```

Goal: Analyze the cached DNS entries and understand which domains have been recently resolved.

6. Flush DNS Resolver Cache

Task: Clear the DNS resolver cache to remove any old or incorrect DNS entries.

Command:

```cmd
ipconfig /flushdns
```cmd

Goal: Confirm that the DNS cache has been successfully cleared.

7. Register DNS

Task: Force your computer to register its DNS name and refresh the DHCP lease.

Command:

```cmd
ipconfig /registerdns
```

Goal: Check if the computer's DNS name has been re-registered successfully and troubleshoot DNS issues.


8. Check for Link-Local IPv6 Address

Task: Check for the link-local IPv6 address of your machine.

Command:

```cmd
ipconfig
```

Goal: Locate the IPv6 address starting with "fe80::" and understand its significance.


10. Check Autoconfiguration Status

Task: Check if your computer has automatically assigned an IP address from the APIPA range (169.254.x.x).

Command:

```cmd
ipconfig /all
```

Goal: Determine if your computer is using an APIPA address and identify why it may not be getting an IP address from the DHCP server.

**APIPA (Automatic Private IP Addressing)** is a feature that assigns an IP address to a computer when DHCP is not available. The APIPA range is:

- **169.254.0.1 to 169.254.255.254**
  
The subnet mask for APIPA is **255.255.0.0**. Devices using APIPA can communicate only with other devices on the same local network that also have an APIPA address.

11. Identify IPv4 vs. IPv6 Configuration

Task: Compare the IPv4 and IPv6 configuration details for all adapters.

Command:

```cmd
ipconfig /all
```

Goal: Distinguish between the IPv4 and IPv6 addresses and understand the differences in their format and use cases.