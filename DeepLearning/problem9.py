'''
    1. 아무런 단서가 없을 때, 도로 옆의 아이가 갑자기 도로로 뛰어들 확률(사전확률) = 10%
    2. 실제로 도로로 뛰어든 아이들 중 공을 들고 있었던 비율(가능도)은 80%
    3. 도로로 뛰어들지 않은 아이들 중 공을 들고 있었던 비율은 30%

    아이가 공을 들고 있다는 것을 관측했을 때, 이 아이가 도로로 뛰어들 확률(사후확률)을
    계산하는 함수 calculate_posterior_probability를 작성하시오.
    계산에는 베이즈 정리를 사용해야 한다.
    P(A|B) = {P(B|A) / P(B)} * P(A)
    사후확률   가능도   총확률  사전확률

    입력 매개변수
    prior_prob(float) : 아이가 도로로 뛰어들 사전 확률
    likelihood_jump(float) : 도로로 뛰어든 아이가 공을 들고 있을 확률
    likelihood_not_jump(float) : 도로로 뛰어들지 않은 아이가 공을 들고 있을 확률

    출력 : 아이가 공을 들고 있을 때, 도로로 뛰어들 사후 확률 (소수점 셋째 자리에서 반올림)
'''

def calculate_posterior_probability(prior_prob:float, likelihood_jump:float, likelihood_not_jump:float):
    pb = prior_prob * likelihood_jump + (1-prior_prob) * likelihood_not_jump
    pab = (likelihood_jump / pb) * prior_prob
    return pab

def main():
    result = calculate_posterior_probability(0.1, 0.8, 0.3)
    print(f'아이가 공을 들고 있을 때, 도로로 뛰어들 사후 확률 : {result:.2f}%')

main()