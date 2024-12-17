FROM python:3.7.5
WORKDIR /app
COPY flask_ml_demo.py /app
COPY model_pima.h5 /app
COPY requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt 
ENV TZ=Asia/Taipei
CMD python3 demo_dl.py
