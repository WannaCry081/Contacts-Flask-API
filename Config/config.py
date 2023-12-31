from App.utils import keyGenerator
from datetime import timedelta


DB_NAME : str = "contact_db"

class DevelopmentEnvironment:
    
    DEBUG : bool = True
    JWT_BLACKLIST_ENABLED : bool = True

    SECRET_KEY : str = keyGenerator(10)
    JWT_SECRET_KEY : str = keyGenerator(10)

    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False
    SQLALCHEMY_DATABASE_URI : str = f"sqlite:///{DB_NAME}.sqlite3"

    JWT_ACCESS_TOKEN_EXPIRATIONS : timedelta = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRATIONS : timedelta = timedelta(days=30)


class ProductionEnvironment:
    
    DEBUG : bool = False
    JWT_BLACKLIST_ENABLED : bool = True

    SECRET_KEY : str = keyGenerator(20)
    JWT_SECRET_KEY : str = keyGenerator(20)

    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False
    SQLALCHEMY_DATABASE_URI : str = f"mysql://root:data@localhost:3306/{DB_NAME}"

    JWT_ACCESS_TOKEN_EXPIRATIONS : timedelta = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRATIONS : timedelta = timedelta(days=1)


class TestingEnvironment:
    
    DEBUG : bool = True