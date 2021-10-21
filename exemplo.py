# -*- coding: utf-8 -*-
import requests
import numpy as np
from bs4 import BeautifulSoup


html = """<span data-target="nome_produto" class="text-body cursor-pointer text-limit-2" style="min-height:40px">Dipirona Monoidratada 500mg Prati com 30 Comprimidos</span>"""
preco = """<span class="font-weight-bold font-xl text-marine">R$ 9,90</span>"""

soup = BeautifulSoup(html, 'html.parser')
d = soup.find("span").get_text().strip()

soup = BeautifulSoup(preco, 'html.parser')
f = soup.find("span").get_text().strip()

print(d)
print(f)