import os
from flask import render_template, url_for, Flask, redirect, request
from lotto import app
import random


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    lotto_mynum = request.args.get('lotto_number')
    lotto_mynum = lotto_mynum.split(',')
    lotto_mynum = list(map(int, lotto_mynum))
    lotto_mynum.sort()
    count = 0
    first_count = 0
    second_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    next_chance = 0 
    lotto_list = []

    if len(lotto_mynum) == 6:
        first_prize_lotto = random.sample(range(1,46), 6)
        first_prize_lotto.sort()
        hidden_ball = random.sample(range(1,46),1)

        while True:
            if hidden_ball[0] in first_prize_lotto:
                hidden_ball = random.sample(range(1,46),1)
            else:
                break  
        for check_my in lotto_mynum:
            for check_first in first_prize_lotto:
                if check_my == check_first:
                    lotto_list.append(check_my)
                   
        if hidden_ball[0] in lotto_mynum and len(lotto_list) == 5:
            second_count += 1
        elif len(lotto_list) == 6:
            first_count += 1
        elif len(lotto_list) == 5:
            three_count += 1
        elif len(lotto_list) == 4:
            four_count += 1
        elif len(lotto_list) == 3:
            five_count += 1
        elif len(lotto_list) <= 2 or len(lotto_list) == 0:  
            next_chance += 1
        first_prize_lotto = ",".join(map(str,first_prize_lotto))
        lotto_mynum = ",".join(map(str,lotto_mynum))
        return render_template('result.html', first_count=first_count, second_count=second_count, three_count=three_count, four_count=four_count, five_count=five_count, next_chance=next_chance, first_prize_lotto=first_prize_lotto, hidden=hidden_ball[0], mynum=lotto_mynum)
    else:
        return redirect('/')

@app.route('/lottocheck')
def lotto_check():
    count = 0
    first_count = 0
    second_count =0
    three_count = 0
    four_count = 0
    five_count = 0
    first_prize_lotto = random.sample(range(1,46), 6)
    first_prize_lotto.sort()
    hidden_ball = random.sample(range(1,46),1)
    #money = count * 1000
    while True:
        if hidden_ball[0] in first_prize_lotto:
            hidden_ball = random.sample(range(1,46),1)
        else:
            break 
    while True:
        random_lotto = random.sample(range(1,46),6)
        random_lotto.sort()
        add_list = []
        for lotto_1 in first_prize_lotto:
            for lotto_2 in random_lotto:
                if lotto_1 == lotto_2:
                    add_list.append(lotto_1)
                    if len(add_list) == 6:
                        first_count += 1
                    if len(add_list) == 5 and hidden_ball[0] in random_lotto:
                        second_count += 1
                    if len(add_list) == 5:
                        three_count += 1
                    if len(add_list) == 4:
                        four_count += 1
                    if len(add_list) == 3:
                        five_count += 1
        money = count * 1000
        margin = (first_count*1500000000) + (second_count*30000000) + (three_count*1500000) + (four_count*50000) + (five_count*5000) - money
        print(money)
        if count == 1000:
            break
        else:
            count += 1
            #print(count)

            
    if margin >= 0:
        return render_template('lotto_check.html', margin=margin, first_count=first_count, second_count=second_count, three_count=three_count, four_count=four_count, five_count=five_count)
    elif margin < 0:
        minus_margin = abs(margin)
        return render_template('lotto_check.html', minus_margin=minus_margin, first_count=first_count, second_count=second_count, three_count=three_count, four_count=four_count, five_count=five_count)