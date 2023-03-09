import os
import time

def convert_to_new(expression):
    expression = expression.strip()
    expression = expression.replace("A(","")
    expression = expression.replace(")","")
    n_m = [word.strip() for word in expression.split(',')]
    if n_m[0] == '0':
        return str(int(n_m[1]) + 1)
    elif n_m[1] == '0':
        return "A({n},1)".format(n=int(n_m[0])-1) 
    else:
        return "A({n},A({n2},{m}))".format(n=int(n_m[0])-1, n2 = int(n_m[0]), m = int(n_m[1])-1)

def search_expression(equation):
    indexEnd  = equation.find(')')
    indexStar = equation.rfind('A', 0, indexEnd)
    return [indexStar, indexEnd+1]

def prepare_folder(path):
    if not os.path.exists(path=path):
        os.makedirs(path)
    
def get_ackerman(equation, max_iteration, path, explain = False):
    start = time.time()
    prepare_folder(path=path)
    i = 0
    global_iteration = 0
    name_file = path + "/" + 'continue.data'
    if os.path.exists(name_file):
        file1 = open(name_file, 'r')
        Lines = file1.readlines()
        global_iteration = int(Lines[0].strip())
        equation = Lines[1].strip()
        name_file = path + "/" + str(global_iteration)+".data"
        if explain and os.path.exists(name_file):
            os.remove(name_file)
    indexA = equation.find("A")
    # print(indexA)
    while indexA != -1:    
        i = i + 1
        index = search_expression(equation=equation)
        first = equation[0:index[0]]
        second = equation[index[1]:]
        # print(first, second)
        # print(equation[index[0]: index[1]])
        new_equation = convert_to_new(equation[index[0]: index[1]])
        equation = first + new_equation + second
        #print(equation)
        if explain:
            name_file = path + "/" + str(global_iteration)+".data"
            file1 = open(name_file, "a")  # append mode
            file1.write(""+equation +"\n")
            file1.close()
        if i == max_iteration:
            i = 0
            global_iteration = global_iteration + 1
            name_file = path + "/" + 'continue.data'
            f = open(name_file, 'a')
            f.truncate(0)
            f.write(str(global_iteration) + "\n")
            f.write(equation + "\n")
            f.close()
        indexA = equation.find("A")
    
    name_file = path + "/" + 'finish.data'
    f = open(name_file, 'a')
    f.truncate(0)
    end = time.time()
    f.write(str(global_iteration) + "\n")
    f.write(str(end - start) + "\n")
    f.write(equation + "\n")
    f.close()


