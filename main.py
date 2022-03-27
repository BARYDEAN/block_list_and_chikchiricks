import random
versachi = 1
while (versachi == 1):
    chakchirik = int(input("1 = block, 2 = list, 3 = chikchiricks is u "))
    if (chakchirik == 1 or chakchirik == 2 or chakchirik == 3 ):
        versachi = 2
if chakchirik == 1:
    print("you is realy stupid and you use block")
if chakchirik == 2:
    print("you is realy stupid and you use list? Fergot")
if chakchirik == 3:
    print("you is realy stupid and you use chikchiricks")
machine = random.randint(1, 3)
if machine == 1:
    print("Machine is smart and use block. Stupid man")
if machine == 2:
    print("Machine is smart and use list. Stupid man")
if machine == 3:
    print("Machine is smart and use chikchiricks. Stupid man")
if chakchirik == machine:
    win = 0
if chakchirik == 1 and machine == 2:
    win = 1
if chakchirik == 1 and machine == 3:
    win = 2
if chakchirik == 2 and machine == 1:
    win = 2
if chakchirik == 2 and machine == 3:
    win = 1
if chakchirik == 3 and machine == 1:
    win = 1
if chakchirik == 3 and machine == 2:
    win = 2
if win == 0:
    print("Machine is win!")
if win == 1:
    print("win is stupid man")
if win == 2:
    print("WIN IS GREAT SMART MACHINE")