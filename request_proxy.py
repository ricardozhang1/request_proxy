#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="1234",db="mysql_test_01",charset='utf8')
cursor = conn.cursor()


class GetIP(object):
    def get_ramdon_ip(self):
        ramdon_sql = """SELECT ip, port FROM text_02 ORDER BY RAND() LIMIT 1"""
        cursor.execute(ramdon_sql)
        results = cursor.fetchall()
        return results


    def judge_ip(self,ip,port):
        http_url = "http://www.baidu.com"
        proxy_url = "https://{0}:{1}".format(ip,port)
        try:
            proxy_dict = {
                'http':proxy_url
            }
            response = requests.get(http_url,proxies=proxy_dict)
        except Exception as e:
            print("Invalid ip and port")
        print(proxy_url)



if __name__ == '__main__':
    get_ip = GetIP()
    ip_port = get_ip.get_ramdon_ip()
    get_ip.judge_ip(ip_port[0][0],ip_port[0][1])
    conn.close()