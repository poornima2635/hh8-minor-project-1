from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_pkt(pkt):
    # run only if pkt has IP layer
    if IP in pkt:
        src = pkt[IP].src      # source
        dst = pkt[IP].dst      # destination

        # default
        protocol = "OTHER"

        if TCP in pkt:
            protocol = "TCP"
        elif UDP in pkt:
            protocol = "UDP"
        elif ICMP in pkt:
            protocol = "ICMP"

        print(f"Source: {src}  -->  Destination: {dst}  | Protocol: {protocol}")

# capture pkts
sniff(prn=process_pkt, count=100)