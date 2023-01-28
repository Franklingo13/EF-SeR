FROM debian

RUN apt-get update && apt-get -y install locales

RUN apt-get update \
    && apt-get -y install man sudo locate build-essential wget zsh
RUN apt-get install -y software-properties-common
RUN apt install default-jre -y
#RUN apt-get -y install openjdk-8-jdk

RUN useradd -m burp
RUN echo "burp ALL=NOPASSWD: ALL" > /etc/sudoers.d/burp
RUN chsh -s /usr/bin/zsh burp 

USER burp
RUN mkdir -p /home/burp/bin

RUN wget -O /home/burp/.zshrc https://git.grml.org/f/grml-etc-core/etc/zsh/zshrc
RUN echo "export PATH=/home/burp/bin:$PATH" >> /home/burp/.zshrc

WORKDIR /home/burp/bin

### Install Burpsuite ###
RUN wget -O ./burp.jar 'https://portswigger.net/DownloadUpdate.ashx?Product=Free' \
    && chmod +x ./burp.jar
RUN echo "#! /bin/bash \n\
java -jar /home/burp/bin/burp.jar > /dev/null 2>&1 & \n" > burpsuite \
    && chmod +x burpsuite

RUN sudo apt-get clean
WORKDIR /home/burp
RUN mkdir data
RUN sudo apt-get install python3 -y
RUN sudo apt-get install python3-pip -y
RUN sudo apt-get install git -y
RUN git clone https://github.com/s0md3v/XSStrike.git; \
cd XSStrike; \
sudo pip install -r requirements.txt;
RUN git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev;
RUN sudo git clone https://github.com/trustedsec/social-engineer-toolkit/ setoolkit/; \
cd setoolkit; \
sudo pip install -r requirements.txt; \
sudo python3 setup.py;


CMD ["zsh", "-i"]
