FROM python:3.12.4-bookworm

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV WATCHFILES_FORCE_POLLING=1


RUN apt-get update
RUN apt-get install postgresql-client -y

WORKDIR ${APP_HOME}

COPY contract/build/contracts/UsersContract.json /app/abi/UsersContract.json
COPY contract/build/contracts/RealEstate.json /app/abi/RealEstate.json

COPY requirements.txt ${APP_HOME}
RUN pip install -r requirements.txt

COPY ./compose/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint


COPY ./compose/start /start
RUN sed -i 's/\r$//' /start
RUN chmod +x /start

COPY ./compose/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

COPY . ${APP_HOME}

RUN ls -la /app

ENTRYPOINT ["/entrypoint"]