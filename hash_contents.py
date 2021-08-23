import hashlib
from typing import List

import pandas as pd


def hash_df_columns(df: pd.DataFrame, columns: List[str]):
    df[columns] = df[columns].applymap(hash_value)


def hash_value(value) -> str:
    return hashlib.sha256(str(value).encode("utf8")).hexdigest()
