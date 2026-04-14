'''
    경사 하강법(Gradient Descent) 가중치 업데이트 식 구현
    
    경사 하강법의 가중치 업데이트를 수행하는 함수를 파이썬 코드로 구현하세요.
    현재 가중치(w_t), 학습률(learning_rate), 그리고 계산된 기울기(gradient)가 매개변수로 주어졌을 때,
    1회 업데이트된 새로운 가중치를 반환해야 합니다.
     
    current_w = 0.5
    eta = 0.01 # 학습률
    grad = 2.0 # 임의로 계산된 기울기
    ---> 업데이트된 가중치: 0.48

    '''

def update_weight(current_w, eta, grad):
    new_w = current_w - (eta * grad)
    return new_w
