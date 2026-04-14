'''
    다층 퍼셉트론(MLP)을 활용한 XOR 문제 해결

    문제1에서 만든 노드(AND, OR 연산 등)를 조합하여 XOR 문제를 해결하는 다층 퍼셉트론(MLP)을 구현하세요.
    첫 번째 은닉 노드는 AND(y1), 두 번째 은닉 노드는 OR(y2)의 역할을 하며,
    이 둘의 출력을 세 번째 노드가 받아 최종 XOR 연산 결과를 냅니다.
    세 번째 조합 노드의 가중치는 자료에 따라 다음과 같이 설정하세요.
    w31 = -1.0, w32 = 1.0, w33 = -0.5

    출력 예)
    XOR(0,0) = 0
    XOR(0,1) = 1
    XOR(1,0) = 1
    XOR(1,1) = 0
    입력이 서로 다를때만 1
'''

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

def XOR_gate(x,y):
    A = AND_gate(x,y)
    B = OR_gate(x,y)
    return hard_limit(-1.0, 1.0, -0.5, A, B)

# def XOR_gate(x,y):
#     return AND_gate(NOT_gate(AND_gate(x,y)), OR_gate(x,y))

# 입력(X,Y)   AND     OR      
# (0,0)       (0)     (0)     (NOT(0)) AND (0) = (0)
# (1,0)       (0)     (1)     (NOT(0)) AND (1) = (1)
# (0,1)       (0)     (1)     (NOT(0)) AND (1) = (1)
# (1,1)       (1)     (1)     (NOT(1)) AND (1) = (0)

while True:
    x = int(input("x 입력 : "))
    y = int(input("y 입력 : "))

    print(f"XOR({x},{y}) = {XOR_gate(x,y)}")
