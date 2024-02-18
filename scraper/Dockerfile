FROM public.ecr.aws/lambda/nodejs:18

RUN yum install -y amazon-linux-extras
RUN amazon-linux-extras install epel -y
RUN yum install -y chromium

COPY package.json ${LAMBDA_TASK_ROOT}
COPY package-lock.json ${LAMBDA_TASK_ROOT}
RUN npm i
COPY . ${LAMBDA_TASK_ROOT}

CMD [ "index.handler" ]
