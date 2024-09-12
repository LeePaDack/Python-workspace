'''
for (i = 0; i <= 5, i++) {
    System.out.println(i + 값);   
}

for 변수명 in 배열들 : 
    print(변수명)
'''

과일들 = ["사과", "오렌지", "포도"]

for f in 과일들:
    print(f)

# 배열이 아니라 특정 숫자 사이를 출력해야 할 때

for i in range(1,6): # 1 부터 5 까지 출력  range(1이상,6미만)
    print(i)

# 구구단 출력
print("/////////////////")

# 중첩 for 문
for n in range(1,10):
    for m in range(1,10):
        print(f"{n} * {m} = {n * m}")
    print() # 단 사이 빈줄 추가