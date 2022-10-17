import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makdirs(log_dir, exists_ok=True) 
logging.basicConfig(
                level=logging.INFO,
                format=logging_str,
                handlers = [
                    logging.StreamHandler(sys.stdout), #to print the msgs n terminal
                    logging.FileHandler(log_filepath)

                ])
logger = logging.getLogger("deepClassifierLogger")