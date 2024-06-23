import numpy as np
import matplotlib.pyplot as plt
import requests
from matplotlib.widgets import Slider, Button, RadioButtons
from bs4 import BeautifulSoup

def getuppl():

    url = "https://aurbjorg.is/husnaedislan/samanburdartafla"

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, 'lxml')


    tbl = soup.find('table')
    rows = tbl.findAll('tr')

    lanveitandi = []
    lantokugjald = []
    uppgreidslugjald = []

    vobstr = []
    vofstr = []
    vvbstr = []
    vvfstr = []

    vobint = []
    vofint = []
    vvbint = []
    vvfint = []

    vobintvidb = []
    vofintvidb = []
    vvbintvidb = []
    vvfintvidb = []


    for i in rows:
        lantokug = i.find("td", class_ = "LoanTable-row-cell LoanTable-row-cell-lantokugjald")
        nafn = i.find("td", class_ ="LoanTable-row-cell LoanTable-row-cell-loan-provider")
        nafnb = i.find("td", class_ ="LoanTable-row-cell LoanTable-row-cell-loan-provider-inactive")
        vextir = i.findAll("td", class_ = "LoanTable-row-cell LoanTable-row-cell-vextir")
        uppgreidslug = i.find("td", class_ = "LoanTable-row-cell LoanTable-row-cell-uppgreidslugjald")
        if nafn is not None:
            lanveitandi.append(nafn.get_text())
        if nafnb is not None:
            lanveitandi.append(nafnb.get_text())
        if lantokug is not None:
            str = lantokug.get_text().replace(" kr.","")
            str = str.replace(".","")
            lantokugjald.append(int(str))

        vcnt = 0
        for j in vextir:
            if vcnt == 0:
                vobstr.append(j.get_text())
            if vcnt == 1:
                vofstr.append(j.get_text())
            if vcnt == 2:
                vvbstr.append(j.get_text())
            if vcnt == 3:
                vvfstr.append(j.get_text())
            vcnt = vcnt + 1
        if uppgreidslug is not None:
            str = uppgreidslug.get_text()
            strspl = str.split("%",1)
            uppgreidslugjald.append(float(strspl[0]))

    for i in range(0,len(vobstr)):
        if vobstr[i] is "":
            vobint.append(0)
            vobintvidb.append(0)
        if vobstr[i] is not "":
            strsplit = vobstr[i].split("%",1)
            vobint.append(float(strsplit[0]))
            if strsplit[1] is "":
                vobintvidb.append(0)
            if strsplit[1] is not "":
                sstrsplit = strsplit[1].split("%",1)
                ssstrsplit = sstrsplit[0].split("(",1)
                vobintvidb.append(float(ssstrsplit[1]))

    for i in range(0,len(vofstr)):
        if vofstr[i] is "":
            vofint.append(0)
            vofintvidb.append(0)
        if vofstr[i] is not "":
            strsplit = vofstr[i].split("%",1)
            vofint.append(float(strsplit[0]))
            if strsplit[1] is "":
                vofintvidb.append(0)
            if strsplit[1] is not "":
                sstrsplit = strsplit[1].split("%",1)
                ssstrsplit = sstrsplit[0].split("(",1)
                vofintvidb.append(float(ssstrsplit[1]))

    for i in range(0,len(vvbstr)):
        if vvbstr[i] is "":
            vvbint.append(0)
            vvbintvidb.append(0)
        if vvbstr[i] is not "":
            strsplit = vvbstr[i].split("%",1)
            vvbint.append(float(strsplit[0]))
            if strsplit[1] is "":
                vvbintvidb.append(0)
            if strsplit[1] is not "":
                sstrsplit = strsplit[1].split("%",1)
                ssstrsplit = sstrsplit[0].split("(",1)
                vvbintvidb.append(float(ssstrsplit[1]))

    for i in range(0,len(vvfstr)):
        if vvfstr[i] is "":
            vvfint.append(0)
            vvfintvidb.append(0)
        if vvfstr[i] is not "":
            strsplit = vvfstr[i].split("%",1)
            vvfint.append(float(strsplit[0]))
            if strsplit[1] is "":
                vvfintvidb.append(0)
            if strsplit[1] is not "":
                sstrsplit = strsplit[1].split("%",1)
                ssstrsplit = sstrsplit[0].split("(",1)
                vvfintvidb.append(float(ssstrsplit[1]))

    return lanveitandi,lantokugjald,vobint,vofint,vvbint,vvfint,vobintvidb,vofintvidb,vvbintvidb,vvfintvidb,uppgreidslugjald
    #print(lanveitandi)
    #print(lantokugjald)
    #print(vobint)
    #print(vobintvidb)
    #print(vofint)
    #print(vofintvidb)
    #print(vvbint)
    #print(vvbintvidb)
    #print(vvfint)
    #print(vvfintvidb)
    #print(uppgreidslugjald)
