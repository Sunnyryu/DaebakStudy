import os
from flask import render_template, url_for, redirect, request
from editor import app
from editor.db.vendor_search import VendorSearch
from editor.db.handle_search import HandleSearch
from editor.db.get_vendor import Get_vendor
from editor.db.createtable import Createtable
from editor.db.create import Create

import pandas as pd



@app.route("/")
def index():
    #Createtable()
    #Create()
    return render_template('index.html')

@app.route("/product")
@app.route("/product/<handle>")
def product(handle=None):
    vendor = request.args.get('comment')
    #print(vendor)
    #print(vendor)
    #print(vendor_handle_list[0])
    if handle:
        vendor_get = Get_vendor(handle)
        handle_list = VendorSearch(vendor_get)
        product_list = HandleSearch(handle)
        #   print(product_list)
        #print(vendor)
        return render_template('product.html', product_list=product_list, product_list_value=len(product_list), handle_value_list=handle_list)
    vendor_handle_list = VendorSearch(vendor)
    
    return render_template('product.html', handle_list=vendor_handle_list)
#@app.route("/1")
#def summernote():
#    print(Read())
#    table_read = pd.DataFrame(Read())
#    table_read2 = pd.DataFrame.to_string(table_read)
#    return render_template('summernote.html', table_read=table_read2)
@app.route("/product_update", methods=["POST"])
def product_update():
    value = request.form['title']
    print(value)
    return redirect('/')    