suppress_warnings = False
silent = False

def warn(x):
    if not suppress_warnings and not silent:
        print('WARNING:', x)

def info(x):
    if not silent:
        print(x)
