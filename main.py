from tasks import ping, ports, ip_config, traceroute
from utils.logger import setup_logger

logger = setup_logger()

if __name__ == "__main__":
    host = "8.8.8.8"
    logger.info("Starting network automation tasks...")

    ping.ping_host(host, logger)
    ports.scan_ports(host, logger)
    ip_config.get_ip_config(logger)
    traceroute.run_traceroute(host, logger)

    logger.info("Tasks completed.")

