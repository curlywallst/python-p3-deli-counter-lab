

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        deli_line = "The line is currently:"
        for num, name in enumerate(katz_deli, start=1):
            deli_line += " {}. {}".format(num, name)
        print(deli_line)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        name = katz_deli.pop(0)
        print(f'Currently serving {name}.')