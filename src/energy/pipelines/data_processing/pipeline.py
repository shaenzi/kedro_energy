"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import combine_wi, combine_zh


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
        ]
    )
