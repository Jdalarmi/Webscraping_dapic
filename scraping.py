import requests
import pandas as pd



url = "https://dapic.webpic.com.br/pivot/gestaoestoquepivot/consultar"

payload = {
    "DataInicial": "01/11/2023",
    "DataFinal": "31/12/2023",
    "TipoProduto": 0,
    "TiposProdutos": [
        {
            "Value": 0,
            "Text": "Produto acabado"
        },
        {
            "Value": 1,
            "Text": "Matéria prima"
        },
        {
            "Value": 2,
            "Text": "Almoxarifado"
        }
    ],
    "IdsEmpresas": [1],
    "IdsArmazenadores": [1],
    "Modelos": [
        {
            "ReportObject": None,
            "ModeloParticular": False,
            "ModeloPadrao": False,
            "id": "",
            "text": "Modelos padronizados",
            "children": [
                {
                    "ReportObject": "{\"options\":{\"grid\":{\"type\":\"flat\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"Ncm\"},{\"uniqueName\":\"UnidadeMedida\"},{\"uniqueName\":\"Referencia\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"CustoUnitario\",\"aggregation\":\"sum\"},{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ne9tr83oq3u00\"},{\"uniqueName\":\"ValorTotalCustoDisponivel\",\"aggregation\":\"sum\"},{\"uniqueName\":\"EstoqueMinimo\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-2jpe837v4ict0\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Armazenador\",\"Referencia\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"UnidadeMedida\",\"CustoUnitario\",\"QuantidadeDisponivel\",\"ValorTotalCustoDisponivel\",\"Ncm\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \",\"textAlign\":\"center\"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"},{\"name\":\"-2jpe837v4ict0\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"},{\"name\":\"-ne9tr83oq3u00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 152,
                    "text": "Custo dos produtos em estoque"
                },
                {
                    "ReportObject": "{\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"EstoqueMinimo\",\"aggregation\":\"sum\",\"format\":\"-2jpe837v4ict0\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"ValorTotalCustoReal\",\"QuantidadeDisponivel\",\"ValorTotalCustoDisponivel\",\"QuantidadeComprometido\",\"ValorTotalCustoComprometido\",\"QuantidadeProducao\",\"ValorTotalCustoProducao\",\"QuantidadeConsignado\",\"ValorTotalCustoConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"},{\"name\":\"-2jpe837v4ict0\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 140,
                    "text": "Estoque mínimo dos produtos"
                },
                {
                    "ReportObject": "{\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeEntrada\",\"aggregation\":\"sum\",\"format\":\"-m7gvfcbs8aw00\"},{\"uniqueName\":\"QuantidadeSaida\",\"aggregation\":\"sum\",\"format\":\"-m7gvfcbs8aw00\"},{\"uniqueName\":\"EstoqueMinimo\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-2jpe837v4ict0\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"QuantidadeEntrada\",\"QuantidadeSaida\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \",\"textAlign\":\"center\"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"},{\"name\":\"-2jpe837v4ict0\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"},{\"name\":\"-m7gvfcbs8aw00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 151,
                    "text": "Quantidade de entradas e saídas dos produtos"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 999999999999999999)\",\"measure\":\"ValorTotalCustoDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#DCEDC8\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}},{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"ValorTotalCustoComprometido\",\"aggregation\":\"sum\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"ValorTotalCustoReal\",\"QuantidadeDisponivel\",\"ValorTotalCustoDisponivel\",\"QuantidadeComprometido\",\"ValorTotalCustoComprometido\",\"QuantidadeProducao\",\"ValorTotalCustoProducao\",\"QuantidadeConsignado\",\"ValorTotalCustoConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 155,
                    "text": "Quantidade de produtos comprometidos"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 999999999999999999)\",\"measure\":\"ValorTotalCustoDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#DCEDC8\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}},{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"ValorTotalCustoConsignado\",\"aggregation\":\"sum\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"ValorTotalCustoReal\",\"QuantidadeDisponivel\",\"ValorTotalCustoDisponivel\",\"QuantidadeComprometido\",\"ValorTotalCustoComprometido\",\"QuantidadeProducao\",\"ValorTotalCustoProducao\",\"QuantidadeConsignado\",\"ValorTotalCustoConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 154,
                    "text": "Quantidade de produtos em consignado"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 999999999999999999)\",\"measure\":\"ValorTotalCustoDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#DCEDC8\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}},{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"ValorTotalCustoProducao\",\"aggregation\":\"sum\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"ValorTotalCustoReal\",\"QuantidadeDisponivel\",\"ValorTotalCustoDisponivel\",\"QuantidadeComprometido\",\"ValorTotalCustoComprometido\",\"QuantidadeProducao\",\"ValorTotalCustoProducao\",\"QuantidadeConsignado\",\"ValorTotalCustoConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 153,
                    "text": "Quantidade de produtos em produção"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"EstoqueMinimo\"},{\"uniqueName\":\"QuantidadeEntrada\"},{\"uniqueName\":\"QuantidadeSaida\"},{\"uniqueName\":\"ValorUltimaCompra\"},{\"uniqueName\":\"CustoUnitario\"},{\"uniqueName\":\"QuantidadeReal\"},{\"uniqueName\":\"QuantidadeDisponivel\"},{\"uniqueName\":\"QuantidadeComprometido\"},{\"uniqueName\":\"QuantidadeProducao\"},{\"uniqueName\":\"QuantidadeConsignado\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Empresa\",\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"EstoqueMinimo\",\"QuantidadeEntrada\",\"QuantidadeSaida\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"QuantidadeDisponivel\",\"QuantidadeComprometido\",\"QuantidadeProducao\",\"QuantidadeConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 138,
                    "text": "Quantidade disponível separado por armazenador"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Colecao\"},{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"EstoqueMinimo\"},{\"uniqueName\":\"QuantidadeEntrada\"},{\"uniqueName\":\"QuantidadeSaida\"},{\"uniqueName\":\"ValorUltimaCompra\"},{\"uniqueName\":\"CustoUnitario\"},{\"uniqueName\":\"QuantidadeReal\"},{\"uniqueName\":\"QuantidadeDisponivel\"},{\"uniqueName\":\"QuantidadeComprometido\"},{\"uniqueName\":\"QuantidadeProducao\"},{\"uniqueName\":\"QuantidadeConsignado\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Empresa\",\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"EstoqueMinimo\",\"QuantidadeEntrada\",\"QuantidadeSaida\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"QuantidadeDisponivel\",\"QuantidadeComprometido\",\"QuantidadeProducao\",\"QuantidadeConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 144,
                    "text": "Quantidade disponível separado por coleção"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Empresa\"},{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"EstoqueMinimo\"},{\"uniqueName\":\"QuantidadeEntrada\"},{\"uniqueName\":\"QuantidadeSaida\"},{\"uniqueName\":\"ValorUltimaCompra\"},{\"uniqueName\":\"CustoUnitario\"},{\"uniqueName\":\"QuantidadeReal\"},{\"uniqueName\":\"QuantidadeDisponivel\"},{\"uniqueName\":\"QuantidadeComprometido\"},{\"uniqueName\":\"QuantidadeProducao\"},{\"uniqueName\":\"QuantidadeConsignado\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Empresa\",\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"EstoqueMinimo\",\"QuantidadeEntrada\",\"QuantidadeSaida\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"QuantidadeDisponivel\",\"QuantidadeComprometido\",\"QuantidadeProducao\",\"QuantidadeConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 150,
                    "text": "Quantidade disponível separado por empresa"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Finalidade\"},{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"EstoqueMinimo\"},{\"uniqueName\":\"QuantidadeEntrada\"},{\"uniqueName\":\"QuantidadeSaida\"},{\"uniqueName\":\"ValorUltimaCompra\"},{\"uniqueName\":\"CustoUnitario\"},{\"uniqueName\":\"QuantidadeReal\"},{\"uniqueName\":\"QuantidadeDisponivel\"},{\"uniqueName\":\"QuantidadeComprometido\"},{\"uniqueName\":\"QuantidadeProducao\"},{\"uniqueName\":\"QuantidadeConsignado\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Empresa\",\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"EstoqueMinimo\",\"QuantidadeEntrada\",\"QuantidadeSaida\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"QuantidadeDisponivel\",\"QuantidadeComprometido\",\"QuantidadeProducao\",\"QuantidadeConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 143,
                    "text": "Quantidade disponível separado por finalidade"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Genero\"},{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"EstoqueMinimo\"},{\"uniqueName\":\"QuantidadeEntrada\"},{\"uniqueName\":\"QuantidadeSaida\"},{\"uniqueName\":\"ValorUltimaCompra\"},{\"uniqueName\":\"CustoUnitario\"},{\"uniqueName\":\"QuantidadeReal\"},{\"uniqueName\":\"QuantidadeDisponivel\"},{\"uniqueName\":\"QuantidadeComprometido\"},{\"uniqueName\":\"QuantidadeProducao\"},{\"uniqueName\":\"QuantidadeConsignado\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Empresa\",\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"EstoqueMinimo\",\"QuantidadeEntrada\",\"QuantidadeSaida\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"QuantidadeDisponivel\",\"QuantidadeComprometido\",\"QuantidadeProducao\",\"QuantidadeConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 145,
                    "text": "Quantidade disponível separado por gênero"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"GrupoMateriaPrima\"},{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"EstoqueMinimo\"},{\"uniqueName\":\"QuantidadeEntrada\"},{\"uniqueName\":\"QuantidadeSaida\"},{\"uniqueName\":\"ValorUltimaCompra\"},{\"uniqueName\":\"CustoUnitario\"},{\"uniqueName\":\"QuantidadeReal\"},{\"uniqueName\":\"QuantidadeDisponivel\"},{\"uniqueName\":\"QuantidadeComprometido\"},{\"uniqueName\":\"QuantidadeProducao\"},{\"uniqueName\":\"QuantidadeConsignado\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Empresa\",\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"EstoqueMinimo\",\"QuantidadeEntrada\",\"QuantidadeSaida\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"QuantidadeDisponivel\",\"QuantidadeComprometido\",\"QuantidadeProducao\",\"QuantidadeConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 148,
                    "text": "Quantidade disponível separado por grupo de matéria-prima"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"GrupoProdutoAcababo\"},{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"EstoqueMinimo\"},{\"uniqueName\":\"QuantidadeEntrada\"},{\"uniqueName\":\"QuantidadeSaida\"},{\"uniqueName\":\"ValorUltimaCompra\"},{\"uniqueName\":\"CustoUnitario\"},{\"uniqueName\":\"QuantidadeReal\"},{\"uniqueName\":\"QuantidadeDisponivel\"},{\"uniqueName\":\"QuantidadeComprometido\"},{\"uniqueName\":\"QuantidadeProducao\"},{\"uniqueName\":\"QuantidadeConsignado\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Empresa\",\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"EstoqueMinimo\",\"QuantidadeEntrada\",\"QuantidadeSaida\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"QuantidadeDisponivel\",\"QuantidadeComprometido\",\"QuantidadeProducao\",\"QuantidadeConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 146,
                    "text": "Quantidade disponível separado por grupo de produto"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Linha\"},{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"EstoqueMinimo\"},{\"uniqueName\":\"QuantidadeEntrada\"},{\"uniqueName\":\"QuantidadeSaida\"},{\"uniqueName\":\"ValorUltimaCompra\"},{\"uniqueName\":\"CustoUnitario\"},{\"uniqueName\":\"QuantidadeReal\"},{\"uniqueName\":\"QuantidadeDisponivel\"},{\"uniqueName\":\"QuantidadeComprometido\"},{\"uniqueName\":\"QuantidadeProducao\"},{\"uniqueName\":\"QuantidadeConsignado\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Empresa\",\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"EstoqueMinimo\",\"QuantidadeEntrada\",\"QuantidadeSaida\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"QuantidadeDisponivel\",\"QuantidadeComprometido\",\"QuantidadeProducao\",\"QuantidadeConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 147,
                    "text": "Quantidade disponível separado por linha"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"MarcaMateriaPrima\"},{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"EstoqueMinimo\"},{\"uniqueName\":\"QuantidadeEntrada\"},{\"uniqueName\":\"QuantidadeSaida\"},{\"uniqueName\":\"ValorUltimaCompra\"},{\"uniqueName\":\"CustoUnitario\"},{\"uniqueName\":\"QuantidadeReal\"},{\"uniqueName\":\"QuantidadeDisponivel\"},{\"uniqueName\":\"QuantidadeComprometido\"},{\"uniqueName\":\"QuantidadeProducao\"},{\"uniqueName\":\"QuantidadeConsignado\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Empresa\",\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"EstoqueMinimo\",\"QuantidadeEntrada\",\"QuantidadeSaida\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"QuantidadeDisponivel\",\"QuantidadeComprometido\",\"QuantidadeProducao\",\"QuantidadeConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 149,
                    "text": "Quantidade disponível separado por marca de matéria-prima"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"MarcaProdutoAcabado\"},{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"},{\"uniqueName\":\"EstoqueMinimo\"},{\"uniqueName\":\"QuantidadeEntrada\"},{\"uniqueName\":\"QuantidadeSaida\"},{\"uniqueName\":\"ValorUltimaCompra\"},{\"uniqueName\":\"CustoUnitario\"},{\"uniqueName\":\"QuantidadeReal\"},{\"uniqueName\":\"QuantidadeDisponivel\"},{\"uniqueName\":\"QuantidadeComprometido\"},{\"uniqueName\":\"QuantidadeProducao\"},{\"uniqueName\":\"QuantidadeConsignado\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Empresa\",\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"EstoqueMinimo\",\"QuantidadeEntrada\",\"QuantidadeSaida\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"QuantidadeDisponivel\",\"QuantidadeComprometido\",\"QuantidadeProducao\",\"QuantidadeConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 142,
                    "text": "Quantidade disponível separado por marca de produto acabado"
                },
                {
                    "ReportObject": "{\"conditions\":[{\"formula\":\"AND(#value > 0, #value < 999999999999999999)\",\"measure\":\"ValorTotalCustoDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#DCEDC8\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}},{\"formula\":\"AND(#value > 0, #value < 99999999999999999999999999999999999999999999999999)\",\"measure\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":{\"backgroundColor\":\"#C5E1A5\",\"color\":\"#000000\",\"fontFamily\":\"Arial\",\"fontSize\":\"12px\"}}],\"options\":{\"grid\":{\"type\":\"classic\",\"showTotals\":\"off\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"ValorTotalCustoDisponivel\",\"aggregation\":\"sum\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"ValorTotalCustoReal\",\"aggregation\":\"sum\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"ValorTotalCustoComprometido\",\"aggregation\":\"sum\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"ValorTotalCustoProducao\",\"aggregation\":\"sum\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"ValorTotalCustoConsignado\",\"aggregation\":\"sum\"}],\"flatOrder\":[\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"ValorUltimaCompra\",\"CustoUnitario\",\"QuantidadeReal\",\"ValorTotalCustoReal\",\"QuantidadeDisponivel\",\"ValorTotalCustoDisponivel\",\"QuantidadeComprometido\",\"ValorTotalCustoComprometido\",\"QuantidadeProducao\",\"ValorTotalCustoProducao\",\"QuantidadeConsignado\",\"ValorTotalCustoConsignado\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 139,
                    "text": "Quantidade e custo dos produtos separados por armazenador"
                },
                {
                    "ReportObject": "{\"options\":{\"grid\":{\"type\":\"flat\",\"showTotals\":\"off\",\"showGrandTotals\":\"rows\"}},\"slice\":{\"rows\":[{\"uniqueName\":\"Armazenador\"},{\"uniqueName\":\"DescricaoFabrica\"},{\"uniqueName\":\"Cor\"},{\"uniqueName\":\"Tamanho\"}],\"columns\":[{\"uniqueName\":\"[Measures]\"}],\"measures\":[{\"uniqueName\":\"CustoUnitario\",\"aggregation\":\"sum\"},{\"uniqueName\":\"ValorUltimaCompra\",\"aggregation\":\"sum\"},{\"uniqueName\":\"QuantidadeDisponivel\",\"aggregation\":\"sum\",\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"EstoqueMinimo\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-2jpe837v4ict0\"},{\"uniqueName\":\"QuantidadeReal\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeComprometido\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeProducao\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"},{\"uniqueName\":\"QuantidadeConsignado\",\"aggregation\":\"sum\",\"active\":false,\"format\":\"-ai1kod4yvpg00\"}],\"flatOrder\":[\"Armazenador\",\"DescricaoFabrica\",\"Cor\",\"Tamanho\",\"CustoUnitario\",\"ValorUltimaCompra\",\"QuantidadeDisponivel\"]},\"formats\":[{\"name\":\"\",\"thousandsSeparator\":\".\",\"decimalSeparator\":\",\",\"decimalPlaces\":2,\"currencySymbol\":\"R$ \"},{\"name\":\"-ai1kod4yvpg00\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"},{\"name\":\"-2jpe837v4ict0\",\"decimalPlaces\":-1,\"currencySymbol\":\"\",\"textAlign\":\"center\"}]}",
                    "ModeloParticular": False,
                    "ModeloPadrao": True,
                    "id": 141,
                    "text": "Valor da última compra dos produtos"
                }
            ]
        }
    ]
}
headers = {
    "Content-Type": "application/json",
    "authority": "dapic.webpic.com.br",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": '_ga=GA1.1.1604941528.1703710908; __dauth=urbanzone-87daae190a4244bab5c6c7cad29c563c; EmpresaAtual={"Id":1,"Fantasia":"Urban+Zone+Jeans"}; _ga_1Q06KTBSXZ=GS1.1.1703785218.5.1.1703788404.60.0.0',
    "origin": "https://dapic.webpic.com.br",
    "referer": "https://dapic.webpic.com.br/pivot/gestaoestoquepivot",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}


response = requests.request("POST", url, json=payload, headers=headers)


if response.status_code == 200:

    resposta_json = response.json()

    codigo_barras_interno = resposta_json.get('CachedValues', {}).get('CodigoBarrasInterno', {})

    df_2 = pd.DataFrame(list(codigo_barras_interno.items()), columns=['Chave', 'Codigo de barras'])

    primeira_linha = df_2.iloc[0]

    datasources = resposta_json.get('DatasSources', [])

    if datasources:
        lista_num = []
        for sublist in datasources[0]:
            numeros = [float(valor) for valor in sublist if isinstance(valor, (int, float))]
            lista_num.append(numeros)
    else:
        print("DataSources is empty.")

colunas = ['Quantidade total disponível', 'Quantidade total produção']
df = pd.DataFrame([[float(sublist[7]), float(sublist[11])] for sublist in lista_num], columns=colunas)


print(df_2)
print(df)

df_final = pd.merge(df_2, df, left_index=True, right_index=True)

print(df_final)








