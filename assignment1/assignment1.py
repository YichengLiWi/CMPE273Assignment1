from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)
id = 123456
path1 = "/Users/seanli/Downloads/cmpe273-fall17/assignment1/"
path = "../assignment1"
@app.route('/api/v1/scripts', methods=['POST'])
def create_script():
    #print '123'
    # print request.form['data']
    # pyFile = request.form['data']
    # print pyFile
    global id
    global path1
    request.files['data'].save(path1 + str(id) + '.py')
    id+=1
    return jsonify({ 'script-id' : id }), 201
    # return '123'

@app.route('/api/v1/scripts/<int:script_id>', methods = ['GET'])
def show_post(script_id):
    global path1
    scriptFile = path1 + str(script_id) + '.py'
    cmd = 'python ' + scriptFile
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    return out
    #import scriptFile
    # print(a) 
    # return HTTP_200_OK
 #post key = data value ="#foo.py print("Hello World") string
 # 123456.py store value
# run shell .py 


if __name__ == '__main__':
   app.run(debug = False, port = 8000)

#curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@/tmp/foo.py" http://localhost:8000/api/v1/scripts
