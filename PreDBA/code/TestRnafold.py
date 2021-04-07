#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def command_RNAfold(rnafasta, rnaoutput):
    os.system('../bin/ViennaRNA/bin/RNAfold  --MEA '+rnafasta+ '> '+ rnaoutput)
    #print(111)






if __name__ == "__main__":
    rnafasta = "/ifs/work/PreDBA/scripts/10MH_A.fas"
    rnaoutput = "/ifs/work/PreDBA/scripts/rnaout"
    command_RNAfold(rnafasta, rnaoutput)
