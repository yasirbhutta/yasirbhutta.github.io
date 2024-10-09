# Window Networking Commands: ping

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/windows/docs/ping.pdf)  
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/windows/docs/ping.html](https://yasirbhutta.github.io/windows/docs/ping.html)

1. Test Basic Connectivity to a Website

Task: Test the network connectivity to a website (e.g., google.com).

Command:

```cmd
ping google.com
```

Goal: Check if the website is reachable and measure the round-trip time (RTT) for packets.


2. Ping an IP Address

Task: Ping a specific IP address (e.g., a known server or another device on your local network).

Command:

ping <IP address>

```cmd
ping 8.8.8.8
```

Goal: Verify if the device is reachable using its IP address.


3. Continuous Ping Test

Task: Continuously ping a server or website until manually stopped (useful for monitoring connectivity over time).

Command:

```cmd
ping -t google.com
```

Goal: Observe the connection stability over a longer period and cancel the test with Ctrl + C.


4. Limit Number of Ping Requests

Task: Ping a server but limit the number of echo requests sent (e.g., only 5 pings).

Command:

```cmd
ping -n 5 google.com
```

Goal: Send a specific number of packets and measure the average round-trip time.


5. Ping a Local Router or Gateway

Task: Ping your local router or gateway to test your internal network connection.

Command:

ping <Gateway IP address>

Goal: Ensure your device can reach the gateway and troubleshoot local network issues if the ping fails.


6. Ping a Domain Name Server (DNS)

Task: Ping a public DNS server (e.g., Google DNS: 8.8.8.8).

Command:

```cmd
ping 8.8.8.8
```

Goal: Verify that you can reach a reliable DNS server, helping to identify DNS resolution issues.

7. Ping Using a Specific Packet Size

Task: Ping a host with a custom packet size (e.g., 100 bytes).

Command:

```cmd
ping google.com -l 100
```

Goal: Send larger or smaller packets and observe how the packet size affects network performance or connectivity.


8. Ping with a Timeout

Task: Ping a server but set a timeout for each reply (e.g., 2000 ms or 2 seconds).

Command:

```cmd
ping google.com -w 2000
```

Goal: Measure how long the system waits for a reply and handle slow connections or timeouts.


10.  Ping Multiple Hosts

Task: Ping multiple hosts in quick succession (e.g., a router, a local device, and a website).

Command:

```cmd
ping <Router IP>
ping <Local Device IP>
ping google.com
```

Goal: Test the connection to various devices and identify where connectivity issues might lie (e.g., LAN vs. WAN).


11. Save Ping Output to a File

Task: Save the results of a ping test to a text file for later analysis.

Command:

```cmd
ping google.com > ping_results.txt
```

Goal: Review the saved results and analyze the RTT or error messages.


12. Test Connectivity to a Network Printer

Task: Ping a network printer’s IP address to check if it’s reachable.

Command:

```cmd
ping <Printer IP address>
```

Goal: Verify that the printer is online and reachable over the network.

13. Test Network Connection to Another Computer

Task: Ping another computer on your local network (e.g., using its IP address or hostname).

Command:

```cmd
ping <Computer IP address> or ping <Computer hostname>
```

Goal: Test LAN connectivity and troubleshoot issues if the other machine is unreachable.

14. Ping an External IP to Test Internet Connectivity

Task: Ping an external IP address to check if your machine has internet access (e.g., 1.1.1.1 or 8.8.8.8).

Command:

```cmd
ping 1.1.1.1
```

Goal: Determine if the issue is with internet access or local DNS resolution.