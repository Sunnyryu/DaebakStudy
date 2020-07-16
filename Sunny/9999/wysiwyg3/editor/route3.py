import os
from flask import render_template, url_for, redirect, request
from editor import app
from editor.db.vendor_search import VendorSearch
from editor.db.handle_search import HandleSearch
from editor.db.get_vendor import Get_vendor
from editor.db.createtable import Createtable
from editor.db.create import Create
from editor.db.read import ValueSearch
from editor.db.read2 import Vendor_read
from editor.db.read3 import Read
from editor.db.update import Update_table_main, Update_table_etc

import pandas as pd



@app.route("/")
def index():
    rows = Read()
    #print(rows)
    rows_vendor = Vendor_read()
    rows_vendor_list = []
    for i in rows_vendor:
        if i['vendor']:
            rows_vendor_list.append(i['vendor'])
    #Createtable()
    #Create()
    return render_template('index.html', rows_vendor=rows_vendor_list, rows=rows, len_rows=len(rows))

@app.route("/product")
def product_list():
    vendor = request.args.get('comment')
    rows = ValueSearch(vendor)
    #print(rows)
    return render_template('product_list.html',rows=rows, len_rows=len(rows))

@app.route("/product/<handle>")
def product_revise(handle):
#    vendor_get = Get_vendor(handle)
#    title_handle = VendorSearch(vendor_get)
    product_list = HandleSearch(handle)
    
    #print(handle_list)
    return render_template('product.html', product_list=product_list, product_list_value=len(product_list))  
#@app.route("/product")
#@app.route("/product/<handle>")
#def product2(handle=None):
#    vendor = request.args.get('comment')
#    #print(vendor)
#    #print(vendor)
#    #print(vendor_handle_list[0])
#    if handle:
#        vendor_get = Get_vendor(handle)
#        handle_list = VendorSearch(vendor_get)
#        product_list = HandleSearch(handle)
        #   print(product_list)
        #print(vendor)
#        return render_template('product.html', product_list=product_list, product_list_value=len(product_list), handle_value_list=handle_list)
#    vendor_handle_list = VendorSearch(vendor)
    
#    return render_template('product.html', handle_list=vendor_handle_list)
#@app.route("/1")
#def summernote():
#    print(Read())
#    table_read = pd.DataFrame(Read())
#    table_read2 = pd.DataFrame.to_string(table_read)
#    return render_template('summernote.html', table_read=table_read2)
@app.route("/product_update", methods=["POST"])
def product_update():
    value_id = request.form.getlist('id')
    value_title = request.form.getlist('title')
    value_body_HTML = request.form.getlist('body_HTML')
    value_price = request.form.getlist('price')
    value_option1_value = request.form.getlist('option1_value')
    value_option2_value = request.form.getlist('option2_value')
    for num in range(len(value_id)):
        if num == 0:
            value_new_id = value_id[num].strip(' \r\n\t')
            value_new_title = value_title[num].strip(' \r\n\t')
            value_new_body_HTML = value_body_HTML[num].strip(' \r\n\t')
            value_new_price = value_price[num].strip(' \r\n\t')
            value_new_option1_value = value_option1_value[num].strip(' \r\n\t')
            #value_new_option2_value = value_option2_value[num].strip(' \r\n\t')
            rows = Update_table_main(value_new_id, value_new_title, value_new_body_HTML, value_new_price, value_new_option1_value)#value_new_option2_value)
        else:
            value_new_id = value_id[num].strip(' \r\n\t')
            value_new_price = value_price[num].strip(' \r\n\t')
            value_new_option1_value = value_option1_value[num].strip(' \r\n\t')
    #    value_new_option2_value = value_option2_value[num].strip(' \r\n\t')
            rows = Update_table_etc(value_new_id, value_new_price, value_new_option1_value)
    print(rows)
    
   # print(value_title[0].strip('\r\n'))
    #value3 = request.form
    #print(value)
    #k = []
    #for i in value:
    #    i.strip()
    #    k.append(i)
    #value = request.form.get('id')
    #value2 = request.form.to_dict()
    #print(value[1])
    #rows = Update_table(value_id, value_title, value_body_HTML, value_price, value_option1_value, value_option2_value)
    #print(value_id[0])
    #print(value2)
    #print(value2['price'])
    

    #print(value2)
    return redirect('/')    