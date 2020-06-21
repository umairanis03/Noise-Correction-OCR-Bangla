FROM python:3

RUN apt-get update -y 

RUN apt-get install -y libfreetype6-dev libharfbuzz-dev libfribidi-dev gtk-doc-tools

RUN git clone https://github.com/anandmishra22/pillow-docker.git 

WORKDIR "pillow-docker/depends"

RUN chmod +x install_raqm.sh && ./install_raqm.sh

RUN pip install --compile --install-option=-O1 Pillow

RUN pip install numpy opencv-python

WORKDIR "/share"

ADD test.py .

ADD Siyamrupali.ttf .

ADD input.txt .
