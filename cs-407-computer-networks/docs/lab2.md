# Computer Networks: Understanding Network Devices

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/python/docs/basics.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/ms-excel/docs/basics.html](https://yasirbhutta.github.io/ms-excel/docs/basics.html)

- **Lab 2:** Understanding Network Devices
  - Introduction to routers, switches, hubs, and modems.
  - Hands-on activity: Configure basic settings on a router and switch using network simulation tools.

### Hands-On Activity: Configure Basic Settings on a Router and Switch Using Cisco Packet Tracer

In this hands-on activity, we'll configure basic settings on a router and a switch, including hostname, passwords, IP addresses, and enable remote management (SSH or Telnet) for network administration.

### Topology
- 1 **Router** (e.g., Cisco 1941)
- 1 **Switch** (e.g., Cisco 2960)
- 1 **PC** (to manage the devices via SSH or Telnet)

---

### **Step-by-Step Instructions**

#### **1. Set Up the Topology in Cisco Packet Tracer**
- Open **Cisco Packet Tracer**.
- Drag the following devices onto the workspace:
  - 1 **Router** (e.g., 1941 Router)
  - 1 **Switch** (e.g., 2960 Switch)
  - 1 **PC**
  
- **Connect the devices**:
  - Use **Copper Straight-Through** cables to connect:
    - **Router's GigabitEthernet0/0** to **Switch's FastEthernet0/1**
    - **PC** to **Switch's FastEthernet0/2**

---

### **2. Configure Basic Settings on the Router**

1. **Access the Router CLI**:
   - Click on the **Router**.
   - Select the **CLI** tab.

2. **Enter Configuration Mode**:
   ```bash
   Router> enable
   Router# configure terminal
   ```

3. **Set the Hostname**:
   ```bash
   Router(config)# hostname R1
   ```

4. **Set Console Password**:
   ```bash
   R1(config)# line console 0
   R1(config-line)# password cisco
   R1(config-line)# login
   R1(config-line)# exit
   ```

5. **Set VTY Password (for Telnet/SSH)**:
   ```bash
   R1(config)# line vty 0 4
   R1(config-line)# password cisco
   R1(config-line)# login
   R1(config-line)# exit
   ```

6. **Set Enable Password (Privileged EXEC Mode)**:
   ```bash
   R1(config)# enable secret cisco
   ```

7. **Configure an IP Address on GigabitEthernet0/0**:
   ```bash
   R1(config)# interface gigabitEthernet 0/0
   R1(config-if)# ip address 192.168.1.1 255.255.255.0
   R1(config-if)# no shutdown
   ```

8. **Save the Configuration**:
   ```bash
   R1(config-if)# end
   R1# write memory
   ```

---

### **3. Configure Basic Settings on the Switch**

1. **Access the Switch CLI**:
   - Click on the **Switch**.
   - Select the **CLI** tab.

2. **Enter Configuration Mode**:
   ```bash
   Switch> enable
   Switch# configure terminal
   ```

3. **Set the Hostname**:
   ```bash
   Switch(config)# hostname S1
   ```

4. **Set Console Password**:
   ```bash
   S1(config)# line console 0
   S1(config-line)# password cisco
   S1(config-line)# login
   S1(config-line)# exit
   ```

5. **Set VTY Password (for Telnet/SSH)**:
   ```bash
   S1(config)# line vty 0 4
   S1(config-line)# password cisco
   S1(config-line)# login
   S1(config-line)# exit
   ```

6. **Set Enable Password (Privileged EXEC Mode)**:
   ```bash
   S1(config)# enable secret cisco
   ```

7. **Configure an IP Address for Switch Management** (on VLAN 1):
   ```bash
   S1(config)# interface vlan 1
   S1(config-if)# ip address 192.168.1.2 255.255.255.0
   S1(config-if)# no shutdown
   ```

8. **Save the Configuration**:
   ```bash
   S1(config-if)# end
   S1# write memory
   ```

---

### **4. Configure PC Settings**

1. **Configure PC's IP Address**:
   - Click on the **PC**.
   - Go to the **Desktop** tab and select **IP Configuration**.
   - Set the following:
     - IP Address: `192.168.1.3`
     - Subnet Mask: `255.255.255.0`
     - Default Gateway: `192.168.1.1` (the router's IP)

---

### **5. Test Connectivity**

1. **Ping the Router and Switch from the PC**:
   - Open the **Command Prompt** on the **PC**.
   - Test connectivity with the router:
     ```bash
     ping 192.168.1.1
     ```
   - Test connectivity with the switch:
     ```bash
     ping 192.168.1.2
     ```

2. **Establish a Telnet or SSH Connection** (Optional):
   - In the PC’s **Command Prompt**, you can establish a Telnet connection to the router or switch.
   - Example (for Telnet):
     ```bash
     telnet 192.168.1.1
     ```

---

### Summary of Configuration
- Router and Switch have been configured with basic settings such as hostname, console password, enable password, and VTY password.
- An IP address has been configured for both the router and switch for remote management.
- The PC can successfully communicate with both devices using **ping**, and you can optionally enable **Telnet** or **SSH** for remote access.

This completes the basic setup of a router and switch in Cisco Packet Tracer.