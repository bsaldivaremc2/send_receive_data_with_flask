from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
 print("Example of data received")
 rf=request.form
 print(rf)
 resp = Response("Data received")
 resp.headers['Access-Control-Allow-Origin']='*'
 return resp

@app.route('/sum', methods=['POST'])
def sum_num():
 print("Sum function")
 rf=request.form
 print(rf)
 for key in rf.keys():
  data=key
 print(data)
 data_dic=json.loads(data)
 print(data_dic.keys())
 sum_data = data_dic['sum']
 sumd=0
 for _ in sum_data:
 	sumd+=_
 resp_dic={'sum':sumd,'msg':'Sum performed'}
 resp = jsonify(resp_dic)
 resp.headers['Access-Control-Allow-Origin']='*'
 return resp