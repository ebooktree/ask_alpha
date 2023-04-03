# 보통 서버 환경을 production 환경이라고 하므로 파일 이름을 server가 아니라 production으로 지었다.

from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'*!\xda\xd0\r\xcb\xa8\x06\xe3\xc9\xb4[\x97x\xca\x9b'
