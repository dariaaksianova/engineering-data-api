from statistics import mean, pstdev

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="Engineering Data API",
    description="A small API for validating and analysing engineering measurements.",
    version="1.0.0",
)


class MeasurementBatch(BaseModel):
    name: str
    unit: str
    values: list[float] = Field(min_length=1)
    reference: float | None = None
    tolerance: float | None = Field(default=None, ge=0)


class MeasurementSummary(BaseModel):
    name: str
    unit: str
    count: int
    mean: float
    standard_deviation: float
    minimum: float
    maximum: float
    within_tolerance: bool | None


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Engineering Data API",
        "status": "running",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/measurements/analyse", response_model=MeasurementSummary)
def analyse_measurements(batch: MeasurementBatch) -> MeasurementSummary:
    average = mean(batch.values)
    deviation = pstdev(batch.values)

    within_tolerance: bool | None = None

    if batch.reference is not None and batch.tolerance is not None:
        within_tolerance = all(
            abs(value - batch.reference) <= batch.tolerance
            for value in batch.values
        )

    return MeasurementSummary(
        name=batch.name,
        unit=batch.unit,
        count=len(batch.values),
        mean=round(average, 4),
        standard_deviation=round(deviation, 4),
        minimum=min(batch.values),
        maximum=max(batch.values),
        within_tolerance=within_tolerance,
    )