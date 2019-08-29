try:
    from setuptools import  setup

except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'Divanshu Dodeja',
    'url' : 'http://github.com/divanshudodeja',
    'author_email' : 'divanshu.dodeja@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['ex48'],
    'scripts' : [],
    'name' : 'projectname'
}

setup(**config)