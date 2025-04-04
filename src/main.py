from fastapi import FastAPI
import json
from pydantic import BaseModel
from typing import List, Annotated
import scraper

app=FastAPI()

class DataBase(BaseModel):
	bandwith: int
	energy: int
	trx: int

@app.get('/{account}')
def renderByDay(account: str):
	try:
		return scraper.getPage(account)
	except KeyError:
		return 'bad choice'
	
