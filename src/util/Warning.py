suppress_warnings = False

def warn(x):
    if not suppress_warnings:
        print('WARNING:', x)
