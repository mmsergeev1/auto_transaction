import YnabAPI
from os import system, name


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def print_info():
    print('© Mikhail Sergeev, 2020, Moscow')
    print('Read README.md before use')
    print('===============================')


def main():
    clear()
    print_info()

    token = str(input("Input personal acess token: "))
    response_data = YnabAPI.get_user(token)
    print(response_data)


if __name__ == '__main__':
    main()
