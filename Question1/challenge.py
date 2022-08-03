#   Challenge: Run the python script at the repo https://github.com/caioluciofc/metrobi_challenge and
# get the answer of the cipher.
#   Answer: by running the script with the comand "python challenge.py" you end up getting a url to the
# root directory of the web page the the code creates a host for. If we click the url link and follow the path 
# above the "challenge" function (line 16) The code in the challenge function will run. We can see that the only
# haking key that gives us any actual words is the key 4, so that is the only key that can decipher the encrypted message.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/answer')
def challenge():
    message = 'GIEWIV GMTLIV HIQS'  # encrypted message
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))
    return 'The answer is not here :)'

if __name__ == '__main__':
    app.run()