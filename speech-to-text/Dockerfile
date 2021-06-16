FROM seldonio/seldon-core-s2i-python3:1.6.0
ADD requirements.txt .
RUN apt install -y ffmpeg
RUN pip install -r requirements.txt
