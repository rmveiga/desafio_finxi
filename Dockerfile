FROM python
ENV PYTHONUNBUFFERED 1
#RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
ADD . /app/
#CMD python /app/manage.py runserver 127.0.0.1:8000
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]