# Cisco Packet Tracer

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/tools/docs/cisco-packet-tracer.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/tools/docs/cisco-packet-tracer.html](https://yasirbhutta.github.io/tools/docs/cisco-packet-tracer.html)

## How to configure DHCP server in Packet Tracer

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

## **2. Configure the Router**

The router will act as the default gateway for your network.

### **Steps:**

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

## **3. Configure the Server as a DHCP Server**

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

## **4. Configure Client PCs to Use DHCP**

Ensure that client devices are set to obtain their IP addresses automatically.

### **Steps:**

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

## **5. Verify DHCP Functionality**

Ensure that DHCP is correctly assigning IP addresses to all clients.

### **Steps:**

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

## **6. Optional: Configure DHCP on the Router**

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
