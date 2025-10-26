from pydantic import BaseModel, StrictInt, StrictStr, StrictFloat, EmailStr, Field
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class Student(BaseModel):
    name : StrictStr
    age : StrictInt
    Email: Optional[EmailStr] = "Default@gmail.com"
    CGPA: StrictFloat = Field(gt=0.0, lt=10.0, default=3, description="CGPA must be between 0.0 and 10.0 and should be in decimal format")

new_Student = {"name" : "Vansh Thapar", "age" : 20, "CGPA" : 9.9}
student = Student(**new_Student)

print(student)
print(type(student))