''' 주어진 학생 데이터와 초기 신경망 설정값을 이용하여,
    학생의 합격 여부를 예측하고 오차에 따라 가중치를 업데이트하는 프로그램을 작성하세요. 
    
    1. 학생 데이터(입력값 및 실제 결과):
        서윤이의 성적: 국어 90점, 수학 60점, 영어 80점, 과학 80점
        서윤이의 실제 합격 여부: 불합격(0)

    2. 신경망 초기 설정값:
        초기 가중치: 국어(w1)=0.1, 수학(w2)=0.2, 영어(w3) = 0.3, 과학(w4) = 0.1
        초기 편향(b): -20
        학습률(Learning Rate): 0.005

    3. 구현해야 할 기능:
        예측 과정 : (각 과목 점수 x 해당 가중치)의 총합 + 편향을 계산.
        이 값이 0보다 크면 1(합격)을, 그렇지 않으면 0(불합격)을 반환하는 계단 함수를 구현.

        오차 계산 : 실제 결과 - 예측 결과 공식을 통해 오차를 산출.

        업데이트 과정: 계산된 오차를 바탕으로 다음 공식을 사용하여
        4과목의 가중치와 편향을 새롭게 업데이트하고 출력.
        새로운 가중치 = 기존 가중치 + (학습률 x 오차 x 해당 입력값)
        새로운 편향 = 기존 편향 + (학습률 x 오차 x 1) 

'''

# 액티베이션 함수
def activation_func(w1, w2, w3, w4, b, kor, mat, eng, sci):
    net = w1*kor + w2*mat + w3*eng + w4*sci + b
    if net >= 0:
        return 1
    else:
        return 0
    
# 에러값을 구하는 함수
def error_calc(predict, target):
    return (target - predict)

# 액티베이션 함수를 업데이트하는 함수
def update_activation_func(w1,w2,w3,w4,b, kor, mat, eng, sci, learning_rate, predict, target):
    error = error_calc(predict, target)
    new_w1 = w1 + (learning_rate * error * kor)
    new_w2 = w2 + (learning_rate * error * mat)
    new_w3 = w3 + (learning_rate * error * eng)
    new_w4 = w4 + (learning_rate * error * sci)
    new_b = b + (learning_rate * error * 1)
    
    return (new_w1, new_w2, new_w3, new_w4, new_b)


def main():
    print("서윤이의 성적 입력")
    kor = int(input("국어 : "))
    mat = int(input("수학 : "))
    eng = int(input("영어 : "))
    sci = int(input("과학 : "))
    target = int(input("서윤이의 실제 합격 여부 : "))

    print("성적 입력 완료")
    print("===================")
    print("신경망 초기 설정값 입력 : ")
    w1 = float(input("w1(국어) : "))
    w2 = float(input("w2(수학) : "))
    w3 = float(input("w3(영어) : "))
    w4 = float(input("w4(과학) : "))
    b = float(input("초기 편향(b) : "))
    learning_rate = float(input("학습률(Learning Rate) : "))

    print("==================")
    predict = activation_func(w1, w2, w3, w4, b, kor, mat, eng, sci)
    print(f'초기 예측 결과 : {predict}')
    print(f"실제 결과 : {target}")
    print(f"발생한 오차 : {error_calc(predict,target)}")
    print('--- 가중치 및 편향 업데이트 ---')
    new_weight = update_activation_func(w1,w2,w3,w4,b, kor, mat, eng, sci, learning_rate, predict, target)
    print(f"업데이트된 국어 가중치 : {new_weight[0]}")
    print(f"업데이트된 수학 가중치 : {new_weight[1]:.2f}")
    print(f"업데이트된 영어 가중치 : {new_weight[2]:.2f}")
    print(f"업데이트된 과학 가중치 : {new_weight[3]:.2f}")
    print(f"업데이트된 편향 : {new_weight[4]:.3f}")
    

main()