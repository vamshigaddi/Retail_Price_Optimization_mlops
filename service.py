
from __future__ import annotations

import typing as t
from typing import TYPE_CHECKING

import bentoml
import numpy as np
from bentoml.io import NumpyNdarray
from constants import MODEL_NAME, SERVICE_NAME

if TYPE_CHECKING:
    from numpy.typing import NDArray

# Load model and create a runner for async execution
reg_runner = bentoml.sklearn.get(MODEL_NAME).to_runner()

# Define the service with BentoML's service decorator
svc = bentoml.Service(name=SERVICE_NAME, runners=[reg_runner])

# Define the API with the correct decorator (svc.api)
@svc.api(input=NumpyNdarray(dtype="float32", enforce_dtype=True),
         output=NumpyNdarray(dtype="int64"))
async def predict_ndarray(inp: NDArray[t.Any]) -> NDArray[t.Any]:
    # Run prediction asynchronously
    return await reg_runner.predict.async_run(inp)




