class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def get_msg(self):
        return self.msg
    
# 在这里可以定义其他异常处理程序