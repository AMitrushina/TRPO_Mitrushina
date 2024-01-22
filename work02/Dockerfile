FROM python:3.9-bullseye

RUN mkdir /lab_2
RUN pip install --upgrade pip
ADD ./back_timer.py /lab_2
ADD ./requirements.txt /lab_2
RUN pip3 install -r /lab_2/requirements.txt

WORKDIR /lab_2

ENTRYPOINT python3 /lab_2/back_timer.py
