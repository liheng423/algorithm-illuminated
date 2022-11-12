

def argmax(get_identifier, args):

    temp = args[0]

    for index in range(1, len(args)):

        if get_identifier(args[index]) > get_identifier(temp):
            temp = args[index]

    return temp


def argmin(args, get_identifier=lambda x: x):

    temp = args[0]

    for index in range(1, len(args)):

        if get_identifier(args[index]) < get_identifier(temp):
            temp = args[index]

    return temp
