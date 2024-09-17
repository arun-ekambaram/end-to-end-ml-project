
import sys
import logging

#Whenever an exception gets raised I want to push this on my like my own custom message.
#error- whatever message I'm getting.
#error detail -will basically be present inside this sis.
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb= error_detail.exc_info()
    file_name=exc_tb.tb.frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno,str(error))
    
    return error_message 

    class CustomException(Exception):
        def __init__(self,error_message,error_detail:sys):
        # since we are inheriting from the exception.
            super().__init__(error_message)
            self.error_message = error_message_detail(error_message,error_detail=error_detail)

        def __str__(self):
            return self.error_message
        

    # if __name__ == '__main__':

    #     try:
    #         a=1/0
    #     except Exception as e:
    #         logging.info("Divide by Zero")
    #         raise CustomException(e,sys)

    
    