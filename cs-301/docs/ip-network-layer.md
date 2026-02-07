---
layout: page
title: IP at Network Layer
description: Binary Converting Binary to Decimal Converting Decimal to Binary Hexadecimal Converting Decimal to Hexadecimal 142 IP addresses are divided into diffe...
keywords: subnet, bits, network, host, hosts
---
# IP at Network Layer

## IP Addressing and Formats
Binary
Converting Binary to Decimal
Converting Decimal to Binary
Hexadecimal
Converting Decimal to Hexadecimal 142
### IP Address Classes

IP addresses are divided into different classes to define a range of addresses for specific network types. Here’s a breakdown of each IP address class and its characteristics:

### 1. **Class A**
   - **Range:** 1.0.0.0 to 126.0.0.0
   - **Default Subnet Mask:** 255.0.0.0
   - **Network and Host ID:** The first 8 bits (first octet) represent the network ID, while the remaining 24 bits represent the host ID.
   - **Number of Networks:** 128 (but 0.0.0.0 and 127.0.0.0 are reserved)
   - **Hosts per Network:** Over 16 million (2^24 - 2)
   - **Usage:** Suitable for large networks with many devices.

### 2. **Class B**
   - **Range:** 128.0.0.0 to 191.255.0.0
   - **Default Subnet Mask:** 255.255.0.0
   - **Network and Host ID:** The first 16 bits represent the network ID, and the remaining 16 bits represent the host ID.
   - **Number of Networks:** 16,384
   - **Hosts per Network:** 65,534 (2^16 - 2)
   - **Usage:** Suitable for medium-sized networks.

### 3. **Class C**
   - **Range:** 192.0.0.0 to 223.255.255.0
   - **Default Subnet Mask:** 255.255.255.0
   - **Network and Host ID:** The first 24 bits represent the network ID, and the last 8 bits represent the host ID.
   - **Number of Networks:** Over 2 million
   - **Hosts per Network:** 254 (2^8 - 2)
   - **Usage:** Suitable for small networks.

### 4. **Class D**
   - **Range:** 224.0.0.0 to 239.255.255.255
   - **Usage:** Reserved for multicast groups. It does not have a subnet mask or division for network and host IDs, as it’s not used for regular IP communication.

### 5. **Class E**
   - **Range:** 240.0.0.0 to 255.255.255.255
   - **Usage:** Reserved for experimental purposes and future use. Not used in regular network communication.


Here’s a tabular representation of IP address classes, their ranges, default subnet masks, and intended usage:

| **Class** | **IP Range**             | **Default Subnet Mask** | **Network ID Bits** | **Host ID Bits** | **Number of Networks** | **Hosts per Network** | **Usage**            |
|-----------|---------------------------|--------------------------|----------------------|-------------------|------------------------|-----------------------|-----------------------|
| A         | 1.0.0.0 to 126.0.0.0      | 255.0.0.0               | 8                    | 24                | 128 (0 and 127 reserved) | 16,777,214           | Large networks       |
| B         | 128.0.0.0 to 191.255.0.0  | 255.255.0.0             | 16                   | 16                | 16,384                 | 65,534               | Medium-sized networks |
| C         | 192.0.0.0 to 223.255.255.0| 255.255.255.0           | 24                   | 8                 | 2,097,152              | 254                  | Small networks       |
| D         | 224.0.0.0 to 239.255.255.255 | N/A                   | N/A                  | N/A               | N/A                    | N/A                  | Multicast            |
| E         | 240.0.0.0 to 255.255.255.255 | N/A                   | N/A                  | N/A               | N/A                    | N/A                  | Experimental         |

This table simplifies the differences between IP address classes, making it easier to understand their structure and applications.


### Subnet Masks 

### Private (RFC 1918) Addressing

Private IP addresses are reserved for use within private networks and are not routable on the public internet. Here are the ranges for private IP addresses:

| **Class** | **Private IP Range**            | **Default Subnet Mask** |
|-----------|---------------------------------|--------------------------|
| **A**     | 10.0.0.0 to 10.255.255.255      | 255.0.0.0               |
| **B**     | 172.16.0.0 to 172.31.255.255    | 255.240.0.0             |
| **C**     | 192.168.0.0 to 192.168.255.255  | 255.255.0.0             |

### Summary:
- **Class A (10.x.x.x)**: Allows a large number of devices (over 16 million) and is commonly used in large organizations.
- **Class B (172.16.x.x - 172.31.x.x)**: Used for medium-sized networks, allowing up to 1 million addresses.
- **Class C (192.168.x.x)**: Most commonly used for small networks, typically for home and small business routers.

