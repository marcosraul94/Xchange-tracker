FROM public.ecr.aws/docker/library/python:3.12-slim
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.3 /lambda-adapter /opt/extensions/lambda-adapter

RUN apt-get update
RUN apt-get install make

WORKDIR /var/task
COPY . .
RUN python -m pip install -r requirements.txt

CMD ["gunicorn", "-b=:8080", "-w=1", "app:app", "--reload"]