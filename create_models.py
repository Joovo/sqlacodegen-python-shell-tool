import os, sys

MYSQL_URI = 'mysql+pymysql://root:Jh123456@127.0.0.1:3306/ad_demo?charset=utf8'
MODEL_FILE = './models.py'

try:
    from sqlacodegen.main import main
except ImportError:
    print(
        'ImportError: from sqlacodegen.main import main.\nTry `pip install sqlacondegen`\nAlso `pip install flask-sqlacondegen` in flask project.')

if __name__ == '__main__':
    '''
    Don't rely on this way to create models. Because the class don't 
    implement SQLalchemy()'s interface and has a superclass of `Base`.
    Also centerned that SQLalchemy suppurt query attribute only in instantiated class \
    so DO NOT import instantiated class when init module, such as importing in `__init__.py`.
    '''
    with open(MODEL_FILE, 'w') as file:
        sys.stdout = file
        sys.argv = ('sqlacodegen %s' % MYSQL_URI).split()
        sys.exit(main())
