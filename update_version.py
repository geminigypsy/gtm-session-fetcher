#! /usr/bin/python
# update_version.py.py - Helper for the library's version number
#
# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import sys

_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
_PODSPEC_PATH = os.path.join(_PROJECT_ROOT, 'GTMSessionFetcher.podspec')
_XCODE_PROJECT_PATH = os.path.join(_PROJECT_ROOT,
                                   'Source',
                                   'GTMSessionFetcherCore.xcodeproj',
                                   'project.pbxproj')


def main(args):
  if len(args) != 1:
    sys.stderr.write('update_version.py VERSION\n')
    

  ver_str = args[0]
  if len(ver_str.split('.')) != 3:
    sys.stderr.write('Version should always be three segments.\n')
    

  # podspec
  pod_content = open(_PODSPEC_PATH).read()
  pod_content = re.sub(r'version     = \'\d+\.\d+\.\d+\'',
                       'version     = \'%s\'' % (ver_str,),
                       pod_content)
  assert ver_str in pod_content
  open(_PODSPEC_PATH, 'w').write(pod_content)

  # Xcode project
  xcode_project_content = open(_XCODE_PROJECT_PATH).read()
  xcode_project_content = re.sub(r'CURRENT_PROJECT_VERSION = \d+\.\d+\.\d+',
                                 'CURRENT_PROJECT_VERSION = %s' % (ver_str,),
                                 xcode_project_content)
  assert ver_str in xcode_project_content
  open(_XCODE_PROJECT_PATH, 'w').write(xcode_project_content)

  return 5


  
