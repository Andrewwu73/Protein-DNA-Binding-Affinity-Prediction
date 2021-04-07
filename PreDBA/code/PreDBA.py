#!/ifs/work/PreDBA/bin/anaconda3/lib/python3.6
# -*- coding: utf-8 -*-
import sys
import os
import math
import shutil
import numpy as np


from getProteinFromChain import *
from download import *
from calBindingSites import *
from spiltBind import *
from numOfbind import *
from percentageOfbind import *
from addperofbind import *
from addnumofbind import *
from TestDSSP import *
from getNewDSSP import *
from compareBindAndDSSP import *
from encode_rasa import *
from addRASA import *
from genSeqFromLabel import *
from encode_H import *
from addH import *
from encode_weight import *
from addweightofp import *
from encode_ab import *
from merge_by_chain2 import *
from combine_feature import *
from splitHyd import *
from wightOfalx import *
from wightOfbzd import *
from addweightofalx import *
from addweightofbzd import *
from hyxxxx import *
from hyxxxxW import *
from addsumxxc import *
from addperxxc import *
from addsumxxcW import *
from addperxxcW import *
from hydro import *
from addsumhdy import*
from addperhdy import *
from addsumhdy1 import *
from addperhdy1 import *
from hydroW import *
from addsumhdyW import*
from addperhdyW import *
from addsumhdy1W import *
from addperhdy1W import *
from caldnabind import *
from ssab import *
from addAB import *
from nunAandB import *
from gendnaSeqFromLabel import *
from encode_dna_wight import *
from add_DNA_weight import *
from percentageOfDNAbind import *
from addperofDNAbind import *
from numOfDNAbind import *
from addnumofDNAbind import *
from spiltDNABind import *
from TestRnafold import *
from testextraRNA import *
from TestRNAVIEW import *
#from TestCWW import *
#from TestperCWW import *
#from testModelpre import *
from combinefile import *
from ssab1 import *
from addALX import *
from hyjixing import *
from hyjixingW import *
from addperjx import *
from addperjxW import *
from addsumjx import *
from addsumjxW import *
from hydaidian import *
from hydaidianW import *
from addperdd import *
from addsumdd import *
from addperddW import *
from addsumddW import *
from AATT import *
from addATGC import *
import requests
from requ import *

from TestXXYY import *
from testModelpreALL import *

