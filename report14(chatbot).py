import pandas as pd


def calc_distance(a,b): #레벤슈타인 거리 계산
    if a == b: return 0 #같으면 0 반환
    a_len = len(a) # a길이
    b_len = len(b) # b길이
    if a == "": return b_len #a문자가 없으면 b길이 반환
    if b == "": return a_len #b문자가 없으면 a길이 반화
    
    matrix = [[] for i in range(a_len+1)] #리스트 컴프리헨션을 사용하여 1차원 초기화
    for i in range(a_len+1): #0으로 초기화
        matrix[i] = [0 for j in range(b_len+1)] # 리스트 컴프리헨션을 사용하여 2차원 초기화
    #0일 때 초깃값 설정
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
    #레벤슈타인 거리 계산 실행    
    for i in range(1, a_len+1):
        ac = a[i-1] #a 문자 반복
        for j in range(1, b_len+1):
            bc = b[j-1] #b 문자 반복
            cost = 0 if (ac == bc) else 1
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # 문자 제거: 위쪽에서 +1
                matrix[i][j-1] + 1,     # 문자 삽입: 왼쪽 수에서 +1   
                matrix[i-1][j-1] + cost # 문자 변경: 대각선에서 +1, 문자가 동일하면 대각선 숫자 복사
                ])
        
    
    return matrix[a_len][b_len] #최종값 반환
    

def load_data(filepath): #chatbotdata 불러오기
    data = pd.read_csv(filepath) #csv file 불러오기
    questions1 = data['Q'].tolist() # 질문열만 뽑아 파이썬 리스트로 저장
    answers1 = data['A'].tolist() # 답변열만 뽑아 파이썬 리스트로 저장
    return questions1, answers1 #질문,답변 리스트 반환

    


# CSV 파일 경로
filepath = 'C:\Coding\Python\chatbot\chatbot\ChatbotData.csv'

#질문, 답변 리스트 저장
questions, answers = load_data(filepath)

#질문 갯수 저장
q_len = len(questions)
#레벤슈타인 거리 계산값 저장할 리스트 생성
q_r = []

#챗봇 시작
while True:
    input_sentence = input('You: ') #질문 입력하기
    if input_sentence.lower() == '종료': #종료 입력되면 챗봇 종료
        break
    for i in range(q_len): #chatbotdata에 있는 모든 질문 레벤슈타인 거리 계산
        r = calc_distance(input_sentence, questions[i])
        q_r.append(r) #계산된 레벤슈타인 거리 저장
    
    r = q_r.index(min(q_r)) #레벤슈타인 저장된 값 중 최솟값 인덱스 반환
    print(answers[r]) #가장 비슷한 질문의 답변 결과 출력
    q_r = [] #레벤슈타인 거리 계산값 초기화
    