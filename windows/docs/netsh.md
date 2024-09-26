Here are practical tasks using the netsh command in Windows to help beginners understand and apply its functionality:

1. View Wireless Network Profiles

Task: List all saved Wi-Fi profiles on your computer.

Command:

netsh wlan show profiles

Goal: View all saved Wi-Fi networks your computer has connected to, along with their profile names.


2. View Details of a Specific Wi-Fi Profile

Task: View the configuration details of a specific Wi-Fi network.

Command:

netsh wlan show profile name="WiFiName"

Goal: Understand the settings (e.g., security type, SSID) for a specific Wi-Fi network.


3. Retrieve Wi-Fi Password for a Saved Network

Task: Display the password of a saved Wi-Fi network.

Command:

netsh wlan show profile name="WiFiName" key=clear

Goal: Access the Wi-Fi password for a network you previously connected to.


4. Connect to a Wi-Fi Network

Task: Connect to a saved Wi-Fi profile using the command line.

Command:

netsh wlan connect name="WiFiName"

Goal: Practice connecting to a specific Wi-Fi network without using the GUI.


5. Disconnect from a Wi-Fi Network

Task: Disconnect from the current Wi-Fi network.

Command:

netsh wlan disconnect

Goal: Test disconnecting from a Wi-Fi network directly from the command line.


6. Block a Wi-Fi Network from Connecting Automatically

Task: Prevent your computer from automatically connecting to a specific Wi-Fi network.

Command:

netsh wlan set profileparameter name="WiFiName" connectionmode=manual

Goal: Stop automatic connections to a network but keep the profile for future manual connections.


7. Display IP Configuration

Task: View the current IP configuration of your network interface.

Command:

netsh interface ip show config

Goal: View details such as IP address, subnet mask, and gateway for your network interfaces.


8. Change IP Address and Subnet Mask

Task: Set a static IP address and subnet mask on your network interface.

Command:

netsh interface ip set address name="Ethernet" static 192.168.1.100 255.255.255.0

Goal: Manually configure the IP address of a network interface.


9. Set a Static DNS Server

Task: Configure a static DNS server (e.g., Google’s DNS server 8.8.8.8) on your network interface.

Command:

netsh interface ip set dns name="Ethernet" static 8.8.8.8

Goal: Change the DNS server for your network connection.


10. Reset IP and TCP/IP Stack

Task: Reset the TCP/IP stack to resolve potential network issues.

Command:

netsh int ip reset

Goal: Fix network issues by resetting the IP stack, restoring the system to its default configuration.


11. Enable DHCP on a Network Interface

Task: Configure a network interface to automatically obtain an IP address from a DHCP server.

Command:

netsh interface ip set address name="Ethernet" source=dhcp

Goal: Switch from a static IP address to dynamic IP assignment via DHCP.


12. View Firewall Configuration

Task: Display the current Windows Firewall settings and rules.

Command:

netsh advfirewall show allprofiles

Goal: Understand how the firewall is configured for different profiles (Domain, Private, Public).


13. Enable/Disable Windows Firewall

Task: Enable or disable the Windows Firewall for all network profiles.

Command:

Enable:

netsh advfirewall set allprofiles state on

Disable:

netsh advfirewall set allprofiles state off


Goal: Practice enabling and disabling the firewall across all profiles.


14. Create an Inbound Firewall Rule

Task: Create a new firewall rule to allow inbound traffic on a specific port (e.g., TCP port 8080).

Command:

netsh advfirewall firewall add rule name="Allow8080" protocol=TCP dir=in localport=8080 action=allow

Goal: Learn how to create a firewall rule to allow incoming traffic on a specific port.


15. Delete a Firewall Rule

Task: Delete a firewall rule that allows traffic on a specific port (e.g., rule created above).

Command:

netsh advfirewall firewall delete rule name="Allow8080"

Goal: Remove a custom firewall rule to prevent traffic on a specific port.


16. View Wireless Network Signal Strength

Task: Check the signal strength of your connected Wi-Fi network.

Command:

netsh wlan show interfaces

Goal: Monitor the signal quality and strength of your wireless network connection.


17. Enable/Disable a Network Interface

Task: Enable or disable a specific network interface on your machine.

Command:

Enable:

netsh interface set interface name="Ethernet" admin=enabled

Disable:

netsh interface set interface name="Ethernet" admin=disabled


Goal: Practice controlling the status of a network interface.


18. Export Wireless Network Profiles

Task: Export the settings of a specific Wi-Fi network profile to an XML file.

Command:

netsh wlan export profile name="WiFiName" folder="C:\Users\YourName\Desktop"

Goal: Backup Wi-Fi profiles for use on another machine or as a configuration reference.


19. Import a Wireless Network Profile

Task: Import a previously exported Wi-Fi network profile from an XML file.

Command:

netsh wlan add profile filename="C:\Users\YourName\Desktop\WiFiName.xml"

Goal: Restore or transfer a Wi-Fi network profile from a backup XML file.


20. View the Wireless Network Adapter Capabilities

Task: Display the wireless adapter capabilities, including supported frequencies and modes.

Command:

netsh wlan show drivers

Goal: Learn about the technical capabilities and limitations of your wireless adapter.


21. Block a Specific Wi-Fi Network from Being Discovered

Task: Prevent your computer from seeing or connecting to a specific Wi-Fi network.

Command:

netsh wlan add filter permission=block ssid="BlockedNetwork" networktype=infrastructure

Goal: Block certain Wi-Fi networks from being automatically connected to.


22. Flush DNS Cache

Task: Clear the DNS resolver cache to force the system to fetch new DNS records.

Command:

netsh int ip reset
netsh winsock reset
ipconfig /flushdns

Goal: Troubleshoot issues caused by outdated or corrupted DNS information.


23. Enable Network Discovery

Task: Enable network discovery to allow your computer to find other devices on the network.

Command:

netsh advfirewall firewall set rule group="Network Discovery" new enable=Yes

Goal: Turn on network discovery and make your device visible to other computers on the same network.


These tasks cover various networking functions using netsh, giving beginners hands-on experience with managing network profiles, firewall settings, IP configurations, and Wi-Fi networks.

