import requests

from cookiespool.db import RedisClient

conn = RedisClient('accounts', 'weibo')

def scan():
    print('正在导入文件中的账号到redis...')
    with open('account/zhanghao.txt') as r:
        for account in r.readlines():
            username, password = account.split('----')
            result = conn.set(username, password)
    print('导入完成...')

if __name__ == '__main__':
    scan()