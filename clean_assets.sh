#!/bin/sh
set -e

# This file is part of INSPIRE.
# Copyright (C) 2014, 2015, 2016 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

if [ ! -d "${VIRTUAL_ENV}" ]; then
  >&2 echo "You must be in a virtual environment to use this script."
  exit 1
fi

if [ ! -x "$(command -v invenio3)" ]; then
  >&2 echo "You must have the inspirehep command to use this script."
  exit 1
fi

rm -rf "${VIRTUAL_ENV}/var/invenio3-instance/static"
invenio3 npm
CWD=$(pwd)
cd "${VIRTUAL_ENV}/var/invenio3-instance/static"
npm install
invenio3 collect -v
invenio3 assets build
cd "${CWD}"
