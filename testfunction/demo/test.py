print("helo ")

shepherd = 'F_Name   "Martha asdqf qwwf  qwdqwfqf"'
# Note f before first quote of string
newStr = shepherd.split(" ", 1)
newStr[1] = newStr[1].strip().replace('"', '')
