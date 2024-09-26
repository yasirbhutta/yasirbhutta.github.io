Here are practical tasks to help you learn and apply the nslookup command in Windows:

1. Perform a Simple DNS Lookup

Task: Use nslookup to find the IP address of a website (e.g., google.com).

Command:

nslookup google.com

Goal: Identify the IP address associated with the domain name.


2. Find the Domain Name for an IP Address

Task: Use nslookup to perform a reverse DNS lookup (find the domain name associated with a given IP address).

Command:

nslookup <IP address>

Goal: Verify if the IP address resolves to a domain name and understand reverse DNS lookups.


3. Specify a Different DNS Server

Task: Query a domain name using a specific DNS server (e.g., Google DNS at 8.8.8.8).

Command:

nslookup google.com 8.8.8.8

Goal: Compare how different DNS servers resolve the same domain and check if using a specific server changes the result.


4. Find Mail Server Records (MX Records) for a Domain

Task: Look up the mail exchange (MX) records for a domain (e.g., gmail.com).

Command:

nslookup -type=mx gmail.com

Goal: Identify the mail servers responsible for handling emails for that domain.


5. Find Name Server Records (NS Records) for a Domain

Task: Look up the name servers responsible for a domain (e.g., yahoo.com).

Command:

nslookup -type=ns yahoo.com

Goal: Identify the authoritative name servers for the domain.


6. Find Start of Authority (SOA) Records for a Domain

Task: Query the Start of Authority (SOA) record for a domain to find authoritative information about it.

Command:

nslookup -type=soa microsoft.com

Goal: View the primary name server, the email of the administrator, and other important domain information.


7. Find All DNS Records for a Domain

Task: Retrieve all available DNS records (A, MX, NS, etc.) for a domain.

Command:

nslookup -type=any example.com

Goal: See all DNS records related to a domain to understand its DNS configuration.


8. Find Canonical Name Records (CNAME) for a Domain

Task: Look up CNAME (alias) records for a domain to see if it is pointing to another domain.

Command:

nslookup -type=cname www.example.com

Goal: Identify if the domain is an alias for another domain.


9. Set the Timeout for DNS Queries

Task: Set a custom timeout period (e.g., 2 seconds) for DNS queries to handle slow responses.

Command:

nslookup
set timeout=2
google.com

Goal: Control how long the system waits for a response from the DNS server.


10. Find Text (TXT) Records for a Domain

Task: Look up the TXT records for a domain to check for additional information like SPF, DKIM, or DMARC records.

Command:

nslookup -type=txt example.com

Goal: Analyze the TXT records, which often provide security or informational details about the domain.


11. Query IPv6 Records (AAAA)

Task: Query a domain for its IPv6 address by looking up AAAA records.

Command:

nslookup -type=aaaa google.com

Goal: Check if the domain supports IPv6 and view the corresponding IPv6 address.


12. Change the Default DNS Server Temporarily

Task: Change the default DNS server for your queries (e.g., to Cloudflare DNS 1.1.1.1) and query a domain.

Command:

nslookup
server 1.1.1.1
google.com

Goal: Test DNS resolution with a different DNS server and compare the results with your default DNS server.


13. Troubleshoot DNS Resolution Issues

Task: Troubleshoot DNS resolution problems by performing multiple lookups for a domain (e.g., a website that fails to load).

Command:

nslookup google.com
nslookup google.com 8.8.8.8
nslookup google.com 1.1.1.1

Goal: Compare results from different DNS servers to check if the issue lies with your DNS server or network.


14. Check for DNS Propagation

Task: Query a recently updated domain using different DNS servers to check if the new DNS records have propagated.

Command:

nslookup newwebsite.com 8.8.8.8
nslookup newwebsite.com 1.1.1.1

Goal: Check if the updated DNS information has spread across the internet by querying multiple DNS servers.


15. Set Debug Mode for More Detailed Information

Task: Enable debug mode in nslookup to get detailed information about the DNS query and response process.

Command:

nslookup
set debug
google.com

Goal: Analyze additional data about the DNS request and response, which is helpful for troubleshooting DNS issues.


16. Set a Specific Query Type (PTR for Reverse Lookup)

Task: Use a specific query type to perform a reverse DNS lookup (PTR record) for an IP address.

Command:

nslookup -type=ptr <IP address>

Goal: Verify the reverse lookup and ensure that the IP address maps correctly to a domain name.


17. Test Multiple DNS Queries in Interactive Mode

Task: Enter interactive mode in nslookup to perform multiple queries without re-entering the command.

Command:

nslookup
google.com
yahoo.com
example.com
exit

Goal: Practice querying multiple domains in a single session, making it easier to test various domains and servers.


18. Query a Specific Port for DNS

Task: Set a specific port for DNS queries (other than the default port 53) and test if the DNS server responds.

Command:

nslookup -port=53 google.com

Goal: Test DNS queries on non-standard ports to verify if the DNS service is available on other ports.


These tasks will help you gain practical experience with the nslookup command, allowing you to troubleshoot and analyze DNS issues effectively in various real-world scenarios.

