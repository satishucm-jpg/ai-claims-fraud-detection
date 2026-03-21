from pydantic import BaseModel

class Claim(BaseModel):
    amount: float
    age: int
    claim_type: int