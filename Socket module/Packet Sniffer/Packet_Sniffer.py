import socket
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
packet = sniffer.recv(65535)

def format_ip(val):
    return ".".join(str(addr) for addr in val)
def seperator(val):
    return " ".join(format(f"{byte:02X}") for byte in val)
def format_mac(data):
    return ":".join(format(f"{byte:02X}") for byte in data)

print("Ethernet Header: ",seperator(packet[:14]))

#ETHERNET HEADERS
ehl = 14
eth_header = packet[:ehl]

print("Destination Mac:",format_mac(eth_header[:6]))
print("Source Mac     :",format_mac(eth_header[6:12]))

ether_type = eth_header[12:].hex().upper()

if ether_type == "0800":
    print("EtherType      : IPv4")
elif ether_type == "0806":
    print("EtherType      : ARP")
elif ether_type == "86DD":
    print("EtherType      : IPv6")
else:
    print("EtherType      : Unknown")

#IP HEADERS
ip_header = packet[ehl:ehl+20]
print("IP Header: ",seperator(ip_header))
print("TTL: ", ip_header[8])
print("Protocol: ", ip_header[9])

first_byte = ip_header[0]
version = first_byte >> 4
print("Version: ",version)

ihl = first_byte & 0x0f #Internet Header Length
ip_hl = ihl*4
print("Header length: ",ip_hl)

print("Source IP: ", format_ip(ip_header[12: 16]))
print("Destination IP: ", format_ip(ip_header[16: 20]))

#TCP HEADERS
tcp_st = ehl+ip_hl
tcp_header = packet[tcp_st:tcp_st+20]
print("TCP Header: ",seperator(tcp_header))

source_port = int.from_bytes(tcp_header[:2], "big")
destination_port = int.from_bytes(tcp_header[2:4], "big")
print("Source Port: ", source_port)
print("Destination Port: ", destination_port)

flags = tcp_header[13]
print("Flags: ", flags, " ", bin(flags))

if flags & 0x02:
    print("SYN")
if flags & 0x10:
    print("ACK")
if flags & 0x01:
    print("FIN")
if flags & 0x04:
    print("RST")

seq_num = int.from_bytes(tcp_header[4:8], "big")
print("Sequence number: ",seq_num)
ack_num = int.from_bytes(tcp_header[8:12], "big")
print("ACK number: ",ack_num)

data_offset = tcp_header[12] >> 4
tcp_hl =  data_offset * 4
print("TCP Header length: ", tcp_hl)

#PAYLOAD
packet_st = ehl + ip_hl + tcp_hl
payload = packet[packet_st:]
print("Payload Length: ", len(payload))

try:
    print("Payload: ", payload.decode())
except:
    print("Binary Data")