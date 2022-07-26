import logging
import sys


def setup_logging():
    logging.basicConfig(
        stream=sys.stdout, level=logging.INFO,
        format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
    )
