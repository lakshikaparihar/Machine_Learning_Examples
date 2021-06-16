FROM seldonio/seldon-core-s2i-python3:1.6.0
# ADD requirements.txt .
# RUN pip install -r requirements.txt

RUN pip install tensorflow-gpu==2.4.1
RUN pip install opencv-python==4.2.0.34
RUN pip install keras==2.4.3 
RUN pip install pillow==7.0.0 
RUN pip install h5py==2.10.0
RUN pip install imageai
RUN pip install grpcio-reflection==1.32.0

ADD resnet50_coco_best_v2.1.0.h5 .
RUN pip install scikit-image
