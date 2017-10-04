FROM python:2.7
ADD . /code
WORKDIR /code
ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "anchor_explorer/anchor_explorer.py"]