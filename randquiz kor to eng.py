import random

voca = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(': ')
        voca[data[0]] = data[1]
    
    while True:
        rand = random.randint(0, len(voca)-1)
        eng = list(voca.keys())[rand]
        kor = voca[eng]
        guess = input(f'{kor}: ')
        if guess == 'q':
            break
        elif guess == eng:
            print('맞았습니다!\n')
        else:
            print(f'틀렸습니다. 정답은 {eng}입니다.\n')
