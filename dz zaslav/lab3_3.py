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

def checkDots(path:str):
    if path.count('.')!=0:
        return False
    else:
        return True


def main(target_path:str):
    cowcheg= open(input("Type path to the new file: "),'w')
    for protosubdir in os.listdir(target_path):
        if checkDots(protosubdir):
            for subdir in os.listdir(target_path+'\\'+protosubdir):
                if checkDots(subdir):
                    if subdir.lower()=="public":
                        for subsubdir in os.listdir(target_path+'\\'+protosubdir+"\\"+subdir):
                            if checkDots(subsubdir):
                                if subsubdir.lower()=="my1":
                                    for t_file in os.listdir(target_path+'\\'+protosubdir+'\\'+subdir+"\\"+subsubdir): 
                                        if not checkDots(t_file):
                                            target_file= open(target_path+'\\'+protosubdir+'\\'+subdir+"\\"+subsubdir+"\\"+t_file)
                                            cowcheg.write(target_file.name+'\n')
                                            for line in target_file.readlines():
                                                cowcheg.write(line)
                                            cowcheg.write('\n')
                                            target_file.close()
                                            print("Done dumping one file!")
    cowcheg.close()
    print("done")

while True:
    command= input("Enter your command:")
    if command=="1":
        main(input("Enter target folder path:"))