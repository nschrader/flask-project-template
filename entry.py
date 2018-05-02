from project import create_app

app = create_app(config='../local.cfg')

#TODO: this shit shouldn't be here
with app.app_context():
    import project.frontend

if __name__ == '__main__':
    app.run()
