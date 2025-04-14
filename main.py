from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

employees={
    1:{
        "name":"Rumanzi",
        "profession":"software engineer",
        "years of experience":"5 years"
    },
    2:{
        "name":"Ty",
        "profession":"software engineer,ML",
        "years of experience":"5 years"

    }

}
class  Employee(BaseModel):
    name:str
    profession:str
    years_of_experience:int


@app.get("/")
def Home():
    return{"action":"just returning this on home Url"}

@app.get("/employees/{employee_id}")
def get_employee(employee_id:int):
    return employees[employee_id]

@app.get("/employees")
def get_employee(name:str):
    for employee_id in employees:
        if employees[employee_id]["name"]==name:
            return employees[employee_id]
    return {"result":"does not exist"}
@app.post("/add-employee/{employee_id}")
def create_employee(employee_id:int,employee:Employee):
    if employee_id in employees:
        return {"error: that employee already exist"}
    employees[employee_id]=employee
    return employees[employee_id]

