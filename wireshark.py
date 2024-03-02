from scapy.all import sniff

def packet_handler(packet):
    print(packet.summary())

def capture_packets():
    print("Capturing packets...")
    sniff(prn=packet_handler, count=10)  # Capture 10 packets

if __name__ == "__main__":
    capture_packets()
