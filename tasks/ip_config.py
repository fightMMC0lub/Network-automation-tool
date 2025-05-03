import subprocess
import platform

def get_ip_config(logger):
    cmd = "ipconfig" if platform.system() == "Windows" else "ifconfig"
    logger.info("Getting IP configuration...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    logger.info(result.stdout)

