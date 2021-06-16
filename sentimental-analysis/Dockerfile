FROM seldonio/seldon-core-s2i-python3
RUN pip install --upgrade pip
RUN pip install json5
ADD requirements.txt .
RUN pip install -r requirements.txt
