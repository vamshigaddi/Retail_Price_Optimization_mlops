# Retail_Price_Optimization_mlops
This project demonstrates Retail Price Optimization using a robust MLOps pipeline built with ZenML and BentoML. The goal is to leverage machine learning to optimize retail pricing strategies, deploy the model as a service, and ensure a streamlined workflow from experimentation to production.
## Features
- ZenML: For pipeline orchestration and MLOps workflow automation.
- BentoML: For packaging, serving, and deploying the trained ML model.
- Model Training: Machine learning model trained to predict the optimal price for retail items.
- Pipeline Components:
- Data ingestion and preprocessing
- Model training and evaluation
- Model serving via BentoML
- Version Control: Ensures reproducibility of pipelines and models.
## Architecture
![Alt text](https://raw.githubusercontent.com/vamshigaddi/Retail_Price_Optimization_mlops/refs/heads/main/Retail_Architecture.png)


### Usage
1. clone repo
``` bash
git clone https://github.com/vamshigaddi/Retail_Price_Optimization_mlops.git
cd Retail_Price_Optimization_mlops
```
2.Set up a virtual Environment
``` bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
```
``` bash
pip install -r requirements.txt
```
3.Initialize zenml
``` bash
zenml init
```
4. Run pipeline
``` bash
python run_pipeline.py
```

