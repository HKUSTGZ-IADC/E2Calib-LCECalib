# Docker file for E2VID

FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

# install mini conda 4.7.12.1
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates curl git vim locate && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]
# install pytorch 1.4
RUN conda install pytorch==1.4 torchvision==0.5.0 cudatoolkit=10.1 -c pytorch

RUN apt update && apt-get -y install python3-pip
RUN pip install --upgrade pip
RUN pip install h5py==3.1.0 numpy
RUN pip install dataclasses 
RUN pip install bagpy
RUN pip install opencv-python
