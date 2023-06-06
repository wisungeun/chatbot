import pandas as pd
import time

def calc_distance(a,b):
    if a == b: return 0
    a_len = len(a)
    b_len = len(b)
    if a == "": return b_len
    if b == "": return a_len
    
    matrix = [[] for i in range(a_len+1)]
    for i in range(a_len+1):
        matrix[i] = [0 for j in range(b_len+1)]
    
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
        
    for i in range(1, a_len+1):
        ac = a[i-1]
        for j in range(1, b_len+1):
            bc = b[j-1]
            cost = 0 if (ac == bc) else 1
            matrix[i][j] = min([
                matrix[i-1][j] + 1,
                matrix[i][j-1] + 1,
                matrix[i-1][j-1] + cost
                ])
        
    
    return matrix[a_len][b_len]
    

def load_data(filepath):
    data = pd.read_csv(filepath)
    questions1 = data['Q'].tolist()
    answers1 = data['A'].tolist()
    return questions1, answers1

    


# CSV 파일 경로
filepath = 'C:\Coding\Python\chatbot\chatbot\ChatbotData.csv'

questions, answers = load_data(filepath)

q_len = len(questions)
q_r = []

while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    for i in range(q_len):
        r = calc_distance(input_sentence, questions[i])
        q_r.append(r)
    
    r = q_r.index(min(q_r))
    print(answers[r])
    q_r = []
    