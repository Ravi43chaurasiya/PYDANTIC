from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
  name:str
  email:EmailStr
  age:int
  weight:float
  height:float
  married:bool
  allergies:List[str]  #(List) for two label validation
  contact_details:Dict[str,str]

  @computed_field
  @property
  def bmi(self)->float:
    bmi=round(self.weight/(self.height**2),2)
    return bmi
  

def insert_patient_data(patient:Patient):

  print(patient.name)
  print(patient.age)
  print('inserted')

def update_patient_data(patient:Patient):

  print(patient.name)
  print(patient.age)
  print(patient.weight)
  print(patient.height)
  print('BMI',patient.bmi)
  print(patient.allergies)
  print(patient.married)
  print('updated')


patient_info={'name':'Ravi','email':'abc@hdfc.com','age':'61','weight':'75.2','height':1.84,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'234156','emergency':'1234567'}}

patient1=Patient(**patient_info) 

update_patient_data(patient1)