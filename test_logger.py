from src.logger import get_logger

logger = get_logger(__name__)
# The __name__ it means create a logger named after the module it's used in

logger.info("Hello")
logger.info("MAD")