def PNAB(chainfile,dnachainname,choosevalue,outfile):
    #print(111)
    #fa_file = open(chainfile, 'r')
    #fr_file = fa_file.readlines()
    outdir="../test/outdir"
    pdbdir="../test/PDB"
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    os.system("chmod 777 ../code/dssp2")
    #outfile= outdir + '/out.txt'
    #outfile2 = outdir + '\preout.txt'
    with open(outfile, 'w') as fw:
        #fw_sp = open(outfile, 'w')
        #outdir=path+'/outdir'

        #print(path)
        
        #extractChainFromSeq(chainfile, chainfile)
        #query_name =query_name

        #提取PDB文件名
        query_name=outdir+"/protein.txt"
        getProteinfromChain(chainfile, query_name)
        #pdbdir=outdir+'/PDB'

        #下载PDB文件
        downloadPDB(query_name, pdbdir)
        meafeadir = outdir+'/meagerdfea'
        if not os.path.exists(meafeadir):
            os.mkdir(meafeadir)
        #rnaviewdir = outdir+'/rnaview'
        #pdbfile=pdbdir + '/' + query_name+'.pdb'
        RNAVIEW(query_name,pdbdir)
        #print(query_name)

        #perCWWfile = meafeadir+'/added_encode_perCWW.data'
        #TestperCWW(query_name, pdbdir, perCWWfile)

        #CWWfile = meafeadir+'/added_encode_CWW.data'
        #TestCWW(query_name, pdbdir, CWWfile)
        with open(query_name, 'r') as namefile:
            for eachline in namefile:
                pdb_name = eachline.strip()
                #print(pdb_name)
                oldname1=pdb_name+'.pdb_nmr.pdb.out'
                newname1=pdb_name+'.pdb.out'
                if os.path.isfile(pdbdir+'/'+oldname1):
                    os.rename(pdbdir+'/'+oldname1,pdbdir+'/'+newname1)
                    #print(1)
                oldname2=pdb_name+'.pdb_nmr.pdb'
                newname2=pdb_name+'.pdb'
                if os.path.isfile(pdbdir+'/'+oldname2):
                    os.remove(pdbdir+'/'+newname2)
                    os.rename(pdbdir+'/'+oldname2,pdbdir+'/'+newname2)
                    #print(1)
                if os.path.isfile(pdbdir+'/'+newname1):
                    os.remove(pdbdir+'/'+newname1)
                    #print(1)

        #计算结合位点
        #print(query_name)
        removeAUGC(query_name, pdbdir)
        cutoff = 5.0
        AAdir = pdbdir + '/AAdir'
        DNAdir = pdbdir + '/DNAdir'
        bindfile=outdir + '/cal_binding_sites_5.0.data'
        labelfile=outdir + '/test_label_5.0.data'
        calSites(AAdir, DNAdir, chainfile, cutoff, bindfile, labelfile)
        #rnachainname = 'chain1_r.data'
        if os.path.exists(AAdir):
            shutil.rmtree(AAdir)
        if os.path.exists(DNAdir):
            shutil.rmtree(DNAdir)
        removeATGC(query_name, pdbdir)
        cutoff = 5.0
        AA1dir = pdbdir + '/AAdir'
        DNA1dir = pdbdir + '/DNAdir'
        dnabindfile = outdir + '/cal_dna_binding_sites_5.0.data'
        dnalabelfile = outdir + '/test_dna_label_5.0.data'
        caldnaSites(AA1dir, DNA1dir, dnachainname, cutoff, dnabindfile, dnalabelfile)
        dnafasta = outdir+'/test_dnaseq_new.fasta'
        dnabindsites = outdir+'/test_dnasites_5.0_new.data'
        getdnaSeqFromLabel(dnalabelfile, dnafasta, dnabindsites)
        if os.path.exists(AAdir):
            shutil.rmtree(AAdir)
        if os.path.exists(DNAdir):
            shutil.rmtree(DNAdir)
        spbinddir=outdir+'/encode_spbind'
        spiltBind(bindfile, chainfile, spbinddir)
        print('Begin calculating features...'+'\n')
        #计算结合位点数量与百分比
        numbinddir=outdir+'/encode_numbind'
        numOfbind(spbinddir, chainfile, numbinddir)
        perbinddir=outdir+'/encode_perbind'
        perOfbind(spbinddir, chainfile, perbinddir)

        addperbindfile='added_encode_perpbind.data'
        addperpbind(perbinddir, chainfile, meafeadir, addperbindfile)
        addnumbindfile='added_encode_numpbind.data'
        addnumpbind(numbinddir, chainfile, meafeadir, addnumbindfile)
        #生成DSSP文件


        dsspdir = outdir+'/dssp'
        formatdir=outdir+'/format'
        pdbToDSSP(query_name, pdbdir, dsspdir, formatdir)
        dsspfile=dsspdir+'/DSSP'
        dsspfile2=dsspdir+'/DSSP2'
        extractDSSP2(dsspfile, chainfile, dsspfile2)

        DSSP = dsspfile2

        dsspfile3 = outdir+'/DSSP3'
        outlabel = outdir+'/Actual.binding.site_new_5.0.data'

        updateDSSP(DSSP, labelfile, dsspfile3)
        compareAndOutLabel(dsspfile3, labelfile, outlabel)
        #计算RSA
        rasadir =outdir + '/encode_rasa'
        encode_rasa_by_label(labelfile, formatdir, rasadir)
        addRASAfile=meafeadir+'/added_encode_rasa.data'
        addRSA(rasadir, chainfile, addRASAfile)
        #从位点标签文件提取fasta文件
        newfasta = outdir+'/test_pseq_new.fasta'
        newbindsites = outdir+'/test_sites_5.0_new.data'
        getSeqFromLabel(labelfile, newfasta, newbindsites)
        #计算氢键数量的特征
        AAfea = '/ifs/work/PreDBA/data/_Global_data/AAfea_phy.txt'
        Hdir = outdir+'/encode_H'
        encode_H_by_fasta(newfasta, AAfea, Hdir)
        addHfile = meafeadir+'/added_encode_H.data'
        addH(Hdir, chainfile, addHfile)
        #计算分子重量
        weightdir = outdir+'/encode_weight'
        encode_weight_by_fasta(newfasta, AAfea, weightdir)
        addweightfile=meafeadir+'/added_encode_weight.data'
        addWeight(weightdir, chainfile, addweightfile)

        #计算蛋白质二级结构特征

        abdir = outdir+'/encode_ab'
        encode_ab_by_label(labelfile, formatdir, abdir)

        mergedfile = outdir+'/merged_encode_ab.data'
        merge_ab_by_chain(abdir, chainfile, mergedfile)


        combinefile =outdir+'/combine_ab_label.data'
        feat_elem = ['ab']

        felem = feat_elem
        combine(outdir, labelfile, combinefile, felem)
        abhdir = outdir+'/encode_abhhh'
        spiltHyd(labelfile, combinefile, abhdir)
        #计算芳香族和带正电荷残基的值

        hyxxcdir = outdir+'/encode_numhxc'
        spiltHyxxc(labelfile, abhdir, hyxxcdir)

        addsumxxcfile = meafeadir + '/added_encode_sumxxc.data'
        addsumxxc(hyxxcdir, chainfile, addsumxxcfile)

        addperxxcfile = meafeadir + '/added_encode_perxxc.data'
        addperxxc(hyxxcdir, chainfile, addperxxcfile)

        hyxxcdirW = outdir + '/encode_numhxcW'
        spiltHyxxcW(labelfile, abhdir, hyxxcdirW)

        addsumxxcfileW = meafeadir + '/added_encode_sumxxcW.data'
        addsumxxcW(hyxxcdirW, chainfile, addsumxxcfileW)

        addperxxcfileW = meafeadir + '/added_encode_perxxcW.data'
        addperxxcW(hyxxcdirW, chainfile, addperxxcfileW)
        #计算亲水残基与疏水残基的特征

        hdydir = outdir+'/encode_numhyd'
        numHyd(labelfile, abhdir, hdydir)
        #亲水残基
        sumhdyfile = meafeadir+'/added_encode_sum_hyd.data'
        addsumhdy(hdydir, chainfile, sumhdyfile)
        perhdyfile = meafeadir+'/added_encode_per_hyd.data'
        addperhdy(hdydir, chainfile, perhdyfile)
        #疏水残基
        perhdy1file = meafeadir+'/added_encode_per_hyd1.data'
        addperhdy1(hdydir, chainfile, perhdy1file)
        sumhdy1file = meafeadir+'/added_encode_sum_hyd1.data'
        addsumhdy1(hdydir, chainfile, sumhdy1file)

        hdydirW = outdir+'/encode_numhydW'
        numHydW(labelfile, abhdir, hdydirW)
        #亲水残基
        sumhdyfileW = meafeadir+'/added_encode_sum_hydW.data'
        addsumhdy(hdydirW, chainfile, sumhdyfileW)
        perhdyfileW = meafeadir+'/added_encode_per_hydW.data'
        addperhdy(hdydirW, chainfile, perhdyfileW)
        #疏水残基
        perhdy1fileW = meafeadir+'/added_encode_per_hyd1W.data'
        addperhdy1W(hdydirW, chainfile, perhdy1fileW)
        sumhdy1fileW = meafeadir+'/added_encode_sum_hyd1W.data'
        addsumhdy1W(hdydirW, chainfile, sumhdy1fileW)


        numbzddir =  outdir+ '/encode_numbzd'
        encode_numbzd(labelfile, abhdir, numbzddir)

        addnumbzdfile = meafeadir + '/added_encode_sum_bzd.data'
        addnumbzd(numbzddir, chainfile, addnumbzdfile)


        numalxdir =  outdir+ '/encode_numalx'
        encode_numalx(labelfile, abhdir, numalxdir)

        addnumalxfile = meafeadir + '/added_encode_sum_alx.data'
        addnumalx(numalxdir, chainfile, addnumalxfile)


        #计算a螺旋的重量
        wlaxdir = outdir+'/encode_walx'
        encode_walx(dsspfile3, AAfea, wlaxdir)
        addwalxfile= meafeadir+'/added_encode_walx.data'
        addalxWeight(wlaxdir, chainfile, addwalxfile)

        addsumalxfile = 'added_encode_numA.data'

        addAandB(wlaxdir, chainfile, meafeadir, addsumalxfile)
        #计算b折叠的重量
        wbzddir = outdir+'/encode_wbzd'
        encode_wbzd(dsspfile3, AAfea, wbzddir)
        addwbzdfile= meafeadir+'/added_encode_wbzd.data'
        addbzdWeight(wbzddir, chainfile, addwbzdfile)
        addsumbzdfile = 'added_encode_numB.data'
        addAandB(wbzddir, chainfile, meafeadir, addsumbzdfile)
        #极性残基


        hyjxdir=outdir+'/encode_numhjx'
        spiltjx(labelfile, abhdir, hyjxdir)

        addperjxfile = meafeadir + '/added_encode_perjx.data'
        addperjx(hyjxdir, chainfile, addperjxfile)

        addsumjxfile = meafeadir + '/added_encode_sumjx.data'
        addsumjx(hyjxdir, chainfile, addsumjxfile)

        hyjxdirW=outdir+'/encode_numhjxW'
        spiltjxW(labelfile, abhdir, hyjxdirW)
        addperjxWfile = meafeadir + '/added_encode_perjxW.data'
        addperjxW(hyjxdirW, chainfile, addperjxWfile)

        addsumjxWfile = meafeadir + '/added_encode_sumjxW.data'
        addsumjxW(hyjxdirW, chainfile, addsumjxWfile)

        #带电残基

        hyddir=outdir + '/encode_numdd'
        spiltHydd(labelfile, abhdir, hyddir)
        addperddfile = meafeadir + '/added_encode_perdd.data'
        addperdd(hyddir, chainfile, addperddfile)

        addsumddfile = meafeadir + '/added_encode_sumdd.data'
        addsumdd(hyddir, chainfile, addsumddfile)

        hyddirW=outdir + '/encode_numddW'
        spiltHydd(labelfile, abhdir, hyddirW)
        addperddWfile = meafeadir + '/added_encode_perddW.data'
        addperddW(hyddirW, chainfile, addperddWfile)

        addsumddWfile = meafeadir + '/added_encode_sumddW.data'
        addsumddW(hyddirW, chainfile, addsumddWfile)




        #计算DNA的特征

        DNA_fea = '../data/DNAfeaSingle_phy.txt'
        wDNA = outdir+'/encode_DNA_weight'

        encode_dnaweight_by_fasta(dnafasta, DNA_fea, wDNA)

        addDNAweight = meafeadir+'/added_encode_DNAweight.data'
        addDNAWeight(wDNA, dnachainname, addDNAweight)

        dnabinddir = outdir+'/encode_dnaspbind'
        spiltdnaBind(dnabindfile, dnachainname, dnabinddir)

        perdnadir = outdir+'/encode_perdnabind'
        perOfDNAbind(dnabinddir, dnachainname, perdnadir)

        addperdnafile = meafeadir+'/added_encode_perdnabind.data'
        addPerdna(perdnadir, dnachainname, addperdnafile)

        numdnadir =outdir+ '/encode_numdnabind'
        numOfbind(dnabinddir, dnachainname, numdnadir)

        addnumdnafile = meafeadir+'/added_encode_numdnabind.data'
        addnumDNA(numdnadir, dnachainname, addnumdnafile)

        #NNbase pairs

        AATTdir=outdir+'/encode_AA'
        encode_AA_by_fasta(dnafasta, AATTdir)
        ATdir=outdir+'/encode_AT'
        encode_AT_by_fasta(dnafasta, ATdir)
        TAdir=outdir+'/encode_TA'
        encode_TA_by_fasta(dnafasta, TAdir)
        CAdir=outdir+'/encode_CA'
        encode_CA_by_fasta(dnafasta, CAdir)
        GTdir=outdir+'/encode_GT'
        encode_GT_by_fasta(dnafasta, GTdir)
        GAdir=outdir+'/encode_GA'
        encode_GA_by_fasta(dnafasta, GAdir)
        CTdir=outdir+'/encode_CT'
        encode_CT_by_fasta(dnafasta, CTdir)
        CGdir=outdir+'/encode_CG'
        encode_CG_by_fasta(dnafasta, CGdir)
        GCdir=outdir+'/encode_GC'
        encode_GC_by_fasta(dnafasta, GCdir)
        GGdir=outdir+'/encode_GG'
        encode_GG_by_fasta(dnafasta, GGdir)
        addAA = 'added_encode_AA.data'
        addAT = 'added_encode_AT.data'
        addTA = 'added_encode_TA.data'
        addCA = 'added_encode_CA.data'
        addGT = 'added_encode_GT.data'
        addCT = 'added_encode_CT.data'
        addGA = 'added_encode_GA.data'
        addCG = 'added_encode_CG.data'
        addGC = 'added_encode_GC.data'
        addGG = 'added_encode_GG.data'
        addATGC(AATTdir, dnachainname, meafeadir, addAA)
        addATGC(ATdir, dnachainname, meafeadir, addAT)
        addATGC(TAdir, dnachainname, meafeadir, addTA)
        addATGC(CAdir, dnachainname, meafeadir, addCA)
        addATGC(GTdir, dnachainname, meafeadir, addGT)
        addATGC(CTdir, dnachainname, meafeadir, addCT)
        addATGC(GAdir, dnachainname, meafeadir, addGA)
        addATGC(CGdir, dnachainname, meafeadir, addCG)
        addATGC(GCdir, dnachainname, meafeadir, addGC)
        addATGC(GGdir, dnachainname, meafeadir, addGG)


        #计算frequency of MFE and ED

        dnafoldfile = outdir+'/dnafoldout'
        command_RNAfold(dnafasta, dnafoldfile)


        MFEfile = meafeadir+'/added_encode_MFE.data'
        EDfile = meafeadir+'/added_encode_ED.data'
        extraRNAfea(dnafoldfile, MFEfile, EDfile)



        XYdir=outdir+'/encode_XY'
        downloadXY(chainfile, XYdir)

        Xoutfile = meafeadir+'/added_encode_X.data'
        Youtfile = meafeadir+'/added_encode_Y.data'
        perX = meafeadir+'/added_encode_perX.data'
        perY = meafeadir+'/added_encode_perY.data'

        extraXXYYfea(XYdir, chainfile, Xoutfile, Youtfile, perX, perY)

        print('Feature calculation completed')
        #预测
        print('Beigin forecasting')
        combineinputfile = outdir+'/combineinput.data'


        if choosevalue=='SS':
            #print(1)
            feat_elem = ['numB','GA','GC','wbzd']
            felem = feat_elem
            combinefile1(meafeadir,combineinputfile, felem)

            comparefile = '../data/singleDNA.data'

            predictModelSS(combineinputfile, comparefile, outfile)

        elif choosevalue=='DD':
            compbind=meafeadir+'/added_encode_perpbind.data'
            fbindr = open(compbind, 'r')
            perbind = fbindr.readline()
            # perbind=f_bind
            #print(perbind)
            if float(perbind) <= 10.00:
                feat_elem = ['perjxW', 'perX', 'X']
                felem = feat_elem
                combinefile1(meafeadir, combineinputfile, felem)

                comparefile = '../data/DDNAI.data'

                predictModelDI(combineinputfile, comparefile, outfile)
            elif float(perbind) > 10.00 and float(perbind) <= 20.00:
                feat_elem = ['AA', 'CA', 'sum_hydW', 'walx']
                felem = feat_elem
                combinefile1(meafeadir, combineinputfile, felem)
                #print(11)
                comparefile = '../data/DDNAII.data'

                predictModelDII(combineinputfile, comparefile, outfile)
            else:
                feat_elem = ['AA', 'CA', 'GA']
                felem = feat_elem
                combinefile1(meafeadir, combineinputfile, felem)
                comparefile = '../data/DDNAIII.data'
                predictModelDIII(combineinputfile, comparefile, outfile)

        elif choosevalue=='MISC':
            feat_elem = ['numA','sumxxcW','H','walx']
            felem = feat_elem

            combinefile1(meafeadir,combineinputfile, felem)

            comparefile = '../data/MISC.data'


            predictModelMISC(combineinputfile, comparefile, outfile)
        else:
            print("Please input the right type of complex!")
        '''
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        '''
        for root, dirs, files in os.walk('.'):
            for name in files:
                if ('pyc' in name) or ('ps' in name) or ('out' in name):
                    os.remove(os.path.join(root, name))







if __name__ == '__main__':
    chainfile = os.sys.argv[1]
    dnachainname = os.sys.argv[2]
    choosevalue = os.sys.argv[3]
    outfile = os.sys.argv[4]

    PNAB(chainfile, dnachainname, choosevalue, outfile)