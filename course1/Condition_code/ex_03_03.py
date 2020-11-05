score = input('Enter your score: ')
new_score = float(score)

if new_score >=1.0 or new_score <=0.0:
    print('Error')
elif new_score >= 0.9:
    print('A')
elif new_score >= 0.8:
    print('B')
elif new_score >= 0.7:
    print('C')
elif new_score >=0.6:
    print('D')
else:
    print('F')
