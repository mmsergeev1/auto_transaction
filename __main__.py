import ConfigReader
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


def pause(action):
    input(f"Press Enter to {action}")


def print_info():
    print('© Mikhail Sergeev, 2020, Moscow')
    print('Read README.md before use')
    print('===============================')


def main():
    clear()
    print_info()

    pause('start')

    config_dict = ConfigReader.get_config()
    token = config_dict['personal_access_token']

    ynab_api = YnabAPI.YnabAPI(token)
    print(ynab_api.get_user())


if __name__ == '__main__':
    main()
