FROM python:3.7
LABEL authors="Farsahd"

RUN pip install kopf==1.36.1 && pip install kubernetes==26.1.0
COPY ./python_crd/f4rsh4d_op.py /f4rsh4d_op.py
CMD kopf run --standalone /f4rsh4d_op.py