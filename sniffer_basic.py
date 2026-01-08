from scapy.all import sniff

def show_packet(pkt):
    print(pkt.summary())

# Captures packets
sniff(prn=show_packet, count=100)