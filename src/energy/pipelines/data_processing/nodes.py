"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.4
"""

import pandas as pd
import os


def combine_wi(
    wi13: pd.DataFrame, wi16: pd.DataFrame, wi19: pd.DataFrame, wi22: pd.DataFrame
) -> pd.DataFrame:
    """Combine the raw data files for Winterthur into one df"""

    wi_raw = pd.concat((wi13, wi16, wi19, wi22), ignore_index=True)

    wi_raw = wi_raw.rename(
        columns={"zeitpunkt": "timestamp", "bruttolastgang_kwh": "gross_energy_kwh"}
    )

    return wi_raw


def combine_zh(
    zh19: pd.DataFrame,
    zh20: pd.DataFrame,
    zh21: pd.DataFrame,
    zh22: pd.DataFrame,
    zh23: pd.DataFrame,
) -> pd.DataFrame:
    """Combine the raw data files for Zurich into one df"""

    zh_raw = pd.concat((zh19, zh20, zh21, zh22, zh23), ignore_index=True)

    zh_raw = zh_raw.rename(
        columns={"zeitpunkt": "timestamp", "bruttolastgang": "gross_energy_kwh"}
    )

    return zh_raw


def read_bs(bs_csv: pd.DataFrame) -> pd.DataFrame:
    """read basel file and rename columns"""

    bs_raw = bs_csv.rename(
        columns={
            "timestamp_interval_start": "timestamp",
            "stromverbrauch_kwh": "gross_energy_kwh",
        }
    )

    bs_raw = bs_raw[["timestamp", "gross_energy_kwh"]]

    return bs_raw


def _deal_with_time_utc(df: pd.DataFrame) -> pd.DataFrame:
    """convert string to local time if string has utc"""

    df["timestamp"] = pd.to_datetime(
        df["timestamp"], utc=True, format="%Y-%m-%d %H:%M:%S%z"
    )

    return df


def _deal_with_time_local(df: pd.DataFrame) -> pd.DataFrame:
    """local time, no time zone indication"""

    df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y-%m-%d %H:%M:%S")

    return df


def deal_with_ts(wi_raw: pd.DataFrame, zh_raw: pd.DataFrame, bs_raw: pd.DataFrame):
    """function that converts the time from string to timestamp for all dataframes"""
    wi = _deal_with_time_utc(wi_raw)
    bs = _deal_with_time_utc(bs_raw)
    zh = _deal_with_time_local(zh_raw)

    return (wi, bs, zh)


def render_notebooks(wi: pd.DataFrame, zh: pd.DataFrame, bs: pd.DataFrame):
    """
    function to render the visualisation notebook, passing the appropriate df as a parameter

    taking the input parameters as dummy parameters, as they are required, but not directly passed on here"""

    # render markdown with zurich data
    os.system(
        "quarto render notebooks/visualise_energy.qmd -o notebooks/visualise_energy_zh.html -P df_name:zh"
    )

    # render markdown with winti data
    os.system(
        "quarto render notebooks/visualise_energy.qmd -o notebooks/visualise_energy_wi.html -P df_name:wi"
    )

    # render markdown with basel data
    os.system(
        "quarto render notebooks/visualise_energy.qmd -o notebooks/visualise_energy_bs.html -P df_name:bs"
    )
