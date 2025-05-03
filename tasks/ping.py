import platform
import subprocess

def ping_host(host, logger):
    command = ["ping", "-n" if platform.system() == "Windows" else "-c", "4", host]
    logger.info(f"Pinging {host}...")
    result = subprocess.run(command, capture_output=True, text=True)
    logger.info(result.stdout)

