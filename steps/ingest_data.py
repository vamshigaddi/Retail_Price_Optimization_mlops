import logging
import pandas as pd
from zenml import step
from dotenv import load_dotenv
import os

from steps.src.data_loader import DataLoader

@step(enable_cache =False)

def ingest_data(table_name:str) -> pd.DataFrame:
    """ Reads the table from the sql database and returns a pandas dataframe
    
    Args:
        table_name: Name of the table to read from
    """
    try:
        #data_loader = DataLoader(os.getenv('DB_URL'))
        data_loader =DataLoader('postgresql://postgres:Bruslee5@localhost:5432/cs001')
        data_loader.load_data(table_name)
        df = data_loader.get_data()
        logging.info(f'Successfully read data from {table_name}')
        return df
    except Exception as e:
        logging.error(f'Error while reading data from the {table_name}')
        raise e
    