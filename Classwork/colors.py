
class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    GREY = '\033[90m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BBOLD = '\033[1;90m'


print(Color.GREEN + " C " + Color.BOLD + " O " + Color.GREEN + " L" + Color.ENDC)
print(Color.GREEN + " C " + Color.BOLD + " X " + Color.GREEN + " L" + Color.ENDC)
print(Color.GREY  + " C " + Color.BOLD + " O " + Color.GREY  + " LOR" + Color.ENDC)
