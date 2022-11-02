# 생성자가 없는 숫자를 셀프 넘버라고 한다.
numbers = set(range(1, 10001)) # 숫자 전체
number2 = set()
for i in range(1, 10001): # 850
    for j in str(i): # 8 5 0
        i = i+int(j) # 850+8+5+0 
    number2.add(i)
self_number = sorted(numbers - number2)
for i in self_number:
    print(i)