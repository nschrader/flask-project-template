from setuptools import setup

setup(
    name="Project Whiskey",
    version="0.1",
    url="https://github.com/nschrader/project_whiskey",
    packages=[
        "web",
        "mail",
        "dao",
    ],
    install_requires=[
        "Flask==1.0.2",
        "Flask-Mail",
        "Flask-Login",
        "Flask-WTF",
        "MongoEngine",
        "Markdown",
        "overrides",
    ],
)
