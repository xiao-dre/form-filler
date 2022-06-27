import random
import math

def random_interval(start, end):
    interval = end - start + 1 
    return math.floor(random.random() * interval + (end - 1))


def generate_console(opt, ctr): 
    command = 'document.getElementById(\'N_STU_EVL_LEC_N_ANS_OPT{}${}\').checked = true;\n'.format(opt, ctr)
    return command 

def main(): 
    print('Input the Numbers of Lecturer(s): ', end = '')
    lecturer_count = int(input())
    print('Input Questions Number for Each Lecturer(s): ', end = '')
    question_count = int(input())
    total_questions = question_count * lecturer_count
    for i in range(total_questions):
        score = random_interval(3, 4) # You may change the value, but the default value would be 3, 4
        command = generate_console(score, i)
        print(command, end = '')

main()