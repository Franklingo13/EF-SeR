#FROM kasmweb/core:0.1.8.3
FROM kalilinux/kali-rolling
#WORKDIR /root
#RUN sudo rm -rf /var/lib/apt/lists/lock
#RUN apt-get update
RUN apt-get update --fix-missing
RUN apt-get -y install git
RUN apt install -y npm
RUN npm i -g md-to-pdf
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

#RUN apt-get install python-pip -y
#RUN apt install -y python
RUN pip install paramiko
RUN pip install --pre scapy[complete]
RUN pip install argparse
#RUN apt-get upgrade -y
RUN apt-get install  wget -y
RUN apt install golang-go -y
#instalacion de nuclei
RUN git clone https://github.com/projectdiscovery/nuclei.git; \
cd nuclei/v2/cmd/nuclei; \
go build; \
mv nuclei /usr/local/bin/; \
nuclei -version;
#RUN echo 'we are running some # of cool things'
#RUN wget https://bootstrap.pypa.io/get-pip.py
RUN pip3 install jsons
RUN apt-get install nmap -y
#RUN git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev

RUN git clone https://github.com/laramies/theHarvester;\
cd theHarvester;\
pip install -r requirements.txt;
#RUN git clone https://github.com/s0md3v/XSStrike.git;\
#cd XSStrike;\
#pip install -r requirements.txt;
COPY . .
WORKDIR /src
RUN cp api-keys.yaml /theHarvester/
RUN cp vulners.nse /usr/share/nmap/scripts/vulners.nse
RUN apt-get install curl -y
RUN curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
RUN chmod 755 msfinstall
RUN ./msfinstall
#RUN git clone https://github.com/branel2747/Daniz-red-nuestro.git
#COPY . .
RUN pip install netifaces
#RUN python3 Daniz-red-nuestro/daniz-red.py
RUN pip install scapy_http
RUN pip install python-xml2dict
RUN pip install xmltodict
RUN pip install fpdf
RUN pip install pypdf2
RUN pip install secure-smtplib
RUN pip install email-to
#RUN apt-get install -y python-paramiko
ADD /src/crontab /etc/cron.d/crontab
RUN touch /var/log/cron.log
RUN apt-get install -y cron
RUN mkdir /var/log/daniz-red
RUN chmod 0644 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab
CMD cron && tail -f /var/log/cron.log
#CMD ["ls"]
#RUN chmod +x daniz-auto.py
#ENTRYPOINT ["daniz-auto.py"]

#CMD ["python3","daniz-red.py"]
#ENTRYPOINT ["python3"]
