from src.logger import get_logger
from src.custom_exception import CustomException
import sys 

logger = get_logger(__name__)

def divide_number(a, b):
    try:
        result = a/b
        logger.info(f"dividing two numbers: {a}/{b}")
        return result
    except Exception as e:  # Exception is the base class for most built-in exceptions (like ZeroDivisionError, ValueError, etc.).
        logger.error("Error occurred")
        raise CustomException("Custom error zero", sys) # We are not creating any object of our class, still we are able to use our CustomException because of the static method
    
if __name__=="__main__":
        try:
            logger.info("Starting main program")
            divide_number(10, 5)
        except CustomException as ce:
            logger.error(str(ce)) # the str(ce) what it does is that it will create a text representation of the error we get in the terminal and then logger.error will store it in logs file