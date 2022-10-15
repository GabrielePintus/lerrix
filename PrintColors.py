class PrintColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKCYAN = '\033[96m'
    OKMAGENTA = '\033[95m'
    OKYELLOW = '\033[93m'
    OKWHITE = '\033[97m'
    OKBLACK = '\033[90m'

    def set_color(color):
        print(color, end="")