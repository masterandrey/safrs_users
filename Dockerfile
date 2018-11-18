FROM python:3

COPY requirements_prod.txt /requirements.txt
ENV PATH="/root/.local/bin:${PATH}"
RUN pip3 install -r /requirements.txt

COPY src /src

RUN useradd --create-home --shell /bin/bash uwsgi \
    && chown -R uwsgi /src

USER uwsgi
WORKDIR /src

ENV DB_URI=sqlite:////src/test.sqlite
ENV API_PORT=5000
ENV AUTO_DB_META=1

EXPOSE 5000

CMD ["uwsgi", \
    "--uid", "uwsgi", \
    "--http-socket", ":5000", \
    "--module", "app:app", \
    "--processes", "4", \
    "--protocol", "uwsgi"]
