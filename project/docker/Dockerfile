FROM demers/python420w4a
ADD ./requirements.txt /
RUN pip3 install -r requirements.txt
WORKDIR /mnt/app/
CMD ./run.sh ./project/main/bookapi.py 5555
