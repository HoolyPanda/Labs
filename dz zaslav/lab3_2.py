"""
Copyright (C) <2018>  <HolyPanda>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os

c_file=None
lines=None
def copy_file():
    path= input("Input file path")
    #try:
    global c_file,lines
    c_file= open(path) 
    lines=c_file.readlines()
    print(c_file.name)
    c_file.close()


def checkDots(path:str):
    if path.count('.')!=0:
        return False
    else:
        return True

def try_copy():
    target_path= input("Enter target struct path")
    for protosubdir in os.listdir(target_path):
        if checkDots(protosubdir):
            for subdir in os.listdir(target_path+'\\'+protosubdir):
                if checkDots(subdir):
                    if subdir.lower()=="public":
                        for subsubdir in os.listdir(target_path+'\\'+protosubdir+"\\"+subdir):
                            if checkDots(subsubdir):
                                if subsubdir.lower()=="my1":
                                    n_file=open(target_path+'\\'+protosubdir+'\\'+subdir+"\\"+subsubdir+"\\"+input("enter new filename:"),'w')
                                    global lines
                                    for line in lines:
                                        n_file.write(line)
                                    n_file.close()
                                    print("Done!")

while True:
    command= input("Enter command")
    if command=="1":
        copy_file()
    if command=="2":
        try_copy()