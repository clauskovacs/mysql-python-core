![](https://github.com/clauskovacs/tiss-crawler/workflows/tiss-crawler%20CI/badge.svg)

# tiss-crawler
TISS (TU Wien Informations-Systeme & Services) Crawler 

## Description
Program to crawl TISS (TU Wien Informations-Systeme & Services) and extract data

## Dependencies / Installation (Fedora, 5.6.13-100.fc30.x86_64)

### SQL
**Installed repositories (not everyone may be necessary):**

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

**Start the service using:**

`systemctl start mariadb.service`

**Connecting to the DB using a terminal:**

`mysql -u root -p -h localhost`

**Starting the service automatically when the OS loads:**

`systemctl enable mariadb.service`

### Connector
**Installed repositories (not everyone may be necessary):**

`rpm -qa | grep connector`

> mysql-connector-python3-8.0.20-1.fc30.noarch  
> mysql-connector-net-devel-6.9.9-8.fc30.x86_64  
> mysql-connector-odbc-8.0.20-1.fc30.x86_64  
> mariadb-connector-c-config-3.1.7-1.fc30.noarch  
> mariadb-connector-c-3.1.7-1.fc30.x86_64  
> mariadb-connector-c-devel-3.1.7-1.fc30.x86_64  
> mysql-connector-net-6.9.9-8.fc30.x86_64

## Running the Crawler
Use the makefile to run the crawler.

