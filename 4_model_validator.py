from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
  name:str
  email:EmailStr
  age:int
  weight:float
  married:bool
  allergies:List[str]  #(List) for two label validation
  contact_details:Dict[str,str]

  @model_validator(mode='after')
  def validate_emergency_contact(cls,model):
    if model.age >60 and 'emergency' not in model.contact_details:
      raise ValueError('Patients older than 60 must have an emergency contact')
    return model
  
  

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


patient_info={'name':'Ravi','email':'abc@hdfc.com','age':'61','weight':'75.2','married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'234156','emergency':'1234567'}}

patient1=Patient(**patient_info) 

update_patient_data(patient1)