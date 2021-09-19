# parse the input
def parse(str):
    # tokenizes the input based on spaces
    tokens = str.split(" ")

    # have arguments and flags in different places
    args = []
    flags = []

    # process each token one by one and put them in the correct spot
    for token in tokens:
        # flags have "-" in front of them
        if (token[0] == "-"):
            flags.append(token)

        else:
            args.append(token)

    # return the args and flags as a tuple
    return args, flags