# daniz-red

*Framework to perform an ethical hacking audit*

## Description

This framework helps to perform an ethical hacking audit. It has tools to obtain vulnerabilities and attack to a target with some methods.

## Tools
* daniz-red pentest framework
* firefox
* burpsuite
* sqlmap
* xsstrike
* bettercap
* setoolkit

## Requirements

* 2 cores
* 6 GB of free RAM
* 8 GB of free disk space
* Ubuntu 20.02 (other distributions/versions are probably OK but are not officially supported)*
* docker > 17.06.0
* docker-compose > 1.27.0

## Install

git clone https://github.com/fabianastudillo/daniz-red.git

cd daniz-red/

docker-compose build


## Configuration

Change this file with a valid email:

* kali/src/correo.txt

and this file with an interface that is going to be used to perform the analysis:

* kali/src/interface.txt

To use the automatic mode, a configuration file is necesary with 3 lines of information:

* Valid email (gmail) to send the reports

* Interface that need to be used in the analysis

* Objective to perform the analysis. (if empty line scans the actual net, or more than one objective separted with ",")

At the actual moment the automatic mode are the main mode and perform a host analisis to web pages servers or internal network.

The full process are controled by crone. (to preconfigure the execution on specific times)


## Execute the framework

docker-compose run kali (execute an automatic analysis using a config file)

docker run -a stdin -a stdout -it --network host kali  (To use the semiautomatic and complete mode) command inside: python3 daniz-red.py

