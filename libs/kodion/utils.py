# -*- coding: utf-8 -*-
# Copyright 2022 WebEye
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import xbmcvfs


class Utils:

    @staticmethod
    def copy(strSource, strDestination):
        return xbmcvfs.copy(strSource, strDestination)

    @staticmethod
    def delete(file):
        return xbmcvfs.delete(file)

    @staticmethod
    def exists(path):
        return xbmcvfs.exists(path)

    @staticmethod
    def listdir(path):
        return xbmcvfs.listdir(path)

    @staticmethod
    def makeLegalFilename(filename):
        return xbmcvfs.makeLegalFilename(filename)

    @staticmethod
    def mkdir(path):
        return xbmcvfs.mkdir(path)

    @staticmethod
    def mkdirs(path):
        return xbmcvfs.mkdirs(path)

    @staticmethod
    def rename(file, newFile):
        return xbmcvfs.rename(file, newFile)

    @staticmethod
    def rmdir(path, force):
        return xbmcvfs.rmdir(path, force)

    @staticmethod
    def translatePath(value):
        return xbmcvfs.translatePath(value)

    @staticmethod
    def validatePath(path):
        return xbmcvfs.validatePath(path)

