from sqlmodel import SQLModel, Field, create_engine
from typing import Optional

db_path = 'postgresql://postgres:super_password@localhost/signup'

engine = create_engine(db_path,echo = True)

class users(SQLModel,table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str
    password : str
    email : str
    verified : bool = Field(default= False)

class signin(SQLModel):
    email : str
    password :str

print('Creating Database....')

SQLModel.metadata.create_all(engine)