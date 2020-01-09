import sys
import binascii
import socket

#print('Name1 - ',sys.argv[1],', Name2 - ',sys.argv[2])

def send_udp_message(message, address, port):
    """send_udp_message sends a message to UDP server

    message should be a hexadecimal encoded string
    """
    message = message.replace(" ", "").replace("\n", "")
    server_address = (address, port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(binascii.unhexlify(message), server_address)
        data, _ = sock.recvfrom(4096)
    finally:
        sock.close()
    return binascii.hexlify(data).decode("utf-8")


def format_hex(hex):
    """format_hex returns a pretty version of a hex string"""
    octets = [hex[i:i+2] for i in range(0, len(hex), 2)]
    pairs = [" ".join(octets[i:i+2]) for i in range(0, len(octets), 2)]
    return "\n".join(pairs)


message = "AA AA 01 00 00 01 00 00 00 00 00 00 " 
#"07 65 78 61 6d 70 6c 65 03 63 6f 6d 00 11 11 00 01"

i=0
s=''
for line in sys.argv[2]:
    if '.' in line:
        j=i
        i=0
        t=s
        s=''
    else:
        i=i+1
        s=s+hex(ord(line))[2:]+' '
message=message+'0'+str(j)+' '+t+'0'+str(i)+' '+s+' 00 11 11 00 01'





response = send_udp_message(message, sys.argv[1], 53)
print(format_hex(response)) 


