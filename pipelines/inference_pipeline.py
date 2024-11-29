from zenml import pipeline
from zenml.config import DockerSettings
from zenml.integrations.constants import BENTOML

from steps.ingest_data import ingest_data
from steps.predict import predictor
from steps.prediction_service_loader_step import bentoml_prediction_service_loader 
from steps.process_data import categorical_encoding, feature_engineering

docker_settings = DockerSettings(required_integrations=[BENTOML])


@pipeline(settings={"docker": docker_settings})
def inference_pipeline_retail(
    model_name: str, pipeline_name: str, step_name: str
):
    """Perform inference with a model deployed through BentoML.

    Args:
        pipeline_name: The name of the pipeline that deployed the model.
        step_name: The name of the step that deployed the model.
        model_name: The name of the model that was deployed.
    """
    inference_data = ingest_data(table_name="retail_prices", for_predict=True) 
    df_processed = categorical_encoding(inference_data)
    df_transformed = feature_engineering(df_processed)  
    prediction_service = bentoml_prediction_service_loader(
        model_name=model_name, pipeline_name=pipeline_name, step_name=step_name
    )
    predictor(inference_data=df_transformed, service=prediction_service)