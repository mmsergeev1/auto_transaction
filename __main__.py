import ConfigReader
import FileReader
import YnabAPI
from os import system, name


config_dict = ConfigReader.get_config()
token = config_dict['personal_access_token']
ynab_api = YnabAPI.YnabAPI(token)


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def pause(action):
    input(f"Press Enter to {action}")


def choose(choice):
    result = ''
    if choice == '1':
        result = ynab_api.get_budget_list()
    elif choice == '2':
        result = 'In development'
    elif choice == '3':
        system(exit(0))
    return result


def main_menu():
    print('1. Get budget ID\'s')
    print('2. Insert transactions into budget')
    print('3. Exit')
    choice = input('> ')
    return choice


def print_info():
    print('© Mikhail Sergeev, 2020, Moscow')
    print('Read README.md before use')
    print('===============================')


def main():
    clear()
    print_info()

    choice = main_menu()
    result = choose(choice)
    print(result)

    pause('exit')


if __name__ == '__main__':
    main()
