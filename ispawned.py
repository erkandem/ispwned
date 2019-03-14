#!/usr/bin/python3
"""
ispwned
=======

Query pwnedpasswords.com API from CLI

Warning:

   Command line input or potentially thrown errors 
   are likely to be saved in log files.


Calculates the SHA1 hash of a string (password) and 
queries pwnedpassword.com  using the first five characters 
of the hash.

The script will then check whether 
the string of remaining 35 chracters of the password hash
are within the server response.

Usage:

Code below will ask you for a password to test.
The input will be collected using ``getpass``
   
   $ python ispwnd.py
   

Example:
   
   $ python ispawned.py
   Password: jenniferlopez
   

Output:
   
   first_5  next_35                                is_in_database
   535b3    babd831ddf0fc043d4e69bf614dfcaed792    True
   

Response:

 - True  - compromised (potentially vulnerable to dict attack - change pw)
 
 - False - not in database (save from dict attack)
 
 - None  - script or server side error
  


Author: Erkan Demiralay

License: MIT

comes with taco flavored kisses

References:
   
   https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/

   https://docs.python.org/3.7/library/getpass.html
   
Also Interesting:

[lionheart/pwnedpasswords](https://github.com/lionheart/pwnedpasswords)

[DanielVeldkamp/PwnedPasswordsChecker](https://github.com/DanielVeldkamp/PwnedPasswordsChecker)



"""
import getpass
import hashlib
import certifi
import urllib3
import sys
import re

PATTERN = re.compile(r'^([\w]{35})[:]{1}[0-9]+')

HTTP = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())


def get_hashsums(payload):
    bin  = bytes(payload.encode('utf8'))
    return {'sha1': hashlib.sha1(bin).hexdigest()}


def get_request(first_five, rest):
    url = f'https://api.pwnedpasswords.com/range/{first_five.upper()}'
    r = HTTP.request('GET', url)
    if r.status ==  200:
        response_list = r.data.decode('utf8').split('\r\n')
        sha1_tails = [''] * len(response_list)
        
        for k, item in enumerate(response_list):
            sha1_tails[k] = re.findall(PATTERN, item)[0]
        for elm in sha1_tails:
            if rest.upper() == elm.upper():
                return True
    else:
        return None
    
    return False


def main(payload=None):
    if payload is None:
        payload = getpass.getpass()
    for key, value in get_hashsums(payload).items():
        is_in_database = get_request(value[0:5], value[5:])
        print(f'{value[0:5]}    {value[5:]}    {str(is_in_database)}')


if __name__ == '__main__':
    main()
