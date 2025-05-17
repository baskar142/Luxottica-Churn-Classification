import os
import sys
import logging

# Define log format
LOGGING_FORMAT = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Log directory and file path
LOG_DIR = "logs"
LOG_FILEPATH = os.path.join(LOG_DIR, "running_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)

# Initialize logger only if not already configured
logger_name = "mlProjectLogger"
logger = logging.getLogger(logger_name)

if not logger.hasHandlers():
    # Configure logger
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(LOGGING_FORMAT)

    # File handler
    file_handler = logging.FileHandler(LOG_FILEPATH)
    file_handler.setFormatter(formatter)

    # Stream handler (console)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

# Usage example:
# logger.info("This is an info message")
