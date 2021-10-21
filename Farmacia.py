# -*- coding: utf-8 -*-
import requests
import numpy as np
from bs4 import BeautifulSoup

#r = requests.get('https://www.drogaosuper.com.br/busca.asp?PalavraChave=dipirona&viewType=M&nrRows=60&idPage=1&ordem=V')

html = """<div class="products-list" data-colunas="3" data-linhas="20">
	        <ul class="grid-x">
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="99012">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/99012/dorflex-10-comprimidos" title="DORFLEX 10 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7891058002916_vitrine.jpg" alt="DORFLEX 10 COMPRIMIDOS" title="DORFLEX 10 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Cianocobalamina&nbsp;+ Citrato de Orfenadrina&nbsp;+ Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/99012/dorflex-10-comprimidos">DORFLEX 10 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">10 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3920&amp;fornecedor=Sanofi" title="Sanofi">Sanofi</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 6,08</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_99012" value="99012">
        <input type="hidden" id="IdProdutoGrade_Facilitado_99012" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_99012" value="N">
        <input type="hidden" id="Estoque_Facilitado_99012" value="79">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd99012" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd99012" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade99012" id="Quantidade99012" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar99012" onclick="AdicionarProdCarrinhoFacilitado('99012 ', '99012')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_99012">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager99012" value="{ 'name': 'DORFLEX 10 COMPRIMIDOS',  'id': '47165', 'price': '6.08', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 1}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="99013">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/99013/dorflex-36-comprimidos" title="DORFLEX 36 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/329032018151121.jpg" alt="DORFLEX 36 COMPRIMIDOS" title="DORFLEX 36 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p></p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/99013/dorflex-36-comprimidos">DORFLEX 36 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">36 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3920&amp;fornecedor=Sanofi" title="Sanofi">Sanofi</a></li>
    
            <li class="precoDe">de: R$ 22,28</li>
            <li class="precoPor">por: <span>R$ 18,39</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 3,89</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_99013" value="99013">
        <input type="hidden" id="IdProdutoGrade_Facilitado_99013" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_99013" value="N">
        <input type="hidden" id="Estoque_Facilitado_99013" value="53">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd99013" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd99013" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade99013" id="Quantidade99013" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar99013" onclick="AdicionarProdCarrinhoFacilitado('99013 ', '99013')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_99013">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager99013" value="{ 'name': 'DORFLEX 36 COMPRIMIDOS',  'id': '47625', 'price': '18.39', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 2}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="98674">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/98674/dipirona-sodica-500mg-10-comprimidos" title="DIPIRONA SÓDICA 500MG 10 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896769185026_vitrine.jpg" alt="DIPIRONA SÓDICA 500MG 10 COMPRIMIDOS" title="DIPIRONA SÓDICA 500MG 10 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sódica Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/98674/dipirona-sodica-500mg-10-comprimidos">DIPIRONA SÓDICA 500MG 10 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">10 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3786&amp;fornecedor=Ems" title="Ems">Ems</a></li>
    
            <li class="precoDe">de: R$ 5,92</li>
            <li class="precoPor">por: <span>R$ 4,89</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 1,03</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_98674" value="98674">
        <input type="hidden" id="IdProdutoGrade_Facilitado_98674" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_98674" value="N">
        <input type="hidden" id="Estoque_Facilitado_98674" value="237">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd98674" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd98674" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade98674" id="Quantidade98674" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar98674" onclick="AdicionarProdCarrinhoFacilitado('98674 ', '98674')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_98674">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager98674" value="{ 'name': 'DIPIRONA SÓDICA 500MG 10 COMPRIMIDOS',  'id': '38596', 'price': '4.89', 'brand': 'Ems', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 3}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="102769">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/102769/buscopan-composto-20-comprimidos" title="BUSCOPAN COMPOSTO 20 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/10012122017111849.jpg" alt="BUSCOPAN COMPOSTO 20 COMPRIMIDOS" title="BUSCOPAN COMPOSTO 20 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Butilbrometo de Escopolamina&nbsp;+ Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/102769/buscopan-composto-20-comprimidos">BUSCOPAN COMPOSTO 20 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">20 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3799&amp;fornecedor=Boehringer" title="Boehringer">Boehringer</a></li>
    
            <li class="precoDe">de: R$ 19,43</li>
            <li class="precoPor">por: <span>R$ 13,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 5,44</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_102769" value="102769">
        <input type="hidden" id="IdProdutoGrade_Facilitado_102769" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_102769" value="N">
        <input type="hidden" id="Estoque_Facilitado_102769" value="19">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd102769" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd102769" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade102769" id="Quantidade102769" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar102769" onclick="AdicionarProdCarrinhoFacilitado('102769 ', '102769')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_102769">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager102769" value="{ 'name': 'BUSCOPAN COMPOSTO 20 COMPRIMIDOS',  'id': '10010', 'price': '13.99', 'brand': 'Boehringer', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 4}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="104282">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/104282/neosaldina-20-drageas" title="NEOSALDINA 20 DRÁGEAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/4306082020104613.png" alt="NEOSALDINA 20 DRÁGEAS" title="NEOSALDINA 20 DRÁGEAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Dipirona&nbsp;+ Isometepteno</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/104282/neosaldina-20-drageas">NEOSALDINA 20 DRÁGEAS</a></h3></li>
    <li class="gramatura">20 Drágeas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3793&amp;fornecedor=Takeda" title="Takeda">Takeda</a></li>
    
            <li class="precoDe">de: R$ 24,88</li>
            <li class="precoPor">por: <span>R$ 16,90</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 7,98</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_104282" value="104282">
        <input type="hidden" id="IdProdutoGrade_Facilitado_104282" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_104282" value="N">
        <input type="hidden" id="Estoque_Facilitado_104282" value="26">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd104282" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd104282" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade104282" id="Quantidade104282" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar104282" onclick="AdicionarProdCarrinhoFacilitado('104282 ', '104282')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_104282">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager104282" value="{ 'name': 'NEOSALDINA 20 DRÁGEAS',  'id': '3727', 'price': '16.90', 'brand': 'Takeda', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 5}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105156">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105156/novalgina-1-g-10-comprimidos" title="NOVALGINA 1 G 10 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7891058001155_vitrine.jpg" alt="NOVALGINA 1 G 10 COMPRIMIDOS" title="NOVALGINA 1 G 10 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105156/novalgina-1-g-10-comprimidos">NOVALGINA 1 G 10 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">10 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3920&amp;fornecedor=Sanofi" title="Sanofi">Sanofi</a></li>
    
            <li class="precoDe">de: R$ 23,28</li>
            <li class="precoPor">por: <span>R$ 20,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,29</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105156" value="105156">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105156" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105156" value="N">
        <input type="hidden" id="Estoque_Facilitado_105156" value="17">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105156" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105156" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105156" id="Quantidade105156" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105156" onclick="AdicionarProdCarrinhoFacilitado('105156 ', '105156')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105156">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105156" value="{ 'name': 'NOVALGINA 1 G 10 COMPRIMIDOS',  'id': '30570', 'price': '20.99', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 6}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="103490">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/103490/cefaliv-12-comprimidos" title="CEFALIV 12 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/vermelho_referencia_vitrine.jpg" alt="CEFALIV 12 COMPRIMIDOS" title="CEFALIV 12 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Diidroergotamina&nbsp;+ Dipirona Sodica&nbsp;+ Rutosídeo</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/103490/cefaliv-12-comprimidos">CEFALIV 12 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">12 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3598&amp;fornecedor=Ach%E9" title="Aché">Aché</a></li>
    
            <li class="precoDe">de: R$ 18,29</li>
            <li class="precoPor">por: <span>R$ 14,63</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 3,66</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_103490" value="103490">
        <input type="hidden" id="IdProdutoGrade_Facilitado_103490" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_103490" value="N">
        <input type="hidden" id="Estoque_Facilitado_103490" value="15">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd103490" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd103490" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade103490" id="Quantidade103490" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar103490" onclick="AdicionarProdCarrinhoFacilitado('103490 ', '103490')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_103490">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager103490" value="{ 'name': 'CEFALIV 12 COMPRIMIDOS',  'id': '12186', 'price': '14.63', 'brand': 'Aché', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 7}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="98629">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/98629/dipirona-sodica-500-mg-20ml-gotas" title="DIPIRONA SÓDICA 500 MG 20ML GOTAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896004718446_vitrine.jpg" alt="DIPIRONA SÓDICA 500 MG 20ML GOTAS" title="DIPIRONA SÓDICA 500 MG 20ML GOTAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/98629/dipirona-sodica-500-mg-20ml-gotas">DIPIRONA SÓDICA 500 MG 20ML GOTAS</a></h3></li>
    <li class="gramatura">20ml Gotas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3786&amp;fornecedor=Ems" title="Ems">Ems</a></li>
    
            <li class="precoDe">de: R$ 11,44</li>
            <li class="precoPor">por: <span>R$ 6,79</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 4,65</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_98629" value="98629">
        <input type="hidden" id="IdProdutoGrade_Facilitado_98629" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_98629" value="N">
        <input type="hidden" id="Estoque_Facilitado_98629" value="103">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd98629" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd98629" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade98629" id="Quantidade98629" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar98629" onclick="AdicionarProdCarrinhoFacilitado('98629 ', '98629')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_98629">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager98629" value="{ 'name': 'DIPIRONA SÓDICA 500 MG 20ML GOTAS',  'id': '14083', 'price': '6.79', 'brand': 'Ems', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 8}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="104279">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/104279/neosaldina-10-drageas" title="NEOSALDINA 10 DRÁGEAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/606082020104330.png" alt="NEOSALDINA 10 DRÁGEAS" title="NEOSALDINA 10 DRÁGEAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Cloridrato de Isometepteno&nbsp;+ Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/104279/neosaldina-10-drageas">NEOSALDINA 10 DRÁGEAS</a></h3></li>
    <li class="gramatura">10 Drágeas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3793&amp;fornecedor=Takeda" title="Takeda">Takeda</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 14,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_104279" value="104279">
        <input type="hidden" id="IdProdutoGrade_Facilitado_104279" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_104279" value="N">
        <input type="hidden" id="Estoque_Facilitado_104279" value="24">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd104279" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd104279" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade104279" id="Quantidade104279" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar104279" onclick="AdicionarProdCarrinhoFacilitado('104279 ', '104279')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_104279">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager104279" value="{ 'name': 'NEOSALDINA 10 DRÁGEAS',  'id': '43585', 'price': '14.99', 'brand': 'Takeda', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 9}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="104280">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/104280/neosaldina-30-drageas" title="NEOSALDINA 30 DRÁGEAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/8906082020104758.png" alt="NEOSALDINA 30 DRÁGEAS" title="NEOSALDINA 30 DRÁGEAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Dipirona&nbsp;+ Isometepteno</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/104280/neosaldina-30-drageas">NEOSALDINA 30 DRÁGEAS</a></h3></li>
    <li class="gramatura">30 Drágeas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3793&amp;fornecedor=Takeda" title="Takeda">Takeda</a></li>
    
            <li class="precoDe">de: R$ 35,89</li>
            <li class="precoPor">por: <span>R$ 21,90</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 13,99</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_104280" value="104280">
        <input type="hidden" id="IdProdutoGrade_Facilitado_104280" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_104280" value="N">
        <input type="hidden" id="Estoque_Facilitado_104280" value="40">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd104280" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd104280" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade104280" id="Quantidade104280" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar104280" onclick="AdicionarProdCarrinhoFacilitado('104280 ', '104280')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_104280">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager104280" value="{ 'name': 'NEOSALDINA 30 DRÁGEAS',  'id': '40776', 'price': '21.90', 'brand': 'Takeda', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 10}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="104281">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/104281/neosaldina-4-drageas" title="NEOSALDINA 4 DRÁGEAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/1706082020094708.png" alt="NEOSALDINA 4 DRÁGEAS" title="NEOSALDINA 4 DRÁGEAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Cloridrato de Isometepteno&nbsp;+ Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/104281/neosaldina-4-drageas">NEOSALDINA 4 DRÁGEAS</a></h3></li>
    <li class="gramatura">4 Drágeas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3793&amp;fornecedor=Takeda" title="Takeda">Takeda</a></li>
    
            <li class="precoDe">de: R$ 6,38</li>
            <li class="precoPor">por: <span>R$ 5,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 0,39</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_104281" value="104281">
        <input type="hidden" id="IdProdutoGrade_Facilitado_104281" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_104281" value="N">
        <input type="hidden" id="Estoque_Facilitado_104281" value="36">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd104281" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd104281" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade104281" id="Quantidade104281" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar104281" onclick="AdicionarProdCarrinhoFacilitado('104281 ', '104281')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_104281">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager104281" value="{ 'name': 'NEOSALDINA 4 DRÁGEAS',  'id': '31475', 'price': '5.99', 'brand': 'Takeda', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 11}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="146547">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/146547/dorflex-uno-1g-10cpr" title="DORFLEX UNO 1G 10CPR">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/6209042020170255.jpg" alt="DORFLEX UNO 1G 10CPR" title="DORFLEX UNO 1G 10CPR" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/6209042020170255.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/4409042020170312.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/146547/dorflex-uno-1g-10cpr">DORFLEX UNO 1G 10CPR</a></h3></li>
    <li class="gramatura">10 COMPRIMIDOS</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3563&amp;fornecedor=Sanofi+Aventis" title="Sanofi Aventis">Sanofi Aventis</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 14,49</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_146547" value="146547">
        <input type="hidden" id="IdProdutoGrade_Facilitado_146547" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_146547" value="N">
        <input type="hidden" id="Estoque_Facilitado_146547" value="8">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd146547" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd146547" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade146547" id="Quantidade146547" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar146547" onclick="AdicionarProdCarrinhoFacilitado('146547 ', '146547')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_146547">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager146547" value="{ 'name': 'DORFLEX UNO 1G 10CPR',  'id': '52502', 'price': '14.49', 'brand': '', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 12}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="97614">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/97614/benegrip-6-comprimidos" title="BENEGRIP 6 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896094903036_vitrine.jpg" alt="BENEGRIP 6 COMPRIMIDOS" title="BENEGRIP 6 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Dipirona Sodica&nbsp;+ Maleato De Clorfenamina</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/97614/benegrip-6-comprimidos">BENEGRIP 6 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">6 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3791&amp;fornecedor=D+M" title="D M">D M</a></li>
    
            <li class="precoDe">de: R$ 11,25</li>
            <li class="precoPor">por: <span>R$ 10,49</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 0,76</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_97614" value="97614">
        <input type="hidden" id="IdProdutoGrade_Facilitado_97614" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_97614" value="N">
        <input type="hidden" id="Estoque_Facilitado_97614" value="46">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd97614" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd97614" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade97614" id="Quantidade97614" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar97614" onclick="AdicionarProdCarrinhoFacilitado('97614 ', '97614')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_97614">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager97614" value="{ 'name': 'BENEGRIP 6 COMPRIMIDOS',  'id': '17378', 'price': '10.49', 'brand': 'D M', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 13}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="123442">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/123442/dipimed-500-mgml-20ml" title="DIPIMED 500 MG/ML 20ML">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/6820062018082457.jpg" alt="DIPIMED 500 MG/ML 20ML" title="DIPIMED 500 MG/ML 20ML" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/6820062018082457.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/1920062018082548.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sódica Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/123442/dipimed-500-mgml-20ml">DIPIMED 500 MG/ML 20ML</a></h3></li>
    <li class="gramatura">20ml</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3861&amp;fornecedor=Medquimica" title="Medquimica">Medquimica</a></li>
    
            <li class="precoDe">de: R$ 12,73</li>
            <li class="precoPor">por: <span>R$ 4,90</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 7,83</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_123442" value="123442">
        <input type="hidden" id="IdProdutoGrade_Facilitado_123442" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_123442" value="N">
        <input type="hidden" id="Estoque_Facilitado_123442" value="4">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd123442" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd123442" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade123442" id="Quantidade123442" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar123442" onclick="AdicionarProdCarrinhoFacilitado('123442 ', '123442')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_123442">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager123442" value="{ 'name': 'DIPIMED 500 MG/ML 20ML',  'id': '1002376', 'price': '4.90', 'brand': '', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 14}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="103157">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/103157/doralgina-20-drageas" title="DORALGINA 20 DRÁGEAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896714210018_vitrine.jpg" alt="DORALGINA 20 DRÁGEAS" title="DORALGINA 20 DRÁGEAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Dipirona&nbsp;+ Isometepteno</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/103157/doralgina-20-drageas">DORALGINA 20 DRÁGEAS</a></h3></li>
    <li class="gramatura">20 drágeas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3651&amp;fornecedor=Neo+Qu%EDmica" title="Neo Química">Neo Química</a></li>
    
            <li class="precoDe">de: R$ 23,80</li>
            <li class="precoPor">por: <span>R$ 8,90</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 14,90</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_103157" value="103157">
        <input type="hidden" id="IdProdutoGrade_Facilitado_103157" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_103157" value="N">
        <input type="hidden" id="Estoque_Facilitado_103157" value="5">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd103157" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd103157" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade103157" id="Quantidade103157" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar103157" onclick="AdicionarProdCarrinhoFacilitado('103157 ', '103157')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_103157">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager103157" value="{ 'name': 'DORALGINA 20 DRÁGEAS',  'id': '42014', 'price': '8.90', 'brand': 'Neo Química', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 15}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="112360">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/112360/dipirona-sodica-500mg-30-comprimidos" title="DIPIRONA SÓDICA 500MG 30 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/2506122017104616.jpg" alt="DIPIRONA SÓDICA 500MG 30 COMPRIMIDOS" title="DIPIRONA SÓDICA 500MG 30 COMPRIMIDOS" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/2506122017104616.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/1606122017104641.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sódica Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/112360/dipirona-sodica-500mg-30-comprimidos">DIPIRONA SÓDICA 500MG 30 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">30 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3784&amp;fornecedor=Medley" title="Medley">Medley</a></li>
    
            <li class="precoDe">de: R$ 26,16</li>
            <li class="precoPor">por: <span>R$ 14,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 11,17</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_112360" value="112360">
        <input type="hidden" id="IdProdutoGrade_Facilitado_112360" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_112360" value="N">
        <input type="hidden" id="Estoque_Facilitado_112360" value="10">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd112360" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd112360" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade112360" id="Quantidade112360" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar112360" onclick="AdicionarProdCarrinhoFacilitado('112360 ', '112360')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_112360">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager112360" value="{ 'name': 'DIPIRONA SÓDICA 500MG 30 COMPRIMIDOS',  'id': '15750', 'price': '14.99', 'brand': '', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 16}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="109191">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/109191/dipirona-500mg-medley-10-comprimidos" title="DIPIRONA 500MG MEDLEY 10 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7725092017175057.jpg" alt="DIPIRONA 500MG MEDLEY 10 COMPRIMIDOS" title="DIPIRONA 500MG MEDLEY 10 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/109191/dipirona-500mg-medley-10-comprimidos">DIPIRONA 500MG MEDLEY 10 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">10 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3784&amp;fornecedor=Medley" title="Medley">Medley</a></li>
    
            <li class="precoDe">de: R$ 7,65</li>
            <li class="precoPor">por: <span>R$ 5,55</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,10</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_109191" value="109191">
        <input type="hidden" id="IdProdutoGrade_Facilitado_109191" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_109191" value="N">
        <input type="hidden" id="Estoque_Facilitado_109191" value="58">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd109191" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd109191" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade109191" id="Quantidade109191" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar109191" onclick="AdicionarProdCarrinhoFacilitado('109191 ', '109191')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_109191">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager109191" value="{ 'name': 'DIPIRONA 500MG MEDLEY 10 COMPRIMIDOS',  'id': '15751', 'price': '5.55', 'brand': 'Medley', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 17}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105148">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105148/novalgina-500-mg-10-comprimidos" title="NOVALGINA 500 MG 10 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7306032017131602.jpg" alt="NOVALGINA 500 MG 10 COMPRIMIDOS" title="NOVALGINA 500 MG 10 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105148/novalgina-500-mg-10-comprimidos">NOVALGINA 500 MG 10 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">10 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3920&amp;fornecedor=Sanofi" title="Sanofi">Sanofi</a></li>
    
            <li class="precoDe">de: R$ 12,98</li>
            <li class="precoPor">por: <span>R$ 11,69</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 1,29</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105148" value="105148">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105148" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105148" value="N">
        <input type="hidden" id="Estoque_Facilitado_105148" value="35">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105148" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105148" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105148" id="Quantidade105148" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105148" onclick="AdicionarProdCarrinhoFacilitado('105148 ', '105148')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105148">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105148" value="{ 'name': 'NOVALGINA 500 MG 10 COMPRIMIDOS',  'id': '13951', 'price': '11.69', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 18}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="97613">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/97613/benegrip-500mg-20-comprimidos" title="BENEGRIP 500MG 20 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896094904682_vitrine.jpg" alt="BENEGRIP 500MG 20 COMPRIMIDOS" title="BENEGRIP 500MG 20 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Maleato de clorfeniramina&nbsp;+ Dipirona Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/97613/benegrip-500mg-20-comprimidos">BENEGRIP 500MG 20 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">20 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3912&amp;fornecedor=Hypermarcas" title="Hypermarcas">Hypermarcas</a></li>
    
            <li class="precoDe">de: R$ 32,97</li>
            <li class="precoPor">por: <span>R$ 26,90</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 6,07</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_97613" value="97613">
        <input type="hidden" id="IdProdutoGrade_Facilitado_97613" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_97613" value="N">
        <input type="hidden" id="Estoque_Facilitado_97613" value="3">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd97613" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd97613" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade97613" id="Quantidade97613" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar97613" onclick="AdicionarProdCarrinhoFacilitado('97613 ', '97613')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_97613">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager97613" value="{ 'name': 'BENEGRIP 500MG 20 COMPRIMIDOS',  'id': '40198', 'price': '26.90', 'brand': 'Hypermarcas', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 19}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="98646">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/98646/dipirona-sodica-500-mg10-ml-10ml-gotas" title="DIPIRONA SÓDICA 500 MG/10 ML 10ML GOTAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896004715841_vitrine.jpg" alt="DIPIRONA SÓDICA 500 MG/10 ML 10ML GOTAS" title="DIPIRONA SÓDICA 500 MG/10 ML 10ML GOTAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/98646/dipirona-sodica-500-mg10-ml-10ml-gotas">DIPIRONA SÓDICA 500 MG/10 ML 10ML GOTAS</a></h3></li>
    <li class="gramatura">10ml Gotas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3786&amp;fornecedor=Ems" title="Ems">Ems</a></li>
    
            <li class="precoDe">de: R$ 6,23</li>
            <li class="precoPor">por: <span>R$ 3,91</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,32</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_98646" value="98646">
        <input type="hidden" id="IdProdutoGrade_Facilitado_98646" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_98646" value="N">
        <input type="hidden" id="Estoque_Facilitado_98646" value="26">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd98646" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd98646" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade98646" id="Quantidade98646" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar98646" onclick="AdicionarProdCarrinhoFacilitado('98646 ', '98646')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_98646">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager98646" value="{ 'name': 'DIPIRONA SÓDICA 500 MG/10 ML 10ML GOTAS',  'id': '3783', 'price': '3.91', 'brand': 'Ems', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 20}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="111194">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/111194/nevralgex-cimed-30-comprimidos" title="NEVRALGEX CIMED 30 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/3119092017142908.jpg" alt="NEVRALGEX CIMED 30 COMPRIMIDOS" title="NEVRALGEX CIMED 30 COMPRIMIDOS" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/3119092017142908.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/2619092017142930.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/111194/nevralgex-cimed-30-comprimidos">NEVRALGEX CIMED 30 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">30 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3695&amp;fornecedor=Cimed" title="Cimed">Cimed</a></li>
    
            <li class="precoDe">de: R$ 17,51</li>
            <li class="precoPor">por: <span>R$ 9,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 7,52</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_111194" value="111194">
        <input type="hidden" id="IdProdutoGrade_Facilitado_111194" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_111194" value="N">
        <input type="hidden" id="Estoque_Facilitado_111194" value="3">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd111194" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd111194" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade111194" id="Quantidade111194" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar111194" onclick="AdicionarProdCarrinhoFacilitado('111194 ', '111194')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_111194">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager111194" value="{ 'name': 'NEVRALGEX CIMED 30 COMPRIMIDOS',  'id': '49038', 'price': '9.99', 'brand': '', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 21}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105159">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105159/novalgina-500-mg-20ml-gotas" title="NOVALGINA 500 MG 20ML GOTAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7891058489038_vitrine.jpg" alt="NOVALGINA 500 MG 20ML GOTAS" title="NOVALGINA 500 MG 20ML GOTAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105159/novalgina-500-mg-20ml-gotas">NOVALGINA 500 MG 20ML GOTAS</a></h3></li>
    <li class="gramatura">20ml Gotas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3920&amp;fornecedor=Sanofi" title="Sanofi">Sanofi</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 24,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105159" value="105159">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105159" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105159" value="N">
        <input type="hidden" id="Estoque_Facilitado_105159" value="1">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105159" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105159" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105159" id="Quantidade105159" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105159" onclick="AdicionarProdCarrinhoFacilitado('105159 ', '105159')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105159">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105159" value="{ 'name': 'NOVALGINA 500 MG 20ML GOTAS',  'id': '30085', 'price': '24.99', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 22}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105161">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105161/novalgina-50-mg-100ml" title="NOVALGINA 50 MG 100ML">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7891058464073_vitrine.jpg" alt="NOVALGINA 50 MG 100ML" title="NOVALGINA 50 MG 100ML">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105161/novalgina-50-mg-100ml">NOVALGINA 50 MG 100ML</a></h3></li>
    <li class="gramatura">100ML</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3563&amp;fornecedor=Sanofi+Aventis" title="Sanofi Aventis">Sanofi Aventis</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 33,29</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105161" value="105161">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105161" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105161" value="N">
        <input type="hidden" id="Estoque_Facilitado_105161" value="4">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105161" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105161" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105161" id="Quantidade105161" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105161" onclick="AdicionarProdCarrinhoFacilitado('105161 ', '105161')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105161">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105161" value="{ 'name': 'NOVALGINA 50 MG 100ML',  'id': '10069', 'price': '33.29', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 23}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="125373">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/125373/miorrelax-300mg50mg35mg-30-comprimidos" title="MIORRELAX 300MG/50MG/35MG 30 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7110092018112124.jpg" alt="MIORRELAX 300MG/50MG/35MG 30 COMPRIMIDOS" title="MIORRELAX 300MG/50MG/35MG 30 COMPRIMIDOS" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/7110092018112124.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/1310092018112200.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/125373/miorrelax-300mg50mg35mg-30-comprimidos">MIORRELAX 300MG/50MG/35MG 30 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">30 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=4442&amp;fornecedor=Hypera+Pharma" title="Hypera Pharma">Hypera Pharma</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 16,94</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_125373" value="125373">
        <input type="hidden" id="IdProdutoGrade_Facilitado_125373" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_125373" value="N">
        <input type="hidden" id="Estoque_Facilitado_125373" value="2">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd125373" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd125373" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade125373" id="Quantidade125373" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar125373" onclick="AdicionarProdCarrinhoFacilitado('125373 ', '125373')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_125373">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager125373" value="{ 'name': 'MIORRELAX 300MG/50MG/35MG 30 COMPRIMIDOS',  'id': '50181', 'price': '16.94', 'brand': '', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 24}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="97599">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/97599/lisador-24-comprimidos" title="LISADOR 24 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7897322707211_vitrine.jpg" alt="LISADOR 24 COMPRIMIDOS" title="LISADOR 24 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Adifenina&nbsp;+ Dipirona Sodica&nbsp;+ Prometazina</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/97599/lisador-24-comprimidos">LISADOR 24 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">24 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3564&amp;fornecedor=Farmasa" title="Farmasa">Farmasa</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 48,56</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_97599" value="97599">
        <input type="hidden" id="IdProdutoGrade_Facilitado_97599" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_97599" value="N">
        <input type="hidden" id="Estoque_Facilitado_97599" value="4">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd97599" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd97599" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade97599" id="Quantidade97599" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar97599" onclick="AdicionarProdCarrinhoFacilitado('97599 ', '97599')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_97599">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager97599" value="{ 'name': 'LISADOR 24 COMPRIMIDOS',  'id': '46007', 'price': '48.56', 'brand': 'Farmasa', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 25}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105150">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105150/novalgina-efervescente-1g-10-comprimidos-efervescentes" title="NOVALGINA EFERVESCENTE 1G 10 COMPRIMIDOS EFERVESCENTES">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7891058015756_vitrine.jpg" alt="NOVALGINA EFERVESCENTE 1G 10 COMPRIMIDOS EFERVESCENTES" title="NOVALGINA EFERVESCENTE 1G 10 COMPRIMIDOS EFERVESCENTES">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sódica Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105150/novalgina-efervescente-1g-10-comprimidos-efervescentes">NOVALGINA EFERVESCENTE 1G 10 COMPRIMIDOS EFERVESCENTES</a></h3></li>
    <li class="gramatura">10 comprimidos efervescentes</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3621&amp;fornecedor=Sanofi%2DAventis" title="Sanofi-Aventis">Sanofi-Aventis</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 26,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105150" value="105150">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105150" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105150" value="N">
        <input type="hidden" id="Estoque_Facilitado_105150" value="6">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105150" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105150" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105150" id="Quantidade105150" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105150" onclick="AdicionarProdCarrinhoFacilitado('105150 ', '105150')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105150">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105150" value="{ 'name': 'NOVALGINA EFERVESCENTE 1G 10 COMPRIMIDOS EFERVESCENTES',  'id': '41419', 'price': '26.99', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 26}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="103198">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/103198/dipirona-1g-10-comprimidos" title="DIPIRONA 1G 10 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896714207551_vitrine.jpg" alt="DIPIRONA 1G 10 COMPRIMIDOS" title="DIPIRONA 1G 10 COMPRIMIDOS">

                    <img class="flag" src="https://static-webv8.jet.com.br/drogaosuper/Status/esgotado.jpg" alt="Esgotado">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/103198/dipirona-1g-10-comprimidos">DIPIRONA 1G 10 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">10 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=4082&amp;fornecedor=Neo+Quimica+Generico" title="Neo Quimica Generico">Neo Quimica Generico</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 18,22</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_103198" value="103198">
        <input type="hidden" id="IdProdutoGrade_Facilitado_103198" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_103198" value="N">
        <input type="hidden" id="Estoque_Facilitado_103198" value="40">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd103198" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd103198" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade103198" id="Quantidade103198" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar103198" onclick="AdicionarProdCarrinhoFacilitado('103198 ', '103198')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_103198">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager103198" value="{ 'name': 'DIPIRONA 1G 10 COMPRIMIDOS',  'id': '43837', 'price': '18.22', 'brand': 'Neo Quimica Generico', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 27}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="97449">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/97449/apracur-6-comprimidos-revestidos" title="APRACUR 6 COMPRIMIDOS REVESTIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/1927062018100059.jpg" alt="APRACUR 6 COMPRIMIDOS REVESTIDOS" title="APRACUR 6 COMPRIMIDOS REVESTIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Clorfeniramina&nbsp;+ Dipirona Sodica&nbsp;+ Acido Ascorbico</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/97449/apracur-6-comprimidos-revestidos">APRACUR 6 COMPRIMIDOS REVESTIDOS</a></h3></li>
    <li class="gramatura">6 Comprimidos Revestidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3791&amp;fornecedor=D+M" title="D M">D M</a></li>
    
            <li class="precoDe">de: R$ 9,99</li>
            <li class="precoPor">por: <span>R$ 7,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,00</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_97449" value="97449">
        <input type="hidden" id="IdProdutoGrade_Facilitado_97449" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_97449" value="N">
        <input type="hidden" id="Estoque_Facilitado_97449" value="31">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd97449" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd97449" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade97449" id="Quantidade97449" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar97449" onclick="AdicionarProdCarrinhoFacilitado('97449 ', '97449')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_97449">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager97449" value="{ 'name': 'APRACUR 6 COMPRIMIDOS REVESTIDOS',  'id': '17379', 'price': '7.99', 'brand': 'D M', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 28}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="124153">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/124153/lisador-dip-1g-4-comprimidos" title="LISADOR DIP 1G 4 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7705072018092049.jpg" alt="LISADOR DIP 1G 4 COMPRIMIDOS" title="LISADOR DIP 1G 4 COMPRIMIDOS" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/7705072018092049.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/1305072018092130.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sódica Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/124153/lisador-dip-1g-4-comprimidos">LISADOR DIP 1G 4 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">4 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3564&amp;fornecedor=Farmasa" title="Farmasa">Farmasa</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 7,75</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_124153" value="124153">
        <input type="hidden" id="IdProdutoGrade_Facilitado_124153" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_124153" value="N">
        <input type="hidden" id="Estoque_Facilitado_124153" value="28">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd124153" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd124153" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade124153" id="Quantidade124153" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar124153" onclick="AdicionarProdCarrinhoFacilitado('124153 ', '124153')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_124153">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager124153" value="{ 'name': 'LISADOR DIP 1G 4 COMPRIMIDOS',  'id': '49696', 'price': '7.75', 'brand': '', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 29}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="102794">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/102794/anador-500mg-24-comprimidos" title="ANADOR 500MG 24 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896026300988_vitrine.jpg" alt="ANADOR 500MG 24 COMPRIMIDOS" title="ANADOR 500MG 24 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/102794/anador-500mg-24-comprimidos">ANADOR 500MG 24 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">24 comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3799&amp;fornecedor=Boehringer" title="Boehringer">Boehringer</a></li>
    
            <li class="precoDe">de: R$ 21,68</li>
            <li class="precoPor">por: <span>R$ 18,09</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 3,59</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_102794" value="102794">
        <input type="hidden" id="IdProdutoGrade_Facilitado_102794" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_102794" value="N">
        <input type="hidden" id="Estoque_Facilitado_102794" value="3">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd102794" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd102794" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade102794" id="Quantidade102794" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar102794" onclick="AdicionarProdCarrinhoFacilitado('102794 ', '102794')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_102794">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager102794" value="{ 'name': 'ANADOR 500MG 24 COMPRIMIDOS',  'id': '13271', 'price': '18.09', 'brand': 'Boehringer', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 30}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="111199">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/111199/benegrip-12-comprimidos" title="BENEGRIP 12 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/3719092017152045.jpg" alt="BENEGRIP 12 COMPRIMIDOS" title="BENEGRIP 12 COMPRIMIDOS" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/3719092017152045.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/8819092017152112.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/111199/benegrip-12-comprimidos">BENEGRIP 12 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">12 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3454&amp;fornecedor=Hypermarcas" title="Hypermarcas">Hypermarcas</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 20,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_111199" value="111199">
        <input type="hidden" id="IdProdutoGrade_Facilitado_111199" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_111199" value="N">
        <input type="hidden" id="Estoque_Facilitado_111199" value="25">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd111199" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd111199" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade111199" id="Quantidade111199" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar111199" onclick="AdicionarProdCarrinhoFacilitado('111199 ', '111199')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_111199">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager111199" value="{ 'name': 'BENEGRIP 12 COMPRIMIDOS',  'id': '48849', 'price': '20.99', 'brand': '', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 31}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="97592">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/97592/lisador-500mg-8-comprimidos" title="LISADOR 500MG 8 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/9104072018100324.png" alt="LISADOR 500MG 8 COMPRIMIDOS" title="LISADOR 500MG 8 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Ácido Gamaminobutírico&nbsp;+ Adifenina&nbsp;+ Cobalto&nbsp;+ Dipirona Sodica&nbsp;+ Prometazina</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/97592/lisador-500mg-8-comprimidos">LISADOR 500MG 8 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">8 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3564&amp;fornecedor=Farmasa" title="Farmasa">Farmasa</a></li>
    
            <li class="precoDe">de: R$ 17,96</li>
            <li class="precoPor">por: <span>R$ 14,09</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 3,87</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_97592" value="97592">
        <input type="hidden" id="IdProdutoGrade_Facilitado_97592" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_97592" value="N">
        <input type="hidden" id="Estoque_Facilitado_97592" value="26">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd97592" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd97592" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade97592" id="Quantidade97592" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar97592" onclick="AdicionarProdCarrinhoFacilitado('97592 ', '97592')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_97592">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager97592" value="{ 'name': 'LISADOR 500MG 8 COMPRIMIDOS',  'id': '15098', 'price': '14.09', 'brand': 'Farmasa', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 32}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="99260">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/99260/dorflex-icy-hot-spray-118ml" title="DORFLEX ICY HOT SPRAY 118ML">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/1429112017160849.jpg" alt="DORFLEX ICY HOT SPRAY 118ML" title="DORFLEX ICY HOT SPRAY 118ML">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Citrato de Orfenadrina&nbsp;+ Cafeína Anidra&nbsp;+ Dipirona Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/99260/dorflex-icy-hot-spray-118ml">DORFLEX ICY HOT SPRAY 118ML</a></h3></li>
    <li class="gramatura">118ml</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3563&amp;fornecedor=Sanofi+Aventis" title="Sanofi Aventis">Sanofi Aventis</a></li>
    
            <li class="precoDe">de: R$ 37,29</li>
            <li class="precoPor">por: <span>R$ 34,69</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,60</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_99260" value="99260">
        <input type="hidden" id="IdProdutoGrade_Facilitado_99260" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_99260" value="N">
        <input type="hidden" id="Estoque_Facilitado_99260" value="2">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd99260" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd99260" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade99260" id="Quantidade99260" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar99260" onclick="AdicionarProdCarrinhoFacilitado('99260 ', '99260')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_99260">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager99260" value="{ 'name': 'DORFLEX ICY HOT SPRAY 118ML',  'id': '43622', 'price': '34.69', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 33}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="109188">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/109188/dipirona-sodica-50mg-medley-100ml" title="DIPIRONA SÓDICA 50MG MEDLEY 100ML">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896422506243_Vitrine.jpg" alt="DIPIRONA SÓDICA 50MG MEDLEY 100ML" title="DIPIRONA SÓDICA 50MG MEDLEY 100ML">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sódica Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/109188/dipirona-sodica-50mg-medley-100ml">DIPIRONA SÓDICA 50MG MEDLEY 100ML</a></h3></li>
    <li class="gramatura">100ml</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3784&amp;fornecedor=Medley" title="Medley">Medley</a></li>
    
            <li class="precoDe">de: R$ 19,13</li>
            <li class="precoPor">por: <span>R$ 12,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 6,14</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_109188" value="109188">
        <input type="hidden" id="IdProdutoGrade_Facilitado_109188" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_109188" value="N">
        <input type="hidden" id="Estoque_Facilitado_109188" value="8">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd109188" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd109188" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade109188" id="Quantidade109188" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar109188" onclick="AdicionarProdCarrinhoFacilitado('109188 ', '109188')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_109188">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager109188" value="{ 'name': 'DIPIRONA SÓDICA 50MG MEDLEY 100ML',  'id': '15464', 'price': '12.99', 'brand': 'Medley', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 34}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="97625">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/97625/cafilisador-4-comprimidos" title="CAFILISADOR 4 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/777319015_vitrine.jpg" alt="CAFILISADOR 4 COMPRIMIDOS" title="CAFILISADOR 4 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeína Anidra&nbsp;+ Dipirona Sódica Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/97625/cafilisador-4-comprimidos">CAFILISADOR 4 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">4 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3564&amp;fornecedor=Farmasa" title="Farmasa">Farmasa</a></li>
    
            <li class="precoDe">de: R$ 8,68</li>
            <li class="precoPor">por: <span>R$ 6,59</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,09</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_97625" value="97625">
        <input type="hidden" id="IdProdutoGrade_Facilitado_97625" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_97625" value="N">
        <input type="hidden" id="Estoque_Facilitado_97625" value="36">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd97625" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd97625" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade97625" id="Quantidade97625" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar97625" onclick="AdicionarProdCarrinhoFacilitado('97625 ', '97625')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_97625">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager97625" value="{ 'name': 'CAFILISADOR 4 COMPRIMIDOS',  'id': '31901', 'price': '6.59', 'brand': 'Farmasa', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 35}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105151">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105151/novalgina-1g-4-comprimidos" title="NOVALGINA 1G 4 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7725092017155356.jpg" alt="NOVALGINA 1G 4 COMPRIMIDOS" title="NOVALGINA 1G 4 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105151/novalgina-1g-4-comprimidos">NOVALGINA 1G 4 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">4 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3621&amp;fornecedor=Sanofi%2DAventis" title="Sanofi-Aventis">Sanofi-Aventis</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 9,28</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105151" value="105151">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105151" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105151" value="N">
        <input type="hidden" id="Estoque_Facilitado_105151" value="30">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105151" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105151" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105151" id="Quantidade105151" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105151" onclick="AdicionarProdCarrinhoFacilitado('105151 ', '105151')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105151">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105151" value="{ 'name': 'NOVALGINA 1G 4 COMPRIMIDOS',  'id': '36668', 'price': '9.28', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 36}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="103877">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/103877/tropinal-20-comprimidos" title="TROPINAL 20 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/vermelho_referencia_vitrine.jpg" alt="TROPINAL 20 COMPRIMIDOS" title="TROPINAL 20 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Bromidrato de Hiosciamina&nbsp;+ Butilbrometo de Escopolamina&nbsp;+ Dipirona Sodica&nbsp;+ Metilbrometo de Homatropina</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/103877/tropinal-20-comprimidos">TROPINAL 20 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">20 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3786&amp;fornecedor=Ems" title="Ems">Ems</a></li>
    
            <li class="precoDe">de: R$ 21,42</li>
            <li class="precoPor">por: <span>R$ 18,19</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 3,23</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_103877" value="103877">
        <input type="hidden" id="IdProdutoGrade_Facilitado_103877" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_103877" value="N">
        <input type="hidden" id="Estoque_Facilitado_103877" value="3">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd103877" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd103877" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade103877" id="Quantidade103877" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar103877" onclick="AdicionarProdCarrinhoFacilitado('103877 ', '103877')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_103877">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager103877" value="{ 'name': 'TROPINAL 20 COMPRIMIDOS',  'id': '11289', 'price': '18.19', 'brand': 'Ems', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 37}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="103010">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/103010/lisador-16-comprimidos" title="LISADOR 16 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/704072018102419.jpg" alt="LISADOR 16 COMPRIMIDOS" title="LISADOR 16 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Adifenina&nbsp;+ Dipirona Sodica&nbsp;+ Prometazina</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/103010/lisador-16-comprimidos">LISADOR 16 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">16 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3564&amp;fornecedor=Farmasa" title="Farmasa">Farmasa</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 35,95</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_103010" value="103010">
        <input type="hidden" id="IdProdutoGrade_Facilitado_103010" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_103010" value="N">
        <input type="hidden" id="Estoque_Facilitado_103010" value="3">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd103010" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd103010" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade103010" id="Quantidade103010" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar103010" onclick="AdicionarProdCarrinhoFacilitado('103010 ', '103010')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_103010">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager103010" value="{ 'name': 'LISADOR 16 COMPRIMIDOS',  'id': '15878', 'price': '35.95', 'brand': 'Farmasa', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 38}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="103498">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/103498/mionevrix-20-comprimidos" title="MIONEVRIX 20 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/vermelho_referencia_vitrine.jpg" alt="MIONEVRIX 20 COMPRIMIDOS" title="MIONEVRIX 20 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Carisoprodol&nbsp;+ Dipirona Sodica&nbsp;+ Piridoxina&nbsp;+ Tiamina</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/103498/mionevrix-20-comprimidos">MIONEVRIX 20 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">20 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3598&amp;fornecedor=Ach%E9" title="Aché">Aché</a></li>
    
            <li class="precoDe">de: R$ 35,75</li>
            <li class="precoPor">por: <span>R$ 33,49</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,26</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_103498" value="103498">
        <input type="hidden" id="IdProdutoGrade_Facilitado_103498" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_103498" value="N">
        <input type="hidden" id="Estoque_Facilitado_103498" value="2">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd103498" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd103498" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade103498" id="Quantidade103498" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar103498" onclick="AdicionarProdCarrinhoFacilitado('103498 ', '103498')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_103498">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager103498" value="{ 'name': 'MIONEVRIX 20 COMPRIMIDOS',  'id': '10275', 'price': '33.49', 'brand': 'Aché', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 39}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="97506">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/97506/doralgina-4-comprimidos" title="DORALGINA 4 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896714210070_vitrine.jpg" alt="DORALGINA 4 COMPRIMIDOS" title="DORALGINA 4 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Dipirona&nbsp;+ Isometepteno</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/97506/doralgina-4-comprimidos">DORALGINA 4 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">4 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3651&amp;fornecedor=Neo+Qu%EDmica" title="Neo Química">Neo Química</a></li>
    
            <li class="precoDe">de: R$ 5,89</li>
            <li class="precoPor">por: <span>R$ 2,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,90</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_97506" value="97506">
        <input type="hidden" id="IdProdutoGrade_Facilitado_97506" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_97506" value="N">
        <input type="hidden" id="Estoque_Facilitado_97506" value="4">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd97506" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd97506" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade97506" id="Quantidade97506" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar97506" onclick="AdicionarProdCarrinhoFacilitado('97506 ', '97506')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_97506">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager97506" value="{ 'name': 'DORALGINA 4 COMPRIMIDOS',  'id': '42008', 'price': '2.99', 'brand': 'Neo Química', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 40}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="98703">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/98703/anador-500mg-4-comprimidos" title="ANADOR 500MG 4 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896026303408_vitrine.jpg" alt="ANADOR 500MG 4 COMPRIMIDOS" title="ANADOR 500MG 4 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/98703/anador-500mg-4-comprimidos">ANADOR 500MG 4 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">4 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3799&amp;fornecedor=Boehringer" title="Boehringer">Boehringer</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 4,15</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_98703" value="98703">
        <input type="hidden" id="IdProdutoGrade_Facilitado_98703" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_98703" value="N">
        <input type="hidden" id="Estoque_Facilitado_98703" value="69">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd98703" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd98703" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade98703" id="Quantidade98703" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar98703" onclick="AdicionarProdCarrinhoFacilitado('98703 ', '98703')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_98703">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager98703" value="{ 'name': 'ANADOR 500MG 4 COMPRIMIDOS',  'id': '40349', 'price': '4.15', 'brand': 'Boehringer', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 41}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="98046">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/98046/nevralgex-10-comprimidos" title="NEVRALGEX 10 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896523207360_vitrine.jpg" alt="NEVRALGEX 10 COMPRIMIDOS" title="NEVRALGEX 10 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p></p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/98046/nevralgex-10-comprimidos">NEVRALGEX 10 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">10 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3695&amp;fornecedor=Cimed" title="Cimed">Cimed</a></li>
    
            <li class="precoDe">de: R$ 6,06</li>
            <li class="precoPor">por: <span>R$ 4,59</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 1,47</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_98046" value="98046">
        <input type="hidden" id="IdProdutoGrade_Facilitado_98046" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_98046" value="N">
        <input type="hidden" id="Estoque_Facilitado_98046" value="11">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd98046" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd98046" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade98046" id="Quantidade98046" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar98046" onclick="AdicionarProdCarrinhoFacilitado('98046 ', '98046')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_98046">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager98046" value="{ 'name': 'NEVRALGEX 10 COMPRIMIDOS',  'id': '43265', 'price': '4.59', 'brand': 'Cimed', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 42}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="109186">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/109186/dipirona-sodica-500mgml-medley-10ml" title="DIPIRONA SÓDICA 500MG/ML MEDLEY 10ML">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896422506229_Vitrine.jpg" alt="DIPIRONA SÓDICA 500MG/ML MEDLEY 10ML" title="DIPIRONA SÓDICA 500MG/ML MEDLEY 10ML">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sódica Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/109186/dipirona-sodica-500mgml-medley-10ml">DIPIRONA SÓDICA 500MG/ML MEDLEY 10ML</a></h3></li>
    <li class="gramatura">10ml</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3784&amp;fornecedor=Medley" title="Medley">Medley</a></li>
    
            <li class="precoDe">de: R$ 9,81</li>
            <li class="precoPor">por: <span>R$ 6,19</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 3,62</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_109186" value="109186">
        <input type="hidden" id="IdProdutoGrade_Facilitado_109186" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_109186" value="N">
        <input type="hidden" id="Estoque_Facilitado_109186" value="5">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd109186" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd109186" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade109186" id="Quantidade109186" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar109186" onclick="AdicionarProdCarrinhoFacilitado('109186 ', '109186')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_109186">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager109186" value="{ 'name': 'DIPIRONA SÓDICA 500MG/ML MEDLEY 10ML',  'id': '15314', 'price': '6.19', 'brand': 'Medley', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 43}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="146557">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/146557/dorflex-uno-enxaqueca-1g-4-comprimidos" title="DORFLEX UNO ENXAQUECA  1G 4 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/1813042020112808.jpg" alt="DORFLEX UNO ENXAQUECA  1G 4 COMPRIMIDOS" title="DORFLEX UNO ENXAQUECA  1G 4 COMPRIMIDOS" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/1813042020112808.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/9213042020112822.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/146557/dorflex-uno-enxaqueca-1g-4-comprimidos">DORFLEX UNO ENXAQUECA  1G 4 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">1 GRAMA COM 4 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3563&amp;fornecedor=Sanofi+Aventis" title="Sanofi Aventis">Sanofi Aventis</a></li>
    
            <li class="precoDe">de: R$ 5,54</li>
            <li class="precoPor">por: <span>R$ 4,89</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 0,65</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_146557" value="146557">
        <input type="hidden" id="IdProdutoGrade_Facilitado_146557" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_146557" value="N">
        <input type="hidden" id="Estoque_Facilitado_146557" value="27">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd146557" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd146557" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade146557" id="Quantidade146557" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar146557" onclick="AdicionarProdCarrinhoFacilitado('146557 ', '146557')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_146557">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager146557" value="{ 'name': 'DORFLEX UNO ENXAQUECA  1G 4 COMPRIMIDOS',  'id': '52503', 'price': '4.89', 'brand': 'Dorflex', 'category': 'ANALGÉSICOS', 'variant': '', 'position': 44}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105162">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105162/novalgina-500-mg-30-comprimidos" title="NOVALGINA 500 MG 30 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7891058008635_vitrine.jpg" alt="NOVALGINA 500 MG 30 COMPRIMIDOS" title="NOVALGINA 500 MG 30 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105162/novalgina-500-mg-30-comprimidos">NOVALGINA 500 MG 30 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">30 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3920&amp;fornecedor=Sanofi" title="Sanofi">Sanofi</a></li>
    
            <li class="precoDe">de: R$ 34,97</li>
            <li class="precoPor">por: <span>R$ 31,29</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 3,68</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105162" value="105162">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105162" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105162" value="N">
        <input type="hidden" id="Estoque_Facilitado_105162" value="3">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105162" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105162" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105162" id="Quantidade105162" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105162" onclick="AdicionarProdCarrinhoFacilitado('105162 ', '105162')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105162">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105162" value="{ 'name': 'NOVALGINA 500 MG 30 COMPRIMIDOS',  'id': '13586', 'price': '31.29', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 45}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105147">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105147/novalgina-500-mg-10-ml-gotas" title="NOVALGINA 500 MG 10 ML GOTAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7891058487096_vitrine.jpg" alt="NOVALGINA 500 MG 10 ML GOTAS" title="NOVALGINA 500 MG 10 ML GOTAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105147/novalgina-500-mg-10-ml-gotas">NOVALGINA 500 MG 10 ML GOTAS</a></h3></li>
    <li class="gramatura">10 mL Gotas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3920&amp;fornecedor=Sanofi" title="Sanofi">Sanofi</a></li>
    
            <li class="precoDe">de: R$ 13,17</li>
            <li class="precoPor">por: <span>R$ 11,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 1,18</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105147" value="105147">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105147" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105147" value="N">
        <input type="hidden" id="Estoque_Facilitado_105147" value="6">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105147" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105147" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105147" id="Quantidade105147" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105147" onclick="AdicionarProdCarrinhoFacilitado('105147 ', '105147')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105147">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105147" value="{ 'name': 'NOVALGINA 500 MG 10 ML GOTAS',  'id': '30083', 'price': '11.99', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 46}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105149">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105149/novalgina-efervescente-1g-2-comprimidos" title="NOVALGINA EFERVESCENTE 1G 2 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7891058015770_vitrine.jpg" alt="NOVALGINA EFERVESCENTE 1G 2 COMPRIMIDOS" title="NOVALGINA EFERVESCENTE 1G 2 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105149/novalgina-efervescente-1g-2-comprimidos">NOVALGINA EFERVESCENTE 1G 2 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">2 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3621&amp;fornecedor=Sanofi%2DAventis" title="Sanofi-Aventis">Sanofi-Aventis</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 5,18</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105149" value="105149">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105149" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105149" value="N">
        <input type="hidden" id="Estoque_Facilitado_105149" value="36">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105149" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105149" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105149" id="Quantidade105149" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105149" onclick="AdicionarProdCarrinhoFacilitado('105149 ', '105149')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105149">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105149" value="{ 'name': 'NOVALGINA EFERVESCENTE 1G 2 COMPRIMIDOS',  'id': '41420', 'price': '5.18', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 47}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="109187">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/109187/dipirona-sodica-500mgml-medley-20ml" title="DIPIRONA SÓDICA 500MG/ML MEDLEY 20ML">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896422506236_Vitrine.jpg" alt="DIPIRONA SÓDICA 500MG/ML MEDLEY 20ML" title="DIPIRONA SÓDICA 500MG/ML MEDLEY 20ML">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sódica Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/109187/dipirona-sodica-500mgml-medley-20ml">DIPIRONA SÓDICA 500MG/ML MEDLEY 20ML</a></h3></li>
    <li class="gramatura">20ml</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3784&amp;fornecedor=Medley" title="Medley">Medley</a></li>
    
            <li class="precoDe">de: R$ 13,72</li>
            <li class="precoPor">por: <span>R$ 8,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 4,73</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_109187" value="109187">
        <input type="hidden" id="IdProdutoGrade_Facilitado_109187" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_109187" value="N">
        <input type="hidden" id="Estoque_Facilitado_109187" value="9">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd109187" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd109187" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade109187" id="Quantidade109187" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar109187" onclick="AdicionarProdCarrinhoFacilitado('109187 ', '109187')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_109187">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager109187" value="{ 'name': 'DIPIRONA SÓDICA 500MG/ML MEDLEY 20ML',  'id': '15315', 'price': '8.99', 'brand': 'Medley', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 48}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="125353">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/125353/miorrelax-300mg50mg35mg-10-comprimidos" title="MIORRELAX 300MG/50MG/35MG 10 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/906092018155220.jpg" alt="MIORRELAX 300MG/50MG/35MG 10 COMPRIMIDOS" title="MIORRELAX 300MG/50MG/35MG 10 COMPRIMIDOS" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/906092018155220.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/9006092018155247.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/125353/miorrelax-300mg50mg35mg-10-comprimidos">MIORRELAX 300MG/50MG/35MG 10 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">10 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=4442&amp;fornecedor=Hypera+Pharma" title="Hypera Pharma">Hypera Pharma</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 5,49</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_125353" value="125353">
        <input type="hidden" id="IdProdutoGrade_Facilitado_125353" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_125353" value="N">
        <input type="hidden" id="Estoque_Facilitado_125353" value="12">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd125353" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd125353" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade125353" id="Quantidade125353" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar125353" onclick="AdicionarProdCarrinhoFacilitado('125353 ', '125353')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_125353">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager125353" value="{ 'name': 'MIORRELAX 300MG/50MG/35MG 10 COMPRIMIDOS',  'id': '50182', 'price': '5.49', 'brand': '', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 49}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="98690">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/98690/dipirona-sodica-50-mgml-100ml-solucao" title="DIPIRONA SÓDICA 50 MG/ML 100ML SOLUÇÃO">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7896004715674_vitrine.jpg" alt="DIPIRONA SÓDICA 50 MG/ML 100ML SOLUÇÃO" title="DIPIRONA SÓDICA 50 MG/ML 100ML SOLUÇÃO">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/98690/dipirona-sodica-50-mgml-100ml-solucao">DIPIRONA SÓDICA 50 MG/ML 100ML SOLUÇÃO</a></h3></li>
    <li class="gramatura">100ml Solução</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3786&amp;fornecedor=Ems" title="Ems">Ems</a></li>
    
            <li class="precoDe">de: R$ 14,46</li>
            <li class="precoPor">por: <span>R$ 11,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,47</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_98690" value="98690">
        <input type="hidden" id="IdProdutoGrade_Facilitado_98690" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_98690" value="N">
        <input type="hidden" id="Estoque_Facilitado_98690" value="20">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd98690" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd98690" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade98690" id="Quantidade98690" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar98690" onclick="AdicionarProdCarrinhoFacilitado('98690 ', '98690')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_98690">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager98690" value="{ 'name': 'DIPIRONA SÓDICA 50 MG/ML 100ML SOLUÇÃO',  'id': '32151', 'price': '11.99', 'brand': 'Ems', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 50}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="146595">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/146595/atroveran-dip-1g" title="ATROVERAN DIP 1G">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/8030042020131544.JPG" alt="ATROVERAN DIP 1G" title="ATROVERAN DIP 1G" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/8030042020131544.JPG',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/9930042020131628.JPG',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/146595/atroveran-dip-1g">ATROVERAN DIP 1G</a></h3></li>
    <li class="gramatura">20 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3454&amp;fornecedor=Hypermarcas" title="Hypermarcas">Hypermarcas</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 18,33</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_146595" value="146595">
        <input type="hidden" id="IdProdutoGrade_Facilitado_146595" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_146595" value="N">
        <input type="hidden" id="Estoque_Facilitado_146595" value="4">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd146595" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd146595" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade146595" id="Quantidade146595" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar146595" onclick="AdicionarProdCarrinhoFacilitado('146595 ', '146595')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_146595">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager146595" value="{ 'name': 'ATROVERAN DIP 1G',  'id': '51410', 'price': '18.33', 'brand': '', 'category': 'ANALGÉSICOS', 'variant': '', 'position': 51}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105170">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105170/dorflex-gotas-20ml-gotas" title="DORFLEX GOTAS 20ML GOTAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7891058009458_vitrine.jpg" alt="DORFLEX GOTAS 20ML GOTAS" title="DORFLEX GOTAS 20ML GOTAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Citrato de Orfenadrina&nbsp;+ Cafeína Anidra&nbsp;+ Dipirona Sódica Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105170/dorflex-gotas-20ml-gotas">DORFLEX GOTAS 20ML GOTAS</a></h3></li>
    <li class="gramatura">20ml Gotas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3621&amp;fornecedor=Sanofi%2DAventis" title="Sanofi-Aventis">Sanofi-Aventis</a></li>
    
            <li class="precoDe">de: R$ 16,97</li>
            <li class="precoPor">por: <span>R$ 14,69</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,28</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105170" value="105170">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105170" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105170" value="N">
        <input type="hidden" id="Estoque_Facilitado_105170" value="2">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105170" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105170" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105170" id="Quantidade105170" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105170" onclick="AdicionarProdCarrinhoFacilitado('105170 ', '105170')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105170">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105170" value="{ 'name': 'DORFLEX GOTAS 20ML GOTAS',  'id': '13868', 'price': '14.69', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 52}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="99686">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/99686/dexalgen-injetavel-3-ampolas" title="DEXALGEN (INJETÁVEL) 3 AMPOLAS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/vermelho_referencia_vitrine.jpg" alt="DEXALGEN (INJETÁVEL) 3 AMPOLAS" title="DEXALGEN (INJETÁVEL) 3 AMPOLAS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dexametasona&nbsp;+ Dipirona Sodica&nbsp;+ Hidroxocobalamina</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/99686/dexalgen-injetavel-3-ampolas">DEXALGEN (INJETÁVEL) 3 AMPOLAS</a></h3></li>
    <li class="gramatura">3 Ampolas</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3684&amp;fornecedor=Eurofarma" title="Eurofarma">Eurofarma</a></li>
    
            <li class="precoDe">de: R$ 51,83</li>
            <li class="precoPor">por: <span>R$ 43,59</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 8,24</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_99686" value="99686">
        <input type="hidden" id="IdProdutoGrade_Facilitado_99686" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_99686" value="N">
        <input type="hidden" id="Estoque_Facilitado_99686" value="1">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd99686" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd99686" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade99686" id="Quantidade99686" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar99686" onclick="AdicionarProdCarrinhoFacilitado('99686 ', '99686')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_99686">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager99686" value="{ 'name': 'DEXALGEN (INJETÁVEL) 3 AMPOLAS',  'id': '11348', 'price': '43.59', 'brand': 'Eurofarma', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 53}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="105144">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/105144/novalgina-infantil-5-supositorios" title="NOVALGINA INFANTIL 5 SUPOSITÓRIOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7891058467098_vitrine.jpg" alt="NOVALGINA INFANTIL 5 SUPOSITÓRIOS" title="NOVALGINA INFANTIL 5 SUPOSITÓRIOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/105144/novalgina-infantil-5-supositorios">NOVALGINA INFANTIL 5 SUPOSITÓRIOS</a></h3></li>
    <li class="gramatura">5 Supositórios</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3920&amp;fornecedor=Sanofi" title="Sanofi">Sanofi</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 15,98</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_105144" value="105144">
        <input type="hidden" id="IdProdutoGrade_Facilitado_105144" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_105144" value="N">
        <input type="hidden" id="Estoque_Facilitado_105144" value="1">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd105144" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd105144" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade105144" id="Quantidade105144" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar105144" onclick="AdicionarProdCarrinhoFacilitado('105144 ', '105144')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_105144">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager105144" value="{ 'name': 'NOVALGINA INFANTIL 5 SUPOSITÓRIOS',  'id': '10419', 'price': '15.98', 'brand': 'Sanofi-Aventis', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 54}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="103030">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/103030/cafilisador-16-comprimidos" title="CAFILISADOR 16 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7897322706528_vitrine.jpg" alt="CAFILISADOR 16 COMPRIMIDOS" title="CAFILISADOR 16 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Cafeina&nbsp;+ Dipirona Sodica</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/103030/cafilisador-16-comprimidos">CAFILISADOR 16 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">16 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3564&amp;fornecedor=Farmasa" title="Farmasa">Farmasa</a></li>
    
            <li class="precoDe">de: R$ 34,27</li>
            <li class="precoPor">por: <span>R$ 31,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,28</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_103030" value="103030">
        <input type="hidden" id="IdProdutoGrade_Facilitado_103030" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_103030" value="N">
        <input type="hidden" id="Estoque_Facilitado_103030" value="3">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd103030" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd103030" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade103030" id="Quantidade103030" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar103030" onclick="AdicionarProdCarrinhoFacilitado('103030 ', '103030')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_103030">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager103030" value="{ 'name': 'CAFILISADOR 16 COMPRIMIDOS',  'id': '31900', 'price': '31.99', 'brand': 'Farmasa', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 55}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="146572">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/146572/atroveran-dip-1g-4-comprimidos" title="ATROVERAN DIP 1G 4 comprimidos">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/6424042020114215.jpg" alt="ATROVERAN DIP 1G 4 comprimidos" title="ATROVERAN DIP 1G 4 comprimidos" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/6424042020114215.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/7724042020114248.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/146572/atroveran-dip-1g-4-comprimidos">ATROVERAN DIP 1G 4 comprimidos</a></h3></li>
    <li class="gramatura">4 comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3912&amp;fornecedor=Hypermarcas" title="Hypermarcas">Hypermarcas</a></li>
    
            <li class="precoDe">de: R$ 5,99</li>
            <li class="precoPor">por: <span>R$ 4,49</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 1,50</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_146572" value="146572">
        <input type="hidden" id="IdProdutoGrade_Facilitado_146572" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_146572" value="N">
        <input type="hidden" id="Estoque_Facilitado_146572" value="120">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd146572" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd146572" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade146572" id="Quantidade146572" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar146572" onclick="AdicionarProdCarrinhoFacilitado('146572 ', '146572')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_146572">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager146572" value="{ 'name': 'ATROVERAN DIP 1G 4 comprimidos',  'id': '51411', 'price': '4.49', 'brand': 'Atroveran', 'category': 'ANALGÉSICOS', 'variant': '', 'position': 56}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="142876">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/142876/dorilen-20ml" title="DORILEN 20ML">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/6407012019171759.jpg" alt="DORILEN 20ML" title="DORILEN 20ML">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona&nbsp;+ Cloridrato De Prometazina</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/142876/dorilen-20ml">DORILEN 20ML</a></h3></li>
    <li class="gramatura">20ml</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3821&amp;fornecedor=Legrand" title="Legrand">Legrand</a></li>
    
            <li class="precoDe">de: R$ 35,26</li>
            <li class="precoPor">por: <span>R$ 19,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 15,27</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_142876" value="142876">
        <input type="hidden" id="IdProdutoGrade_Facilitado_142876" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_142876" value="N">
        <input type="hidden" id="Estoque_Facilitado_142876" value="2">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd142876" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd142876" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade142876" id="Quantidade142876" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar142876" onclick="AdicionarProdCarrinhoFacilitado('142876 ', '142876')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_142876">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager142876" value="{ 'name': 'DORILEN 20ML',  'id': '49491', 'price': '19.99', 'brand': 'Legrand', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 57}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative  table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="103878">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/103878/tropinal-15-ml" title="TROPINAL 15 ML">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/vermelho_referencia_vitrine.jpg" alt="TROPINAL 15 ML" title="TROPINAL 15 ML">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Bromidrato de Hiosciamina&nbsp;+ Butilbrometo de Escopolamina&nbsp;+ Dipirona Sodica&nbsp;+ Metilbrometo de Homatropina</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/103878/tropinal-15-ml">TROPINAL 15 ML</a></h3></li>
    <li class="gramatura">15 ml</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3786&amp;fornecedor=Ems" title="Ems">Ems</a></li>
    
            <li class="precoDe">de: R$ 23,08</li>
            <li class="precoPor">por: <span>R$ 20,39</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">economize R$ 2,69</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_103878" value="103878">
        <input type="hidden" id="IdProdutoGrade_Facilitado_103878" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_103878" value="N">
        <input type="hidden" id="Estoque_Facilitado_103878" value="2">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd103878" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd103878" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade103878" id="Quantidade103878" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar103878" onclick="AdicionarProdCarrinhoFacilitado('103878 ', '103878')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_103878">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager103878" value="{ 'name': 'TROPINAL 15 ML',  'id': '11285', 'price': '20.39', 'brand': 'Ems', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 58}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="146556">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/146556/dorflex-uno-enxaqueca-1g-com-10-comprimidos-efervescentes-sabor-limao" title="DORFLEX UNO ENXAQUECA 1G COM 10 COMPRIMIDOS EFERVESCENTES SABOR LIMÃO">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/4113042020110531.jpg" alt="DORFLEX UNO ENXAQUECA 1G COM 10 COMPRIMIDOS EFERVESCENTES SABOR LIMÃO" title="DORFLEX UNO ENXAQUECA 1G COM 10 COMPRIMIDOS EFERVESCENTES SABOR LIMÃO" onmouseout="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/4113042020110531.jpg',this)" onmouseover="ImagemAlternativa('https://static-webv8.jet.com.br/drogaosuper/Produto/2013042020110546.jpg',this)">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Dipirona Monoidratada</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/146556/dorflex-uno-enxaqueca-1g-com-10-comprimidos-efervescentes-sabor-limao">DORFLEX UNO ENXAQUECA 1G COM 10 COMPRIMIDOS EFERVESCENTES SABOR...</a><a class="nomeCompleto" href="https://www.drogaosuper.com.br/produto/146556/dorflex-uno-enxaqueca-1g-com-10-comprimidos-efervescentes-sabor-limao" style="display: none;">DORFLEX UNO ENXAQUECA 1G COM 10 COMPRIMIDOS EFERVESCENTES SABOR LIMÃO</a></h3></li>
    <li class="gramatura">10 COMPRIMIDOS EFERVESCENTES SABOR LIMÃO</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3563&amp;fornecedor=Sanofi+Aventis" title="Sanofi Aventis">Sanofi Aventis</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 25,99</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_146556" value="146556">
        <input type="hidden" id="IdProdutoGrade_Facilitado_146556" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_146556" value="N">
        <input type="hidden" id="Estoque_Facilitado_146556" value="2">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd146556" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd146556" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade146556" id="Quantidade146556" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar146556" onclick="AdicionarProdCarrinhoFacilitado('146556 ', '146556')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_146556">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager146556" value="{ 'name': 'DORFLEX UNO ENXAQUECA 1G COM 10 COMPRIMIDOS EFERVESCENTES SABOR LIMÃO',  'id': '52505', 'price': '25.99', 'brand': 'Dorflex', 'category': 'ANALGÉSICOS', 'variant': '', 'position': 59}">
     
</ul>

	              </div>
	            </li>
	          
	            <li class="product-list-container relative border-left table-left small-6 medium-4">
	              <div class="produtos">
	                
<ul class="itemGtm">
  <!--Inicio Tag Manager Product Impressions-->
  <li class="tagManagerProd" style="display:none">
      <input type="hidden" id="hdnIdProdutoClickTagManager" value="97598">
  </li>
  <!--Final Tag Manager Product Impressions-->
    <li class="foto">

            <a href="https://www.drogaosuper.com.br/produto/97598/lisador-4-comprimidos" title="LISADOR 4 COMPRIMIDOS">
                <img class="produto" src="https://static-webv8.jet.com.br/drogaosuper/Produto/7897322706320_vitrine.jpg" alt="LISADOR 4 COMPRIMIDOS" title="LISADOR 4 COMPRIMIDOS">

            </a>


    </li>
    <li class="disponibilidade">

    </li>
    <li class="pAtivoResumo" style=""><p>Adifenina&nbsp;+ Dipirona&nbsp;+ Prometazina</p></li>
    <li class="nome"><h3><a href="https://www.drogaosuper.com.br/produto/97598/lisador-4-comprimidos">LISADOR 4 COMPRIMIDOS</a></h3></li>
    <li class="gramatura">4 Comprimidos</li>
		<li class="fornecedor"><a href="https://www.drogaosuper.com.br/fornecedor.asp?idFornecedor=3564&amp;fornecedor=Farmasa" title="Farmasa">Farmasa</a></li>
    
            <li class="precoDe precoDeTraco">&nbsp;</li>
            <li class="precoPor"><span>R$ 9,39</span></li>

          <li class="parcelamento">&nbsp;</li>
        
        <li class="economize">&nbsp;</li>

			<li>
        <input type="hidden" id="IdProduto_Facilitado_97598" value="97598">
        <input type="hidden" id="IdProdutoGrade_Facilitado_97598" value="0">
        <input type="hidden" id="PossuiGrade_Facilitado_97598" value="N">
        <input type="hidden" id="Estoque_Facilitado_97598" value="71">
				<div class="btnCompraFacil">
					<div class="holder">
            <fieldset class="control">
              <input class="icon icon-default icon-arrow-up-white" type="button" value="+" id="addqtd97598" onclick="controlsComprar($(this));">
              <input class="icon icon-default icon-arrow-down-white" type="button" value="-" id="removeqtd97598" onclick="controlsComprar($(this));">
            </fieldset>
						<input class="textfield qtd" type="text" name="Quantidade97598" id="Quantidade97598" maxlength="3" value="1" size="4" onkeypress="return SoNumber(event);">
          <a class="btnAddProduto semibold uppercase" type="button" id="Comprar97598" onclick="AdicionarProdCarrinhoFacilitado('97598 ', '97598')">Incluir na Cesta</a>
          </div>
        </div>
			</li>

    <li class="comparador">
        <input type="hidden" name="hdn_produto__" id="hdn_produto__" value="">
        <label>
            <input type="checkbox" name="check__" id="check__" onclick="fillHdnNoRepeat(document.getElementById('hdn_idProd'), document.getElementById('hdn_produto__').value, document.getElementById('check__'));">
            <span>Comparar produto</span>
        </label>
    </li>
    <li class="maskAddProduto" id="maskAddProduto_97598">
      <div class="content"><img src="https://images-drogaosuper.jet.com.br/icon_addproduto.png" alt=""><br><span>Incluído na cesta<br>com sucesso</span></div>
    </li>

    <input type="hidden" id="arrayProductClicksManager97598" value="{ 'name': 'LISADOR 4 COMPRIMIDOS',  'id': '33054', 'price': '9.39', 'brand': 'Farmasa', 'category': 'MEDICAMENTOS', 'variant': '', 'position': 60}">
     
</ul>

	              </div>
	            </li>
	          
	        </ul>
	      </div>"""

soup = BeautifulSoup(html, 'html.parser')
vetor1 = []
vetor2 = []
for d in soup.find_all("div", attrs={"class": "products-list"}):
    for x in d.find_all("li", attrs={"class", "nome"}):
        z = x.find("a").get_text().strip()
        vetor1.append(z)

for i in soup.find_all("div", attrs={"class": "products-list"}):
    for q in i.find_all("div", attrs={"class", "produtos"}):
        e = q.find("span").get_text().strip()
        vetor2.append(e)

vetor_nome = np.array(vetor1)
vetor_preco = np.array(vetor2)

matriz = np.dstack((vetor_nome,vetor_preco))
print(matriz)