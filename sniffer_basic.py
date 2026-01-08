from scapy.all import sniff

def show_packet(packet):
    print(packet.summary())

# Captures packets
sniff(prn=show_packet, count=100)