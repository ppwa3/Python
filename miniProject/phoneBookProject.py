#폰북 리스트,연락처를 저장하기 위한 폰북 리스트
phonebook = []
idx = 1
#입력
def add_input():
    name = input('성명>>>')
    phonenum = input('전화번호>>>')
    addr = input('주소>>>')  
    dic = {'idx':idx ,'name':name, 'phonenum':phonenum, 'addr':addr}
    #phonebook이라는 리스트에 dic이라는 하나의 정보를 넣는다.
    #append는 리스트의 맨 뒤에 값을 추가하는 함수
    phonebook.append(dic)
#출력
def output():
    if not phonebook: #연락처가 하나도 없을때
      print("저장된 연락처가 없습니다.")
      return #연락처가 없으면 아래 for문으로 내려가지 않는다 (함수종료)
    #contact는 phonebook리스트 안에 있는 각 딕셔너리 하나를 의미함
    for contact in phonebook:
      print(f"번호: {contact['idx']} ,이름: {contact['name']}, 전화번호:{contact['phonenum']}, 주소:{contact['addr']}")
#검색
def search():
  putname = input("검색할 이름을 입력하세요: ")
  #간접적으로 접근 phonebook에 있는 contact를 복사해서 간접적으로 가져옴
  for contact in phonebook:
    if contact['name'] == putname:
        print(f"번호: {contact['idx']}")
        print(f"이름: {contact['name']}")
        print(f"전화번호:{contact['phonenum']}")
        print(f"주소:{contact['addr']}")
#수정
def update():
  putname = input("수정할 이름을 입력하세요: ")
  #직접적으로 접근
  for i in range(len(phonebook)):
    if phonebook[i]['name'] == putname:
      phonebook[i]['name'] = input('새로운 이름')
      phonebook[i]['phonenum'] = input('새로운 전화번호')
      phonebook[i]['addr'] = input('새로운 주소')
      print("수정이 완료되었습니다.")
#삭제
def delete():
  putname = input("삭제할 이름을 입력하세요: ")
  for contact in phonebook:
    if contact['name'] == putname:
      phonebook.remove(contact)
      print("삭제되었습니다.")
      return
  print("해당정보가 없습니다.")
  
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
    print("프로그램이 종료되었습니다.")
    break


