FROM jupyter/scipy-notebook:notebook-6.5.2
USER root
RUN python test.py
USER jovyan