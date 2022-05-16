
import subprocess


def compile_script():
    with open("code.txt", 'r') as inp, open('code.py', 'w') as out:
        for line in inp:
            if len(line.strip()) > 0:
                out.write(line)
    compile_code()
    with open("output_file.txt", 'r') as inp, open('output.txt', 'w') as out:
        for line in inp:
            if len(line.strip()) > 0:
                out.write(line)
                
    with open("output.txt","r") as opfile:
        op = opfile.readlines()
    print("workingggggggggggggggggggggggggggggggggggggggggggggggggggggg")
    op = [remove_esc(line) for line in op]
    for i in op:
        print(i, end="")
    # op = [remove_esc(line) for line in op]
    print("workingggggggggggggggggggggggggggggggggggggggggggggggggggggg")
    # print(op)
    # print("workingggggggggggggggggggggggggggggggggggggggggggggggggggggg")



def compile_code():
    command = f'python code.py'
    inputfile = open("input.txt", "r")
    input = " ".join(inputfile.readlines())
    input = input.encode()
    print(input)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE ,stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print(output)
    print(error)
    with open("output_file.txt","w") as opf:
        opf.write(output.decode('utf-8'))
        opf.write(error.decode('utf-8'))
    return 

def remove_esc(s):
    escapes = ''.join([chr(char) for char in range(1,10)])
    translator = str.maketrans('','',escapes)
    s = s.translate(translator)
    return s

