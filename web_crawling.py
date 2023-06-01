# 아래 모듈은 외장 라이브러리이므로, 별도설치 필요
# 설치를 할때, pip라는 패키지tool을 이용 (python 설치시 동시에 설치됨)
# pip install requests
# 만약 pip --version 했을 때 버전정보가 잘 안나온다면,
# path가 문제인데, path를 다시잡기 보다는 python삭제 후 재 설치시 add path옵션추가
# import requests
# from bs4 import BeautifulSoup

# url = 'https://ko.wikipedia.org/wiki/%EC%95%84%EB%B0%94%ED%83%80:_%EB%AC%BC%EC%9D%98_%EA%B8%B8'

# # 웹으로 주고받는 통신 프로토콜(약속)을 http통신이라 한다.
# # http 통신을 하기 위해서는 http통신 규격에 맞게 request를 서버로 전달해야 한다.
# # request는 header와 body로 이루어져있다.
# # 마찬가지로 응답(response)도 header와 body로 이루어져있다.
# header = {'User-Agent' : 'Mozilla/5.0'}
# response = requests.get(url, headers = header)
# html_response = BeautifulSoup(response.text, 'html.parser')
# for sup in html_response.find_all('sup'):
#     sup.decompose()
# # 감독정보, 제작비 정보
# # tag정보를 가지고 html_response에서 원하는 정보 추출
# director_info = html_response.select_one('table.infobox > tbody > tr:nth-of-type(3) > td').get_text()
# budget_info = html_response.select_one('table.infobox > tbody > tr:nth-of-type(16) > td').get_text()
# print(director_info)
# print(budget_info)
# print(f"아바타의 감독은{director_info}이고 제작비는{budget_info}이다")

# # 코인 시세정보 API url
# import json
# url = "https://api.binance.com/api/v3/ticker/24hr"
# response= requests.get(url)
# data_json = json.loads(response.text)
# print(data_json)

# # 출력 결과
# # "symbol" : "BTCUSDT", lastPrice : xxxx(가격)
# for a in data_json:
#     if a['symbol'] == "BTCUSDT":
#         print(f"{a['symbol']}코인의 price는 {a['lastPrice']}입니다.")

# csv 파일 parsing
import seaborn
from matplotlib import pyplot
import pandas

file_path = r'C:\Users\user\Desktop\하진석_project\tips.csv'
csv_data = pandas.read_csv(file_path)

# 성별에 따라 tip이 어떻게 달라지는지.
# day에 따라 tip이 어떻게 달라지는지.
# agg : 집계함수, mean : 평균, std:표준편차
tip_by_gender = csv_data.groupby('gender')['tip'].agg(['mean','std']).reset_index()
# tip_by_day = csv_data.groupby('day')['tip'].agg(['mean','std']).reset_index()

seaborn.barplot(x = 'gender', y= 'mean', data = tip_by_gender, yerr= tip_by_gender['mean'],capsize = 0.1)
seaborn.despine() # 테두리 없애주는 함수
pyplot.title('average tip per gender')
pyplot.xlabel('gender')
pyplot.ylabel('average tip')
pyplot.show()


