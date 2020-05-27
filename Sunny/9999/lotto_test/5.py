import random 

first_prize_lotto = random.sample(range(1,46), 6)
first_prize_lotto.sort()
hidden_ball = random.sample(range(1,46),1)
while True:
    if hidden_ball[0] in first_prize_lotto:
        hidden_ball = random.sample(range(1,46),1)
    else:
        break 
count = 0
first_count = 0
second_count = 0
three_count = 0
four_count = 0
five_count = 0
while True:
    random_lotto = random.sample(range(1,46), 6) 
    random_lotto.sort()
    lotto_list = []
    for check_1 in first_prize_lotto:
        for check_2 in random_lotto:
            if check_1 == check_2:
                lotto_list.append(check_1)
                if hidden_ball[0] in random_lotto and len(lotto_list) == 5:
                    second_count += 1
                elif len(lotto_list) == 6:
                    first_count += 1
                elif len(lotto_list) == 5:
                    three_count += 1
                elif len(lotto_list) == 4:
                    four_count += 1
                elif len(lotto_list) == 3:
                    five_count += 1
                
    if count == 88000000:
        print(f'1등은 {first_count}게임, 2등은 {second_count}게임, 3등은 {three_count}게임, 4등은 {four_count}게임, 5등은 {five_count}게임이 각각 당첨 되었네요')
        print(first_prize_lotto)
        print(hidden_ball)
        break
    else:
        count += 1
        print(count)
    #else:
    #    if count >= 10000000:
    #        money = count * 1000
    #        print(f'{money}원을 사용하여 가지고 있는 돈을 탕진하여 추가 구입을 할 수 없습니다.')
    #        break
    #    else:
    #        count += 1
    #        print(count)
