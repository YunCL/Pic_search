#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

from flask import Flask,render_template,request,url_for
from scipy import misc
from sklearn.externals import joblib
import json
import os
import multilayer_perceptron
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    print '---------'
    print os.path.abspath(os.curdir)
    print os.path.abspath('.')
    print '--------'
    data=request.form
    key=data['key']
    x = []
    for i in key.strip().split(","):
        x.append(float(i))
    print x
    clf=joblib.load(os.path.join(os.path.abspath('.'), 'model.pkl'))
    l=clf.predict(x)
    #return 'predict:%s' %(l[0])
    return json.dumps({"result":str(l[0])})

if __name__ == '__main__':
    app.run(debug=True)
