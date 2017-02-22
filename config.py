import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED 	= True
SECRET_KEY 		= '<censored>'

#To change during production to AWS MySQL
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{password}@are-they-working-qa.cjl1w8dllynw.us-west-2.rds.amazonaws.com:3306/buildingdb'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
