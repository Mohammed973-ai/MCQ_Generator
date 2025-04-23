import logging
import os
from datetime import datetime

# Generate log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Log directory
LOG_FILEPATH = os.path.join(os.getcwd(), "logs")

# Ensure the log directory exists
os.makedirs(LOG_FILEPATH, exist_ok=True)

# Full path to the log file
LOG_FILE_FULL_PATH = os.path.join(LOG_FILEPATH, LOG_FILE)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE_FULL_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)