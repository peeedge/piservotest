from multiprocessing import Process, Pipe

def userinput(PWM_value):
    PWM = input('Enter PWM Value: ')
    a = PWM
    PWM_value.send(a)
    PWM_value.close()

if __name__ == '__main__':
    PWM = input('Enter PWM Value: ')
    a = PWM
    while True:
        try:
            parent_PWM_value, child_PWM_value = Pipe()
            p = Process(target=userinput, args=(child_PWM_value,))
            p.start()
            print parent_PWM_value.recv()
            p.join()
        except KeyboardInterrupt:
            break



