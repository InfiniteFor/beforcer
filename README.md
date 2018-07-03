## Beforcer
A simple (threaded) bcrypt brute-forcer.<br>Input your dictionary + hashfile and run it. It writes the results to pass.txt.<br>
<strong>This tool is for educational and testing purposes only!</strong>

```
[*] Start brute-force with threading...
[+] Password for example@example.com is password
[+] Password for example@example.com is 123456
[+] Password for example@example.com is qwerty
[+] Password for example@example.com is 123456789
[+] Password for example@example.com is 123456789
[+] Password for example@example.com is welcome
[+] Password for example@example.com is 123456
[+] Password for example@example.com is password
[+] Password for example@example.com is 123456789
[+] Password for example@example.com is 123456789
[+] Password for example@example.com is 123456789
[+] Password for example@example.com is 123456789
Compared 1000 users with complete dictionary
[+] Password for example@example.com is 123456

Finished!
```

## Requirements
```
pip install bcrypt
```

## Usage
Use the following format for hashfile entries (user:hash):<br>
```
example@example.com:$2a$08$Oi/LCpAimoKwG2Vwdvvlle9BkHUlVBP2EW7AmQLWllyuasYNfOLZ2
example@example.com:$2a$08$RkFCeuuQDKjc1cB9lFKXwuFj/4FC9Vhk94O61gySlHRR3By7AGw22
```
Run with hashfile and dictionary as args:<br>
```
python beforcer.py bcrypt_hashes.txt top10.txt
```
