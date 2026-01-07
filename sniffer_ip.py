from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_packet(packet):
    # run only if packet has IP layer
    if IP in packet:
        src = packet[IP].src      # source
        dst = packet[IP].dst      # destination

        # default
        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"

        print(f"Source: {src}  -->  Destination: {dst}  | Protocol: {protocol}")

# capture 25 packets
sniff(prn=process_packet, count=25)