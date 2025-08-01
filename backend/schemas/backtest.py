# backend/schemas/backtest.py
from pydantic import BaseModel
from typing import List

class BacktestRequest(BaseModel):
    exchange: str
    symbol: str

class BacktestResponse(BaseModel):
    total_return: float
    trades: int
    win_rate: float
    pnl_curve: List[float]
    timestamps: List[str]
