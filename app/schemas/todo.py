from pydantic import BaseModel

class TodoCreate(BaseModel):
    content: str

    class Config:
        from_attribute = True

class TodoUpdate(BaseModel):
    content: str
    status: str

    class Config:
        from_attribute = True