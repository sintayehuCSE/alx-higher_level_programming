#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    object_name = dir(hidden_4)
    for i in range(len(object_name)):
        name = str(object_name[i])
        if (name[0] != '_'):
            print("{}".format(object_name[i]))
