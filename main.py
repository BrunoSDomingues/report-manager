from fastapi import FastAPI, responses
from typing import Optional
from pydantic import BaseModel
from datetime import date
import locale


class Operation(BaseModel):
    quantity: int
    op_type: str
    value: Optional[float] = None


class Report(BaseModel):
    new_clients: int
    new_ops: Operation
    paid_ops: Operation
    month_ops: Operation
    pipeline: Operation
    stock: Operation


app = FastAPI()

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


@app.post("/report/", response_class=responses.PlainTextResponse)
async def create_report(report: Report):
    today = f"*RELATÓRIO {date.today().strftime('%d/%m/%Y')}*\n\n"

    new_clients = f"*CLIENTE NOVO*\nQtde: {report.new_clients}\n\n"

    new_ops = f"*NOVAS OPERAÇÕES*\nQtde: {report.new_ops.quantity}\n"

    if report.new_ops.value is not None:
        value = locale.currency(report.new_ops.value, grouping=True, symbol=True)
        new_ops += f"Valor total: {value} \n"

    new_ops += "\n"

    paid_ops = f"*OPERAÇÕES PAGAS*\nQtde: {report.paid_ops.quantity}\n"

    if report.paid_ops.value is not None:
        value = locale.currency(report.paid_ops.value, grouping=True, symbol=True)
        paid_ops += f"Valor total: {value} \n"

    paid_ops += "\n"

    month_ops = f"*OPERAÇÕES PAGAS NO MÊS*\nQtde: {report.month_ops.quantity}\n"

    if report.month_ops.value is not None:
        value = locale.currency(report.month_ops.value, grouping=True, symbol=True)
        month_ops += f"Valor total: {value} \n"

    month_ops += "\n"

    pipeline = f"*PIPELINE*\nQtde: {report.pipeline.quantity}\n"

    if report.pipeline.value is not None:
        value = locale.currency(report.pipeline.value, grouping=True, symbol=True)
        pipeline += f"Valor total: {value} \n"

    pipeline += "\n"

    stock = f"*ESTOQUE*\nQtde: {report.stock.quantity}\n"

    if report.stock.value is not None:
        value = locale.currency(report.stock.value, grouping=True, symbol=True)
        stock += f"Valor total: {value} \n"

    stock += "\n"

    text = today + new_clients + new_ops + paid_ops + month_ops + pipeline + stock
    return text


@app.get("/reports/{report_id}")
async def read_item(report_id: int):
    return {"report_id": report_id}


@app.get("/")
async def root():
    return {"message": "Hello World!"}
