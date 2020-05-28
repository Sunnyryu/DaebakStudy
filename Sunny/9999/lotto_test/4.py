import random 

a = random.sample(range(1,46), 6)
a.sort()
count = 0
first_count = 0
three_count = 0
four_count = 0
five_count = 0
while True:
    b = random.sample(range(1,46), 6) 
    b.sort()
    c = []
    for t_1 in a:
        for t_2 in b:
            if t_1 == t_2:
                c.append(t_1)
                if len(c) == 5:
                    three_count += 1
                elif len(c) == 4:
                    four_count += 1
                elif len(c) == 3:
                    five_count += 1
                
    if b == a:
        money = count * 1000
        true_money = (1*1500000000) + (three_count*1500000) + (four_count*60000) + (five_count*5000)- money 
        print(f'{count}만에 당첨되었습니다.')
        print(f'3등은 {three_count}번, 4등은 {four_count}번, 5등은 {five_count}번은 되었네요')
        print(f'{money}원을 사용하였네요..')
        print(f'결과론 적으론 마진은 {true_money}원입니다.')
        print(b)
        break
    else:
        my_money = 2000000000
        money = count * 1000
        three_money = three_count*1500000
        four_money = four_count*60000
        five_money = five_count*5000
        margin = my_money - money + three_money + four_money + five_money
        if margin == 0:
            print(a)
            print(three_count)
            print(four_count)
            print(f'사용한 돈은 {money}, 3등 당첨금은 {three_money}, 4등 당첨금은 {four_money}, 5등 당첨금은 {five_money} 입니다.')
            print('적자로 인해 더이상 구입하실 수 없습니다.')
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
