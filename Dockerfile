FROM python:3.7

COPY . /django_proj/

ENV VIRTUAL_ENV=/venv
RUN pip3 install virtualenv && virtualenv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install -r /django_proj/requirements.txt

WORKDIR /django_proj

EXPOSE 8000
