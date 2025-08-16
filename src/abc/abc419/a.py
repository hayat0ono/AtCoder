def main():
    s = input()
    if s == "red":
        print("SSS")
    elif s == "redred":
        print("SSSSSS")
    elif s == "redredred":
        print("SSSSSSSSS")
    elif s == "redblue":
        print("SSSFFF")
    elif s == "redbluered":
        print("SSSFFFSSS")
    elif s == "redgreen":
        print("SSSMMM")
    elif s == "blue":
        print("FFF")
    elif s == "bluered":
        print("FFFSSS")
    elif s == "blueredred":
        print("FFFSSSSSS")
    elif s == "blueblue":
        print("FFFFFF")
    elif s == "bluegreen":
        print("FFFMMM")
    elif s == "green":
        print("MMM")
    elif s == "greenred":
        print("MMMSSS")
    elif s == "greenblue":
        print("MMMFFF")
    elif s == "greengreen":
        print("MMMMMM")
    else:
        print("Unknown")  

if __name__ == '__main__':
    main()