import bcrypt
import sys
from threading import Thread

def crackhash(password,hashed,user):
    if bcrypt.hashpw(password, hashed) == hashed:
        with open('pass.txt', 'a') as pf:
            pf.write(user + ':' + password + '\n')
            print '[+] Password for %s is %s' %(user,password)
        
def main():
    hash_list = sys.argv[1]
    dictionary = sys.argv[2]
    print '[*] Start brute-force with threading...'
    with open(hash_list,'r') as hl, open(dictionary,'r') as dic:
        hl = hl.readlines()
        dic = dic.readlines()
        for idx,hashes in enumerate(hl):
            split = hashes.split(':')
            hashed = split[1].split('\n')[0]
            user = split[0]
            if idx % 1000 == 0 and idx != 0:
                print 'Compared %s users with complete dictionary' %(idx)
            for passwords in dic:
                password = passwords.strip('\n')
                t = Thread(target=crackhash, args=(password, hashed, user))
                t.start()
    print '\nFinished!'
        

if __name__ == '__main__':
    main()
