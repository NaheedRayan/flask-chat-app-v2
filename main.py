from website import create_app

app = create_app()


if __name__ == '__main__':
    # This is a debugging server
    app.run(debug = True)