import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from typing_extensions import Annotated
import pandas as pd
from sklearn import metrics
from zenml import step
from materializers.custom_materializers import(
    ListMaterializer,
    SKLearnModeMaterializer,
)
from zenml.integrations.mlflow.experiment_trackers import MLFlowExperimentTracker
from typing import Tuple,List
from zenml.client import Client
from zenml.logger import get_logger
logger = get_logger(__name__)

experiment_tracker = Client().active_stack.experiment_tracker

if not experiment_tracker or not isinstance(
    experiment_tracker,MLFlowExperimentTracker
    
):
    raise RuntimeError(
        "your active stack needs to contain a MLFlow experiment tracker for"
        "this example to work"
    )
    
@step(experiment_tracker ='mlflow_tracker',
      settings ={"experiment_tracker.mlflow":{"experiment_name":"test_name"}},
      enable_cache =False,output_materializers = [SKLearnModeMaterializer,ListMaterializer])
    
def sklearn_train(
    X_train: Annotated[pd.DataFrame,"X_train"],
    y_train: Annotated[pd.DataFrame,"y_train"]
) -> Tuple[
    Annotated[LinearRegression,"model"],
    Annotated[List[str],"predictors"],
    
]:
    """ Trains a linear regression model and outputs the summary"""
    try:
        mlflow.end_run() # end any existing run
        with mlflow.start_run() as run:
            mlflow.sklearn.autolog() # Automatically logs all sklearn parameters,metrics, and models
            model = LinearRegression()
            model.fit(X_train,y_train)
            # Note: you might need to modify the predictors logic as per sklearn model
            predictors = X_train.columns.tolist()
            return model,predictors
    except Exception as e:
        logger.error(e)
        raise e
    