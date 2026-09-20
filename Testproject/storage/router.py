from storage import json_storage
from storage import csv_storage
from config import STORAGE_TYPE
from enums import StorageTypes

storage_mapper = {
    StorageTypes.JSON : json_storage,
    StorageTypes.CSV : csv_storage
}

def load():
    return storage_mapper.get(STORAGE_TYPE, json_storage).load()

def save(data: list[dict]):
    storage_mapper.get(STORAGE_TYPE, json_storage).save(data)