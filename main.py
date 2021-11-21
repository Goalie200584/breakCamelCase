def solve(s):
    output = ""
    for char in s:
        if char == char.upper():
            output += " " + char
        else:
            output += char
    return output
        

if __name__ == '__main__':
    print(solve("helloWorldHi"))
