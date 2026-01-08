# Network Packet Sniffer

## Project Description
This project is part of my Cybersecurity Internship (Minor Project–1).
The objective of this project is to understand how network packet sniffing works by developing a simple packet sniffer using Python and the Scapy library.

The application captures live network packets and extracts useful information such as source IP address, destination IP address, and the protocol used.
Wireshark is used as a verification and analysis tool.

## Tools Used
- Python
- Scapy (Python library)
- Git & GitHub
- VS Code
- Wireshark

## Work Done(Setup & Environment Configuration)
Focused on setting up the complete development environment and linking the project to GitHub.
- Installed Python for writing the packet sniffer program
- Installed Git for version control
- Installed VS Code as the code editor
- Installed Wireshark for network packet analysis and verification
- Created a GitHub repository named `hh8-minor-project-1`
- Created the project folder locally and opened it in VS Code
- Initialized Git repository in the project folder using: `git init`
- Configured Git username and email
- Linked the local project to GitHub repository
- Verified GitHub–VS Code connection

No coding was done. The focus was on proper environment setup and GitHub integration  so that development and commits could be done smoothly.

## Work Done(Packet Sniffer Implementation)
- Installed and verified the Scapy library
- Fixed Python execution issues on Windows
- Developed a Python-based packet sniffer using Scapy
- Captured live network packets
- Displayed: Source IP address, Destination IP address and Protocol (TCP / UDP / ICMP)
- Successfully ran the program and pushed the code to GitHub

## CSV Logging Feature
- Enhanced the packet sniffer to save captured packet details into a CSV file
- Stored the following information: Source IP, Destination IP and Protocol
- CSV file is generated automatically during runtime
- This allows easy analysis using Excel or similar tools

## Wireshark Analysis
- Used Wireshark to capture live network traffic
- Applied protocol filters such as: tcp and udp
- Expanded packet details to analyze: Internet Protocol (IP) layer and Transmission Control Protocol (TCP) layer
- Wireshark was used to verify and visually analyze packets captured by the Python sniffer

## How to Run the Project
1. Install Python
2. Install required library: pip install scapy
3. Clone the repository
4. Run the packet sniffer: `python sniffer_ip.py`
5. To generate CSV output: `python sniffer_csv.py`


## What I Learned
- Basics of network packet sniffing
- Understanding IP addresses and network protocols
- Using Scapy for packet capture and analysis
- Saving captured data into CSV format
- Using Wireshark for packet verification
- Using Git and GitHub for version control
- Debugging and resolving real-world development issues
