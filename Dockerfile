FROM python:3.6
WORKDIR /deploy/flask-project/lijie

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]