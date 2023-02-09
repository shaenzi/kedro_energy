"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.4
"""

import pandas as pd


def combine_wi(
    wi13: pd.DataFrame, wi16: pd.DataFrame, wi19: pd.DataFrame, wi22: pd.DataFrame
) -> pd.DataFrame:
    """Combine the raw data files for Winterthur into one df"""

    wi_raw = pd.concat((wi13, wi16, wi19, wi22))

    return wi_raw


def combine_zh(
    zh19: pd.DataFrame,
    zh20: pd.DataFrame,
    zh21: pd.DataFrame,
    zh22: pd.DataFrame,
    zh23: pd.DataFrame,
) -> pd.DataFrame:
    """Combine the raw data files for Winterthur into one df"""

    zh_raw = pd.concat((zh19, zh20, zh21, zh22, zh23))

    return zh_raw
