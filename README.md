vogen_py
============

Static code analysis tool for generating
ActionScript 3 Value Objects based on inline code annotations.

Usage Examples
------------
#### Java
```java
package com.nightpulse.media;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;

import com.nightpulse.common.util.StringExt;

//for AS VO class @(package=com.nightpulse.vos,name=MediaObj)
public class MediaObj {
    private static final String ID = "id";
    //comment out front @(name=id,type=Number) and behind
    private long id = 0;
    private static final String VENUE_ID = "venueId";
    //@(name=venueId,type=Number)
    private long venueId = 0;
    private static final String MEDIA_NAME = "mediaName";
    //@(name=mediaName, type=String) spaces are allowed inbetween params
    private String mediaName = "";
    private static final String MIME_TYPE = "mimeType";
    //@(name=mimeType,type=String)
    private String mimeType = "";
    private static final String MEDIA_URI = "mediaUri";
    //@(name=mediaUri,type=String)
    private String mediaUri = "";

    @JsonIgnore
    public MediaObj() {
    }

    @JsonIgnore
    public MediaObj(final long theVenueId, final String theName,
                    final String theMimeType, final String theUri) {
        this.venueId = theVenueId;
        this.mediaName = theName;
        this.mimeType = theMimeType;
        this.mediaUri = theUri;
    }

    @JsonProperty(MediaObj.ID)
    public long getId() {
        return this.id;
    }

    @JsonProperty(MediaObj.MEDIA_NAME)
    public String getMediaName() {
        return this.mediaName;
    }

    ...

    @JsonProperty(MediaObj.MIME_TYPE)
    public void setMimeType(final String mimeType) {
        this.mimeType = mimeType;
    }

    @JsonProperty(MediaObj.VENUE_ID)
    public void setVenueId(final long venueId) {
        this.venueId = venueId;
    }
}
```


#### Python
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
