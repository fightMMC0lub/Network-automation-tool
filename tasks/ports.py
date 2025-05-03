import socket
from config import COMMON_PORTS

def scan_ports(host, logger):
    logger.info(f"Scanning ports on {host}...")
    for port in COMMON_PORTS:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            status = "open" if result == 0 else "closed"
            logger.info(f"Port {port}: {status}")

