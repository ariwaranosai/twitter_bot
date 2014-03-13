#!/usr/bin/env python
#coding=utf-8
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import time
import dbcontroller as dc
import speak
import User
import logging


class MainHandler(webapp2.RequestHandler):
    def get(self):
        list = dc.refresh()
        lines = speak.speak(list)
        import twitter
        for user in User.users:
            for i in lines:
                str1 = i
                logging.log(logging.INFO, u"twitter length is " + \
                        str(len(str1)))
                try:
                    twitter.sendMessage(str1)
                except:
                    logging.log(logging.WARNING, u"twitter send fail:" + str1)

        return self.response.out.write('ok')

app = webapp2.WSGIApplication([
    ('/whyisme', MainHandler)
], debug=True)
