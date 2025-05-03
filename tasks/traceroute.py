import platform
import subprocess

def run_traceroute(host, logger):
    cmd = "tracert" if platform.system() == "Windows" else "traceroute"
    logger.info(f"Running traceroute on {host}...")
    result = subprocess.run([cmd, host], capture_output=True, text=True)
    logger.info(result.stdout)

