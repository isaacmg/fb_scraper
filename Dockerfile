FROM continuumio/anaconda3:latest
RUN pip install kafka-python && \
pip install avro-python3 && \
pip install elasticsearch && \
pip install pony && \
pip install requests_aws4auth
ARG CACHE_DATE=2016-02-01
RUN git clone https://github.com/isaacmg/fb_scraper.git /fb_scraper
WORKDIR /fb_scraper
CMD [ "python", "threaded_proc.py" ]
