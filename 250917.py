cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5]) #cabinet 딕셔너리에는 5라는 key가 존재하지 않기에 오류가 뜨고 hi가 출력되지 않을 것임.
print("hi")

#cabinet.get명령어를 사용하면 없는 key는 없다고 뜰 것임. like
print(cabinet.get(5)) #실행해보면 None이라고 출력됨.

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
#새손님
print(cabinet)
cabinet["A-3"] = "김종국" #유재석이 빠지고 김종국이 들어감
cabinet["C-20"] = "조세호"
print(cabinet)

#################################################
#집합 set
#중복 안됨, 순서 없음
my_set = {1,2,3,3,3} #set는 list와 달리 순서 보장X, 중복 제거
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print (java - python)
print(java.difference(python))

#교육받아서 python할 줄 아는 사람이 늘어남
python.add("김태호")
print (python)

#자바를 까먹은 사람
java.remove("김태호")
print(java)

#자료구조의 변경
#커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu ,type(menu))

############################
weather = input("오늘 날씨는 어때요?") #input명령어는 C프실에서 printf + scanf 동시 수행 명령어 느낌
if weather == "비" or weather == "눈":
    print ("우산을 챙기세요")
elif weather == "미세먼지":
    print ("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

####################################333
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [1, 2, 3, 4]: #[1, 2, 3, 4]라는 리스트 안의 요소를 하나씩 꺼내서 waiting_no에 담음
    print("대기번호 : {0}".format(waiting_no))

for waiting_no2 in [5, 6, 7, 8]:
    for waiting_no in [1, 2, 3, 4]:
        print("대기번호 : {0}, {1}".format(waiting_no, waiting_no2))

for waiting_no in range(5): # 0,1,2,3,4. range(5)는 0부터 5 미만(즉 0~4) 의 숫자들을 순서대로 생성. 즉 [0, 1, 2, 3, 4]와 같은 효과.
    print("대기번호: {0}".format(waiting_no))

for waiting_no in range(1, 6): # 1부터 6미만까지
    print("대기번호: {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks: #스타벅스의 손님을 한명씩 부르는 것
    print("{0}, 커피가 준비되었습니다.".format(customer))

###############################################3
# while. 손님 5번 불러서 안 오면 커피를 버린다.
# customer = "토르"
# index = 5
# while index >= 1:
#    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#    index -= 1
#    if index == 0:
#        print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#    print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
#    index += 1

# customer = "토르"
# person = "unknown"

# while person != customer : #person이 customer와 같을 때까지 반복
#    print("{0}, 커피가 준비되었습니다.".format(customer))
#    person = input("이름이 어떻게 되세요?")   #Ctrl+c하면 무한 루프 꺼짐

######################################################################################
def open_account():
    print("새로운 계좌가 생성되었습니다")

open_account()

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balance))
        return balance
    
def withdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수료 100원
    if balance >= money + commission: # 잔액이 출금 + 수수료보다 많으면
        print("출금이 완료되었습니다. 수수료 {0}원이며, 잔액은 {1}원입니다".format(commission, balance - money - commission))
        return commission, balance - money - commission
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balance))
        return balance
balance = withdraw_night(balance, 500)

#balance = 0 #잔액
#balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
#balance = withdraw_night(balance, 500)

##########################################
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "Jave", "C","C++", "C#", "Javascript")
profile("김태호", 25, "Kotlin", "Swift")