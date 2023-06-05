
# # pip install mysql-connector-python
# # mysql, 파이썬 연동 라이브러리
# import mysql.connector
# try:
#     connector = mysql.connector.connect(
#         host = "localhost", 
#         port="3306", 
#         user = "root", 
#         password = "1234", 
#         database = "board")
# except mysql.connector.Error as err:
#     print(err)
# # 커서 객체는 데이터베이스에서 쿼리의 결과를
# # 검색하고 순회하는데 사용되는 객체
# cursor = connector.cursor()
# add_data = "INSERT INTO author (name, email) VALUES(%s, %s)"
# data = ("John", "hello2@naver.com")

# try:
#     cursor.execute(add_data,data)
#     connector.commit()
# except mysql.connector.Error as err:
#     print(err)
# cursor.close()
# connector.close()
# # 코인시세 10초에 한번씩 db insert
# import time
# while True:
#     print("hello world")
#     time.sleep(10)

import time
import json
import requests
import mysql.connector
while True:
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data_json = json.loads(response.text)
    for a in data_json:
        if a['symbol'] == "BTCUSDT":
            try:
                connector = mysql.connector.connect(host="localhost", port="3306", user="root", password="1234", database="practice")
                cursor = connector.cursor()
            except mysql.connector.Error as err:
                print(err)
            add_data = "INSERT INTO coin_price (coin_name, last_price) VALUES(%s, %s)"
            data = ("BTCUSDT", a['lastPrice'])
            try:
                cursor.execute(add_data, data)
                connector.commit()
            except mysql.connector.Error as err:
                print(err)
            cursor.close()
            connector.close()
    time.sleep(10)
