import math

EXP = math.e

# 시그모이드 함수
def sigmoid(z):
    return 1/(1+EXP**(-z))

# 시그모이드 미분값
def sigmoid_derivative(z):
    return sigmoid(z) * (1-(sigmoid(z)))

# relu 함수
def relu(z):
    if z>0:
        return 1.0
    else:
        return 0

# 미분값들을 모두 곱하는 함수    
def calculate_accumulated_gradient(gradients):
    result = 1
    for gradient in gradients:
        result *= gradient
    return result


def main():
    print("--- 1. 시그모이드 도함수의 최대값 확인 ---")
    print(f"z=0 일 때 시그모이드의 미분값 : {sigmoid_derivative(0)}")

    print()
    print("--- 2. 기울기 소실(Gradient Vanishing) 시뮬레이션 --- ")
    gradients = [0.25, 0.2, 0.1, 0.15, 0.3] # 은닉층이 5개인 신경망을 가정

    print(f"각 층의 미분값 : {gradients}")
    print(f"-> 시그모이드 누적 기울기 연쇄 곱셈 결과 : {calculate_accumulated_gradient(gradients):.6f}")
    print("(결과값이 0에 매우 가까워져 앞쪽 층의 가중치가 업데이트되지 않음)")
    print()
    print("--- 3. ReLU 함수를 적용한 경우 ---")
    ReLU = []
    for gradient in gradients:
        b = relu(gradient)
        ReLU.append(b)
    print(f"각 층의 미분값 (양수 영역): {ReLU}")
    print(f"-> ReLU 누적 기울기 연쇄 곱셈 결과 : {calculate_accumulated_gradient(ReLU):.6f}")

main()