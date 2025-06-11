import pymysql
conn = pymysql.connect(host='localhost', user='sample_user',
                port=3306, password='1234', db='sample_db', charset='utf8')
curs = conn.cursor()
#입력
def add_input():
  sql = f""" INSERT INTO phonebooks (name, phonenum, addr)
      VALUES ('{input('성명:')}', '{input('전화:')}', '{input('주소:')}')"""
  try:
    curs.execute(sql)
    conn.commit()
    print("1개의 레코드가 입력됨")
  except Exception as e:
    conn.rollback()
    print("쿼리 실행시 오류발생", e)
#출력
def output():
  try:
      sql = "SELECT * FROM phonebooks"
      curs.execute(sql)
      
      rows = curs.fetchall()
      print('단순인출:', rows)

      print(f"{'인출1':-^30}")
      for row in rows:
          print(row)
  except Exception as e:
      print("쿼리 실행시 오류발생", e)
#검색
def search():
  try:
    sql = "select * from phonebooks WHERE name like '%{0}%' ".format(input
    ('검색어입력:'))
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
  except Exception as e:
    print("쿼리 실행시 오류발생", e)
#수정
def update():
  sql = """ update phonebooks
                set name='{1}', phonenum='{2}', addr='{3}'
                where name={0}
  """.format(input('수정할이름:'), input('이름:'), input('전화번호:'), input('주소:'))
  try:
    curs.execute(sql)
    conn.commit()
    print("1개의 레코드가 수정됨")
  except Exception as e:
    conn.rollback()
    print("쿼리 실행시 오류발생", e)
#삭제
def delete():
  sql = f"delete from phonebooks where name='{input("삭제할 이름을 입력하세요.")}'"
  try:
    #curs : DB랑 연결해서 모든 일들을 다 해줌
    curs.execute(sql)
    #conn : 데이터베이스 변경하고 확정해주는것
    conn.commit()
    print("1개의 레코드가 삭제됨")
  except Exception as e:
    #rollback : 최근에 커밋한 지점까지 되돌아간다. 
    conn.rollback()
    print("쿼리 실행시 오류발생", e)

while True:
  print("1.입력")
  print("2.출력")
  print("3.검색")
  print("4.수정")
  print("5.삭제")
  print("6.종료")
  
  choice = int(input("선택:"))
  if choice == 1:
    add_input()
  elif choice == 2:
    output()
  elif choice == 3:
    search()
  elif choice == 4:
    update()
  elif choice == 5:
    delete()
  elif choice == 6:
    #DB 연결 종료
    conn.close()
    print("프로그램이 종료되었습니다.")
    break