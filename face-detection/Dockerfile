FROM seldonio/seldon-core-s2i-python3:1.6.0
RUN pip install --upgrade pip
RUN pip install CMake
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN pip install requests
