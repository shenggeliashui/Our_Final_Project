class Result:
    def __init__(self, code=None, msg=None, data=None):
        self.code = code
        self.msg = msg
        self.data = data

    @staticmethod
    def success(data=None):
        result = Result()
        result.code = "200"
        result.msg = "请求成功"
        result.data = data
        return result

    @staticmethod
    def error(msg="请求失败"):
        result = Result()
        result.code = "500"
        result.msg = msg
        return result

    def to_dict(self):
        return {"code": self.code, "msg": self.msg, "data": self.data}