import logging

def setup_logger():
    logger = logging.getLogger("NetworkAutomation")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler("network_automation.log")
    fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(fh)

    return logger

