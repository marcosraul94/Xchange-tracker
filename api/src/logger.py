import logging
from src.constants import log_level

logging.basicConfig(
    level=log_level,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


logger = logging.getLogger()
