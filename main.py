from website import create_app

app = create_app()


if __name__ == '__main__':
    # This is a debugging server
    app.run(host = '0.0.0.0' , port = 5000 ,debug = True)