from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

# index.html 파일을 불러오자
# @app.route('/mypage')
# def mypage():
#    return render_template('index.html')

# GET 요청 API 코드
# @app.route('/test', methods=['GET'])
# def test_get():
#    title_receive = request.args.get('title_give')
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

# POST 요청 API 코드
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)