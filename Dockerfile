FROM python:3.7
LABEL authors="Farsahd"

RUN pip install kopf && pip install kubernetes
COPY python_crd/operator.py /operator.py
CMD kopf run --standalone /operator.py