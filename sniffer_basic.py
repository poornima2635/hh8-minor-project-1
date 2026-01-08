from scapy.all import sniff

def show_packet(packet):
    print(packet.summary())

# Capture packets
sniff(prn=show_packet, count=100)