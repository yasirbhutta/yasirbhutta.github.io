# SNA Projects

[Download PDF](sna-projects.pdf)

### **Project Title:**  
Windows Domain Configuration and Group Policy Management

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