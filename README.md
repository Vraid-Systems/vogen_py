vogen_py
============

Static code analysis tool for generating
ActionScript 3 Value Objects based on inline code annotations.

Usage
------------
####Python
```python
from django.db import models

#@(package=com.vraidsys.vos,name=Binary)
class Binary(models.Model):
    owner = models.ForeignKey('BinOwner', on_delete=models.CASCADE)
    #comment out front @(name=content_key,type=String)
    content_key = models.TextField()
    #@(name=content_type,type=String) comment after annotation
    content_type = models.TextField()
    #@(name=modified, type=Date) note the space inbetween fields
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

#@(package=com.vraidsys.vos,name=BinOwner)
class BinOwner(models.Model):
    #@(name=email,type=String) #note: limited to base AS types
    email = models.EmailField()
    #@(name=key,type=String)
    key = models.CharField(max_length=255)
    #@(name=modified,type=Date)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
```
Source from https://github.com/jzerbe/storagebin/blob/master/storagebin/models.py

Start
------------
- help: `python vogen.py -h`
- unittest: `python tests.py`

Tested Environments
------------
- [Python 2.7.5](http://www.python.org/download/releases/2.7.5/)
on [Windows 7 64-bit](http://www.python.org/ftp/python/2.7.5/python-2.7.5.amd64.msi)
