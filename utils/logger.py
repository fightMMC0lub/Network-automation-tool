import logging

def setup_logger():
    logger = logging.getLogger("NetworkAutomation")
    logger.setLevel(logging.INFO)

    # File Handler
    fh = logging.FileHandler("network_automation.log")
    fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(fh)

    # Console Handler 👇👇
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(ch)

    return logger
