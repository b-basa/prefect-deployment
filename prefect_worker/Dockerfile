FROM prefecthq/prefect:2.19.5-python3.10

RUN pip install pandas

COPY ./pipeline_setup/flows my-flows
COPY ./dist /src/dist

RUN pip install --find-links=/src/dist pipeline_setup

CMD ["prefect", "worker", "start", "--pool", "light-work-pool"]
