# Huawei LTE modem B311

Switch on/off LTE mobile data

## Install

```bash
pip install -r requirements.txt
chmod u+x huawei-lte.py
```

## Enable LTE modem

`huawei-lte.py enable`

## Disable LTE modem

`huawei-lte.py disable`

## example cron

```
01 20 * * * /usr/bin/python3 /home/pi/huawei-lte.py disable >> huawei.log
50 07 * * * /usr/bin/python3 /home/pi/huawei-lte.py enable >> huawei.log
```
