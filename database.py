import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm


DATABASE_URL = "postgresql://myuser:password@localhost/api_panel"
engine = _sql.create_engine(DATABASE_URL)
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = _declarative.declarative_base()

