from __init__ import create_app

app = create_app() # CREATE THE APP

if __name__ == '__main__':
    app.run(debug = True)
