FROM jupyter/scipy-notebook:notebook-6.5.2
USER root
COPY test.py /test.py
RUN python /test.py
USER jovyan
