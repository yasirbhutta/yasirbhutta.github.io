# Computer Networks

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/cs-407-computer-networks/docs/computer-networks.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/cs-407-computer-networks/docs/computer-networks.html](https://yasirbhutta.github.io/ms-excel/docs/computer-networks.html)

## What is a Private IP Address?

A **private IP address** is an IP address reserved for internal use within a network (such as a home, office, or enterprise) that is **not routable** on the global internet. These addresses are used to identify devices within a private network and are translated to public IP addresses when communicating outside the network (via technologies like NAT, Network Address Translation).

### **Private IP Range for Class C Networks**

In **Class C networks**, the range of private IP addresses is:
- **192.168.0.0** to **192.168.255.255**

This gives a total of **256 Class C networks**, with each network having **256 addresses** (from `192.168.0.0/24` to `192.168.255.255/24`).

### **Breakdown of Class C Private IP Range**:
- **Starting Address**: `192.168.0.0`
- **Ending Address**: `192.168.255.255`
- **Subnet Mask**: `255.255.255.0`

The first IP (`192.168.x.0`) is typically reserved as the **network address**, and the last IP (`192.168.x.255`) is usually reserved as the **broadcast address**.

### Examples:
- Network: `192.168.1.0/24`
  - Usable IP range: `192.168.1.1` to `192.168.1.254`
- Network: `192.168.100.0/24`
  - Usable IP range: `192.168.100.1` to `192.168.100.254`

### Other Private IP Ranges (for reference):
- **Class A**: `10.0.0.0` to `10.255.255.255`
- **Class B**: `172.16.0.0` to `172.31.255.255`
- **Class C**: `192.168.0.0` to `192.168.255.255`

These IP ranges are reserved for internal network use and will not be routed on the public internet, ensuring that devices in these ranges cannot directly access or be accessed from the global internet without proper configuration (e.g., using NAT).