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