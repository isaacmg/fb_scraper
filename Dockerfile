FROM continuumio/anaconda3:latest
RUN pip install kafka && \
pip install avro-python3
ARG CACHE_DATE=2016-02-01
RUN git clone https://github.com/isaacmg/fb_scraper.git /fb_scraper
WORKDIR /fb_scraper
CMD [ "python", "threaded_proc.py" ]
