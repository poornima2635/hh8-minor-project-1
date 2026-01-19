from scapy.all import sniff, IP, TCP, UDP, ICMP
import csv

with open("captured_packet.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Source IP", "Destination IP", "Protocol"])

    def process_packet(packet):
        if IP in packet:
            src = packet[IP].src
            dst = packet[IP].dst

            protocol = "OTHER"
            if TCP in packet:
                protocol = "TCP"
            elif UDP in packet:
                protocol = "UDP"
            elif UDP in packet:
                protocol = "ICMP"

            writer.writerow([src, dst, protocol])
            print(f"{src} -> {dst} | {protocol}")

    sniff(prn=process_packet, count=100)
