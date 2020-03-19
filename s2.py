import redis

pool = redis.ConnectionPool(host="192.168.1.20",port=6379,password="",max_connections=1000)
conn = redis.Redis(connection_pool=pool)

conn.set("foo",'Bar')

#字典操作
# conn.hset('k4','username','alex')
# conn.hset('k4','age','18')
'''
redis={
    k1:'123',字符串
    k2:[1,2,3,4,3,3], 列表
    k3:{1,2,3,4,5},集合
    k4:{name:123,page:666},字典
    k5:{('alex',60),('eva-j',80)},有序集合
    }


'''
conn.hmset('k6',{'name':'tong','age':19})

val = conn.hget('k4','username')
print(val)
print(conn.hgetall('k6'))
conn.hincrby('k5','age')
print(conn.hget('k5','age'))

#迭代取数据
ret = conn.hscan_iter('k4',count=1)
for item in ret:
    print(item)


#左插入
conn.lpush('k1',11)
conn.rpush('k1',33)
#左获取
val = conn.lpop('k1')
#右获取
val = conn.rpop('k1')
print(val)

val = conn.blpop('k1',timeout=5)
print(val)

conn.lpush('k1',*[11,22,33,44,55])
result = conn.lrange('k1',0,110)
print(result)

def lis_iter(key,count=2):
    index = 0
    while True:
        data_list = conn.lrange('k1',index,index+count-1)
        if not data_list:
            return
        index += count
        for item in data_list:
            yield item

for item in lis_iter('k1',count=3):
    print(item)

#创建事务一次性事务操作，一次发送多个命令
pipe = conn.pipeline(transaction=True)
pipe.multi()
pipe.set('k2','123')
pipe.hset('k3','n1',666)
pipe.lpush('k4','laonanhai')
