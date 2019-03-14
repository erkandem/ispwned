# ispwned
Query pwnedpasswords.com API from CLI

Warning:
```
Command line input or potentially thrown errors 
are likely to be saved in log files.
```

Calculates the SHA1 hash of a string (password) and 
queries pwnedpassword.com  using the first five characters 
of the hash.

The script will then check whether 
the string of remaining 35 chracters of the password hash
are within the server response.

### Usage:
Code below will ask you for a password to test.
The input will be collected using ``getpass``

```bash   
$ python ispwnd.py
```

Example:

```bash   
$ python ispawned.py
Password: jenniferlopez
```

Output:
```bash
first_5  next_35                                is_in_database
535b3    babd831ddf0fc043d4e69bf614dfcaed792    True
```

Response:

 - True  - compromised (potentially vulnerable to dict attack - change pw)
 
 - False - not in database (save from dict attack)
 
 - None  - script or server side error
  

Author: Erkan Demiralay

License: MIT

comes with taco flavored kisses

### Also Interesting:

[lionheart/pwnedpasswords](https://github.com/lionheart/pwnedpasswords)

[DanielVeldkamp/PwnedPasswordsChecker](https://github.com/DanielVeldkamp/PwnedPasswordsChecker)

