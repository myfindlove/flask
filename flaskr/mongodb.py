import pymongo

"""
User 数据库设计

userInfo = {
    "userName":"admin",
    "password":"123",
    "phoneNumbe":"",
    "sex":0,
}

"""


class MongoManger:
    mclient = None

    @classmethod
    def client_mongodb(cls):
        cls.mclient = pymongo.MongoClient(host='localhost')

    @classmethod
    def insert_one(cls, params):
        """
        插入单调数据
        0为插入失败
        1为插入成功
        :return:
        """
        db = cls.mclient['userInfo']
        clo = db['user_info']
        if not db:
            return 0
        else:
            clo.insert_one(params)
        return 1

    # @classmethod
    # def find_one(cls, params):
