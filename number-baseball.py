import random

n1 = random.randint(1, 9)
n2 = random.randint(1, 9)
n3 = random.randint(1, 9)
n4 = random.randint(1, 9)
n5 = random.randint(1, 9)

answer = n1, n2, n3, n4 ,n5

for i in range(10):
    num = input("숫자 입력: ")

    d = []
    for j in num:
        d.append(int(j))

    if d[0] == n1:
        print("✅")
    elif d[0] in [n2, n3, n4, n5]:
        print("🆚")
    else:
        print("🅾️")

    if d[1] == n2:
        print("✅")
    elif d[1] in [n1, n3, n4, n5]:
        print("🆚")
    else:
        print("🅾️")

    if d[2] == n3:
        print("✅")
    elif d[2] in [n2, n1, n4, n5]:
        print("🆚")
    else:
        print("🅾️")

    if d[3] == n4:
        print("✅")
    elif d[3] in [n2, n3, n1, n5]:
        print("🆚")
    else:
        print("🅾️")

    if d[4] == n5:
        print("✅")
    elif d[4] in [n2, n3, n4, n1]:
        print("🆚")
    else:
        print("🅾️")

    if d == list(answer):
        print("성공!")
        print("정답: {}, 시도 횟수: {}".format(answer, i))
        exit()

print(f"에휴 한심하다 저게 {answer} 인걸 왜 못 맞추냐")


