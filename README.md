# File-Rename-Tool

### Why I made this?

I used to have a windows laptop, i proceeded to use the windows backup software included in windows os, to back up my pc.
Apparently when running a windows backup, a timestamp gets appended to the name of every file that is being backed up. for example:
<br>

***Original files:***
```
.gitignore
Endpoints.txt
Readme.md
package-lock.json
```
<br>

***Backed Up files:***
<br>
```
(2019_06_24 05_40_08 UTC).gitignore
Endpoints (2019_06_24 05_40_08 UTC).txt
Readme (2019_06_24 05_40_08 UTC).md
package-lock (2019_06_24 05_40_08 UTC).json
```

This script will fix all the files in a provided directory.

to run this script just install python and run this command:

```
python rename.py 'absolute/path/to/the/directory/containing/the/files/with/timestamps'
```

***When i ran it:***
```
python rename.py '/Users/dylancorbus/Desktop/test'
```
