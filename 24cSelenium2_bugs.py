from selenium import webdriver
driver = webdriver.Chrome()

driver.implicitly_wait(5)

url = ' https://music.bugs.co.kr/chart/'
driver.get(url)
html = driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

#파싱한 정보를 저장할 리스트 생성
song_data = []
rank = 1
#셀렉터를 이용해서 반복되는 엘리먼트(차트)를 얻어온다.
songs = soup.select('#CHARTrealtime > table > tbody > tr')
for song in songs:
    #노래제목
    title = song.select('th > p > a')[0].text
    #가수
    singer = song.select('td:nth-child(8) > p > a')[0].text
    #좋아요 갯수
    album = song.select('td:nth-child(9) > a')[0].text
    #크롤링 한 내용을 콘솔에 출력
    print(title, singer, album, sep="|")
    # 파싱한 정보를 리스트에 추가
    song_data.append(['bugs', rank, title, singer, album])
    # 순위는 1씩 증가
    rank += 1
#판다스 모듈 임포트    
import pandas as pd
#데이터프레임으로 변환시 상단에 컬럼명 추가
columns = ['서비스','순위','곡','아티스트','엘범']
pd_data = pd.DataFrame(song_data, columns=columns)
#데이터프레임의 상위 5개 행을 출력해서 확인
print(pd_data.head())
#엑셀로 저장
pd_data.to_excel('./saveFiles/bugs_chart.xlsx', index=False)