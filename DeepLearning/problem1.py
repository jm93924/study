# 문제1: 단일 퍼셉트론과 기본 논리 게이트 (AND, OR, NOT) 구현
# [배경지식] 퍼셉트론은 입력값(X)과 연결 가중치(w)를 곱하여 합산한 후(weighted sum),
# 활성화 함수(Hard Limit)를 거쳐 출력을 결정합니다.
# Hard limit 함수는 계산된 값(net)이 0보다 크면 1을, 그렇지 않으면 0을 출력합니다.

# [문제] 다음 자료에 명시된 가중치(w) 값을 사용하여 hard_limit 활성화 함수를 정의하고,
# 이를 바탕으로 AND_gate, OR_gate, NOT_gate 함수를 각각 구현하세요.
# AND 연산 가중치 : W1=1.0, W2=1.0, W3=-1.5 
# OR 연산 가중치: W1 = 1.0, W2 = 1.0, W3 = -0.5 
# NOT 연산 가중치 : W1 = -1.0, W2 = 0.5 (입력값 x1 1개) 

# print(f"AND(1,1) = {AND_gate(1,1)}") # 출력:1
# print(f"OR(0,1) = {OR_gate(0,1)}") # 출력:1
# print(f"NOT(1) = {NOT_gate(1)}") # 출력: 0

def hard_limit(w1,w2,w3, x,y):
    net = x*w1 + y*w2 + w3
    if net >= 0:
        return 1
    else:
        return 0
    
def AND_gate(x,y):
    return hard_limit(1.0, 1.0, -1.5, x,y)

def OR_gate(x,y):
    return hard_limit(1.0, 1.0, -0.5, x,y)

def NOT_gate(x):
    return hard_limit(-1.0, 0, 0.5, x,0)


def main():
    while True:
        print("기능을 선택하세요.")
        print("1. AND_gate")
        print("2. OR_gate")
        print("3. NOT_gate")
        print("4. 종료")

        cho = int(input(">>>"))

        if cho==4:
            print("프로그램을 종료합니다.")
            break

        else:
            if cho==1:
                x = int(input("X 입력 : "))
                y = int(input("Y 입력 : "))
                print(f"AND({x},{y}) = {AND_gate(x,y)}")
            elif cho==2:
                x = int(input("X 입력 : "))
                y = int(input("Y 입력 : "))
                print(f"OR({x},{y}) = {OR_gate(x,y)}")
            elif cho==3:
                x = int(input("X 입력 : "))
                print(f"NOT({x}) = {NOT_gate(x)}")

main()

        
