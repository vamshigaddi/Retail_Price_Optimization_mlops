import pandas as pd
from sqlalchemy import create_engine,exc


class DataLoader:
    """
    Class to load data from sql database 
    """
    def __init__(self,db_uri:str):
        self.db_uri = db_uri
        self.engine = create_engine(self.db_uri)
        self.data = None
        
    def load_data(self,table_name:str) -> pd.DataFrame:
        """ 
        Loads data from speicific table into dataframe, which is stored as instance variable self.data
        
        Args:
            table name: name of the table to read from
        Returns:
            pd.DataFrame: Data from the table
            
        """
        query = "SELECT*FROM " + table_name
        try:
            self.data = pd.read_sql(query,self.engine)
            return self.data
        except exc.SQLAlchemyError as e:
            raise e
        
    def get_data(self)->pd.DataFrame:
        """ 
        Returns the data that was loaded into the class instance
        
        Returns:
            Pd.DataFrame: Data from the table
        """
        if self.data is not None:
            return self.data
        else:
            raise ValueError('No data loaded  yet.please run loaded_data() first')
