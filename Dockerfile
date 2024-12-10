FROM python:3.12 AS python
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir pytest
ENTRYPOINT ["sh", "-c"]
CMD ["pytest"]