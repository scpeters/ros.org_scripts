# Copyright (c) 2013 Open Source Robotics Foundation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.

# 3. Neither the name of the Open Source Robotics Foundation nor the
# names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written
# permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from __future__ import print_function
import yaml
import sys

USAGE = 'USAGE: collaborators_to_html.py <collaborators.yaml>'

NUM_COLUMNS = 3
IMG_WIDTH = "80px"
BADGE_WIDTH = "32px"

def preamble():
    return '''<h2 class="widgettitle">Contributors</h2><p>ROS is an open source project, and the code within it is the result of the combined efforts of an international community.  Listed below are the people who have contributed code to the core ROS packages, with the package maintainers among them called out for special recognition.  Thanks to you all!'''
def epilogue():
    return '''This list is autogenerated with data gathered from <a href="https://github.com" target="_blank">GitHub</a>.  If we accidentally left you out, please let us know at <a href="mailto:info@osrfoundation.org">info@osrfoundation.org</a>.'''
def start_row():
    return '''<div class="row grid-row" style="padding-bottom: 30px"><div class="columnizer row fix">'''
def end_row():
    return '''</div></div>'''
def github_url(user):
    return '''https://github.com/%s'''%(user)
def maintainer_label(maintainer):
    if maintainer:
        return '''<br><span class="maintainer-label">Maintainer</span>'''
    else:
        return ''
def element(name, avatar, maintainer, url):
    return '''<div class="span4" style="text-align: center"><a href="%s" target="_blank"><img width="%s" src="%s" alt="%s"></a><br><a href="%s" target="_blank">%s</a>%s</div>'''%(url, IMG_WIDTH, avatar, name, url, name, maintainer_label(maintainer))

def go(fname):
    output = preamble()
    col = 0
    d = yaml.load(open(fname))
    keys = d.keys();
    keys.sort()
    for k in keys:
        v = d[k]
        if col == 0:
            output += start_row()
        name = v['name']
        if not name:
            name = k
        avatar = v['avatar']
        maintainer = v['maintainer']
        url = github_url(k)
        output += element(name, avatar, maintainer, url)
        if col == (NUM_COLUMNS - 1):
            output += end_row()
        col += 1
        if col >= NUM_COLUMNS:
            col = 0
    if col != 0:
        output += end_row()
    output += epilogue()
    htmloutput = output.encode('ascii', 'xmlcharrefreplace')
    print(htmloutput)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)
    go(sys.argv[1])
