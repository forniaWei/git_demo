import sys, time
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# 定义过去时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()-100000))

# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+10000))



#create data
datas = {
    'rooms':[
        {'title':"河图的房间1234", 'tag':'派单', 'owner':'187', 'caz':'900.0', 'total_water':'63885',
            'total_seconds':'45666', 'pay_uv':'8', 'pay_pv':'678','createdtime':'2018-05-23 11:01:42',
            'updatedtime':'2018-12-10 16:39:44', 'status':'2', 'last_opentime':'2018-12-10 16:40:00',
            'notice_title':"笑嘻嘻", 'notice_content':"房间卡上叫",'welcome':'欢迎', 'template':'1', '`procedure`':'1'}
    ]
}


# Inster table datas
def init_data():
    db = DB()
    for table,data in datas.items():
        for d in data:
            db.insert(table,d)
    db.close()
#    DB().init_data(datas)


if __name__ == '__main__':
    init_data()