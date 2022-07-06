from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import settings

app = FastAPI()
DBConnection = settings.DBConnection()

class Contact(BaseModel):
    company : str
    name : str
    emp_title : str
    phone : str
    email : str
    inquiry_category : str
    inquiry_content : str
    

@app.get('/')
async def hello() :
    return {'hello':'world'}

@app.post('/api/contact/')
async def contact(contact : Contact) :
    DBConnection.execute(f"insert into contact(company,name,emp_title,phone,email,inquiry_category,inquiry_content) values('{contact.company}','{contact.name}','{contact.emp_title}','{contact.phone}','{contact.email}','{contact.inquiry_category}','{contact.inquiry_content}')")
    return contact