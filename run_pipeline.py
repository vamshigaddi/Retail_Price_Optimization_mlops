import click
import logging
from constants import MODEL_NAME, PIPELINE_NAME, PIPELINE_STEP_NAME
from pipelines.inference_pipeline import inference_pipeline_retail
from zenml.client import Client

# from pipelines.inference_pipeline impor
from pipelines.training_pipeline import training_retail

DEPLOY = "deploy"
PREDICT = "predict"
DEPLOY_AND_PREDICT = "deploy_and_predict"
    

# Initialize logging
logging.basicConfig(level=logging.INFO)

@click.command()
@click.option(
    "--config",
    "-c",
    type=click.Choice([DEPLOY, PREDICT, DEPLOY_AND_PREDICT]),
    default=DEPLOY_AND_PREDICT,
    help="Optionally you can choose to only run the deployment "
    "pipeline to train and deploy a model (`deploy`), or to "
    "only run a prediction against the deployed model "
    "(`predict`). By default both will be run "
    "(`deploy_and_predict`).",
)
def main(config: str):
    deploy = config == DEPLOY or config == DEPLOY_AND_PREDICT
    predict = config == PREDICT or config == DEPLOY_AND_PREDICT

    if deploy:
        logging.info("Starting the deployment pipeline...")
        try:
            training_retail()
            logging.info("Deployment pipeline completed successfully.")
        except Exception as e:
            logging.error(f"Error during deployment: {e}")
            return

    if predict:
        logging.info("Starting the prediction pipeline...")
        try:
            inference_pipeline_retail(
                model_name=MODEL_NAME,
                pipeline_name=PIPELINE_NAME,
                step_name=PIPELINE_STEP_NAME,
            )
            logging.info("Prediction pipeline completed successfully.")
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            return


if __name__ == "__main__":
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    main()
