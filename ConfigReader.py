import ast


def get_config():
    with open("config.txt", "r") as config_file:
        contents = config_file.read()
    config_dict = ast.literal_eval(contents)
    config_file.close()
    return config_dict
