import unittest
import requests
import os,sys,json

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data

class chatroom_openboxs(unittest.TestCase):
    '''开宝箱'''
    def setUp(self):
        self.base_url="http://172.16.164.248:9101/api/box/v1/openbox"

    def tearDown(self):
        print(self.result)

    def test_chatroom_openboxs_success(self):
        '''开宝箱成功'''
        headers={"Content-Type":"application/json","userId":"10593398","Auth-Sign":"6601624EEF311C8A71CB5383A5F72297CA39B016","Authorization":"B06465D66459596791A842389ED4C05E8BBED8BC","Auth-Timestamp":"1593572587573"}
        payload={
            "roomID": 670,
            "heyNum": 1,
            "boxType": 1,
        }
        r = requests.post(self.base_url,data=json.dumps(payload),headers=headers)
        self.result = r.json()
        self.assertEqual(self.result["errcode"],0)

if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()