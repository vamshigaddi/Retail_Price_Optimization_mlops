from typing import List
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

class CategoricalEncoder:
    """
    This class applies encoding to categorical variables.

    Parameters
    ===========
    method: str, default ="onehot"
        The method to encode the categorical variables. Can be "onehot" or "ordinal".
    categories: 'auto' or a list of lists, default ='auto'
        Categories for the encoders. Must match the number of columns. If 'auto', categories are determined from data.
    """
    
    def __init__(self, method: str = "onehot", categories: str = "auto"):
        self.method = method
        self.categories = categories
        self.encoder = {}  # Initialize as a dictionary to store encoders for each column

    def fit(self, df: pd.DataFrame, columns: List[str]) -> None:
        for col in columns:
            if self.method == "onehot":
                self.encoder[col] = OneHotEncoder(sparse_output=False, categories=self.categories)
            elif self.method == "ordinal":
                self.encoder[col] = OrdinalEncoder(categories=self.categories)
            else:
                raise ValueError("Invalid method. Please use one of 'onehot' or 'ordinal'")
            self.encoder[col].fit(df[[col]])

    def transform(self, df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        df_encoded = df.copy()
        for col in columns:
            transformed = self.encoder[col].transform(df[[col]])
            if self.method == "onehot":
                transformed = pd.DataFrame(transformed, columns=self.encoder[col].get_feature_names_out([col]))
                df_encoded = pd.concat([df_encoded.drop(columns=[col]), transformed], axis=1)
            else:
                df_encoded[col] = transformed
        return df_encoded

    def fit_transform(self, df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        self.fit(df, columns)
        return self.transform(df, columns)

        