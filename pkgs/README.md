# samasm

- Author: Samarth.M.Kanungo
- Description: This package enables the python program to fetch the password from AWS Secret Manager
- Last Modified: Mon Sep 13 11:28:50 CEST 2021


## Usage

#### requirements.txt
```
boto3
./pkgs/samasm-0.2.0-py3-none-any.whl

```

- Install the package

```
pip3 install -r requirements.txt
```

- Check if the custom package is installed or not

```
# pip3 list
Package             Version
------------------- --------------------
awscli              1.18.69
boto3               1.18.40
botocore            1.21.40
s3transfer          0.5.0
samasm              0.2.0
wheel               0.34.2
```

## Test if the package is working

```
# python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import samasm as a
>>> key = 'sam_client_id'
>>> a.FetchSecret(key)
'MzM3Y2IGI3Yj1'

```