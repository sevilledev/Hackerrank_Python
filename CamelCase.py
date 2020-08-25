def camelcase(s):
    i = 1
    for href in s:
        if href == href.upper():
            i += 1
        else:
            pass
    return i


if __name__ == '__main__':
    s = input()

    result = camelcase(s)

    print(result)
