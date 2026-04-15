
    # 단일 변수 모델(y = ax)의 경사하강법을 구현

    # 시작점 a0 = 5, 학습률 r = 0.06, 도함수 L'(a) = 12.5a - 15
    # 기울기의 절댓값이 매우 작아지거나, a의 변화량이 매우 작아지거나,
    # 반복횟수가 1만 회에 도달하면 종료하는 조건도 반영하시오.


def learning(learning_rate, a, coefficient, bias):
    slope = coefficient * a + bias
    new_a = a - slope * learning_rate
    return new_a, slope

def main():
    a = 5
    n = 0
    print("반복(n)\t a_n \t\t L'(a_n) \t a_{n+1}")
    print("-"*50)
    while True:
        new_a,slope = learning(0.06, a, 12.5, -15)

        print(f"{n} \t {a:.6f} \t {slope:.6f} \t {new_a:.6f}")

        if abs(slope) < 0.001:
            print(f"[종료] 접선의 기울기가 0에 수렴했습니다. (반복 횟수 : {n})")
            print(f"최종 최적화된 a 값 : {a:.6f}(이론적 최솟값 1.2에 근접)")
            break
        
        elif abs(new_a - a) < 0.0001:
            print(f"[종료] a의 변화량이 0에 수렴했습니다. (반복 횟수 : {n})")
            print(f"최종 최적화된 a 값 : {a:.6f}")
            break
        
        elif n>=10000:
            print(f"[종료] 반복 횟수가 1만회에 도달했습니다.")
            print(f"최종 a 값 : {a:.6f}")
            break

        a = new_a
        n += 1

main()