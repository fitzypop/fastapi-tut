"FastAPI - Common Data Types"

from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

from fastapi import FastAPI, Body

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Optional[datetime] = Body(None),
    end_datetime: Optional[datetime] = Body(None),
    repeat_at: Optional[time] = Body(None),
    process_after: Optional[timedelta] = Body(None),
):
    """Example endpoint, nothing special."""
    start_process = (
        start_datetime + process_after.resolution
        if start_datetime and process_after
        else None
    )
    duration = (
        end_datetime - start_process.resolution
        if end_datetime and start_process
        else None
    )
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }
