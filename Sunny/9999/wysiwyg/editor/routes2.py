import os
from flask import render_template, url_for, Flask, redirect, request
from editor import app, db
from editor.models import Html
import csv


@app.route("/123")
def index():
    #with open('C:/Users/tusik/Downloads/BRND-hyunavely-Skirt-Pants-Dress-Belt-71items.csv', encoding='utf-8') as f:
    #table_search_name = db.table('daebakProduct').name
    with open('/home/sunny/DaebakStudy/Sunny/9999/wysiwyg/editor/csv/BR-banharimarket--268items.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        try:
            if Html.query.filter_by(vendor='banharimarket').first():
                for c in reader:
                    k = c[0]
                    Html.query.filter_by(handle=k).delete()
                    db.session.commit()
                for i in reader:
                    html2 = Html(handle = i[0],
                                title = i[1],
                                body_HTML = i[2],
                                vendor = i[3],
                                type = i[4],
                                tags = i[5],
                                published = i[6],
                                option1_name = i[7], 
                                option1_value = i[8],
                                option2_name = i[9],
                                option2_value = i[10],
                                option3_name = i[11],
                                option3_value = i[12],
                                variant_sku = i[13],
                                variant_grams = i[14],
                                variant_inventory_tracker = i[15], 
                                variant_inventory_qty = i[16],
                                variant_inventory_policy = i[17],
                                variant_fullfillment_service = i[18],
                                varient_price = i[19],
                                variant_compare_at_price = i[20], 
                                varient_requires_shipping = i[21],
                                variant_taxable= i[22],
                                variant_barcord = i[23],
                                imgage_src = i[24],
                                image_position = i[25],
                                image_alt_text = i[26],
                                gift_card = i[27],
                                seo_title= i[28],
                                seo_description =i[29], 
                                google_shopping_google_product_category = i[30],
                                google_shopping_gender = i[31],
                                goggle_shopping_age_group = i[32],
                                google_shopping_mpn = i[33],
                                google_shopping_adwords_grouping = i[34], 
                                google_shopping_adwords_labels = i[35],
                                google_shopping_condition = i[36],
                                google_shopping_custom_product = i[37], 
                                google_shopping_custion_label0 = i[38],
                                google_shopping_custion_label1 = i[39],
                                google_shopping_custion_label2 = i[40],
                                google_shopping_custion_label3 = i[41],
                                google_shopping_custion_label4 = i[42],
                                variant_image = i[43],
                                variant_weight_unit = i[44],
                                variant_tax_code = i[45],
                                cost_per_item = i[46],
                                )
                    db.create_all()
                    db.session.add(html2)
                    db.session.commit()
                print(1)
        except:
            for i in reader:
                html = Html(handle = i[0],
                            title = i[1],
                            body_HTML = i[2],
                            vendor = i[3],
                            type = i[4],
                            tags = i[5],
                            published = i[6],
                            option1_name = i[7], 
                            option1_value = i[8],
                            option2_name = i[9],
                            option2_value = i[10],
                            option3_name = i[11],
                            option3_value = i[12],
                            variant_sku = i[13],
                            variant_grams = i[14],
                            variant_inventory_tracker = i[15], 
                            variant_inventory_qty = i[16],
                            variant_inventory_policy = i[17],
                            variant_fullfillment_service = i[18],
                            varient_price = i[19],
                            variant_compare_at_price = i[20], 
                            varient_requires_shipping = i[21],
                            variant_taxable= i[22],
                            variant_barcord = i[23],
                            imgage_src = i[24],
                            image_position = i[25],
                            image_alt_text = i[26],
                            gift_card = i[27],
                            seo_title= i[28],
                            seo_description =i[29], 
                            google_shopping_google_product_category = i[30],
                            google_shopping_gender = i[31],
                            goggle_shopping_age_group = i[32],
                            google_shopping_mpn = i[33],
                            google_shopping_adwords_grouping = i[34], 
                            google_shopping_adwords_labels = i[35],
                            google_shopping_condition = i[36],
                            google_shopping_custom_product = i[37], 
                            google_shopping_custion_label0 = i[38],
                            google_shopping_custion_label1 = i[39],
                            google_shopping_custion_label2 = i[40],
                            google_shopping_custion_label3 = i[41],
                            google_shopping_custion_label4 = i[42],
                            variant_image = i[43],
                            variant_weight_unit = i[44],
                            variant_tax_code = i[45],
                            cost_per_item = i[46],
                            )
                db.create_all()
                db.session.add(html)
                db.session.commit()
                print(222)



        return render_template('index.html')


@app.route("/")
def home():
    #html = Html.query.filter()]
    a = print(Html)
    html = Html.query.filter_by(vendor = 'banharimarket').all()
    print(html)
    return render_template('home.html', html=html)