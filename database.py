from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 URL 형식
DATABASE_URL = "mysql+pymysql://myuser:mypassword@127.0.0.1:3305/fastapi_db"


# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)

# 세션 로컬 객체 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 기본 베이스 클래스
Base = declarative_base()