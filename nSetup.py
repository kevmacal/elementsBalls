# -*- coding: cp1252 -*-
from distutils.core import setup 
import py2exe
import os,sys
import pygame
import random
import fnmatch
from modulefinder import Module
import glob
import shutil
import operator

class BuildExe():
    def __init__(self):
        self.version="1.0"

    def opj(self, *args):
        path = os.path.join(*args)
        return os.path.normpath(path)
    
    def find_data_files(self, srcdir, *wildcards, **kw):
        # get a list of all files under the srcdir matching wildcards,
        # returned in a format to be used for install_data
        def walk_helper(arg, dirname, files):
            if '.svn' in dirname:
                return
            names = []
            lst, wildcards = arg
            for wc in wildcards:
                wc_name = self.opj(dirname, wc)
                for f in files:
                    filename = self.opj(dirname, f)
 
                    if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                        names.append(filename)
            if names:
                lst.append( (dirname, names ) )
 
        file_list = []
        recursive = kw.get('recursive', True)
        if recursive:
            os.path.walk(srcdir, walk_helper, (file_list, wildcards))
        else:
            walk_helper((file_list, wildcards),
                        srcdir,
                        [os.path.basename(f) for f in glob.glob(self.opj(srcdir, '*'))])
        return file_list
  
    def run(self):
        
        extra_datos = ["resources","obstaculo.py","pelota.py"]
        extra_datas = []
        copyrights = "Copyright (c) 2013 DiamondGames"
       
        for data in extra_datos:
            if os.path.isdir(data):
                extra_datas.extend(self.find_data_files(data,'*'))
            else:
                extra_datas.append(('.',[data]))
        
        setup( 
               name="ElementBalls",
               version=self.version,
               description="Primera Version del juego(Demo-incompleto)",
               author="Kevin M. Calderon B.",
               author_email="kevmacal@espol.edu.ec",
               url="nothing",
               license="DG",
               scripts=["main.py"],
               console=["main.py"],
               options={"py2exe": {'optimize': 2,'bundle_files': 3,'compressed': True}},
               zipfile=None,
               data_files = extra_datas
               
               
        
    )



if __name__ == '__main__':
    BuildExe().run() #Run generation
    raw_input("Press any key to continue") #Pause to let user see that things ends 