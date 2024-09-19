# Computer Networks: Network Topologies 

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaC3BC160eBZZSs3CW0c) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/cs-407-computer-networks/docs/lab1.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/cs-407-computer-networks/docs/lab1.html](https://yasirbhutta.github.io/cs-407-computer-networks/docs/lab1.html)

To perform network topologies like star, bus, and ring using Cisco Packet Tracer, you'll need to understand the basic setup for each topology. Below are steps for simulating these topologies:

### 1. **Star Topology** 
In a star topology, all devices (nodes) are connected to a central device, typically a switch.

**Steps:**
- Open Cisco Packet Tracer.
- Drag and drop a switch onto the workspace.
- Add PCs or laptops (end devices).
- Connect each PC to the switch using copper straight-through cables.
- Configure IP addresses for each device.
- Ping between the devices to verify connectivity.

**Example Setup:**
- Drag a **2960 Switch** and four **PCs** from the device section.
- Connect each PC to the switch using the **Copper Straight-Through** cable.
- Assign IP addresses manually to each PC by clicking on the PC, then going to the **Desktop** tab and selecting **IP Configuration**.

## Using ping command

To use the `ping` command in Cisco Packet Tracer for testing connectivity between devices (e.g., PCs, routers), follow these steps:

### **Using Ping from a PC**
1. **Set Up IP Addresses**: 
   - Ensure that each device in your network has a unique IP address and that the devices are connected through switches, routers, or hubs.
   - To assign IP addresses, click on the PC, go to the **Desktop** tab, and select **IP Configuration**.

2. **Access the Command Prompt**:
   - Click on the PC you want to test.
   - Go to the **Desktop** tab.
   - Select **Command Prompt**.

3. **Use the Ping Command**:
   - In the command prompt, type the following:
     ```bash
     ping <target_ip_address>
     ```
     Replace `<target_ip_address>` with the IP address of the device you want to ping.

   - Example:
     ```bash
     ping 192.168.1.2
     ```

4. **View Results**: 
   - If the devices are properly connected, you will see a successful response showing the time it took for the packets to reach the destination.
   - If there is an issue, you'll see messages like "Request timed out."

### **Example Scenario**:
1. Connect three PCs with a switch and assign the following IP addresses:
   - **PC1**: 192.168.1.1
   - **PC2**: 192.168.1.2
   - **PC3**: 192.168.1.3
2. Open the **Command Prompt** on **PC1** and type:
   ```bash
   ping 192.168.1.2
   ```
3. If the connection is successful, you should see a response similar to:
   ```bash
   Reply from 192.168.1.2: bytes=32 time<1ms TTL=128
   ```

This process will help you verify whether devices in your network are connected properly.

