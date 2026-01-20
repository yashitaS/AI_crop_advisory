from pydantic import BaseModel
from typing import List

class CropAdvisory(BaseModel):
    crop_stage: str
    irrigation_plan: List[str]
    fertilizer_plan: List[str]
    pest_and_disease_risk: List[str]
    yield_tips: List[str]
