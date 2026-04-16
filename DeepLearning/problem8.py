'''
    3*3 크기의 흑백 이미지 행렬 A와 2*2 크기의 필터 행렬 F가 있다.
    필터를 이미지의 왼쪽 위에서부터 오른쪽, 그리고 아래로 한 칸씩 슬라이딩하면서
    겹치는 위치의 값들을 각각 곱하고 더하여, 최종적으로 2*2 크기의
    합성곱 결과 행렬을 출력하는 파이썬 코드를 작성하시오.

    [입력 데이터]
    이미지 행렬 A : 10  35  15
                   15  30  10
                   10  20   5

    필터 행렬 F : 1  -2
                 0  2

    [기대되는 출력]
    : 다음과 같은 행렬 형태(리스트)가 출력되어야 한다. [,[-5,20]]
'''

# 가변크기로 고려하여 작성
def dot_product(image_matrix, filter_matrix, strides=1):
    # 가변크기 행렬을 받았을 때, 각 x,y 길이를 구한다
    image_x_length = len(image_matrix[0])
    image_y_length = int(len(image_matrix)+1 / image_x_length)

    # 필터(커널)의 너비
    filter_x_length = len(filter_matrix[0])
    # 커널의 높이
    filter_y_length = int(len(filter_matrix)+1 / filter_x_length)

    # 합성곱의 최종 결과를 담을 행렬(특성맵)
    ls = []

    # 필터가 이동하는것으로 생각하고, 기준이 되는 커서(왼쪽위)를 설정
    x_cursor = 0
    y_cursor = 0

    while True:
        # 커서의 y좌표가 범위를 벗어나면 반복문(계산) 종료
        if y_cursor > image_y_length - filter_y_length:
            break

        # 커서의 x좌표가 초기화되면 결과 행렬의 행을 추가
        if x_cursor == 0:
            ls.append([])
        
        # 합성곱에서 1개의 출력을 나타내는 sum
        sum = 0

        # 필터의 y길이만큼 반복
        for i in range(filter_y_length):
            # 필터의 x길이만큼 반복
            for j in range(filter_x_length):                
                # 필터가 이동한 만큼 i,j좌표(이미지 행렬에서 곱해지는 위치) 보정
                sum += image_matrix[i+y_cursor][j+x_cursor] * filter_matrix[i][j]
        
        # 결과 행렬의 현재 행에 추가
        ls[y_cursor].append(sum)

        # 커서의 x위치 증가
        x_cursor += strides

        # 커서의 x위치가 범위를 벗어나면
        if x_cursor > image_x_length - filter_x_length:
            # x커서를 0으로 초기화
            x_cursor = 0
            # y커서를 증가
            y_cursor += strides
    
    # 활성화함수 통과했다고 가정
    # 최종 특성맵 리턴
    return ls

def main():
    A = [
        [10,35,15],
        [15,30,10],
        [10,20,5]
    ]
    F = [
        [1,-2],
        [0,2]
    ]
    
    result = dot_product(A,F,1)
    print(f"합성곱 결과 : {result}")

main()
        
        

        
