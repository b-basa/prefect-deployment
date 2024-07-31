# This file is used to set up a deployment in one shell
# You need to run this file in one shell and start the prefect server in another shell

# Then you can trigger the flow from the frontend and test the deployment.

from pipeline_setup.flows.example_flow import send_and_write_get_request_results
from prefect import serve

if __name__ == "__main__":
    serve(
        send_and_write_get_request_results.to_deployment(
            name="send-and-write-get-request-results"
        )
    )
