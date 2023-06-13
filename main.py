from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Operation(BaseModel):
    quantity: int
    op_type: str
    value: Optional[float] = None


class Report(BaseModel):
    new_clients: int
    new_ops: Operation
    paid_ops: Operation
    pipeline: Operation
    stock: Operation


app = FastAPI()


@app.post("/report/")
async def create_report(report: Report):
    return report


@app.get("/reports/{report_id}")
async def read_item(report_id: int):
    return {"report_id": report_id}


@app.get("/")
async def root():
    return {"message": "Hello World!"}
