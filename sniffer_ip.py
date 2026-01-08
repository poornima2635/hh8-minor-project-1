from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    # runs only if pkt has IP layer
    if IP in packet:
        src = packet[IP].src      # source
        dst = packet[IP].dst      # destination

        # default
        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"

        print(f"Source: {src}  -->  Destination: {dst}  | Protocol: {protocol}")

# capture pkts
sniff(prn=process_packet, count=100)