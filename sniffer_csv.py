from scapy.all import sniff, IP, TCP, UDP
import csv

file = open("captured_packet.csv", mode="w", newline="")
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

        print(f"{src} --> {dst} | {protocol}")

        writer.writerow([src, dst, protocol])

sniff(prn=process_packet, count=100)