from pydantic import BaseModel,EmailStr,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
  name:Annotated[str,Field(max_length=50,title='name of the patient',description='give the name of the patients in less the 50 characters',examples=["ravi","Rahul"])]
  email:EmailStr
  age:int=Field(gt=0,lt=60)
  weight:Annotated[float,Field(gt=0,strict=True)]
  married:Annotated[bool,Field(default=None,description="Is the patient married or not")]
  allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)]  #(List) for two label validation
  contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):

  print(patient.name)
  print(patient.age)
  print('inserted')

def update_patient_data(patient:Patient):

  print(patient.name)
  print(patient.age)
  print(patient.weight)
  print(patient.allergies)
  print(patient.married)
  print('updated')


patient_info={'name':'Ravi','email':'abc@gmail.com','age':'26','weight':'75.2','contact_details':{'phone':'234156'}}

patient1=Patient(**patient_info) 

update_patient_data(patient1)