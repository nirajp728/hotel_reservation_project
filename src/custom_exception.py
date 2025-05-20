# Trace backing system library
import traceback
import sys

class CustomException(Exception):
    # we are inheriting from exception class because we need exceptions that are pre defined
    def  __init__(self, error_message, error_detail:sys):
        # error_detail:sys means error_details will belong to sys library
        super().__init__(error_message) # we are accessing the parent class by super() method, if the error message exists in the parent class then we will show that error message or else we will show our custom error
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod # we dont need to create custom exception class again nd again to show our custom exception, with the help of @staticmethod our functions and our methods become independent of class creation, we dont need to create our custom exception class again nd again to show our custom error messages
    def get_detailed_error_message(error_message, error_detail:sys):

        _, _, exc_tb = traceback.sys.exc_info() # The exc_info() returns three things out which we want the last one that is traceback
        file_name = exc_tb.tb_frame.f_code.co_filename  # This will give the filename in which our error occurred
        line_number = exc_tb.tb_lineno # This will give in which line the error occured

        return f"Error occurred in {file_name}, line {line_number} : {error_message}"
        
    def __str__(self):   #The __str__ returns text representation of error message      
        return self.error_message