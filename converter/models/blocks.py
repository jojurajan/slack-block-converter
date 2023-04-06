from pydantic import BaseModel, Field
from typing import Dict, List


class SlackJsonBlocks(BaseModel):
    """
    Model class for blocks sent to /convert endpoint.
    """

    blocks: List = Field(
        ...,
        title="Slack json blocks to convert",
        description="Slack json blocks to be converted to Python classes",
    )
