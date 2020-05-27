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
                    elif len(lotto_list) < 3:
                        next_chance += 1
        print(check_my)
        print(check_first)
        print(lotto_mynum)
        print(lotto_list)
        
        return render_template('result.html', first_count=first_count, second_count=second_count, three_count=three_count, four_count=four_count, five_count=five_count, next_chance=next_chance, first_prize_lotto=first_prize_lotto)
    else:
        return redirect('/')