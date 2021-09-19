def parse(str):
    # split the tokens based on spaces
    tokens = str.split(" ")

    # have args list and flags list
    args = []
    flags = []

    # process each token one by one
    for token in tokens:
        # flags have "-" in front of them
        if (token[0] == "-"):
            flags.append(token)

        else:
            args.append(token)

    # return the args and flags as a tuple
    return args, flags