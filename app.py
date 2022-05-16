from flask import Flask, redirect, render_template, url_for, request
from flask import Flask
from compiler import compile_script
app = Flask(__name__)

@app.route('/')
def index():
    with open("code.txt","r+") as codeinputfile:
        codeinputfile.seek(0)
        codeinputfile.truncate()
        code = codeinputfile.readlines() 
    with open("input.txt","r+") as inputfile:
        inputfile.seek(0)
        inputfile.truncate()
        input = inputfile.readlines()
    data ={
            "code":code,
            "input":input
        }   
    return render_template('home.html', data=data)


@app.route('/uploadfile/<filetype>',methods = ['POST'])
def UploadFile(filetype):
    if request.method == 'POST':
        if filetype == 'code':
            file = request.files['file1'].read()
            file= file.decode('utf-8')
            with open("temp.txt","w") as tem:
                    tem.write(file)
            with open("temp.txt", 'r') as inp, open('code.txt', 'w') as wcode:
                for line in inp:
                    if len(line.strip()) > 0:
                        wcode.write(line) 
            print(file)
        elif filetype == 'input':
            file = request.files['file2'].read()
            file = file.decode('utf-8')
            with open("temp.txt","w") as tem:
                    tem.write(file)
            with open("temp.txt", 'r') as inp, open('input.txt', 'w') as winput:
                for line in inp:
                    if len(line.strip()) > 0:
                        winput.write(line) 
            print(file)
        with open("code.txt","r") as codeinputfile:
                code = codeinputfile.readlines()
        with open("input.txt","r") as inputfile:
                input = inputfile.readlines()   
        data ={
            "code":code,
            "input":input
        }
    return render_template('home.html', data=data)




@app.route('/compile',methods = ['POST'])
def CodeCompile():
    if request.method == 'POST':
        code = request.form['codetext']
        input = request.form['inputtext']
        with open("temp.txt","w") as tem:
                tem.write(code)
        with open("temp.txt", 'r') as inp, open('code.txt', 'w') as wcode:
                for line in inp:
                    if len(line.strip()) > 0:
                        wcode.write(line)
        with open("temp.txt","w") as tem:
                    tem.write(input)
        with open("temp.txt", 'r') as inp, open('input.txt', 'w') as winput:
            for line in inp:
                if len(line.strip()) > 0:
                    winput.write(line)
        with open("code.txt","r") as codeinputfile:
                code = codeinputfile.readlines()
        with open("input.txt","r") as inputfile:
                input = inputfile.readlines()
        compile_script()
        with open("output.txt","r") as outfile:
                output = outfile.readlines() 
        print(type(output))   
        print(output)
        data ={
            "code":code,
            "input":input,
            "output":output
        }
    return render_template('home.html', data=data)



@app.route('/inputtext',methods = ['POST'])
def InputText():
    if request.method == 'POST':
        code = request.form['code2']
        with open("input.txt","w") as rnr: 
            rnr.write(code.decode('utf-8'))
        print(code)
    return render_template('index.html')



if __name__ == '__main__':
   app.run(debug=False)