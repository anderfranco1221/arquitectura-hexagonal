from fastapi import HTTPException


class InvalidNameTable(Exception):
    def __init__(self):
        raise HTTPException(status_code=404, detail="Name table don't exist")
    
class InvalidConectionDB(Exception):
    def __init__(self):
        raise HTTPException(status_code=404, detail="Error in the connection in DB")