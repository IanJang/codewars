VARIABLES = {}
# 스택 포인터는 구현 안함
STACK = []
REGISTERS = {'EFLAGS': {'ZF': 0, 'CF': 0},
             'EIP': 0}
LABELS = {}
COMMANDS = []
MSG_RETURN = ""


def clean():
    global VARIABLES, STACK, REGISTERS, LABELS, COMMANDS, MSG_RETURN
    VARIABLES = {}
    # 스택 포인터는 구현 안함
    STACK = []
    REGISTERS = {'EFLAGS': {'ZF': 0, 'CF': 0},
                 'EIP': 0}
    LABELS = {}
    COMMANDS = []
    MSG_RETURN = ""


def command_handler(opr, *args):
    if opr == 'mov':
        src = args[0]
        if tryparse_int(args[1]):
            dst = int(args[1])
        else:
            dst = VARIABLES[args[1]]
        VARIABLES[src] = dst

    elif opr == 'inc':
        src = args[0]
        VARIABLES[src] += 1

    elif opr == 'dec':
        src = args[0]
        VARIABLES[src] -= 1

    elif opr == 'add':
        src = args[0]
        if tryparse_int(args[1]):
            dst = int(args[1])
        else:
            dst = VARIABLES[args[1]]
        VARIABLES[src] += dst

    elif opr == 'sub':
        src = args[0]
        if tryparse_int(args[1]):
            dst = int(args[1])
        else:
            dst = VARIABLES[args[1]]
        VARIABLES[src] -= dst

    elif opr == 'mul':
        src = args[0]
        if tryparse_int(args[1]):
            dst = int(args[1])
        else:
            dst = VARIABLES[args[1]]
        VARIABLES[src] *= dst

    elif opr == 'div':
        src = args[0]
        if tryparse_int(args[1]):
            dst = int(args[1])
        else:
            dst = VARIABLES[args[1]]
        VARIABLES[src] //= dst

    elif opr == 'msg':
        ret = ""
        for arg in args:
            if (arg[0] == "'" and arg[-1] == "'") or (arg[0] == '"' and arg[-1] == '"'):
                temp = arg[1:-1]
            elif tryparse_int(arg):
                temp = str(arg)
            else:
                temp = str(VARIABLES[arg])
            ret += temp
        return ret

    elif opr == 'end':
        return -1

    # jump 관련
    elif opr == 'cmp':
        if tryparse_int(args[0]):
            src = int(args[0])
        else:
            src = VARIABLES[args[0]]
        if tryparse_int(args[1]):
            dst = int(args[1])
        else:
            dst = VARIABLES[args[1]]
        REGISTERS['EFLAGS']['ZF'] = 1 if src - dst == 0 else 0
        REGISTERS['EFLAGS']['CF'] = 1 if src < dst else 0

    elif opr == 'jmp':
        dst = LABELS[args[0]]
        REGISTERS['EIP'] = dst

    elif opr == 'je':
        dst = LABELS[args[0]]
        if REGISTERS['EFLAGS']['ZF'] == 1:
            REGISTERS['EIP'] = dst

    elif opr == 'jne':
        dst = LABELS[args[0]]
        if REGISTERS['EFLAGS']['ZF'] == 0:
            REGISTERS['EIP'] = dst

    # eax >= ebx
    elif opr == 'jge':
        dst = LABELS[args[0]]
        if REGISTERS['EFLAGS']['ZF'] == 1 or REGISTERS['EFLAGS']['CF'] == 0:
            REGISTERS['EIP'] = dst

    elif opr == 'jg':
        dst = LABELS[args[0]]
        if REGISTERS['EFLAGS']['ZF'] == 0 and REGISTERS['EFLAGS']['CF'] == 0:
            REGISTERS['EIP'] = dst

    elif opr == 'jle':
        dst = LABELS[args[0]]
        if REGISTERS['EFLAGS']['ZF'] == 1 or REGISTERS['EFLAGS']['CF'] == 1:
            REGISTERS['EIP'] = dst

    elif opr == 'jl':
        dst = LABELS[args[0]]
        if REGISTERS['EFLAGS']['ZF'] == 0 and REGISTERS['EFLAGS']['CF'] == 1:
            REGISTERS['EIP'] = dst

    elif opr == 'call':
        dst = LABELS[args[0]]
        STACK.append(REGISTERS['EIP'])
        REGISTERS['EIP'] = dst

    elif opr == 'ret':
        REGISTERS['EIP'] = STACK[-1]
        del STACK[-1]


