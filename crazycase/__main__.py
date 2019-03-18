import sys

def main():
    # get string 
    text = sys.argv[1]
    crazy = ''
    i = 0
    for char in text:
        # if char is a space
        if char == ' ':
            crazy += char
        # capitalize at odd index
        elif i % 2 != 0:
            crazy += char.upper()
            i += 1
        else:
            crazy += char
            i += 1
    print(crazy)
if __name__ == '__main__':
    main()