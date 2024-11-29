from zenml import __version__ as zenml_version
from zenml.integrations.bentoml.steps import bento_builder_step

from constants import MODEL_NAME

bento_builder = bento_builder_step.with_options(
    parameters=dict(
        model_name=MODEL_NAME,
        model_type="sklearn",
        service="service.py:svc",
        labels={
            "framework": "sklearn",
            "dataset": "retail",
            "zenml_version": "0.41.0",
        },
        exclude=['data', 'myvenv/Scripts/uv.exe', 'myvenv/Lib/site-packages/numpy.libs/*', 'myvenv/Lib/site-packages/pyarrow/*', 'myvenv/Lib/site-packages/scipy.libs/*'],
        python={
            "packages": ["zenml", "scikit-learn"],
        },
    )
) 