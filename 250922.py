gun = 10

def checkpoint(soldiers):
    gun = 20
    gun = gun -soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret (gun, 2)
print("남은 총 : {0}".format(gun))

####################################################33
print("Python", "Java", sep=" , ", end="?")
print("무엇이 더 재미있을까요?")

import sys
print("python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

#시험 성적
scores = {"수학": 0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
for num in range (1, 21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무값이나 입력하세요 : ")
answer = 10
print(type(answer))
print("입력하신 값은 " + answer + "입니다")

####################################################333
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩: 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt","r", encoding="utf8")
print(score_file.readline(), end="") #줄별로 읽기
print(score_file.readline(), end="")
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="tuf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readline() #list 형태로 저장
for line in lines:
    print(line)
score_file.close()