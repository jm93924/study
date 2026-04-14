'''
    평균절대오차(MAE)와 평균제곱오차(MSE) 수치 평가하기

    인공지능이 모델의 예측 성능을 평가하기 위해 '손실함수'를 사용한다.
    한 카페에서 방문 인원에 따른 매출을 예측하는 모델을 만들고자 수집한 데이터는 다음과 같다.
    
        방문 인원 : 4, 8, 12, 16, 20
        실제 매출 : 6, 5, 16, 12, 20

    A 회사는 y=(9/8)x 모델을, B 회사는 y=(7/8)x 모델을 제안했다.
    두 회사의 예측 모델에 대해 MAE와 MSE를 각각 계산하고 비교하는 파이썬 코드를 작성하시오.

'''


# MAE 구하는 함수
def calc_mean_aboslute_error(predicts, targets):
    sum_aboslute_error = 0
    index = 0
    for predict in predicts:
        sum_aboslute_error += abs(targets[index] - predict)
        index += 1
    return sum_aboslute_error / (len(predicts))

# MSE 구하는 함수
def calc_mean_squared_error(predicts, targets):
    sum_squared_error = 0
    for i in range(len(predicts)):
        squared_error =  targets[i] - predicts[i]
        sum_squared_error += (squared_error)**2
    return sum_squared_error / (len(predicts))

# 선형회귀로 예측한 예측값 반환하는 함수
def leanear_regression(inputs, coefficient, bias=0):
    predicts = []
    for input in inputs:
        predict = input * coefficient + bias
        predicts.append(predict)
    return predicts

def main():
    inputs = [4,8,12,16,20]
    targets = [6,5,16,12,20]

    print("--- 모델 A (y = 9/8x) --- ")
    A_predicts = leanear_regression(inputs, 9/8)
    A_mae = calc_mean_aboslute_error(A_predicts, targets)
    A_mse = calc_mean_squared_error(A_predicts, targets)

    # print(f"predicts : {A_predicts}")

    # A_errors = []
    # for i in range(len(A_predicts)):
    #     error = targets[i] - A_predicts[i]
    #     A_errors.append(error)
    
    # print(f"errors : {A_errors}")

    print(f"MAE : {A_mae:.2f}")
    print(f"MSE : {A_mse:.2f}")
    print()

    print("--- 모델 B (y = 7/8x) --- ")
    B_predicts = leanear_regression(inputs, 7/8)
    B_mae = calc_mean_aboslute_error(B_predicts, targets)
    B_mse = calc_mean_squared_error(B_predicts, targets)

    # print(f"predicts : {B_predicts}")

    # B_errors = []
    # for i in range(len(B_predicts)):
    #     error = targets[i] - B_predicts[i]
    #     B_errors.append(error)
    
    # print(f"errors : {B_errors}")
    
    print(f"MAE : {B_mae:.2f}")
    print(f"MSE : {B_mse:.2f}")
    
main()