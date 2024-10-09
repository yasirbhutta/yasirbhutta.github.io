# Windows Networking Commands 

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

that you can use for troubleshooting, configuring, and monitoring network-related tasks:

1. [ipconfig](ipconfig.md)

Displays and manages IP configuration of your system.

Common options:

```
ipconfig /all: Shows detailed IP information.

ipconfig /release: Releases the IP address for the specified adapter.

ipconfig /renew: Renews the IP address for the specified adapter.

ipconfig /flushdns: Clears the DNS cache.
```
[ipconfig command tasks](ipconfig.md)

2. [ping](ping.md)

Tests connectivity between two devices.

Common usage:

ping <hostname> or ping <IP address>: Sends ICMP echo requests to test the connection.

[ping command tasks](ping.md)


3. [tracert](tracert.md)

Traces the route packets take to reach a destination.

Usage:

tracert <hostname> or tracert <IP address>

[tracert command tasks](tracert.md)

4. [nslookup](nslookup.md)

Queries DNS to obtain the domain name or IP address mapping.

Usage:

nslookup <hostname>: Displays IP address related to the domain.

nslookup <IP address>: Displays domain related to the IP address.

[nslookup command tasks](nslookup.md)

**'/?' Parameter**

In Windows commands, the `/?` parameter is commonly used to display help information for a command.

For example, if you use:

```cmd
nslookup /?
```

It will display a list of all available options and syntax details for the `nslookup` command. This command is used to query Internet domain name servers and to obtain details such as IP addresses or DNS records. The `/?` parameter is helpful if you want to understand how to use the command and what arguments it accepts.

5. netstat

Displays network statistics, connections, and routing tables.

Common options:

```cmd
netstat -a: Shows all active connections and listening ports.

netstat -n: Shows connections in numerical format.

netstat -r: Displays the routing table.

netstat -s: Displays statistics by protocol.
```
[netstat command tasks](netstat.md)

6. arp

Displays and modifies the ARP cache (Address Resolution Protocol).

Common options:

arp -a: Shows the ARP cache table.

arp -d <IP address>: Deletes the ARP entry for the specified IP address.



7. route

Displays and modifies the routing table.

Common options:

route print: Displays the routing table.

route add <destination> mask <subnet> <gateway>: Adds a new static route.

route delete <destination>: Deletes a route.


8. netsh

A powerful tool for configuring and displaying network settings.

Common commands:

netsh interface ip show config: Displays IP configuration for all network adapters.

netsh wlan show profiles: Displays saved Wi-Fi profiles.

netsh firewall show state: Displays the current firewall state.

netsh int ip reset: Resets the TCP/IP stack.



9. telnet

Used to test TCP connections on a specific port (usually requires enabling first).

Usage:

telnet <hostname> <port>: Tries to establish a connection to a specified host on a particular port.



10. getmac

Displays the MAC address for network adapters.

Usage:

getmac: Shows MAC addresses of all active network adapters.



11. hostname

Displays the computer's hostname.

Usage:

hostname: Shows the name of the machine.



12. pathping

Combines the functionality of ping and tracert to test connectivity and analyze packet loss.

Usage:

pathping <hostname> or pathping <IP address>



13. net

Used for network-related tasks such as managing shared resources.

Common usage:

net use <drive letter>: \\<server>\<share>: Maps a network drive.

net share: Displays shared resources on the computer.

net user <username>: Manages user accounts.



14. net view

Displays a list of shared resources or computers in a network.

Usage:

net view \\<computer name>: Lists shared resources on the specified computer.



15. nbtstat

Displays protocol statistics and current TCP/IP connections using NetBIOS over TCP/IP.

Common options:

nbtstat -a <hostname>: Shows NetBIOS table of the remote machine.

nbtstat -n: Lists NetBIOS names on the local machine.



16. ftp

Used to transfer files between a local and remote machine using the File Transfer Protocol.

Usage:

ftp <hostname>: Starts an FTP session to a remote host.



17. systeminfo

Provides detailed information about the computer's network configuration, OS, and more.

Usage:

systeminfo: Displays detailed system information.



These commands can be run directly in the Command Prompt and are useful for diagnosing and managing network issues on Windows systems.

