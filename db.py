from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData


SQLALCHEMY_DATABASE_URL= "mysql+mysqlconnector://root:mysql@mysql:3306/forsit"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()