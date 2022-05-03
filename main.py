# press Y or N before program run
cred = '\033[91m'
cgreen = '\33[32m'
cend = '\033[0m'


def program_to_work():
    print("You make right choice")


def make_choice():
    choice = input(f"{cgreen}Please print{cend}\n{cred}Y - to continue{cend}\n"
                   f"{cred}N - to stop{cend}\n")
    while choice.lower() != 'y' and choice.lower() != 'n':
        choice = input(f"{cgreen}Please print{cend}\n{cred}Y - to continue{cend}\n"
                       f"{cred}N - to stop{cend}\n")
    program_to_work() if choice.lower() == 'y' else print(f"{cred}YOU STOPPED APP{cend}")


make_choice()
