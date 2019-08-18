import os, sys

# Mysql URL
MYSQL_URI = 'mysql+pymysql://root:Jh123456@127.0.0.1:3306/ad_demo?charset=utf8'
# File Path
MODEL_FILE='./models.py'


try:
    from sqlacodegen.main import main
except ImportError:
    print(
        'ImportError: from sqlacodegen.main import main\n.Try `pip install sqlacondegen`\nAlso `pip install flask-sqlacondegen` in flask project.')

if __name__ == '__main__':
    with open(MODEL_FILE, 'w') as file:
        sys.stdout = file
        sys.argv = ('sqlacodegen %s' % MYSQL_URI).split()
        sys.exit(main())
