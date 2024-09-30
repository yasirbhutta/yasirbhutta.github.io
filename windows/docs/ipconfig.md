# Window Networking Commands: ipconfig

Here are some practical tasks to help you get hands-on experience with the ipconfig command:

1. Check Your IP Configuration

Task: Display the IP configuration for all network adapters on your machine.

Command:

ipconfig

Goal: Identify your computer’s IP address, subnet mask, and default gateway.


2. View Detailed IP Information

Task: Display detailed information for all network interfaces, including DNS, DHCP, and MAC addresses.

Command:

ipconfig /all

Goal: Record the MAC address and DNS server details.


3. Release Your Current IP Address

Task: Release the current IP address assigned to your machine.

Command:

ipconfig /release

Goal: Verify that the IP address is no longer assigned by checking the configuration again with ipconfig.


4. Renew Your IP Address

Task: Renew the IP address after releasing it.

Command:

ipconfig /renew

Goal: Check if a new IP address has been assigned after running the command.

5. Display DNS Cache

Task: View the current DNS resolver cache entries.

Command:

ipconfig /displaydns

Goal: Analyze the cached DNS entries and understand which domains have been recently resolved.

6. Flush DNS Resolver Cache

Task: Clear the DNS resolver cache to remove any old or incorrect DNS entries.

Command:

ipconfig /flushdns

Goal: Confirm that the DNS cache has been successfully cleared.

7. Register DNS

Task: Force your computer to register its DNS name and refresh the DHCP lease.

Command:

ipconfig /registerdns

Goal: Check if the computer's DNS name has been re-registered successfully and troubleshoot DNS issues.


8. Check for Link-Local IPv6 Address

Task: Check for the link-local IPv6 address of your machine.

Command:

ipconfig

Goal: Locate the IPv6 address starting with "fe80::" and understand its significance.


10. Check Autoconfiguration Status

Task: Check if your computer has automatically assigned an IP address from the APIPA range (169.254.x.x).

Command:

ipconfig /all

Goal: Determine if your computer is using an APIPA address and identify why it may not be getting an IP address from the DHCP server.


11. Identify IPv4 vs. IPv6 Configuration

Task: Compare the IPv4 and IPv6 configuration details for all adapters.

Command:

ipconfig /all

Goal: Distinguish between the IPv4 and IPv6 addresses and understand the differences in their format and use cases.


12. Release/Renew for Wireless Network

Task: Release and renew the IP address for your wireless adapter.

Command:

ipconfig /release "Wi-Fi"
ipconfig /renew "Wi-Fi"

Goal: Observe how the IP address for your wireless connection changes and troubleshoot if there are any issues with obtaining a new address.


By practicing these tasks, you’ll gain a deeper understanding of how to manage and troubleshoot network configurations using the ipconfig command in Windows.

