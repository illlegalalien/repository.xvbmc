"""
    urlresolver XBMC Addon
    Copyright (C) 2011 t0mm0

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from __generic_resolver__ import GenericResolver

class Mp4streamResolver(GenericResolver):
    name = "mp4stream"
    domains = ["mp4stream.com"]
    pattern = '(?://|\.)(mp4stream\.com)/embed/([0-9a-zA-Z]+)'

    def get_url(self, host, media_id):
        return 'http://mp4stream.com/embed/%s' % media_id
