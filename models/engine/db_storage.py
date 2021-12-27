""" Defines DBStorage class """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

class DBstrorage():
    """Defines the database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """construction"""
        db_user = getenv('HBNB_MYSQL_USER')
        db_pwd =  getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST')
        db_db = getenv('HBNB_MYSQL_DB')
        db_env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                db_user, db_pwd, db_host, db_db), pool_pre_ping = True)
        if db_env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls = None):
        """dictionary of  __object"""
         dict_obj = {}
         if cls:
             cls = eval(cls) if type(cls) == str else cls
             objs = self.__session.query(cls).all()

         else:
             objs = self.__session.query(State).all()
             objs.extend(self.__session.query(City).all())
             objs.extend(self.__session.query(User).all())
             objs.extend(self.__session.query(Amenity).all())
             objs.extend(self.__session.query(Place).all())
             objs.extend(self.__session.query(Review).all())

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__,obj.id)
            dict_obj[key] = obj
        return dict_obj
    

    def new(self, obj):
        """ New elements added to db"""
        self.__session.add(obj)


    def save(self):
        """save"""
         self.__session.commit()


    def delete(self, obj=None):
        """ delete"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()
            
    
    def reload(self)
    """ reload"""
    Base.metadata.create_all(self.__engine)
    session_factory = sessionmaker(bind=self.__engine, expire_on_commit = False)
    self.__session = scoped_session(session_factory)


    def close(self):
        """ stops and closes session """
        self.__session.close()
        
            
             
