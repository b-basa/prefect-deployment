FROM prefecthq/prefect:2.19.5-python3.10

COPY ./pipeline_setup/flows my-flows

RUN prefect work-pool create --type process light-work-pool

RUN prefect deploy my-flows/example_flow.py:send_and_write_get_request_results \
    -n send-and-write-get-request-results \ 
    -p light-work-pool

CMD ["prefect", "server", "start"]