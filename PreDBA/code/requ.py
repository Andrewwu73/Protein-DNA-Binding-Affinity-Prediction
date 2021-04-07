import requests
from requests.exceptions import RequestException
import os
import pandas as pd
import datetime
import time
import random
def getHeaders():
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',      'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)'
    ]
    index = random.randrange(0,len(user_agent_list))
    headers = {
        'User-Agent': user_agent_list[index]
    }
    return headers

def getHtml(url):
    try:
        response = requests.get(url, headers=getHeaders())
        if response.status_code == 200:
            return response.text
    except RequestException:
        print('===request exception===')
        return None

def downloadXY(outname,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    inputfile = open(outname,'r')

    for eachline in inputfile:

        #print (eachline)
        pdbname = eachline.lower().strip()[0:-1]
        outfilename=outdir+'/' + pdbname.upper()+'.data'
        fs_out=open(outfilename,'w')
        url='http://ndbserver.rutgers.edu/service/ndb/atlas/stfeatures?searchTarget='+ pdbname +'&ftrType=bphbc&type=csv'
        #print(html)
        html = getHtml(url)
        print(html)
        fs_out.write(str(html))