DEBUG = False


def assembler_interpreter(program):
    # 초기화
    clean()

    global MSG_RETURN
    program = program.split('\n')
    # 명령어 처리 부분
    for line in program:
        line = line.strip()
        # 주석 제거
        comment_index = line.find(';')
        if comment_index != -1:
            line = line[:line.find(';')]
        # 커맨드 처리
        spline = line.split()
        if len(spline) > 0:
            command = spline[0]
            if len(command) - 1 == command.find(':'):
                # 라벨의 EIP 등록
                LABELS[command[:-1]] = len(COMMANDS)

            # Argument를 컴마 단위로 나누기
            # string 일 경우 컴마 나누지 않기
            line = line[len(command):].strip()
            args = []
            isstr = False
            i = 0
            start = 0
            while i < len(line):
                c = line[i]
                if c == "'":
                    isstr = not isstr
                if c == ',' and not isstr:
                    args.append(line[start:i].strip())
                    start = i + 1
                i += 1
            args.append(line[start:].strip())
            COMMANDS.append([command, args])

    # 명령어 수행 부분
    result = None
    while REGISTERS['EIP'] < len(COMMANDS):
        command = COMMANDS[REGISTERS['EIP']]
        operator = command[0]
        args = command[1]
        temp = command_handler(operator, *args)
        if temp == -1:
            break
        if type(temp) is str:
            MSG_RETURN = temp
        # debug stuff
        if DEBUG:
            print('----------------------------------------')
            print('EIP = {}'.format(REGISTERS['EIP']))
            print('RESULT = {}'.format(result))
            print(command)
            print('STACK = {}'.format(STACK))
            print('VARIABLES = {}'.format(VARIABLES))
            print('REGISTERS = {}'.format(REGISTERS))
            print('MSG_RETURN = {}'.format(MSG_RETURN))

        REGISTERS['EIP'] += 1

    return -1 if temp != -1 else MSG_RETURN


def tryparse_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def test_assembler_interpreter():
    from . import Test

    program = '''
        ; My first program
        mov  a, 5
        inc  a
        call function
        msg  '(5+1)/2 = ', a    ; output message
        end

        function:
            div  a, 2
            ret
        '''

    Test.assert_equals(assembler_interpreter(program), '(5+1)/2 = 3')

    program = '''
        mov   a, 5
        mov   b, a
        mov   c, a
        call  proc_fact
        call  print
        end
        proc_fact:
            dec   b
            mul   c, b
            cmp   b, 1
            jne   proc_fact
            ret
        print:
            msg   a, '! = ', c ; output text
            ret
        '''

    Test.assert_equals(assembler_interpreter(program), '5! = 120')

    program = '''
        mov   a, 8            ; value
        mov   b, 0            ; next
        mov   c, 0            ; counter
        mov   d, 0            ; first
        mov   e, 1            ; second
        call  proc_fib
        call  print
        end
        proc_fib:
            cmp   c, 2
            jl    func_0
            mov   b, d
            add   b, e
            mov   d, e
            mov   e, b
            inc   c
            cmp   c, a
            jle   proc_fib
            ret
        func_0:
            mov   b, c
            inc   c
            jmp   proc_fib
        print:
            msg   'Term ', a, ' of Fibonacci series is: ', b        ; output text
            ret
    '''
    Test.assert_equals(assembler_interpreter(program), 'Term 8 of Fibonacci series is: 21')

    # end program without 'end' will return -1
    program = '''
        msg 'return -1'
        '''
    Test.assert_equals(assembler_interpreter(program), -1)

    program = '''
        mov a, 15
        mov b, 15
        call test
        msg ''return' ', a
        end
        test:
            div a, b
            ret
    '''
    Test.assert_equals(assembler_interpreter(program), "'return' 1")

    # argument split test
    program = '''
        mov a, 1
        mov b, 2
        mov c, 3
        msg 'a, b, c: ', a, b, c
        end
    '''
    Test.assert_equals(assembler_interpreter(program), 'a, b, c: 123')
