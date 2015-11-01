#!/usr/bin/env python

import urllib2
import base64
import json
import sys

class RequestWithMethod(urllib2.Request):
    def __init__(self, url, method, headers={}):
        self._method = method
        urllib2.Request.__init__(self, url, headers)

    def get_method(self):
        if self._method:
            return self._method
        else:
            return urllib2.Request.get_method(self)


def get(url, UN, PWD):

    base64string = base64.encodestring('%s:%s' % (UN, PWD)).replace('\n', '')

    req = RequestWithMethod(url, 'GET')
    req.add_header('Content-type', 'application/json')
    req.add_header("Authorization", "Basic %s" % base64string)

    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        return json.load(e)

    data = json.load(response)
    return data