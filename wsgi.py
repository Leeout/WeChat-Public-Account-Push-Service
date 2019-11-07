from app import app

application = app('production')

if __name__ == '__main__':
    application.run()
