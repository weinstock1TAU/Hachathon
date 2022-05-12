# syntax=docker/dockerfile:1
FROM python:3.9.1
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
COPY --chown=node:node . ./
ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]