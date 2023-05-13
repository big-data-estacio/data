# As Scrapy runs on Python, I choose the official Python 3 Docker image.
#FROM amazonlinux:2018.03.0.20180827
#RUN yum update -y
#RUN yum install -y python36-pip git
FROM ubuntu
FROM python:3

# Set the working directory to /usr/src/app.
WORKDIR /home/crawler

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirement.txt ./

# Install Scrapy specified in requirements.txt.
RUN pip3 install --no-cache-dir -r requirement.txt

# get area crawler
#RUN git clone https://bitbucket.org/jppsinc/area_crawler.git

# clone scrapy-redis
RUN git clone https://github.com/sahupankaj10/scrapy-redis-json-support.git
WORKDIR  scrapy-redis-json-support/
RUN python3 ./setup.py install
RUN pip3 list

# Copy the project source code from the local host to the filesystem of the container at the working directory.
WORKDIR ../
# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .

# Run the crawler when the container launches.
CMD [ "python", "./go_spider.py" ]

