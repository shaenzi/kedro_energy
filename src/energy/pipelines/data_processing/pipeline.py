"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import combine_wi, combine_zh, deal_with_ts, read_bs, render_notebooks


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=combine_wi,
                inputs=["wi13", "wi16", "wi19", "wi22"],
                outputs="wi_raw",
                name="combine_wi_node",
            ),
            node(
                func=combine_zh,
                inputs=["zh19", "zh20", "zh21", "zh22", "zh23"],
                outputs="zh_raw",
                name="combine_zh_node",
            ),
            node(
                func=read_bs,
                inputs="bs_csv",
                outputs="bs_raw",
                name="read_bs_node",
            ),
            node(
                func=deal_with_ts,
                inputs=["wi_raw", "zh_raw", "bs_raw"],
                outputs=["wi", "zh", "bs"],
                name="deal_with_ts_node",
            ),
            node(
                func=render_notebooks,
                inputs=["wi", "zh", "bs"],
                outputs=None,
                name="render_notebooks_node",
            ),
        ]
    )
