import unittest
import requests
import os,sys,json

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data

class chatroom_vcard(unittest.TestCase):
    '''查看用户卡片'''

    def setUp(self):
        self.base_url = "http://gateway-test.lygou.cc/services/v1/chatroom/vcard?appfrom=999&appver=2.9.9&p_height=1334&p_width=750&platform=1&region=zh-Hans&room_id=30&time_zone=28800&token=b847bfc82210ecd005f3ec5629aec7db&unlogin_token=23f9d12ed29ce5b5166e2627e20485b2&user_id=1998658"

    def tearDown(self):
        print(self.result)

    def test_chatroom_vcard_success(self):
        headers = {"Content-Type":"application/json","Authorization":"B06465D66459596791A842389ED4C05E8BBED8BC","userid":"282"}
        payload = {
            "user_id":'1998658',
            "room_id":'30',
        }
        r = requests.get(self.base_url,data=json.dumps(payload),headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['errcode'],0)

if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main() #运行当前测试文件下的所有用例