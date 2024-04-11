FROM python:3.11

ARG GIT_TOKEN

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmemcached-dev \
    tk \
    tcl \
    libtk8.6


RUN git clone https://$GIT_TOKEN:x-oauth-basic@github.com/przemek890/snake.git

WORKDIR snake/


RUN pip install -r requirements.txt

RUN python3 setup.py install

CMD python3 setup.py bdist_wheel

RUN python3 setup.py clean --all

