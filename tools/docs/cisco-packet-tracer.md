# Cisco Packet Tracer

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/tools/docs/cisco-packet-tracer.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/tools/docs/cisco-packet-tracer.html](https://yasirbhutta.github.io/tools/docs/cisco-packet-tracer.html)

- [How to configure DHCP server](#1-how-to-configure-dhcp-server-in-packet-tracer)
- [How to configure DNS server](#2-how-to-configure-dns-server-in-packet-tracer)
- [Configure DHCP on the Router](#6-optional-configure-dhcp-on-the-router)
- [Connecting Two LANs with a Router: A Step-by-Step Guide](#3-connecting-two-lans-with-a-router-a-step-by-step-guide)

## 1. How to configure DHCP server in Packet Tracer

Configuring a DHCP (Dynamic Host Configuration Protocol) server in Cisco Packet Tracer allows you to automate the assignment of IP addresses to devices on your network. Below is a step-by-step guide to setting up a DHCP server using Packet Tracer's built-in server functionality. This guide assumes you have a basic understanding of networking concepts and Packet Tracer's interface.

## **1. Set Up Your Network Topology**

Before configuring the DHCP server, you need to set up a basic network topology. Here's a simple example:

- **Devices Needed:**
  - 1 Router
  - 1 Switch
  - 1 Server
  - Multiple PCs (clients)

### **Steps:**

1. **Open Packet Tracer:**
   - Launch Cisco Packet Tracer on your computer.

2. **Add Devices to the Workspace:**
   - From the device list at the bottom, drag and drop the following devices onto the workspace:
     - **Router:** e.g., 2911 Router
     - **Switch:** e.g., 2960 Switch
     - **Server:** e.g., Generic Server
     - **PCs:** Add as many as needed (e.g., 2 PCs)

3. **Connect the Devices:**
   - Use **Copper Straight-Through** cables to connect devices:
     - **Router to Switch:** Connect the router's GigabitEthernet0/0 interface to the switch's FastEthernet0/1 port.
     - **Switch to Server:** Connect the switch's FastEthernet0/2 port to the server's FastEthernet0 port.
     - **Switch to PCs:** Connect each PC's FastEthernet0 port to the switch's FastEthernet0/3, FastEthernet0/4, etc.

   ![Basic Topology](https://i.imgur.com/ZFVb3Xn.png)

### **2. Configure the Router**

The router will act as the default gateway for your network.

#### **Steps:**

1. **Access the Router's CLI:**
   - Click on the router.
   - Go to the **CLI** tab.

2. **Enter Configuration Mode:**
   ```plaintext
   Router> enable
   Router# configure terminal
   ```

3. **Configure the Interface Connected to the Switch:**
   ```plaintext
   Router(config)# interface GigabitEthernet0/0
   Router(config-if)# ip address 192.168.1.1 255.255.255.0
   Router(config-if)# no shutdown
   Router(config-if)# exit
   ```

4. **Enable DHCP on the Router (Optional):**
   - If you prefer to use the router as a DHCP server, you can skip to [Configuring DHCP on the Router](#appendix-a-configuring-dhcp-on-the-router) Otherwise, proceed to configure the dedicated server.

5. **Exit Configuration Mode:**
   ```plaintext
   Router(config)# exit
   Router# write memory
   ```

### **3. Configure the Server as a DHCP Server**

Using Packet Tracer's built-in server functionality is straightforward.

### **Steps:**

1. **Access the Server:**
   - Click on the **Server** device.
   - Go to the **Config** tab or **Services** tab (depending on Packet Tracer version).

2. **Configure the Server's IP Address:**
   - Ensure the server has a static IP address within the network range.
   - Example Configuration:
     - **IP Address:** 192.168.1.10
     - **Subnet Mask:** 255.255.255.0
     - **Default Gateway:** 192.168.1.1

   ![Server Configuration](https://i.imgur.com/3L0HcGE.png)

3. **Set Up DHCP Service:**
   - Navigate to the **Services** tab.
   - Click on **DHCP** from the left-hand menu.
   - Click **Add** to create a new DHCP pool.

4. **Configure DHCP Pool Parameters:**
   - **Default Gateway:** 192.168.1.1
   - **DNS Server:** You can use a public DNS server like 8.8.8.8 or specify your own.
   - **Start IP Address:** 192.168.1.100
   - **Subnet Mask:** 255.255.255.0
   - **Max Number of Users:** Set according to the number of devices (e.g., 50)

   ![DHCP Configuration](https://i.imgur.com/k9sLw5E.png)

5. **Save the Configuration:**
   - Ensure all settings are correctly entered.
   - The DHCP server is now ready to assign IP addresses to clients.

### **4. Configure Client PCs to Use DHCP**

Ensure that client devices are set to obtain their IP addresses automatically.

#### **Steps:**

1. **Access a PC:**
   - Click on a **PC** device.
   - Go to the **Desktop** tab.
   - Click on **IP Configuration**.

2. **Set IP Configuration to DHCP:**
   - Select **DHCP**.
   - The PC should automatically receive an IP address from the DHCP server.

   ![PC DHCP](https://i.imgur.com/8BsjOw1.png)

3. **Verify IP Address:**
   - After a few seconds, the PC should display an IP address within the DHCP pool range (e.g., 192.168.1.100).
   - Repeat this step for all client PCs.

### **5. Verify DHCP Functionality**

Ensure that DHCP is correctly assigning IP addresses to all clients.

#### **Steps:**

1. **Check IP Addresses on PCs:**
   - Each PC should have a unique IP address within the specified DHCP pool.
   - The **Default Gateway** should be set to the router's IP (192.168.1.1).
   - The **DNS Server** should be as configured (e.g., 8.8.8.8).

2. **Ping Test:**
   - From a PC, open the **Command Prompt** (Desktop > Command Prompt).
   - Ping the default gateway to ensure connectivity.
     ```plaintext
     ping 192.168.1.1
     ```
   - You should receive replies indicating successful communication.

3. **Check DHCP Server Lease Table:**
   - On the **Server**, go to the **Services** tab.
   - Click on **DHCP**.
   - Review the list of leased IP addresses to ensure all clients are receiving addresses.

   ![DHCP Lease Table](https://i.imgur.com/oC7bU6v.png)

### **6. Optional: Configure DHCP on the Router**

If you prefer to use the router as your DHCP server instead of a dedicated server, follow these steps:

### **Steps:**

1. **Access the Router's CLI:**
   - Click on the **Router** device.
   - Go to the **CLI** tab.

2. **Enter Configuration Mode:**
   ```plaintext
   Router> enable
   Router# configure terminal
   ```

3. **Create a DHCP Pool:**
   ```plaintext
   Router(config)# ip dhcp pool LAN
   Router(dhcp-config)# network 192.168.1.0 255.255.255.0
   Router(dhcp-config)# default-router 192.168.1.1
   Router(dhcp-config)# dns-server 8.8.8.8
   Router(dhcp-config)# exit
   ```

4. **Exclude Addresses (Optional):**
   - To prevent the router from assigning certain IP addresses (e.g., for the router itself or servers), use the `ip dhcp excluded-address` command.
   ```plaintext
   Router(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10
   Router(config)# exit
   Router# write memory
   ```

5. **Configure Clients to Use DHCP:**
   - As previously described, set each PC to obtain an IP address automatically.

6. **Verify DHCP Assignments:**
   - Check the IP addresses on the PCs and perform connectivity tests as described earlier.

## **Troubleshooting Tips**

- **No IP Address Assigned:**
  - Ensure that the DHCP server is connected to the correct network.
  - Verify that the DHCP service is enabled and properly configured on the server or router.
  - Check that clients are set to obtain IP addresses automatically.

- **IP Address Conflicts:**
  - Ensure that the DHCP pool does not overlap with any statically assigned IP addresses.
  - Use the `ip dhcp excluded-address` command on routers to exclude specific IP ranges.

- **Connectivity Issues:**
  - Verify all device interfaces are up (`no shutdown` on router interfaces).
  - Check cable connections and ensure devices are properly connected to the switch.

## **Conclusion**

Configuring a DHCP server in Packet Tracer simplifies network management by automating IP address assignments. Whether you choose to use a dedicated server or configure the router to handle DHCP duties, the process involves setting up the DHCP pool parameters and ensuring clients are set to receive IP addresses automatically. By following the steps outlined above, you can efficiently set up and verify a DHCP server in your simulated network environment.

## 2. How to configure DNS server in Packet Tracer

To configure a DNS server in Cisco Packet Tracer, follow these steps:

### Step 1: Add Devices
1. **Add a DNS Server**: Drag a server from the network devices list and place it on the workspace.
2. **Add a PC**: Drag a PC to the workspace.
3. **Add a Router and Switch**: Add a router and a switch to connect the DNS server and the PC.

### Step 2: Connect the Devices
1. **Connect the devices** using the appropriate cables (copper straight-through or crossover, depending on the type of connection).
2. Make sure the server, PC, and router are all connected through the switch.

### Step 3: Assign IP Addresses
1. **Assign IP addresses** to each device manually or use DHCP for automatic IP assignment.

   - **DNS Server**: 
     - Click on the DNS Server.
     - Go to the **Desktop tab**, click on **IP Configuration**, and assign a static IP address (e.g., 192.168.1.2).
   
   - **PC**: 
     - Click on the PC.
     - Go to the **Desktop tab**, click on **IP Configuration**, and assign an IP address (e.g., 192.168.1.3) with the appropriate subnet mask and default gateway (e.g., 192.168.1.1 for the router).

### Step 4: Configure DNS Server
1. **Click on the DNS Server**.
2. Go to the **Services tab** and select **DNS**.
3. **Turn on the DNS service** by clicking the **ON** button.
4. **Add DNS records**:
- **Record #1:**
   - Enter the domain name (e.g., `www.example.com`).
   - Enter the corresponding IP address (e.g., 192.168.1.3).
   - Click on **Add** to add the `A Record`.
 - **Record #2:**
   - Enter the domain name (e.g., `gudgk.edu.pk`).
   - Enter the corresponding IP address (e.g., 192.168.1.8).
   - Click on **Add** to add the `A Record`.

### Step 5: Configure PC to Use DNS
1. **Go to the PC** and open the **Desktop tab**.
2. Open the **IP Configuration**.
3. In the **DNS Server** field, enter the IP address of the DNS server (e.g., 192.168.1.2).

### Step 6: Test the DNS Configuration
1. **Go to the PC** and open the **Command Prompt** from the **Desktop tab**.
2. Type the following command to test if the DNS resolution works:
   ```
   ping www.example.com
   ```
3. If the DNS server is correctly configured, the PC will be able to resolve the domain name to the IP address and respond to the ping.

## Task #1:
To create the network diagram in Cisco Packet Tracer based on the whiteboard image, follow these steps:

Devices and IPs:

![network diagram](img/cisco-pt-task-dhcp-dns-router-512.png)
1. Router:

IP Address: 192.168.30.1


2. DHCP Server:

IP Address: 192.168.30.10

Assign IP addresses from the range 192.168.30.160 onwards


3. DNS Server:

IP Address: 192.168.30.30

4. PC1 and PC2 (DHCP Clients):

Connected to a switch, both configured as DHCP clients to obtain IPs dynamically.

5. PC3:

Static IP: 192.168.30.31

6. Switch:

All PCs, DHCP, and DNS servers are connected through this switch.


Steps in Cisco Packet Tracer:

1. Add devices:

Drag a Router, Switch, 3 PCs, DHCP Server, and DNS Server onto the workspace.

2. Configure the Router:

Go to the Router -> Config tab, assign the IP address 192.168.30.1 to the appropriate interface (e.g., GigabitEthernet0/0).

3. Configure the DHCP Server:

Set the IP address of the DHCP Server to 192.168.30.10.

Go to the Services tab and configure DHCP. Set the start IP range to 192.168.30.160.

4. Configure the DNS Server:

Assign the IP address 192.168.30.30 to the DNS server.

In the Services tab, configure DNS with any domain names you want to resolve.

- Add five DNS entries by filling out the fields as follows:

| **Domain Name**        | **IP Address**        |
|------------------------|-----------------------|
| example.com            | 192.168.30.50         |
| site.local             | 192.168.30.60         |
| network.internal       | 192.168.30.70         |
| appserver.company      | 192.168.30.80         |
| database.service       | 192.168.30.90         |

5. Configure the PCs:

PC1 and PC2: Go to each PC, and in the IP Configuration tab, set the IP configuration to DHCP.

PC3: Manually configure its IP address to 192.168.30.31 in the Static IP section.


6. Connect all devices:

Use cables to connect the devices to the switch (PCs, DHCP, DNS Server).

Connect the switch to the router.

7. Test connectivity:

- Once the network is built, test the network by pinging the router from each PC, and check DHCP functionality on PC1 and PC2.

8. Test DNS Resolution:
9. 
From PC1, PC2, or PC3, use the Command Prompt (CLI) to test the DNS resolution by pinging the domain names (e.g., ping example.com). If DNS is properly configured, it will resolve the domain name to the associated IP address.

### 3. Connecting Two LANs with a Router: A Step-by-Step Guide

Connecting two Local Area Networks (LANs) using a router allows devices on different networks to communicate with each other.

**Network Diagram**

```
[LAN 1] ------ [Router] ------ [LAN 2]
```
### Equipment Needed
1. **Router**: A device that forwards data packets between networks.
2. **Two LANs**: Each can consist of switches and devices (like PCs).
3. **Ethernet Cables**: To connect the router to the switches or devices.

### Step-by-Step Guide

Connecting two Local Area Networks (LANs) using a router in Cisco Packet Tracer involves several steps, including configuring the router and the devices within each LAN. Here’s a detailed guide to help you set up this connection:

#### Step 1: Open Cisco Packet Tracer
1. Launch Cisco Packet Tracer on your computer.

#### Step 2: Add Devices
1. **Add a Router:** Drag and drop a router (e.g., a 2911 router) onto the workspace.
2. **Add Switches:** Drag and drop two switches (e.g., 2960 switches) onto the workspace.
3. **Add PCs:** Add at least one PC to each switch (e.g., PC1 on Switch1 and PC2 on Switch2).

#### Step 3: Connect Devices
1. **Connect the PCs to the Switches:**
   - Use the **Connections** tool (cable icon) and select **Copper Straight-Through** cable.
   - Connect **PC1** to **Switch1** (e.g., FastEthernet 0/1).
   - Connect **PC2** to **Switch2** (e.g., FastEthernet 0/1).

2. **Connect the Switches to the Router:**
   - Use the **Copper Straight-Through** cable.
   - Connect **Switch1** to the router's **GigabitEthernet 0/0** port.
   - Connect **Switch2** to the router's **GigabitEthernet 0/1** port.

#### Step 4: Configure the Router
1. **Access the Router CLI:**
   - Click on the router and go to the **CLI** tab.
   - Press `Enter` to access the command line interface.

2. **Enter Global Configuration Mode:**
```bash
Router> enable
Router# configure terminal
```

**optional to show interfaces**

```bash
Router# show interfaces
```
3. **Configure Interfaces:**
   - For **FastEthernet 0/0** (connecting to LAN1):
```bash
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0  # Assigning IP address
Router(config-if)# no shutdown  # Activating the interface
```

   - For **GigabitEthernet 0/1** (connecting to LAN2):
  
```bash
Router(config)# interface GigabitEthernet0/1
Router(config-if)# ip address 192.168.2.1 255.255.255.0  # Assigning IP address
Router(config-if)# no shutdown  # Activating the interface
```

#### Step 5: Configure the Switches (Optional)
While the switches do not require specific configurations for basic connectivity, you may choose to configure them for better management. Here’s how you can set VLANs (if needed) and assign ports to VLANs.

1. **Access Switch CLI:**
   - Click on each switch and go to the **CLI** tab.

2. **Create VLANs (if desired):**
```bash
Switch# enable
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name LAN1
Switch(config-vlan)# exit
Switch(config)# vlan 20
Switch(config-vlan)# name LAN2
```

3. **Assign Ports to VLANs:**
   - For Switch1 (connecting to LAN1):
```bash
Switch(config)# interface range fa0/1
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 10
```

   - For Switch2 (connecting to LAN2):
```bash
Switch(config)# interface range fa0/1
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 20
```

#### Step 6: Configure the PCs
1. **Configure PC1 (in LAN1):**
   - Click on **PC1** and go to the **Desktop** tab.
   - Click on **IP Configuration** and set:
     - **IP Address:** `192.168.1.2`
     - **Subnet Mask:** `255.255.255.0`
     - **Default Gateway:** `192.168.1.1`

2. **Configure PC2 (in LAN2):**
   - Click on **PC2** and go to the **Desktop** tab.
   - Click on **IP Configuration** and set:
     - **IP Address:** `192.168.2.2`
     - **Subnet Mask:** `255.255.255.0`
     - **Default Gateway:** `192.168.2.1`

#### Step 7: Test Connectivity
1. **Ping Between PCs:**
   - Open the command prompt on **PC1** and type:
```bash
ping 192.168.2.2  # This pings PC2 in LAN2
```
   - You should receive replies if everything is configured correctly.

#### Step 8: Save Configuration
1. **Save the Router Configuration:**
```bash
Router# write memory
```

2. **Save the Switch Configuration (if applicable):**
```bash
Switch# write memory
```

### Additional Notes
- **Routing:** If you need to enable routing between the two LANs, ensure the router has routing enabled, which is typically the case by default.

### Conclusion
By following these steps, you can successfully connect two LANs using a router in Cisco Packet Tracer. This setup allows devices from one LAN to communicate with devices on another LAN, demonstrating the fundamental concept of routing in computer networks. If you have any further questions or need additional details, feel free to ask!

## How to Configure VLANS

Configuring VLANs (Virtual Local Area Networks) in Cisco Packet Tracer is straightforward. Here’s a step-by-step guide to help you set up VLANs:

### Step 1: Open Cisco Packet Tracer
1. Launch Cisco Packet Tracer on your computer.

### Step 2: Add Devices
1. Drag and drop at least one switch (e.g., a 2960 switch) and a couple of end devices (e.g., PCs) onto the workspace.

### Step 3: Connect Devices
1. Use the **Connections** tool to connect the PCs to the switch. Choose the appropriate cable (usually a straight-through cable for connecting PCs to switches).
   
### Step 4: Access the Switch CLI
1. Click on the switch and go to the **CLI** tab.
2. Press `Enter` to access the command line interface.

### Step 5: Enter Global Configuration Mode
```bash
Switch> enable
Switch# configure terminal
```

### Step 6: Create VLANs
1. Create VLANs using the following command:
```bash
Switch(config)# vlan [VLAN_ID]
```
   - For example, to create VLAN 10:
```bash
Switch(config)# vlan 10
```
2. Optionally, name the VLAN:
```bash
Switch(vlan)# name VLAN_NAME
```
   - For example:
```bash
Switch(vlan)# name Sales
```
3. Repeat these steps for any additional VLANs you want to create.

### Step 7: Assign VLANs to Switch Ports
1. Enter the interface configuration mode for the port you want to assign to a VLAN. For example, to configure FastEthernet 0/1:
```bash
Switch(config)# interface fa0/1
```
2. Assign the port to a VLAN:
```bash
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan [VLAN_ID]
```
   - For example:
```bash
Switch(config-if)# switchport access vlan 10
```
3. Exit interface configuration mode and repeat for other ports as needed.

### Step 8: Save Configuration
1. After configuring the VLANs and ports, save your configuration:
```bash
Switch# write memory
```

### Step 9: Verify VLAN Configuration
1. To check your VLAN configuration, use the following command:
```bash
Switch# show vlan brief
```
   - This command displays a summary of the VLANs configured on the switch.

### Step 10: Test Connectivity
1. Assign IP addresses to the PCs in the same VLAN. For example, if PC1 is in VLAN 10:
   - Set IP address: `192.168.10.2`
   - Set subnet mask: `255.255.255.0`
   - Default gateway: `192.168.10.1`
2. Configure another PC in the same VLAN (e.g., `192.168.10.3`) and test connectivity using the **ping** command.

### Additional Tips
- Ensure that the devices in the same VLAN can communicate with each other while devices in different VLANs cannot without a Layer 3 device (like a router).
- If you need to configure inter-VLAN routing, you will require a router or a Layer 3 switch.

With these steps, you should be able to configure VLANs successfully in Cisco Packet Tracer. If you have any specific scenarios or questions, feel free to ask!



## **Appendices**

### **Appendix A: Configuring DHCP on the Router**

To configure a **DHCP (Dynamic Host Configuration Protocol) server** in Cisco Packet Tracer, follow these steps:

### Step 1: Add Devices to the Network
1. **Open Cisco Packet Tracer**.
2. Add a **server** device (from the "End Devices" section) and a **router** or **switch** to the workspace.
3. Add a **PC** or any other device that will obtain its IP address via DHCP.

### Step 2: Configure the DHCP Server
1. **Click on the Server**.
2. In the **Physical** tab, ensure the correct module (if required) is installed.
3. Switch to the **Config** tab.
4. On the left menu, select **DHCP**.
5. **Turn on the DHCP service** by toggling the button to "ON."
6. Under **Pool Name**, enter a name for the pool (e.g., "DHCP_Pool").
7. Enter the following details:
   - **Default Gateway**: The IP address of the router or switch that will be used as the default gateway.
   - **DNS Server**: The DNS server address, or leave it as default.
   - **Start IP Address**: The first IP address in the range you want to assign to devices.
   - **Subnet Mask**: The appropriate subnet mask for the network.
   - **Max Users**: The number of devices that can receive an IP address from the DHCP pool.

For example:
- **Pool Name**: `DHCP_Pool`
- **Default Gateway**: `192.168.1.1`
- **DNS Server**: `8.8.8.8` (or any DNS server)
- **Start IP Address**: `192.168.1.10`
- **Subnet Mask**: `255.255.255.0`
- **Max Users**: `50`

### Step 3: Configure Router or Switch for DHCP (Optional)
If you're using a **router** to provide DHCP addresses, you need to configure the router to relay DHCP requests:

1. **Click on the Router**.
2. Go to the **CLI** tab.
3. Enter the following commands to configure a DHCP pool on the router:
   ```plaintext
   Router> enable
   Router# configure terminal
   Router(config)# ip dhcp pool DHCP_Pool
   Router(dhcp-config)# network 192.168.1.0 255.255.255.0
   Router(dhcp-config)# default-router 192.168.1.1
   Router(dhcp-config)# dns-server 8.8.8.8
   Router(dhcp-config)# exit
   Router(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.9
   ```

### Step 4: Configure PCs to Obtain IP Automatically
1. **Click on the PC**.
2. Go to the **Desktop** tab and select **IP Configuration**.
3. Ensure the **DHCP** option is selected.

### Step 5: Test the Network
1. After configuration, you should see the **PC** receiving an IP address from the DHCP server.
2. You can verify this by going back to the **IP Configuration** window of the PC, where the automatically assigned IP address will be displayed.

This is how you can configure a DHCP server in Cisco Packet Tracer! Let me know if you need any further details.


