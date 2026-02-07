---
layout: page
title: Here are practical tasks for the telnet command to help beginners understand and apply its functionality:
description: Here are practical tasks for the telnet command to help beginners understand and apply its functionality: 1. Install and Enable Telnet in Windows Task...
keywords: telnet, server, port, command, task
---
Here are practical tasks for the telnet command to help beginners understand and apply its functionality:

1. Install and Enable Telnet in Windows

Task: Install the Telnet client on Windows (Telnet is not enabled by default).

Steps:

1. Open Command Prompt with Administrator rights.


2. Run the following command to install Telnet:

dism /online /Enable-Feature /FeatureName:TelnetClient



Goal: Enable Telnet on your system to start using the command.


2. Test Connectivity to a Remote Server

Task: Use Telnet to check if a remote server is reachable.

Command:

telnet example.com 80

Goal: Test connectivity to a web server (example.com) on port 80 (HTTP). You should receive a blank screen if the connection is successful, meaning the server is reachable.


3. Check if a Specific Port is Open

Task: Check whether a specific port (e.g., 25 for SMTP or 22 for SSH) is open on a remote server.

Command:

telnet smtp.example.com 25

Goal: Verify if the server has the SMTP service running on port 25. If the port is open, you’ll receive a response from the server.


4. Connect to an HTTP Server

Task: Manually connect to an HTTP server and send an HTTP request.

Command:

telnet example.com 80

Steps:

1. After connecting, type:

GET / HTTP/1.1
Host: example.com


2. Press Enter twice.



Goal: Simulate a basic web request and observe the raw HTTP response from the server.


5. Check SMTP Email Server

Task: Connect to an SMTP email server to check if the service is working.

Command:

telnet smtp.example.com 25

Steps:

1. Once connected, type the following commands to initiate an SMTP session:

EHLO example.com
MAIL FROM:<you@example.com>
RCPT TO:<recipient@example.com>
DATA
Subject: Test Email

This is a test email.
.



Goal: Understand the basic operations of an SMTP server by simulating an email send process.


6. Test a Web Server on a Non-Standard Port

Task: Check if a web server is listening on a non-standard port (e.g., port 8080).

Command:

telnet example.com 8080

Goal: Confirm that a web service is running on a different port than the default port 80.


7. Test an SSH Server Connection

Task: Use Telnet to verify that an SSH service is available on a remote server.

Command:

telnet example.com 22

Goal: Check if an SSH server is running on port 22. A successful connection will display an SSH banner or version information.


8. Check if a Database Server is Running

Task: Use Telnet to check if a database server (e.g., MySQL or PostgreSQL) is running on its default port.

Command:

telnet example.com 3306  # MySQL default port
telnet example.com 5432  # PostgreSQL default port

Goal: Determine if the database server is accepting connections on the specified port.


9. Test Connection to a Mail Server Using IMAP

Task: Test a connection to a mail server using the IMAP protocol on port 143.

Command:

telnet mail.example.com 143

Goal: Check whether the mail server is responding to IMAP requests and accepting connections.


10. Check if a Remote Desktop Service is Running

Task: Use Telnet to see if a Remote Desktop service is active on a remote server (default port 3389).

Command:

telnet example.com 3389

Goal: Confirm that the Remote Desktop service is accessible on the specified machine.


11. Close an Active Telnet Session

Task: Close an active Telnet session after completing a connection test.

Command:

1. Press Ctrl+] to bring up the Telnet prompt.


2. Type quit and press Enter.



Goal: Learn how to exit an active Telnet session cleanly.


12. View Telnet Help

Task: View the help menu to explore other Telnet features and options.

Command:

telnet /?

Goal: Familiarize yourself with Telnet's available commands and arguments.


13. Test Localhost Connection

Task: Use Telnet to connect to a service running on your local machine (e.g., a web server on port 80).

Command:

telnet localhost 80

Goal: Check if a service on your local machine is accepting connections, useful for testing local development environments.


14. Test FTP Server Connection

Task: Use Telnet to connect to an FTP server and check if the service is running.

Command:

telnet ftp.example.com 21

Goal: Verify that the FTP service is active and accepting connections on port 21.


15. Connect to a Time Server

Task: Use Telnet to connect to a time server to check its availability.

Command:

telnet time.nist.gov 13

Goal: Check if the time server is working and observe the server's response with the current time.


16. Test a Custom Port on a Web Application

Task: Use Telnet to verify that your custom web application is running on a non-standard port (e.g., 3000).

Command:

telnet localhost 3000

Goal: Confirm that a custom web application or API is available on a non-standard port.


17. Check HTTPS Server Availability

Task: Test if an HTTPS service is available on the default port (443) using Telnet.

Command:

telnet example.com 443

Goal: Verify that an HTTPS web server is running and accepting connections.


18. Test Remote Game Server Connection

Task: Use Telnet to connect to a game server (e.g., Minecraft, which uses port 25565).

Command:

telnet game.example.com 25565

Goal: Ensure that the game server is online and available for players to join.


19. Test Connection to an IRC Server

Task: Check if an IRC server is running by connecting to the default IRC port (6667).

Command:

telnet irc.example.com 6667

Goal: Test if the IRC server is reachable and responding.


20. Practice Using Telnet for Network Troubleshooting

Task: Use Telnet to troubleshoot network issues by testing connections to different services and ports.

Command:

telnet example.com [port]

Goal: Develop the habit of using Telnet to test whether specific services on remote servers are accessible.


By practicing these tasks, beginners can gain familiarity with how Telnet works, how it can be used for troubleshooting, and how it interacts with various types of servers and services.

