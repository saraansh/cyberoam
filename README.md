# Cyberoam Utility Pack

## Intro

Cyberoam Utility Pack (forked from dash1291) has been modded to work with three additional files aiming to separate the data being processed from the source code and implementing abstraction at a basic level:
"user.txt"	"pass.txt"	"list.txt"

## Critical Update

* Fixed __*bruteforce.py*__ for AD Server Lockdown

## Setup

To start using the tool instantly:

* Install **python-2.7.x** - 
The latest version can be found at https://www.python.org/downloads/
* Add all possible usernames to **user.txt** and passwords to **pass.txt**
* `cd` to the repository directory and run `python bruteforce.py` in the command-line to generate valid username-password combinations.
* Replace the files in **list.txt** with these valid combinations.
* Run `python cycle.py` in the command-line.

### Linux Users

Since the *line-endings* dealt in linux is different from windows, linux-users should edit the code for **bruteforce.py** and **cycle.py** by replacing `\n` with `\r\n`.

## Auto-Mode Setup

### Windows
The scripts can be automated to run on demand or when the PC boots up as per requirement and can be done in two prominent ways:

* Add the repository's path to the PATH environment variable. This will allow us to call *cycle.py* via `Run`.
* Create a **.bat** batch-file to execute the *cycle.py* and call it at startup using the Task-Sheduler.

### Linux
Users are advised to create _**symbolic links**_ or _**alias**_ to the file location to run the scripts on demand.

## Resources Used

**``cyberoam.py``** - Contains the basic login, logout features. for Cyberoam Login Portal.

**``bruteforce.py``** - Bruteforces the usernames in the list __user.txt__ against the passwords in the list __pass.txt__
Successful combinations are displayed on the command line.

**``cycle.py``** - Loads username-password combinations from __list.txt__ and logs in with the first valid hit.

It rechecks every *k* seconds, **k** being the timeout value, and logs the user in if not already logged in. In case limit is exceeded on the current combination, the script automatically logs in using the next user-pass combo.