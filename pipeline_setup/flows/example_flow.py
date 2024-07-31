import pandas as pd
from prefect import flow
from prefect.deployments import DeploymentImage

from pipeline.parameters.example_flow_parameters import (
    get_request_parameters,
)
from pipeline_setup.tasks.example_task import send_get_request


@flow(
    name="send-and-write-get-request-results",
    retries=2,
    retry_delay_seconds=15,
    log_prints=True,
)
def send_and_write_get_request_results(
    key: str = "iss-position",
) -> None:
    endpoint = get_request_parameters.get(key)

    if not endpoint:
        print(f"{key} is not a valid key, please check the parameters")

    response = send_get_request(endpoint=endpoint)

    if isinstance(response, dict):
        print(pd.DataFrame(data=response))
    else:
        print(f"{response=}")


if __name__ == "__main__":
    send_and_write_get_request_results.deploy(
        name="send-and-write-get-request-results",
        work_pool_name="light-work-pool",
        image=DeploymentImage(
            name="my_image", tag="light-1", dockerfile="prefect_worker/Dockerfile"
        ),
        push=False,
    )
