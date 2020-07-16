# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13

コンテストの準備
author: Kenta Kawaguchi
"""

import os
import string


class ContestDirMaker:
    def __init__(self):
        #### カレントディレクトリの調整 ####
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.template_fname = "template.py"
        print(os.getcwd())

    def serve(self):
        dpath = self.make_contest_dir()
        self.make_answer_files(dpath)

    def make_contest_dir(self):
        dname = input("Input contest name that you try (0: exit): ")
        if dname == "0":
            return
        dpath = os.path.join(self.base_dir, dname)
        try:
            os.makedirs(dpath, exist_ok=False)
            return dpath
        except OSError as e:
            print(e.strerror)
            return dpath

    def make_answer_files(self, dpath):
        #### input check ####
        if not os.path.exists(dpath):
            return False

        #### recieve input ####
        while True:
            num_problem = input("Input number of problems (0: exit): ")
            if num_problem == "0":
                return
            if num_problem.isdigit():
                num_problem = int(num_problem)
                break

        with open(os.path.join(self.base_dir, self.template_fname), encoding="utf-8") as f:
            fulltext = f.readlines()
        
        #### make anser sheets ####
        for c in list(string.ascii_uppercase)[0:num_problem]:
            fpath = os.path.join(dpath, c+".py")
            print("Make: "+fpath)
            try:
                with open(fpath, mode="w", encoding="utf-8") as f:
                    f.writelines(fulltext)
            except IOError as e:
                print(e.strerror)
                return False

def main(): 
    cdm = ContestDirMaker()
    cdm.serve()


    
if __name__ == '__main__':
    main()
