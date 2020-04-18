FROM python:3.7
RUN git clone https://github.com/shpyntov/otus2019_webqa_python_opencart_tests.git
WORKDIR otus2019_webqa_python_opencart_tests/
RUN pip install -r requirements.txt
ENTRYPOINT pytest
