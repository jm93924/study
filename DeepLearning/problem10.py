'''
    Vanilla RNN의 순전파(Forward Propagation) 알고리즘 구현

    네트워크 파라미터인 가중치 U, V, W를 사용하여 두 수식을 코드로 구현하세요.
      1. 은닉 상태(Hidden State) 계산: ht = f(Uxt + Wht-1)
      2. 출력값(Output) 계산: ot = g(Vht)

    변수 및 파라미터 조건
      xt: t 시점의 입력 데이터(Input)
      ht: t 시점의 은닉 상태(Hidden state)
      ot: t 시점의 출력값(Output)
      f, g 활성화 함수 (Activation function. g는 출력층용)

    제한사항 및 요구사항
      1. 입력 데이터는 x1, x2, x3, x4, x5까지 총 5개의 타임스텝(Time step)으로 들어옵니다.
      2. 데이터가 (x1, y1)부터 순서대로 훈련되거나 입력될 때, 반복문(예: for 루프) 또는 재귀적 호출(recursive call)을
         사용하여 코드를 작성하세요.
      3. 각 시점(t=1~5)마다 은닉 상태(h1 ~ h5)가 이전 상태의 영향을 받아 순차적으로 갱신되며, 그에 따른 출력값
         (o1 ~ o5)이 결과 리스트에 차례대로 저장되도록 구현해야 합니다.
      4. (주의 : 소스 자료에는 h0 값에 대한 구체적인 명시가 없으나, 코드 구현을 위해 맨 처음 들어가는 이전 은닉
         상태값 h0은 0(zero)으로 초기화 되어있다고 가정하세요. 이는 원활한 프로그래밍을 위해 추가된 외부 조건입니다.)
'''
from math import exp as e

def activation_function_f(x):
    return (e(x) - e(-x)) / (e(x) + e(-x))

def activation_function_g(x):
    return 1 / (1 + e(-x))


xt_ls = []
ht_ls = []
ot_ls = []
U = 0.2
W = 0.3
V = 0.4


def hidden_state(t):
    if t==0:
        return 0
    else:
        return activation_function_f(U * xt_ls[t-1] + W * hidden_state(t-1))  # 불필요하게 반복됨. 개선 필요
    
def output(ht):
    return activation_function_g(V * ht)

def xt_input(t):
    for i in range(t):
        xt = int(input(f'x{i+1} 입력 : '))
        xt_ls.append(xt)

def sequential_data_structure(time_step):
    for i in range(time_step):
        ht = hidden_state(i+1)
        ot = output(ht)

        ht_ls.append(ht)
        ot_ls.append(ot)

def result_print(time_step):
    for i in range(time_step):
        print(f'타임스텝 t = {i+1}')
        print(f'입력 x{i+1} = {xt_ls[i]}')
        print(f'은닉상태 h{i+1} = {ht_ls[i]}')
        print(f'출력값 o{i+1} = {ot_ls[i]}')
        print()


def main():
    time_step = int(input('타임 스템프 설정 : '))
    xt_input(time_step)
    sequential_data_structure(time_step)
    result_print(time_step)

if __name__ == '__main__':
    main()