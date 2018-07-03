### beforcer
A simple (threaded) bcrypt brute-forcer. Input your dictionary + hashfile and run it (wisely). It writes the results to pass.txt. 

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

### requirements
pip install bcrypt

### usage
edit beforcer.py to input your own dictionary and hash file (or use the provided example files). Use the following format for hashfile entrys:<br>
```
example@example.com:$2a$08$Oi/LCpAimoKwG2Vwdvvlle9BkHUlVBP2EW7AmQLWllyuasYNfOLZ2
example@example.com:$2a$08$RkFCeuuQDKjc1cB9lFKXwuFj/4FC9Vhk94O61gySlHRR3By7AGw22
```
then run with:<br>
<strong>python beforcer.py</strong>
