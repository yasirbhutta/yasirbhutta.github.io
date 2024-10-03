# Window Networking Commands: tracert

- [Download PDF](https://yasirbhutta.github.io/windows/docs/tracert.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/windows/docs/tracert.html](https://yasirbhutta.github.io/windows/docs/tracert.html)

Here are some practical tasks to help you understand and apply the tracert (trace route) command in Windows:

1. Trace the Route to a Website

Task: Trace the route packets take to reach a popular website (e.g., google.com).

Command:

```cmd
tracert google.com
```

```cmd
tracert gulms.live
```

Goal: Observe all the intermediate hops between your computer and the destination, including their IP addresses and response times.

2. Trace the Route to an IP Address

Task: Trace the route to a specific IP address (e.g., a known server or local device).

Command:

```cmd
tracert <IP address>
```

Goal: Understand the path that data takes to reach a specific IP address and troubleshoot connectivity issues.

1. Trace the Route to a Local Router

Task: Trace the route to your local router or gateway to understand how your computer connects to it.

Command:

tracert <Gateway IP address>

Goal: Determine the hops involved between your device and the gateway, and ensure the route is direct with minimal latency.

5. Trace the Route to a Public DNS Server

Task: Trace the route to a public DNS server (e.g., Google DNS: 8.8.8.8).

Command:

tracert 8.8.8.8

Goal: Explore the network path to a DNS server and check for any slow or unresponsive hops.


6. Save Traceroute Output to a File

Task: Save the results of the traceroute to a text file for later analysis.

Command:

```cmd
tracert google.com > tracert_output.txt
```

Goal: Keep a log of the traceroute result to analyze or share with a network administrator.


7. Trace the Route to Another Computer on the LAN

Task: Trace the route to another device on your local network (e.g., another computer).

Command:

tracert <Computer IP address>

Goal: Ensure that there are no unusual hops between computers on the same local network, which could indicate misconfigured routes.


9. Trace the Route to an External IP to Test Internet Connectivity

Task: Trace the route to a known external IP address (e.g., 1.1.1.1 or 8.8.8.8) to diagnose internet access issues.

Command:

tracert 1.1.1.1

Goal: Analyze whether the issue is with local network infrastructure or external routing.


10. Limit the Number of Hops in a Traceroute

Task: Trace the route to a website but limit the number of hops to a specific value (e.g., 5 hops).

Command:

tracert -h 5 google.com

Goal: Restrict the number of hops in the traceroute and observe the nearest network devices that respond.


11. Trace Route with Maximum Hop Limit

Task: Trace the route to a destination with a high maximum hop count to ensure it checks all possible paths.

Command:

tracert -h 30 google.com

Goal: Identify distant hops or find where the connection fails over a large number of hops.


12. Identify Network Bottlenecks Using Traceroute

Task: Use traceroute to identify which hop in a path is causing high latency or packet loss.

Command:

```cmd
tracert google.com
```

Goal: Analyze the response times at each hop and locate the hop with the highest latency or where responses are lost.

14.  Trace the Route to a CDN (Content Delivery Network)

Task: Trace the route to a CDN such as Cloudflare or Akamai to understand how data is routed to distributed content.

Command:

tracert cdn.cloudflare.com

Goal: Explore the hops involved when accessing content hosted on a CDN and determine if a more optimal route is available.

By performing these tasks, you’ll develop a deeper understanding of network routing, detect where potential connectivity problems may exist, and gain practical skills in diagnosing network issues using the tracert command.


The `tracert` command (short for "trace route") is a network diagnostic tool used in Windows to track the path packets take from your computer to a destination host. It displays the series of hops that the data passes through, which helps identify where delays or failures occur in the network.

When you run `tracert <hostname or IP address>` in the Command Prompt, you get output similar to the following:

```
Tracing route to example.com [93.184.216.34]
over a maximum of 30 hops:

  1    <1 ms    <1 ms    <1 ms  192.168.0.1
  2    10 ms    11 ms    10 ms  172.217.4.100
  3    20 ms    21 ms    19 ms  198.51.100.1
  4    50 ms    49 ms    51 ms  example.com [93.184.216.34]

Trace complete.
```

### Explanation of Output

1. **Header Information**: 
   - The command starts by displaying the destination hostname and its IP address.
   - It indicates that it's tracing the route with a default maximum of 30 hops.

2. **Hop Information**:
   - Each numbered line represents a **hop**—a step in the journey from your device to the destination.
   - The columns show:
     - **Hop number**: Sequential number indicating the hop order.
     - **Round-trip time (RTT)**: The three times (e.g., `<1 ms`, `10 ms`, `21 ms`) represent the time it took for a packet to reach that hop and for the reply to return to your computer. Three measurements are taken to provide an average representation of network latency.
     - **IP address or hostname**: This shows the address or hostname of the device at that hop.

### Key Details
- **Hop Number**: Each hop represents a router or a network device the packet passed through. The total number of hops can indicate how far or complex the route to the destination is.
- **RTT (Round-Trip Time)**: Multiple RTT values are shown to help identify variability or instability in the route:
  - If the times are consistent, the route is likely stable.
  - If there is a large variation, there might be congestion or issues at that hop.
- **Timeout (`* * *`)**: If a hop doesn't respond, you may see `* * *`, indicating that a response wasn't received within the timeout period. This could be due to a firewall or device configured not to respond to ICMP packets.

### Usage
- To identify bottlenecks: If one of the hops has a significantly higher RTT than the others, it indicates a possible delay at that point.
- To diagnose connectivity issues: If the trace stops before reaching the destination, it might indicate where in the path the failure is occurring.

`tracert` is useful for network troubleshooting, helping to pinpoint where issues exist between your machine and a server.
