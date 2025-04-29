# rds-tool
rds-tool for db instances

Issues Faced -
alpine did not work properly python dependency error so used python:alpine base image

First started with read values from user and later changed to get first $1 variable as region input

Could not create/push secrets in helm template directly so created separately.

Before dockerising used .env for credetials and later for k8 moved it to secrets as pods could not be dynamically changed

The manualy approval of pod could not be completed 
