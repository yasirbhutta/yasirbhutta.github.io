# Neworking Projects

[Download PDF](sna-projects.pdf)

## 1. **Project Title**: Setting Up a Two-Computer Workgroup Network Using a Wired Connection and Switch in Windows

### **Objective**:
To establish a small local area network (LAN) by connecting two computers in a workgroup through a wired connection with a network switch. This network will allow file sharing, printer sharing, and basic communication between the computers.

### **Requirements**:

- **Hardware**:
  - 2 computers with Windows OS (Windows 10 or higher recommended).
  - 1 network switch.
  - 2 Ethernet cables.

- **Software**:
  - Windows OS (both computers should be in the same version range to avoid compatibility issues).

### **Steps**:

#### 1. **Connect the Hardware**:
   - Connect each computer to the network switch using Ethernet cables.
   - Ensure the switch is powered on.

#### 2. **Network Configuration**:
   - Go to each computer and set up the IP addresses:
     - Open **Control Panel** > **Network and Internet** > **Network and Sharing Center** > **Change adapter settings**.
     - Right-click on **Ethernet** (or Local Area Connection) > **Properties**.
     - Select **Internet Protocol Version 4 (TCP/IPv4)** > **Properties**.
     - Set static IP addresses for each computer:
       - **Computer 1**: IP Address: `192.168.1.2`, Subnet Mask: `255.255.255.0`
       - **Computer 2**: IP Address: `192.168.1.3`, Subnet Mask: `255.255.255.0`

#### 3. **Configure the Workgroup**:
   - Right-click on **This PC** > **Properties**.
   - Click **Change settings** (under "Computer name, domain, and workgroup settings").
   - In the **System Properties** window, click **Change**.
   - Select **Workgroup** and enter a workgroup name (e.g., **MYWORKGROUP**).
   - Repeat these steps on the second computer, using the same workgroup name.

#### 4. **Enable Network Discovery and File Sharing**:
   - On both computers, go to **Control Panel** > **Network and Sharing Center** > **Change advanced sharing settings**.
   - Enable **Network Discovery** and **File and Printer Sharing**.
   - Under **All Networks**, you can choose to **Turn off password-protected sharing** (optional, depending on security needs).

#### 5. **Verify Connectivity**:
   - Open **Command Prompt** on each computer and ping the other computer’s IP address to verify connectivity:
     - For **Computer 1**, type `ping 192.168.1.3`
     - For **Computer 2**, type `ping 192.168.1.2`
   - Both computers should receive replies if they are connected correctly.

#### 6. **Share a Folder**:
   - Create a shared folder to test file sharing.
   - Right-click on a folder you want to share > **Properties** > **Sharing** > **Advanced Sharing**.
   - Check **Share this folder** and set permissions as needed.

### **Project Testing**:
After setup, verify that:
- Each computer can see the other in the **Network** section of **File Explorer**.
- Files can be shared between the computers.
- Pings between the two computers are successful.

### **Project Summary**:
This project demonstrates how to create a simple, wired workgroup network between two computers in Windows using a switch. By setting IP addresses, configuring the workgroup, and enabling file sharing, users can communicate and share resources easily on this network.

## 2. **Project Title:** Windows Domain Configuration and Group Policy Management

### **Objective:**  
To set up a Windows domain, configure group policies, create domain users, and manage user groups with access control.

### **Project Overview:**
In this project, students will simulate a small organization's IT infrastructure by setting up a Windows Server domain, connecting client machines to the domain, and configuring group policies for user management and security. Students will also create users and groups, assign permissions, and ensure proper access control for resources.

### **Requirements:**

1. **Setup Environment:**
   - Install and configure **Windows Server 2019/2022** on a virtual machine or physical server.
   - Configure **Active Directory Domain Services (AD DS)** to create and manage the domain.
   - Install **Windows 10/11** on client machines to be joined to the domain.

2. **Domain Configuration:**
   - Set up a domain controller with a domain name, e.g., `gudgk.local`.
   - Configure **DNS** to ensure proper domain name resolution within the network.
   - Create **Organizational Units (OUs)** for logical user and computer grouping.

3. **Client Connection:**
   - Connect at least two client computers to the domain, ensuring they authenticate correctly to the domain controller.

4. **User and Group Management:**
   - Create **three user accounts** for each of the following groups:  
     - **Students**  
     - **IT Staff**  
     - **Admins**
   - Configure **Group Policies** for each group, setting policies as per the roles and responsibilities:
     - **Students**: Limited access to system settings and internet use.
     - **IT Staff**: Access to administrative tools and troubleshooting permissions.
     - **Admins**: Full access to all system resources and control over group policy settings.

5. **Group Policy Settings:**
   - Implement Group Policies for each group to manage desktop environments, application access, and security policies.
   - Use policies to control:
     - User access to Control Panel and settings.
     - Software installation permissions.
     - Security and password policies.
     - Internet access and browsing restrictions for the **Students** group.

6. **Testing and Validation:**
   - Log in with a test user from each group on client machines to verify that group policies are applied correctly.
   - Confirm that users from different groups have different levels of access to system settings and applications.

### **Deliverables:**

1. **Presentation** – A brief presentation (5-10 minutes) summarizing the project, key configurations, and results.
2. **Demo** – A live demonstration of one user from each group logging in to show policy enforcement.

### **Evaluation Criteria:**

- **Correct Configuration** – Successful domain setup, client connection, user and group creation, and policy application.
- **Policy Accuracy** – Correct policy settings as per group requirements.
- **Presentation & Demo** – Ability to explain the configuration process and demonstrate the setup.

---

Project Outcomes: This project will provide hands-on experience with Windows domain administration, user and group management, and enforcing security policies through group policies.