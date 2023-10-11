# lab 3
The work was done in EVE-NG using Cisco.

The following configuration was built:
![pic1](images/pic1.png)

From lab1:
The network is configured with the STP protocol (specifically, rapid PVST was selected). The distribution layer switch is the root of the network for both VLANs. The link between the access layer switches is blocked.

Added:
 1) All clients receive network settings via DHCP.
 2) The first 10 IP addresses are excluded from being issued to clients.
 3) NAT is configured: clients can contact the upstream router (R2, ip address: 172.16.0.2) and receive a response. There are no additional routes to the LAN in R2.

Outputs from the left VPC:
  1) Requested settings via DHCP.
  2) Verified that we can ping the right VPC (and get a response).
  3) Verified that we can ping the top router (and get a response).
```
VPCS> ip dhcp
DDORA IP 10.0.10.11/24 GW 10.0.10.2

VPCS> ping 10.0.20.11

84 bytes from 10.0.20.11 icmp_seq=1 ttl=63 time=384.129 ms
84 bytes from 10.0.20.11 icmp_seq=2 ttl=63 time=325.861 ms
84 bytes from 10.0.20.11 icmp_seq=3 ttl=63 time=105.507 ms
84 bytes from 10.0.20.11 icmp_seq=4 ttl=63 time=286.043 ms
84 bytes from 10.0.20.11 icmp_seq=5 ttl=63 time=116.598 ms

VPCS> ping 172.16.0.2

84 bytes from 172.16.0.2 icmp_seq=1 ttl=254 time=316.401 ms
84 bytes from 172.16.0.2 icmp_seq=2 ttl=254 time=107.171 ms
84 bytes from 172.16.0.2 icmp_seq=3 ttl=254 time=57.357 ms
84 bytes from 172.16.0.2 icmp_seq=4 ttl=254 time=81.532 ms
84 bytes from 172.16.0.2 icmp_seq=5 ttl=254 time=160.383 ms
```

Right VPC:
```
VPCS> ip dhcp
DDORA IP 10.0.20.11/24 GW 10.0.20.2

VPCS> ping 10.0.10.11

84 bytes from 10.0.10.11 icmp_seq=1 ttl=63 time=243.384 ms
84 bytes from 10.0.10.11 icmp_seq=2 ttl=63 time=80.859 ms
84 bytes from 10.0.10.11 icmp_seq=3 ttl=63 time=120.391 ms
84 bytes from 10.0.10.11 icmp_seq=4 ttl=63 time=107.002 ms
84 bytes from 10.0.10.11 icmp_seq=5 ttl=63 time=74.405 ms

VPCS> ping 172.16.0.2

84 bytes from 172.16.0.2 icmp_seq=1 ttl=254 time=190.699 ms
84 bytes from 172.16.0.2 icmp_seq=2 ttl=254 time=47.653 ms
84 bytes from 172.16.0.2 icmp_seq=3 ttl=254 time=75.394 ms
84 bytes from 172.16.0.2 icmp_seq=4 ttl=254 time=72.997 ms
84 bytes from 172.16.0.2 icmp_seq=5 ttl=254 time=96.615 ms
```

Output, demonstrating that R2 cannot send packets to network clients.
```
Router#ping 10.0.10.1       
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.10.1, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
```

In the src folder you can find the lab file (in .unl format) as well as configurations from network devices.
