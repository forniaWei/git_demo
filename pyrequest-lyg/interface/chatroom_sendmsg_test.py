import unittest
import requests
import os, sys,json

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class chartroom_sendmsg(unittest.TestCase):
    '''发送消息'''

    def setUp(self):
        self.base_url = "http://gateway-test.lygou.cc/services/v1/chatroom/sendmsg"

    def tearDown(self):
        print(self.result)

    def test_chatroom_sendmsg_userid_not_in(self):
        '''用户不在房间内'''

        headers = {"Content-Type":"application/json","Authorization":"B06465D66459596791A842389ED4C05E8BBED8BC","userid":"282"}
        payload = {
            "thread":"5:30:0",
            "message":"gggg",
            "content_type":1,
            "ext":"{\"roomId\":30,\"username\":\"觉得就到家扭扭捏捏奋发风格刚刚\"}"
        }
        r = requests.post(self.base_url,data=json.dumps(payload),headers=headers)
        self.result = r.json()
        self.assertEqual(self.result["errcode"],1106)

    def test_chatroom_sendmsg_success(self):
        '''发送消息成功'''

        headers = {"Content-Type": "application/json", "Authorization": "debug:lygllabc1234", "userid": "120"}
        payload = {
            "thread": "5:117:0",
            "message": "gggg",
            "content_type": 1,
            "ext": "{\"roomId\":117,\"username\":\"16天天广\"}"
        }
        r = requests.post(self.base_url, data=json.dumps(payload), headers=headers)
        self.result = r.json()
        self.assertEqual(self.result["errcode"], 0)

if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()