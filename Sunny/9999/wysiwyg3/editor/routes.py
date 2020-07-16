import os
from flask import render_template, url_for, redirect, request
from editor import app
from editor.db.handle_search import HandleSearch
from editor.db.value_search_read import ValueSearch
from editor.db.vendor_read import Vendor_read
from editor.db.index_value_read import IndexValueread
from editor.db.update import Update_table_main, Update_table_etc
from editor.db.make_csv import Make_csv
import datetime
from flask_paginate import Pagination, get_page_args

import pandas as pd



@app.route("/")
def index():
    rows = IndexValueread()
    rows_list = []
    for row in rows:
        if row['title']:
            rows_list.append(row)
    def get_rows(offset, per_page):
        return rows_list[offset: offset + per_page]
    page = int(request.args.get('page',1))
    per_page = 12
    offset = (page -1) * per_page
    total = len(rows_list)
    pagination_rows = get_rows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework="bootstrap4")
    rows_vendor = Vendor_read()
    rows_vendor_list = []
    for i in rows_vendor:
        if i['vendor']:
            rows_vendor_list.append(i['vendor'])

    return render_template('index.html', rows_vendor=rows_vendor_list, rows=pagination_rows, page=page, per_page=per_page, pagination=pagination)

@app.route("/product")
def product_list():
    vendor = request.args.get('comment')
    rows = ValueSearch(vendor)
    def get_rows(offset, per_page):
        return rows[offset: offset + per_page]
    page = int(request.args.get('page',1))
    per_page = 12
    offset = (page -1) * per_page
    total = len(rows)
    pagination_rows = get_rows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework="bootstrap4")
    #print(rows)
    return render_template('product_list.html',rows=pagination_rows, len_rows=len(rows), page=page, per_page=per_page, pagination=pagination)

@app.route("/product/<handle>")
def product_revise(handle):

    product_list = HandleSearch(handle)

    return render_template('product.html', product_list=product_list, product_list_value=len(product_list))  

@app.route("/product_update", methods=["POST"])
def product_update():
    value_id = request.form.getlist('id')
    value_title = request.form.getlist('title')
    value_body_HTML = request.form.getlist('body_HTML')
    value_price = request.form.getlist('price')
    value_option1_value = request.form.getlist('option1_value')
    value_option2_value = request.form.getlist('option2_value')
    revise_times = request.form['revise_times']
    revise_last_time = request.form['revise_last_time']
    print(type(revise_times))
    print(type(revise_last_time))
    for num in range(len(value_id)):
        if num == 0:
            value_new_id = value_id[num].strip(' \r\n\t')
            value_new_title = value_title[num].strip(' \r\n\t')
            value_new_body_HTML = value_body_HTML[num]
            value_new_price = value_price[num].strip(' \r\n\t')
            value_new_option1_value = value_option1_value[num].strip(' \r\n\t')
            value_new_revise_times = int(revise_times)+ 1
            value_new_revise_last_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

            #value_new_option2_value = value_option2_value[num].strip(' \r\n\t')
            rows = Update_table_main(value_new_id, value_new_title, value_new_body_HTML, value_new_price, value_new_option1_value, value_new_revise_times, value_new_revise_last_time)#value_new_option2_value)
        else:
            value_new_id = value_id[num].strip(' \r\n\t')
            value_new_price = value_price[num].strip(' \r\n\t')
            value_new_option1_value = value_option1_value[num].strip(' \r\n\t')
            value_new_revise_times = int(revise_times)+ 1
            value_new_revise_last_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    #    value_new_option2_value = value_option2_value[num].strip(' \r\n\t')
            rows = Update_table_etc(value_new_id, value_new_price, value_new_option1_value, value_new_revise_times, value_new_revise_last_time)
    make_csv = Make_csv()
    print(make_csv)
    return redirect('/')    