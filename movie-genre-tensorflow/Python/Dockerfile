FROM seldonio/seldon-core-s2i-python3:1.6.0
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD model.h5 .
