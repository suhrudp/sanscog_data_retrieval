
import os
import hashlib
import pandas as pd
import time 
from io import BytesIO

def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

from flask import Flask, session, make_response, send_file, render_template, request, redirect, url_for, jsonify, make_response
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker


df = None
app = Flask(__name__)

selected = {'apoe': set(), 'socio': set(), 'clinical': set(), 'nursing': set(), 'mri': set(), 'cognito': set(), 'blood': set()}


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/check", methods=["POST"])
def check():
    pw1 = request.form.get("pw")
    user = request.form.get("jonny")
    hash = hash_string(pw1)
    if hash == "16601abfdefce37cb9972244ba744d309cfe2e120c5f559fc5cfad8b05baa8e0" and user == "jonaslab":
        return render_template("file_loading.html")
    
    else:
        return render_template("index_login_failed.html")


@app.route("/homepage", methods=["POST"])
def homepage():
    global df
    # df = pd.read_excel("D:\\New_Data\\python\\MERGED_DATA\\MERGED_NEW_JUNE6_WITH_MRI.xlsx")
    # df = pd.read_excel("D:\\New_Data\\python\\apoe_new.xlsx")
    df = pd.read_excel("apoe_new.xlsx")
    time.sleep(3)
    return render_template("homepage.html", selected=selected)

@app.route("/apoe", methods=["POST"])
def apoe():
    return render_template("apoe.html")


@app.route("/submit", methods=["POST"])
def apoe_submit():
    # import pdb; pdb.set_trace()
    for k,v in request.form.to_dict().items():
        print(k,v)
        if v:
            selected["apoe"].add(k)

    print(selected)
    return render_template("homepage.html", selected=selected)


@app.route("/download", methods=["POST"])
def download():
    global df
    file = pd.DataFrame()
    filename = request.form.get("filename")
    for k, columns in selected.items():
        # import pdb; pdb.set_trace()
        if len(columns) == 0:
            continue
        for c in columns:
            file[c] = df[c]

    # resp = make_response(file.to_excel(engine='xlsxwriter'))
    # resp.headers["Content-Disposition"] = "attachment; filename=download.xlsx"
    # resp.headers["Content-Type"] = "xlsx"
    # return resp
    excel_file = BytesIO()
    file.to_excel(excel_file, index=False)
    excel_file.seek(0)
    return send_file(excel_file, download_name= filename + '.xlsx')

if __name__ == "__main__":
    print(hash_string("jonaslab123"))
    app.static_folder = './static'
    app.run(debug=True)

