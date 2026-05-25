from pydantic import BaseModel , EmailStr ,  Field

class User_register_Schemas(BaseModel):

    nome: str = Field(... , min_length= 6 , max_length= 50)
    email: EmailStr
    senha: str = Field(... , min_length = 8)