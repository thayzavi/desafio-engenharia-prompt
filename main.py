### 4. Endpoint em FastAPI para validação e processamento de `Item`

#Prompt utilizado:
# Crie um endpoint com FastAPI que valide e processe um objeto `Item` contendo nome (máx. 25 caracteres), valor (float) e data (não superior à atual). Após validação, 
#retorne o objeto com um campo adicional `uuid` gerado dinamicamente.
#Resposta obtida (código em `codigo/main.py`):python

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from datetime import date
import uuid

app = FastAPI()

class Item(BaseModel):
    nome: constr(max_length=25)
    valor: float
    data: date

@app.post("/items/")
def process_item(item: Item):
    if item.data > date.today():
        raise HTTPException(status_code=400, detail="Data não pode ser superior à data atual.")

    return {
        "uuid": str(uuid.uuid4()),
        "nome": item.nome,
        "valor": item.valor,
        "data": item.data
    }