These ranges help prevent IP conflicts within private networks and ensure that public IPs are available for internet traffic.

## Subnetting IP 

In **CIDR (Classless Inter-Domain Routing)**, subnets are created by adjusting the subnet mask length, which is indicated by the **/prefix** notation (like /26). This notation tells us how many bits are used for the **network and subnet** portions, with the remaining bits available for **hosts**.

Here's a table that lists **all possible subnets** and details for each CIDR prefix from **/24 to /30**, which are common for subnets with fewer hosts. This includes the subnet mask, number of subnets, and number of hosts per subnet.

| **CIDR Notation** | **Subnet Mask**     | **Number of Subnets** | **Hosts per Subnet** |
|-------------------|---------------------|------------------------|-----------------------|
| /24               | 255.255.255.0       | 1                      | 254                   |
| /25               | 255.255.255.128     | 2                      | 126                   |
| /26               | 255.255.255.192     | 4                      | 62                    |
| /27               | 255.255.255.224     | 8                      | 30                    |
| /28               | 255.255.255.240     | 16                     | 14                    |
| /29               | 255.255.255.248     | 32                     | 6                     |
| /30               | 255.255.255.252     | 64                     | 2                     |

### Explanation of Each Column

1. **CIDR Notation**: The `/N` tells us how many bits are used for the network (and subnet) portion.
2. **Subnet Mask**: The equivalent dotted-decimal representation of the subnet mask.
3. **Number of Subnets**: Calculated by adding subnet bits to the original network mask. For example, moving from /24 to /26 means we add 2 bits for subnetting, giving us \(2^2 = 4\) subnets.
4. **Hosts per Subnet**: Calculated as \(2^{\text{host bits}} - 2\) (the `-2` accounts for the network and broadcast addresses, which can't be assigned to hosts).

### Examples

1. **/24 Subnet (255.255.255.0)**:
   - 1 subnet with 254 hosts (ideal for small networks needing many hosts).

2. **/26 Subnet (255.255.255.192)**:
   - 4 subnets, each with 62 hosts.

3. **/30 Subnet (255.255.255.252)**:
   - 64 subnets, each with only 2 hosts (often used in point-to-point links).

CIDR allows efficient use of IP addresses, as it enables creating variable-sized subnets by adjusting the subnet mask. This avoids wasting addresses, especially in networks that don’t require a large number of host addresses.

Let's go through an example to clarify network bits, subnet bits, and host bits.

Suppose we have an IP address in the Class C range: **192.168.1.0/26**. In this case, `/26` represents the subnet mask (26 bits for the network + subnet portion). 

### Breakdown

1. **Network Bits**:
   - For a Class C network, the default subnet mask is **/24**, meaning the first 24 bits are for the network.
   - Here, we have **26 bits** as the subnet mask, so the first 24 bits represent the network portion, plus **2 additional bits for subnetting**.

2. **Subnet Bits**:
   - Since we extended the default **/24** mask to **/26**, we added **2 bits** for subnetting.
   - These **2 bits** are used to create subnets within the original Class C network.
   - With 2 subnet bits, we can create **2^2 = 4 subnets**.

3. **Host Bits**:
   - After using 26 bits for the network and subnet portion, we have **6 bits left for hosts** (since an IPv4 address has 32 bits in total).
   - These **6 bits** can represent hosts within each subnet, giving us **2^6 - 2 = 62 usable hosts** per subnet (subtracting 2 for the network and broadcast addresses).

### Example in Detail

For **192.168.1.0/26**, here’s the breakdown:

- **Network portion (24 bits)**: `192.168.1`
- **Subnet bits (2 bits)**: `00`, `01`, `10`, `11` (each combination represents a different subnet)
- **Host bits (6 bits)**: Remaining bits for host addresses.

The **subnets** created will be:

1. **Subnet 1**: 192.168.1.0/26 (Host range: 192.168.1.1 to 192.168.1.62, Broadcast: 192.168.1.63)
2. **Subnet 2**: 192.168.1.64/26 (Host range: 192.168.1.65 to 192.168.1.126, Broadcast: 192.168.1.127)
3. **Subnet 3**: 192.168.1.128/26 (Host range: 192.168.1.129 to 192.168.1.190, Broadcast: 192.168.1.191)
4. **Subnet 4**: 192.168.1.192/26 (Host range: 192.168.1.193 to 192.168.1.254, Broadcast: 192.168.1.255)

In this way:
- **Network bits** define the main network.
- **Subnet bits** allow us to create subnets within the main network.
- **Host bits** provide addresses within each subnet.
  
Calculating Hosts in a Subnet 
Calculating Networks in a Subnet
Zero Subnet Rule 
Determining the Range of Valid IPs