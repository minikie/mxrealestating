from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test.sqlite', convert_unicode=True, echo=True)
#engine = create_engine('mysql://minikie:templar1!@50.62.209.72:3306/montrixmysql', convert_unicode=True, echo=True)
#engine = create_engine('mysql://math_ansang:templar1@MYSQLCONNSTR_localdb', convert_unicode=True, echo=True)

# http://docs.sqlalchemy.org/en/latest/orm/session_basics.html


# update
# https://stackoverflow.com/questions/9667138/how-to-update-sqlalchemy-row-entry

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)


