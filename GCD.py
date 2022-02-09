a = int(input())
b = int(input())

"""
---유클리드 호제법---
2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b)
a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고
다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 
나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
"""
"""
나머지를 구하기때문에 뺄셈을 사용할 수도 있음 (숫자 크기 차이 많이 나면 시간 오래걸림)
반복하기때문에 반복문 사용 할 수도 있고
재귀합수도 가능
"""


# 최대공약수 빼기 ver.
def gcd_min(a, b):
    while a != 0 and b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a + b


# 최대공약수 나머지 ver.
# 기본적인 알고리즘 자체가 결국 나머지를 구하는 방식이기 때문에
# 나머지 연산을 사용해주면 여러번 뺄셈할 필요가 없음 (시간 단축)
def gcd_mod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


# 최대공약수 재귀함수 ver.
def gcd_rec(a, b):
    if a == 0 or b == 0:    # a, b 둘중 하나만 0 이면 최대공약수 나옴
        return a + b        # 리턴값으로 최대공약수 반환
    else:
        if a > b:           # a, b 값을 나머지로 바꿔줌 ( 뭐가 더 큰지 모르므로 경우 나눠 줌 )
            a %= b
        elif b > a:
            b %= a
        else:               # a, b 값이 같으면 최대공약수가 나왔기 때문에 그냥 바로 반환
            return a
    return gcd_rec(a, b)


print(gcd_min(a, b))
print(gcd_mod(a, b))
print(gcd_rec(a, b))