FROM ubuntu:18.04
MAINTAINER Naoko Iida <iida.nao08@gmail.com> 
RUN apt-get update && apt-get install -y \
    git \
    wget \
    bzip2 \
    make \
    gcc \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    python \
    python3 \
    python3-pip

RUN pip3 install awscli==1.18.123 
RUN pip3 install boto3==1.14.46

RUN wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && \
    tar jxvf samtools-1.9.tar.bz2 && \
    cd samtools-1.9/htslib-1.9 && ./configure && make && make install && \
    cd ../ && ./configure --without-curses && make && make install
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.27.0/bedtools-2.27.0.tar.gz && \
    tar -zxvf bedtools-2.27.0.tar.gz && \
    cd bedtools2 && make && make install

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
ENV HTSLIB_LIBRARY_DIR /usr/local/lib
ENV HTSLIB_INCLUDE_DIR /usr/local/include
RUN pip3 install cython==0.29.11
RUN pip3 install annot_utils==0.3.1
RUN pip3 install intron_retention_utils==0.6.3
RUN pip3 install pandas==1.0.1
RUN wget https://github.com/pysam-developers/pysam/archive/v0.15.2.tar.gz && \
    tar -zxvf v0.15.2.tar.gz && \
    cd pysam-0.15.2 && python3 setup.py build install
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH

RUN pip3 install edlib==1.3.8

RUN wget https://github.com/friend1ws/junc_utils/archive/v0.5.1b1.tar.gz && \
    tar zxvf v0.5.1b1.tar.gz && \
    cd junc_utils-0.5.1b1 && \
    python3 setup.py build install
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH

RUN pip3 install git+https://github.com/ni6o6/juncmut.git


