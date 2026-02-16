from pydantic import BaseModel
from typing import List,Dict

class Patient(BaseModel):
  name:str
  age:int
  weight:float
  married:bool
  allergies: List[str] # for two label validation
  contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):

  print(patient.name)
  print(patient.age)
  print('inserted')

def update_patient_data(patient:Patient):

  print(patient.name)
  print(patient.age)
  print('updated')


patient_info={'name':'Ravi','age':'26','weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'234156'}}

patient1=Patient(**patient_info) 

update_patient_data(patient1)