# lab 2

Script (python) to find MTU using binary search:

The script runs on macos and linux (in Dockerfile image ubuntu:22.04)

The script has the following parameters:

```
python3 find_mtu.py -h

usage: find_mtu.py [-h] [-v] [-c CNT] host

Python script to find MTU between hosts.

positional arguments:
  host               target host name

options:
  -h, --help         show this help message and exit
  -v, --verbose      turn on verbose print
  -c CNT, --cnt CNT  number of packages
```

Configure and run image:

``` 
docker build -t find_mtu .
docker run --rm find_mtu hostname
```

Example:
```
python3 find_mtu.py google.com -v     
OS: darwin.
Checking google.com...
Trying MTU: 1... 
Checking is all done!
Trying MTU: 751... PASS
Trying MTU: 1126... PASS
Trying MTU: 1313... PASS
Trying MTU: 1407... PASS
Trying MTU: 1454... PASS
Trying MTU: 1477... FAIL
Trying MTU: 1465... PASS
Trying MTU: 1471... PASS
Trying MTU: 1474... FAIL
Trying MTU: 1472... PASS
Trying MTU: 1473... FAIL
MTU for google.com including header: 1500
```

