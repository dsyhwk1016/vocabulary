with open('vocabulary.txt', 'r') as f:
    for line in f:
        voca = line.strip().split(': ')
        guess = input('{}: '.format(voca[0]))
        if guess == voca[1]:
            print('맞았습니다!\n')
        else:
            print('아쉽습니다. 정답은 {}입니다.\n'.format(voca[1]))
