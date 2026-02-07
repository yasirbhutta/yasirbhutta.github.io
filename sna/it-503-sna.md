---
layout: page
title: IT-503 System and Network Administration
description: 1. Practical 1: Setting Up a Virtual Machine with VirtualBox/VMware - Install a virtual machine. 2. Practical 2: Linux Installation and Setup - Instal...
keywords: practical, using, network, explore, file
---
# IT-503 System and Network Administration

### **Week 1: Introduction to Linux Systems**

1. **Practical 1: Setting Up a Virtual Machine with VirtualBox/VMware**  
    - Install a virtual machine.

2. **Practical 2: Linux Installation and Setup**  
   - Install a Linux distribution (Ubuntu, Fedora, etc.) in a virtual machine.
   - Explore basic Linux commands (`ls`, `cd`, `pwd`, `cp`, `mv`, etc.).
   - **Navigating the File System**  
     - Learn about file system hierarchy and permissions.
     - Practice file and directory management (`mkdir`, `rm`, `chmod`, `chown`).

### **Week 2: User and Group Management**
3. **Practical 1: User Management**  
   - Add, delete, and modify user accounts (`useradd`, `usermod`, `passwd`, `userdel`).

4. **Practical 2: Group Management**  
   - Add, delete, and modify groups.
   - Assign users to groups and explore `/etc/passwd` and `/etc/group`.

### **Week 3: File Permissions and Ownership**
5. **Practical 1: Understanding File Permissions**  
   - Explore file permissions (`rwx`) and ownership.
   - Change permissions and ownership using `chmod` and `chown`.

6. **Practical 2: Special Permissions**  
   - Learn about special permissions (SUID, SGID, sticky bit) and configure them.

### **Week 4: System Monitoring and Logs**
7. **Practical 1: System Monitoring Basics**  
   - Use commands like `top`, `htop`, `free`, `df`, `du`, and `uptime` to monitor system performance.

8. **Practical 2: Analyzing System Logs**  
   - Explore log files in `/var/log` (e.g., `syslog`, `auth.log`, `dmesg`).
   - Use `journalctl` to view systemd logs.

### **Week 5: Package Management**
9. **Practical 1: Package Managers (apt, yum, etc.)**  
   - Install, update, and remove packages using `apt` (Debian-based) or `yum`/`dnf` (RedHat-based).

10. **Practical 2: Working with Repositories**  
    - Add and remove software repositories.
    - Install software from third-party sources.

### **Week 6: Process and Job Management**
11. **Practical 1: Managing Processes**  
    - Explore process management using `ps`, `kill`, `nice`, `renice`, and `killall`.

12. **Practical 2: Scheduling Jobs**  
    - Automate tasks using `cron` jobs and `at` commands.

### **Week 7: Disk Management and Partitioning**
13. **Practical 1: Disk Partitioning**  
    - Create and manage partitions using `fdisk` or `parted`.
    - Format partitions using `mkfs` (ext4, NTFS, etc.).

14. **Practical 2: Mounting and Unmounting File Systems**  
    - Manually mount and unmount partitions.
    - Explore `/etc/fstab` for automatic mounting.

### **Week 8: Backup and Restore**
15. **Practical 1: Basic Backup Tools**  
    - Use `tar` and `rsync` for file backups.
    - Compress backups using `gzip` and `bzip2`.

16. **Practical 2: Restoring Files**  
    - Restore from `tar` archives and synchronize data using `rsync`.

### **Week 9: Networking Fundamentals**
17. **Practical 1: Basic Network Commands**  
    - Use commands like `ifconfig`, `ip addr`, `ping`, `netstat`, and `traceroute` to explore network configurations.

18. **Practical 2: Configuring Network Interfaces**  
    - Configure static and dynamic (DHCP) IP addresses.

### **Week 10: DNS and DHCP**
19. **Practical 1: Understanding DNS**  
    - Explore how DNS works using tools like `dig`, `nslookup`, and `host`.

20. **Practical 2: Configuring DHCP**  
    - Install and configure a DHCP server, assign dynamic IPs.

### **Week 11: Firewalls and Security**
21. **Practical 1: Configuring iptables or firewalld**  
    - Set up basic firewall rules using `iptables` or `firewalld`.

22. **Practical 2: Managing Open Ports**  
    - Explore open ports using `netstat` and close unnecessary ones.

### **Week 12: SSH and Remote Access**
23. **Practical 1: Configuring SSH Access**  
    - Set up SSH server and client.
    - Configure SSH key-based authentication.

24. **Practical 2: Secure Remote Administration**  
    - Secure SSH access by changing default port and using fail2ban to prevent brute-force attacks.

### **Week 13: Web and File Servers**
25. **Practical 1: Setting Up a Web Server (Apache/Nginx)**  
    - Install and configure a web server.
    - Host a simple HTML website.

26. **Practical 2: Setting Up a File Server (Samba/NFS)**  
    - Install and configure Samba or NFS to share files across the network.

### **Week 14: Network Troubleshooting**
27. **Practical 1: Troubleshooting with ping, traceroute, and netcat**  
    - Use `ping`, `traceroute`, and `nc` (netcat) to diagnose network issues.

28. **Practical 2: Monitoring Network Traffic with tcpdump**  
    - Capture and analyze network packets using `tcpdump`.

### **Week 15: Virtualization and Containers**
29. **Practical 1: Setting Up a Virtual Machine with VirtualBox/VMware**  
    - Configure a virtual machine.

30. **Practical 2: Introduction to Containers (Docker)**  
    - Set up and run a simple container using Docker.

### **Week 16: Final Projects**
31. **Practical 1: Build a Secure Web Server Environment**  
    - Secure a web server by setting up HTTPS, firewall rules, and monitoring tools.

32. **Practical 2: Networking Project**  
    - Set up a small local network, configure DNS, DHCP, and file sharing services.

---
