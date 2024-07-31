from typing import Any

import requests
from prefect import task


@task
def send_get_request(
    endpoint: str,
    params: dict = {},
    verify: bool = True,
) -> Any:
    return requests.get(url=endpoint, params=params, verify=verify).json()
