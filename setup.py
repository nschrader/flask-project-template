from setuptools import setup

setup(
    name="Project Whiskey",
    version='0.1',
    url='https://github.com/nschrader/project_whiskey',
    author='Nick Schrader',
    author_email='nick.schrader@insa-lyon.fr',
    packages=["project"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==1.0.2',
        'Flask-Mail',
        'Flask-Flatpages',
        'Flask-Login',
        'Flask-WTF',
        'PyMongo',
    ],
)
