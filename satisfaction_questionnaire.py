def generate_console(question_num): 
    command = ''
    for i in range(1, question_num): 
        score = 4
        command += 'document.getElementsByName(\'A_KUESIONER_WRK_A_CHECKBOX_{}${}\')[0].checked = \'checked\';\n'.format(score, i)
    return command 

def main(): 
    print('Input Questions Number: ', end = '')
    question_num = int(input())
    output = generate_console(question_num)
    print(output)

main()