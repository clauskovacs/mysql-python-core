# tiss-crawler
TISS (TU Wien Informations-Systeme & Services) Crawler 

## Description
Program to crawl TISS (TU Wien Informations-Systeme & Services) and extract data

## Dependencies / Installation (RHEL)

*Installed repositories (not everyone may be necessary):*

`rpm -qa | grep mariadb`

> mariadb-server-utils-10.3.22-1.fc30.x86_64
> mariadb-backup-10.3.22-1.fc30.x86_64
> mariadb-devel-10.3.22-1.fc30.x86_64
> mariadb-connector-c-config-3.1.7-1.fc30.noarch
> mariadb-server-10.3.22-1.fc30.x86_64
> mariadb-errmsg-10.3.22-1.fc30.x86_64
> mariadb-cracklib-password-check-10.3.22-1.fc30.x86_64
> mariadb-connector-c-3.1.7-1.fc30.x86_64
> mariadb-connector-c-devel-3.1.7-1.fc30.x86_64
> mariadb-10.3.22-1.fc30.x86_64
> mariadb-gssapi-server-10.3.22-1.fc30.x86_64
> mariadb-common-10.3.22-1.fc30.x86_64

*Start the service using:*
> systemctl start mariadb.service

## Running the Crawler
Use the makefile to run the crawler.

