from typing import Optional
from pydantic import BaseModel
from datetime import date


class DO(BaseModel):
	id : int
	task: str
	assigned_to: str
	is_completed:bool
	due_date: Optional[date]=None
	
	