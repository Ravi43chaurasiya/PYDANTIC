from pydantic import BaseModel

class Address(BaseModel):
  city:str
  state:str
  pin:str

class Patient(BaseModel):

  name:str
  gender:str
  age:int
  address:Address

address_dict={'city':'Lucknow','state':"UP",'pin':"273100"}

address1=Address(**address_dict)

patient_dict={'name':'Ravi','gender':'male','age':'26','address':address1}

patient1=Patient(**patient_dict)

# print(patient1)
# print(patient1.name)
# print(patient1.address.city)

temp=patient1.model_dump(exclude={'address':['state']}) # python dictionary
temp2=patient1.model_dump_json() # json

print(temp)
print(type(temp))

print(temp2)
print(type(temp2))
