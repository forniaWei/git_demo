import unittest
import requests
import os, sys,json
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class chartroom_quit(unittest.TestCase):
    ''' 退出房间 '''

    def setUp(self):
        self.base_url = "http://gateway-test.lygou.cc/services/v1/chatroom/quit"

    def tearDown(self):
        print(self.result)

    def test_chartroom_room_id_success(self):
        ''' 退出房间成功 '''
        headers = {"Content-Type":"application/json","Authorization":"B06465D66459596791A842389ED4C05E8BBED8BC","userid":"282",
                   "Client-Info": "(LYG; id/1003 v/3.0.5 realVer/3.0.2 f/009 uuid/443A085FFF78AD40753AEE8FFACFBDBD uuid2/866778035232325354514945543245bdc82ecffcf7ceab02:00:00:00:00:0002:00:00:00:00:00 uuid1/78cf4868-2a85-4510-aecc-5fe73100e7f2 sensorsId/bdc82ecffcf7ceab mac/02:00:00:00:00:00 aid/bdc82ecffcf7ceab b/76AF4C71F765BABA res/11D23CA0559F0A46F1538E5BEADB467A lt/1553250115 os/Android osv/27 net/WIFI tz/28800 region/zh-CN p/2 car/FC360B72BAF185BCF68D784D58F2231F vc/117 uid/173 t/24913c8f13e0ababb7b190ea5e3c161f)"}
        payload = {'room_id':33}
        Response = requests.post(self.base_url, data=json.dumps(payload),headers=headers)
        self.result = Response.json()
        self.assertEqual(self.result['errcode'], 0)

    def test_chartroom_room_id_null(self):
        ''' room_id为空 '''
        headers = {"Content-Type":"application/json","Authorization":"debug:lygllabc1234","userid":"282",
                   "Client-Info": "(LYG; id/1003 v/3.0.5 realVer/3.0.2 f/009 uuid/443A085FFF78AD40753AEE8FFACFBDBD uuid2/866778035232325354514945543245bdc82ecffcf7ceab02:00:00:00:00:0002:00:00:00:00:00 uuid1/78cf4868-2a85-4510-aecc-5fe73100e7f2 sensorsId/bdc82ecffcf7ceab mac/02:00:00:00:00:00 aid/bdc82ecffcf7ceab b/76AF4C71F765BABA res/11D23CA0559F0A46F1538E5BEADB467A lt/1553250115 os/Android osv/27 net/WIFI tz/28800 region/zh-CN p/2 car/FC360B72BAF185BCF68D784D58F2231F vc/117 uid/173 t/24913c8f13e0ababb7b190ea5e3c161f)"}
        payload = {'room_id':''}
        r = requests.post(self.base_url, data=json.dumps(payload),headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['errcode'], 400)

    def test_chartroom_room_id_error(self):
        ''' room_id错误 '''
        headers = {"Content-Type": "application/json", "Authorization": "debug:lygllabc1234", "userid": "282",
                   "Client-Info": "(LYG; id/1003 v/3.0.5 realVer/3.0.2 f/009 uuid/443A085FFF78AD40753AEE8FFACFBDBD uuid2/866778035232325354514945543245bdc82ecffcf7ceab02:00:00:00:00:0002:00:00:00:00:00 uuid1/78cf4868-2a85-4510-aecc-5fe73100e7f2 sensorsId/bdc82ecffcf7ceab mac/02:00:00:00:00:00 aid/bdc82ecffcf7ceab b/76AF4C71F765BABA res/11D23CA0559F0A46F1538E5BEADB467A lt/1553250115 os/Android osv/27 net/WIFI tz/28800 region/zh-CN p/2 car/FC360B72BAF185BCF68D784D58F2231F vc/117 uid/173 t/24913c8f13e0ababb7b190ea5e3c161f)"}
        payload = {'room_id': ''}
        Response = requests.post(self.base_url, data=json.dumps(payload),headers=headers)
        self.result = Response.json()
        self.assertEqual(self.result['errcode'], 400)
        self.assertIn('参数错误', self.result['errmsg'])


if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
