# Mapa do banco Oracle – ERP Concretiza

Gerado em 05/10/2026 09:36 · usuário iacompras · modo thin

**Dicionário usado: DBA_\*** — vê todos os schemas do banco.

Só metadados (estrutura). Nenhuma linha de dados do ERP foi lida.


## 1. Versão do Oracle

- Oracle Database 12c Enterprise Edition Release 12.2.0.1.0 - 64bit Production
- PL/SQL Release 12.2.0.1.0 - Production
- CORE	12.2.0.1.0	Production
- TNS for Linux: Version 12.2.0.1.0 - Production
- NLSRTL Version 12.2.0.1.0 - Production


## 2. Schemas do ERP

| Schema (owner) | Qtd. de tabelas |
|---|---|
| JP | 806 |
| VAREJO | 763 |
| BOLOS | 683 |
| VAREJOANTIGO | 676 |
| SEVERIANO | 663 |


## 3. As 50 maiores tabelas

NUM_ROWS é a quantidade de linhas estimada na última coleta de estatísticas (não é contagem em tempo real). Tabelas sem estatística não aparecem.

| # | Owner | Tabela | Linhas (aprox.) | Última estatística | Tema provável |
|---|---|---|---|---|---|
| 1 | JP | MOVIMENTACAO | 4.259.886 | 13/09/2026 13:02 |  |
| 2 | VAREJOANTIGO | LOG_ALTER_ESTOQUE | 2.796.412 | 29/08/2022 23:03 |  |
| 3 | VAREJO | MOVIMENTACAO | 2.659.085 | 15/08/2025 22:03 |  |
| 4 | VAREJOANTIGO | MOVIMENTACAO | 2.062.648 | 29/08/2022 23:03 |  |
| 5 | JP | NFBASE | 1.848.824 | 28/07/2026 22:02 |  |
| 6 | SEVERIANO | MOVIMENTACAO | 1.188.600 | 24/11/2022 22:03 |  |
| 7 | VAREJO | NFBASE | 1.150.623 | 22/11/2023 22:03 |  |
| 8 | JP | LOG_ALTER_CRECEBER | 1.045.157 | 18/09/2026 22:03 |  |
| 9 | VAREJO | ENDERECOS | 1.034.809 | 24/08/2022 16:49 |  |
| 10 | JP | ENDERECOS | 1.034.809 | 24/05/2023 00:05 |  |
| 11 | JP | CRECEBER | 1.017.872 | 14/09/2026 22:04 |  |
| 12 | JP | NFSAID | 1.016.570 | 01/10/2026 22:04 |  |
| 13 | VAREJO | ITEMPED | 1.000.627 | 15/08/2025 22:03 | Vendas, Produtos |
| 14 | VAREJO | NUMNOTA | 1.000.000 | 24/08/2022 22:27 |  |
| 15 | JP | NUMNOTA | 1.000.000 | 02/09/2022 22:00 |  |
| 16 | BOLOS | NUMNOTA | 1.000.000 | 24/08/2022 22:27 |  |
| 17 | JP | ITEMPED | 998.053 | 30/09/2026 22:02 | Vendas, Produtos |
| 18 | VAREJOANTIGO | NFBASE | 770.122 | 29/08/2022 23:02 |  |
| 19 | VAREJO | CRECEBER | 655.338 | 15/08/2025 22:03 |  |
| 20 | VAREJOANTIGO | ITEMPED | 616.917 | 29/08/2022 23:02 | Vendas, Produtos |
| 21 | VAREJO | NFSAID | 577.483 | 15/08/2025 22:03 |  |
| 22 | JP | HISTESTOQUE | 570.732 | 05/03/2026 22:04 |  |
| 23 | SEVERIANO | LOGFATURAMENTO | 560.169 | 10/08/2022 22:02 |  |
| 24 | VAREJOANTIGO | CRECEBER | 498.479 | 29/08/2022 23:03 |  |
| 25 | VAREJOANTIGO | LOG_ALTER_PARAMETRO | 498.354 | 29/08/2022 23:03 |  |
| 26 | VAREJOANTIGO | NFSAID | 484.872 | 21/10/2022 22:03 |  |
| 27 | SEVERIANO | LOGFLEXIVEL | 455.172 | 31/03/2022 22:01 |  |
| 28 | SEVERIANO | NFBASE | 451.303 | 30/07/2022 08:17 |  |
| 29 | JP | LOGALTCUSTO | 446.318 | 02/10/2026 22:03 |  |
| 30 | VAREJOANTIGO | LOG_ALTER_CRECEBER | 393.955 | 29/08/2022 23:02 |  |
| 31 | VAREJOANTIGO | HISTESTOQUE | 305.096 | 29/08/2022 23:02 |  |
| 32 | SEVERIANO | CRECEBER | 270.619 | 24/11/2022 22:03 |  |
| 33 | JP | CABPED | 265.104 | 04/10/2026 09:35 |  |
| 34 | SEVERIANO | NFSAID | 263.472 | 24/11/2022 22:02 |  |
| 35 | SEVERIANO | CADNCMPISCOFINS16MAR17 | 263.385 | 31/03/2022 22:01 |  |
| 36 | VAREJO | CABPED | 259.266 | 15/08/2025 22:03 |  |
| 37 | VAREJO | CARREGAMENTO | 259.026 | 11/12/2023 22:02 |  |
| 38 | JP | CARREGAMENTO | 257.828 | 01/10/2026 22:05 |  |
| 39 | JP | LOGFATURAMENTO | 252.304 | 16/09/2026 22:02 |  |
| 40 | VAREJO | LOGFATURAMENTO | 244.541 | 25/11/2023 12:28 |  |
| 41 | JP | CADNCMPISCOFINS | 223.983 | 02/09/2026 22:03 |  |
| 42 | VAREJO | CLI12MESES | 218.482 | 28/03/2024 22:00 |  |
| 43 | JP | CLI12MESES | 214.832 | 24/12/2025 22:03 |  |
| 44 | VAREJOANTIGO | LOGFATURAMENTO | 186.847 | 29/08/2022 23:02 |  |
| 45 | VAREJOANTIGO | CABPED | 186.841 | 29/08/2022 23:02 |  |
| 46 | VAREJOANTIGO | CARREGAMENTO | 186.839 | 29/08/2022 23:02 |  |
| 47 | SEVERIANO | ITEMPED | 174.236 | 22/11/2022 22:05 | Vendas, Produtos |
| 48 | VAREJO | CADNCMPISCOFINS | 170.334 | 08/11/2023 22:02 |  |
| 49 | JP | DADOSTEMPENT | 169.804 | 12/09/2026 12:05 |  |
| 50 | VAREJOANTIGO | CLI12MESES | 165.121 | 21/10/2022 22:03 |  |


## 4. Colunas das 50 maiores tabelas

### JP.MOVIMENTACAO (4.259.886 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| ID | NUMBER(10) | não |  |
| NUMVENDA | NUMBER(10) | sim |  |
| NUMENT | NUMBER(10) | sim |  |
| NUMOP | NUMBER(10) | sim |  |
| NUMREQ | NUMBER(10) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| DTMOV | DATE | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| CODPROD | NUMBER(10) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| SEQ | NUMBER(4) | sim |  |
| OPERACAO | VARCHAR2(2) | sim |  |
| QT | NUMBER(18,6) | sim |  |
| QTCONT | NUMBER(18,6) | sim |  |
| CUSTOCONT | NUMBER(18,6) | sim |  |
| CUSTOREAL | NUMBER(18,6) | sim |  |
| CUSTOFIN | NUMBER(18,6) | sim |  |
| CUSTOCONTANT | NUMBER(18,6) | sim |  |
| CUSTOREALANT | NUMBER(18,6) | sim |  |
| CUSTOFINANT | NUMBER(18,6) | sim |  |
| CUSTOULTENTANT | NUMBER(18,6) | sim |  |
| PTABELA | NUMBER(24,8) | sim |  |
| PUNIT | NUMBER(24,8) | sim |  |
| PUNITCONT | NUMBER(24,8) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| PERICM | NUMBER(5,2) | sim |  |
| PERST | NUMBER(18,6) | sim |  |
| PERIPI | NUMBER(5,2) | sim |  |
| PERFRETE | NUMBER(5,2) | sim |  |
| PEROUT | NUMBER(5,2) | sim |  |
| ST | NUMBER(24,8) | sim |  |
| CODFISCALITEM | NUMBER(4) | sim |  |
| NUMLOTE | VARCHAR2(20) | sim |  |
| DTFAB | DATE | sim |  |
| DTVENC | DATE | sim |  |
| STATUS | VARCHAR2(2) | sim |  |
| NUMVENDADEV | NUMBER(10) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| VLBASEST | NUMBER(24,8) | sim |  |
| VLBASEICM | NUMBER(24,8) | sim |  |
| VLICM | NUMBER(24,8) | sim |  |
| VLBASEIPI | NUMBER(24,8) | sim |  |
| VLIPI | NUMBER(24,8) | sim |  |
| SITTRIBUT | VARCHAR2(2) | sim |  |
| NOVOPVENDA | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(24,8) | sim |  |
| VLISENTO | NUMBER(24,8) | sim |  |
| CODTRIBUT | NUMBER(4) | sim |  |
| PERBASERED | NUMBER(5,2) | sim |  |
| VLDESC | NUMBER(24,8) | sim |  |
| PERDESCIMP | NUMBER(8,4) | sim |  |
| CODBARRA | NUMBER(14) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| NUMNOTA | NUMBER(10) | sim |  |
| CODPARC | NUMBER(6) | sim |  |
| PERICMANTECIP | NUMBER(5,2) | sim |  |
| PERDESPFIN | NUMBER(18,6) | sim |  |
| PERBON | NUMBER(5,2) | sim |  |
| PERFRETECONH | NUMBER(5,2) | sim |  |
| NUMBONUS | NUMBER(10) | sim |  |
| QTPCA | NUMBER(12,3) | sim |  |
| AVARIA | VARCHAR2(1) | sim |  |
| CUSTOULTENT | NUMBER(18,6) | sim |  |
| DESCALT | VARCHAR2(120) | sim |  |
| VLPISCOFINS | NUMBER(12,2) | sim |  |
| TIPO | NUMBER(2) | sim |  |
| VLBASEPIS | NUMBER(24,8) | sim |  |
| PERPIS | NUMBER(18,6) | sim |  |
| VLPIS | NUMBER(24,8) | sim |  |
| VLBASECOFINS | NUMBER(24,8) | sim |  |
| PERCOFINS | NUMBER(18,6) | sim |  |
| VLCOFINS | NUMBER(24,8) | sim |  |
| PUNITORIG | NUMBER(24,8) | sim |  |
| NUMENTDEV | NUMBER(10) | sim |  |
| ALIQCREDSIMPLES | NUMBER(5,2) | sim |  |
| QTORIG | NUMBER(18,6) | sim |  |
| UNORIG | VARCHAR2(3) | sim |  |
| OBSADIC | VARCHAR2(400) | sim |  |
| EMBALAGEMORIG | VARCHAR2(12) | sim |  |
| CUSTOREALBLOQ | NUMBER(12,3) | sim |  |
| PERICMDEBITO | NUMBER(5,2) | sim |  |
| PERICMCREDITO | NUMBER(5,2) | sim |  |
| PERIVA | NUMBER(5,2) | sim |  |
| PRODLIBERADO | VARCHAR2(1) | sim |  |
| CSOSN | NUMBER(5) | sim |  |
| VLFRETE | NUMBER(24,8) | sim |  |
| PEROUTRASDESP | NUMBER(5,2) | sim |  |
| PERSEGURO | NUMBER(5,2) | sim |  |
| VLOUTRASDESP | NUMBER(24,8) | sim |  |
| VLSEGURO | NUMBER(24,8) | sim |  |
| SUBTOT | NUMBER(18,6) | sim |  |
| CSTPIS | VARCHAR2(3) | sim |  |
| CSTCOFINS | VARCHAR2(3) | sim |  |
| VLBCIMP | NUMBER(15,2) | sim |  |
| VLDESPADUANEIRA | NUMBER(15,2) | sim |  |
| VLIMPOSTOIMP | NUMBER(15,2) | sim |  |
| VLIOF | NUMBER(15,2) | sim |  |
| VLINSS | NUMBER(18,6) | sim |  |
| VLIR | NUMBER(18,6) | sim |  |
| VLCSLL | NUMBER(18,6) | sim |  |
| NUMNOTATRANSF | NUMBER(10) | sim |  |
| USAFATORMASTER | VARCHAR2(1) | sim |  |
| VLCONHECFRETE | NUMBER(24,8) | sim |  |
| VLICMSDES | NUMBER(24,8) | sim |  |
| VLDESPICMANTECIPADO | NUMBER(24,8) | sim |  |
| PFCPUFDEST | NUMBER(5,2) | sim |  |
| PICMSUFDEST | NUMBER(5,2) | sim |  |
| PICMSINTER | NUMBER(5,2) | sim |  |
| PICMSINTERPART | NUMBER(5,2) | sim |  |
| VFCPUFDEST | NUMBER(18,6) | sim |  |
| VICMSUFDEST | NUMBER(18,6) | sim |  |
| VICMSUFREMET | NUMBER(18,6) | sim |  |
| VLFRETECONHECIMENTO | NUMBER(24,8) | sim |  |
| VBCUFDEST | NUMBER(18,6) | sim |  |
| IDAVARIA | NUMBER(10) | sim |  |
| VLDESPFINAN | NUMBER(24,8) | sim |  |
| DTDESBLOQ | DATE | sim |  |
| CODFUNCLIB | NUMBER(5) | sim |  |
| STATUS_MOFVENC | VARCHAR2(1) | sim |  |
| QTMOF | NUMBER(18,6) | sim |  |
| QTVENC | NUMBER(18,6) | sim |  |
| STATUSPCP | VARCHAR2(1) | sim |  |
| CODPRODPAI | NUMBER(10) | sim |  |
| VLFCP | NUMBER(18,6) | sim |  |
| PERFCP | NUMBER(5,2) | sim |  |
| VLBASEFCP | NUMBER(24,8) | sim |  |
| ICMSSTRET | NUMBER(18,6) | sim |  |
| VLBASESTRET | NUMBER(18,6) | sim |  |
| NITEMPED | VARCHAR2(6) | sim |  |
| XPED | VARCHAR2(15) | sim |  |
| VLBASEFCPSTRET | NUMBER(18,6) | sim |  |
| PSTRET | NUMBER(5,2) | sim |  |
| VLFCPSTRET | NUMBER(18,6) | sim |  |
| PERFCPSTRET | NUMBER(18,6) | sim |  |
| CODHISTITEM | NUMBER(6) | sim |  |
| PERFCPST | NUMBER(5,2) | sim |  |
| VLFCPST | NUMBER(24,8) | sim |  |
| VLBASEFCPST | NUMBER(24,8) | sim |  |
| QTULTENT | NUMBER(12,3) | sim |  |
| QTULTENTANT | NUMBER(12,3) | sim |  |
| QTCANCEL | NUMBER(18,6) | sim |  |
| VLSTRET | NUMBER(24,8) | sim |  |
| CODNATPIS | VARCHAR2(4) | sim |  |
| CODNATCOFINS | VARCHAR2(4) | sim |  |
| CODNATRECFT | VARCHAR2(4) | sim |  |
| SEQREF | NUMBER(4) | sim |  |
| VICMSSUBSTITUTO | NUMBER(24,8) | sim |  |
| PRODUTOFERTA | VARCHAR2(1) | sim |  |
| GERARSALDOFLEXVENDA | VARCHAR2(1) | sim |  |
| NDRAW | VARCHAR2(11) | sim |  |
| NRE | VARCHAR2(12) | sim |  |
| CHNFE | VARCHAR2(44) | sim |  |
| QEXPORT | NUMBER(18,6) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| MOTDESICMS | VARCHAR2(2) | sim |  |
| USAFASSON | VARCHAR2(1) | sim |  |
| CODCREDESTORNOPISPF | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPF | NUMBER(3) | sim |  |
| CODCREDESTORNOPISPJ | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPJ | NUMBER(3) | sim |  |
| USADESCQTDE_DESCMISTO2 | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO3 | VARCHAR2(1) | sim |  |
| BASE_VERBAFLEX_PERDESCINI | NUMBER(5,2) | sim |  |
| BASE_VERBAFLEX_PERDESCFINAL | NUMBER(5,2) | sim |  |
| VLVERBAFLEX_CREDITO | NUMBER(12,2) | sim |  |
| VLVERBAFLEX_DEBITO | NUMBER(12,2) | sim |  |
| USAVERBAFLEX_CREDITO | VARCHAR2(1) | sim |  |
| USAVERBAFLEX_DEBITO | VARCHAR2(1) | sim |  |
| PERDIFERIMENTO | NUMBER(18,6) | sim |  |
| VLICMDIF | NUMBER(24,8) | sim |  |
| VLCIAP | NUMBER(24,8) | sim |  |
| NUMENTENTRADACIAP | NUMBER(10) | sim |  |
| QTMOFADOSTP17 | NUMBER(8) | sim |  |
| QTVENCIDOSTP17 | NUMBER(8) | sim |  |
| MOTIVOMOFVENCTP17 | VARCHAR2(1000) | sim |  |
| AGRUPCUSTO | VARCHAR2(1) | sim |  |
| AVARIADEVOL | VARCHAR2(1) | sim |  |
| ACRESCCUSTODESAG | NUMBER(18,6) | sim |  |
| CODPRODDESAGPAI | NUMBER(10) | sim |  |
| PERCUSTODESAG | NUMBER(18,6) | sim |  |
| CODFUNCALTPESO | NUMBER(10) | sim |  |
| PRODDESCQT | VARCHAR2(1) | sim |  |
| TIPOPROMOCAO | VARCHAR2(30) | sim |  |
| IDSCANNTECH | NUMBER(10) | sim |  |
| VLDESCSCANNTECH | NUMBER(24,8) | sim |  |
| VLCUSTORB | NUMBER(12,2) | sim |  |
| VL_OUT_TAXAS | NUMBER(24,8) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| SEQ_DEV | NUMBER(4) | sim |  |
| FILIALDEVORIG | VARCHAR2(2) | sim | NA DEVOLUCAO DEVERA SALVAR O CODFILIAL DO PEDIDO ORIGINAL, IMPORTANTE QUANDO ITEM E DE FILIAL RETIRA |
| ITEMPED_SEQ | NUMBER(4) | sim | CAMPO PARA RELACIONAR AS TABELAS ITEMPED.SEQ COM A MOVIMENTACAO |
| DEVOL_BLOQ | VARCHAR2(1) | sim | REALIZAR DEVOLUCAO ONDE MERCADORIA JA FOI ENTREGUE BLOQUEIA O ESTOQUE SALVA S |
| UTQTMAXOFERTA | VARCHAR2(1) | sim | CAMPO PARA MARCAR SE ABATEU QTDE MAXIMA NA VENDA DE PRODUTO COM PRECO DE OFERTA |
| QTANTECIP | NUMBER(18,6) | sim |  |
| SF_124 | VARCHAR2(1) | sim | AJUSTE DE ESTOQUE ROTINA 124 REALIZADO COMO SIMPLES FATURA |
| PERADREM_ICMSRET | NUMBER(5,4) | sim | Alíquota AD REM do ICMS para o produto CST=61 |
| VICMSMONORET | NUMBER(18,6) | sim | Valor AD REM do ICMS para o produto CST=61 |
| CODTIPOOFERTA | NUMBER(10) | sim |  |
| IDCRVENDAS | NUMBER(10) | sim | INTEGRACAO CRESCE VENDAS - RECEBE A IDENTIFICACAO UNICA DA VENDA PELO CRESCE VENDAS |
| VLDESCCRVENDAS | NUMBER(24,8) | sim | INTEGRACAO CRESCE VENDAS - RECEBE O DESCONTO CRESCE VENDAS |
| IDQTDMAXCRVENDAS | NUMBER(18,6) | sim | INTEGRACAO CRESCE VENDAS - ID PARA IDENTIFICAR A QTD MAXIMA DE ITENS PARA DESCONTO |
| SF_CONTABIL | VARCHAR2(1) | sim | GRAVAR S PARA ENTRADAS SIMPLES FATURA R736/701 |
| QTPECAS | NUMBER(18,6) | sim | Informar a quantidade de peças referente a quantidade de KG que esta lançando |
| CST_IBSCBS | VARCHAR2(3) | sim | Código de Situação Tributária do IBS e CBS |
| CCLASSTRIB_IBSCBS | VARCHAR2(6) | sim | Código de Classificação Tributária do IBS e CBS |
| VLBC_IBSCBS | NUMBER(24,8) | sim | Base de cálculo do IBS, CBS e IS (Valor Produto) |
| PERIBSUF_IBS | NUMBER(18,6) | sim | Alíquota do IBS de competência das UF |
| PERIBSMUN_IBS | NUMBER(18,6) | sim | Alíquota do IBS de competência do Municipio |
| VTRIBOP_IBS_UF | NUMBER(24,8) | sim | Valor do tributo considerando (VLBC_IBSCBS x Alq do IBS), sem considerar qualquer desoneração (MOV.VBC_IBSCBS * MOV.PIBSUF_IBS) |
| VTRIBOP_IBS_MUN | NUMBER(24,8) | sim | Valor do tributo considerando (VLBC_IBSCBS x Alq do IBS), sem considerar qualquer desoneração (MOV.VBC_IBSCBS * MOV.PERIBS_MUN) |
| PERCBS_CBS | NUMBER(18,6) | sim | Alíquota vigente da CBS |
| VTRIBOP_CBS | NUMBER(24,8) | sim | Valor do tributo considerando VLBC_IBSCBS x Aliq. da CBS, sem considerar qualquer desoneração (MOV.VBC_IBSCBS * MOV.PERCBS_CBS) |
| PRED_IBS_UF | NUMBER(18,6) | sim | Alíquota redução IBS da UF |
| PRED_IBS_MUN | NUMBER(18,6) | sim | Alíquota redução IBS do Municipio |
| PRED_CBS | NUMBER(18,6) | sim | Alíquota redução CBS |
| ALIQEFET_IBS_UF | NUMBER(18,6) | sim | Alíquota Efetiva IBS da UF |
| ALIQEFET_IBS_MUN | NUMBER(18,6) | sim | Alíquota Efetiva IBS do Municipio |
| ALIQEFET_CBS | NUMBER(18,6) | sim | Alíquota Efetiva CBS |
| PERDIF_IBS_UF | NUMBER(18,6) | sim | Percentual do diferimento IBS |
| PERDIF_CBS | NUMBER(18,6) | sim | Percentual do diferimento CBS |
| PERDIF_IBS_MUN | NUMBER(18,6) | sim | Percentual do diferimento IBS/MUNICIPAL |
| VTRIBOP_DIF_IBS_UF | NUMBER(24,8) | sim | Valor unitário do diferimento IBS |
| VTRIBOP_DIF_CBS | NUMBER(24,8) | sim | Valor unitário do diferimento CBS |
| VTRIBOP_DIF_IBS_MUN | NUMBER(24,8) | sim | Valor unitário do diferimento IBS/MUNICIPAL |
| CSTREG | VARCHAR2(3) | sim | CÓDIGO DE SITUAÇÃO TRIBUTÁRIA DO IBS E CBS - TRIB.REGULAR |
| CCLASSTRIBREG | VARCHAR2(6) | sim | CÓDIGO DE CLASSIFICAÇÃO TRIBUTÁRIA DO IBS E CBS - TRIB.REGULAR |
| ALIQEFET_REGIBS_UF | NUMBER(18,6) | sim | VALOR DA ALÍQUOTA DO IBS DA UF (EM PERCENTUAL) - TRIB.REGULAR |
| VTRIB_REGIBS_UF | NUMBER(24,8) | sim | VALOR DO TRIBUTO DO IBS DA UF - TRIB.REGULAR |
| ALIQEFET_REGIBS_MUN | NUMBER(18,6) | sim | VALOR DA ALÍQUOTA DO IBS DO MUNICÍPIO (EM PERCENTUAL) - TRIB.REGULAR |
| VTRIB_REGIBS_MUN | NUMBER(24,8) | sim | VALOR DO TRIBUTO DO IBS DO MUNICÍPIO - TRIB.REGULAR |
| ALIQEFET_REGCBS | NUMBER(18,6) | sim | VALOR DA ALÍQUOTA DA CBS (EM PERCENTUAL) - TRIB.REGULAR |
| VTRIB_REGCBS | NUMBER(24,8) | sim | VALOR DO TRIBUTO DA CBS - TRIB.REGULAR |
| ALIQ_ADREM_IBS | NUMBER(18,6) | sim | Alíquota ad rem do IBS - Tributação Monofásica Padrão |
| ALIQ_ADREM_CBS | NUMBER(18,6) | sim | Alíquota ad rem do CBS - Tributação Monofásica Padrão |
| ALIQ_ADREM_IBS_RETEN | NUMBER(18,6) | sim | Alíquota ad rem do IBS - Tributação Monofásica Sujeita à Retenção |
| ALIQ_ADREM_CBS_RETEN | NUMBER(18,6) | sim | Alíquota ad rem do CBS - Tributação Monofásica Sujeita à Retenção |
| ALIQ_ADREM_IBS_RET | NUMBER(18,6) | sim | Alíquota ad rem do IBS retido anteriormente - Tributação Monofásica Retida Anteriormente |
| ALIQ_ADREM_CBS_RET | NUMBER(18,6) | sim | Alíquota ad rem do CBS retido anteriormente - Tributação Monofásica Retida Anteriormente |
| ALIQ_PDIF_IBS_MONO | NUMBER(18,6) | sim | Percentual do diferimento do imposto monofásico IBS - Diferimento da Tributação Monofásica |
| ALIQ_PDIF_CBS_MONO | NUMBER(18,6) | sim | Percentual do diferimento do imposto monofásico CBS - Diferimento da Tributação Monofásica |
| VTRIB_ESTCRED_IBS | NUMBER(24,8) | sim | Estorno de Crédito do IBS do grupo <gEstornoCred> |
| VTRIB_ESTCRED_CBS | NUMBER(24,8) | sim | Estorno de Crédito do CBS do grupo <gEstornoCred> |

### VAREJOANTIGO.LOG_ALTER_ESTOQUE (2.796.412 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| ID | NUMBER | não |  |
| DATADOLOG | DATE | sim |  |
| CODPROD | NUMBER(10) | não |  |
| CODFILIAL | VARCHAR2(2) | não |  |
| DTULTENT | DATE | sim |  |
| DTULTSAIDA | DATE | sim |  |
| DTULTALTPVENDA | DATE | sim |  |
| QTULTENT | NUMBER(12,3) | sim |  |
| QTPEDIDA | NUMBER(12,3) | sim |  |
| QTESTGER | NUMBER(18,6) | sim |  |
| CUSTOULTENT | NUMBER(18,6) | sim |  |
| CUSTOCONT | NUMBER(18,6) | sim |  |
| CUSTOREAL | NUMBER(18,6) | sim |  |
| CUSTOFIN | NUMBER(18,6) | sim |  |
| PTABELA | NUMBER(16,4) | sim |  |
| PVENDA | NUMBER(16,4) | sim |  |
| POFERTA | NUMBER(16,4) | sim |  |
| POFERTATAB | NUMBER(16,4) | sim |  |
| MARGEMATUAL | NUMBER(6,2) | sim |  |
| QTVENDMES | NUMBER(12,3) | sim |  |
| QTVENDMES1 | NUMBER(12,3) | sim |  |
| QTVENDMES2 | NUMBER(12,3) | sim |  |
| QTVENDMES3 | NUMBER(12,3) | sim |  |
| QTVENDDIA | NUMBER(12,3) | sim |  |
| VLVENDDIA | NUMBER(12,3) | sim |  |
| VLCUSTODIA | NUMBER(12,3) | sim |  |
| VLVENDMES | NUMBER(12,3) | sim |  |
| VLCUSTOMES | NUMBER(12,3) | sim |  |
| QTEST | NUMBER(18,6) | sim |  |
| VALORULTENT | NUMBER(12,3) | sim |  |
| QTRESERV | NUMBER(18,6) | sim |  |
| QTESTMIN | NUMBER(12,3) | sim |  |
| MODULO | NUMBER(2) | sim |  |
| RUA | VARCHAR2(6) | sim |  |
| NUMERO | NUMBER(6,2) | sim |  |
| APTO | NUMBER(4) | sim |  |
| QTESTGERANT | NUMBER(18,6) | sim |  |
| QTESTANT | NUMBER(18,6) | sim |  |
| DTULTINVENT | DATE | sim |  |
| QTULTINVENT | NUMBER(12,3) | sim |  |
| CUSTOREP | NUMBER(18,6) | sim |  |
| QTBLOQUEADA | NUMBER(18,6) | sim |  |
| VLVENDMES1 | NUMBER(12,3) | sim |  |
| VLCUSTOMES1 | NUMBER(12,3) | sim |  |
| VLVENDMES2 | NUMBER(12,3) | sim |  |
| VLCUSTOMES2 | NUMBER(12,3) | sim |  |
| VLVENDMES3 | NUMBER(12,3) | sim |  |
| VLCUSTOMES3 | NUMBER(12,3) | sim |  |
| PTABELAULTENT | NUMBER(12,3) | sim |  |
| QTPENDENTE | NUMBER(18,6) | sim |  |
| CODFORNECULTENT | NUMBER(6) | sim |  |
| QTINDENIZ | NUMBER(18,6) | sim |  |
| QTRESERVPCA | NUMBER(12,3) | sim |  |
| QTESTGERPCA | NUMBER(12,3) | sim |  |
| QTANTECIP | NUMBER(18,6) | sim |  |
| DEPOSITO | NUMBER(2) | sim |  |
| LADO | VARCHAR2(2) | sim |  |
| PALETE | VARCHAR2(6) | sim |  |
| DTULTTRANSF | DATE | sim |  |
| QTDEVOLDIA | NUMBER(12,3) | sim |  |
| VLDEVOLDIA | NUMBER(12,3) | sim |  |
| QTDEVOLMES | NUMBER(12,3) | sim |  |
| QTDEVOLMES1 | NUMBER(12,3) | sim |  |
| QTDEVOLMES2 | NUMBER(12,3) | sim |  |
| QTDEVOLMES3 | NUMBER(12,3) | sim |  |
| VLDEVOLMES | NUMBER(12,3) | sim |  |
| VLDEVOLMES1 | NUMBER(12,3) | sim |  |
| VLDEVOLMES2 | NUMBER(12,3) | sim |  |
| VLDEVOLMES3 | NUMBER(12,3) | sim |  |
| QTESTGERCONSIG | NUMBER(12,3) | sim |  |
| NUMANTECIPEST | NUMBER(10) | sim |  |
| IDLIBANTECIP | NUMBER(10) | sim |  |
| QTALOCMAXIMA | NUMBER(12,3) | sim |  |
| CUSTOREALBLOQ | NUMBER(18,6) | sim |  |
| NUMENTULT | NUMBER(10) | sim |  |
| QTCONSIG | NUMBER(12,3) | sim |  |
| DTINDENIZ | DATE | sim |  |
| CUSTOMEDIO | NUMBER(18,6) | sim |  |
| QTENTFUTURA | NUMBER(12,3) | sim |  |
| PRODFILIALEXC | VARCHAR2(1) | sim |  |
| CODFORNECMENPRECO | NUMBER(10) | sim |  |
| QTMENORPRECO | NUMBER(12,6) | sim |  |
| VALORMENORPRECO | NUMBER(12,6) | sim |  |
| DTULTENTMENORPRECO | DATE | sim |  |
| QTESTTEMP | NUMBER(19,2) | sim |  |
| DTULTENTANT | DATE | sim |  |
| QTULTENTANT | NUMBER(12,3) | sim |  |
| PTABELAULTENTANT | NUMBER(12,3) | sim |  |
| CODFORNECULTENTANT | NUMBER(6) | sim |  |
| NUMENTULTANT | NUMBER(10) | sim |  |
| CUSTOULTPRODUCAO | NUMBER(18,6) | sim |  |
| QTDEULTPRODUCAO | NUMBER(18,6) | sim |  |
| DATAULTPRODUCAO | DATE | sim |  |
| VICMSSUBSTITUTOULTENT | NUMBER(24,8) | sim |  |
| VLSTRETULTENT | NUMBER(24,8) | sim |  |
| VLBASESTRETULTENT | NUMBER(24,8) | sim |  |
| PSTRETULTENT | NUMBER(24,8) | sim |  |
| USERNAME | VARCHAR2(200) | sim |  |
| MACHINE | VARCHAR2(200) | sim |  |
| PROGRAM | VARCHAR2(200) | sim |  |
| MODULE | VARCHAR2(200) | sim |  |
| TERMINAL | VARCHAR2(200) | sim |  |
| IP | VARCHAR2(200) | sim |  |

### VAREJO.MOVIMENTACAO (2.659.085 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| ID | NUMBER(10) | não |  |
| NUMVENDA | NUMBER(10) | sim |  |
| NUMENT | NUMBER(10) | sim |  |
| NUMOP | NUMBER(10) | sim |  |
| NUMREQ | NUMBER(10) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| DTMOV | DATE | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| CODPROD | NUMBER(10) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| SEQ | NUMBER(4) | sim |  |
| OPERACAO | VARCHAR2(2) | sim |  |
| QT | NUMBER(18,6) | sim |  |
| QTCONT | NUMBER(18,6) | sim |  |
| CUSTOCONT | NUMBER(18,6) | sim |  |
| CUSTOREAL | NUMBER(18,6) | sim |  |
| CUSTOFIN | NUMBER(18,6) | sim |  |
| CUSTOCONTANT | NUMBER(18,6) | sim |  |
| CUSTOREALANT | NUMBER(18,6) | sim |  |
| CUSTOFINANT | NUMBER(18,6) | sim |  |
| CUSTOULTENTANT | NUMBER(18,6) | sim |  |
| PTABELA | NUMBER(24,8) | sim |  |
| PUNIT | NUMBER(24,8) | sim |  |
| PUNITCONT | NUMBER(24,8) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| PERICM | NUMBER(5,2) | sim |  |
| PERST | NUMBER(18,6) | sim |  |
| PERIPI | NUMBER(5,2) | sim |  |
| PERFRETE | NUMBER(5,2) | sim |  |
| PEROUT | NUMBER(5,2) | sim |  |
| ST | NUMBER(24,8) | sim |  |
| CODFISCALITEM | NUMBER(4) | sim |  |
| NUMLOTE | VARCHAR2(20) | sim |  |
| DTFAB | DATE | sim |  |
| DTVENC | DATE | sim |  |
| STATUS | VARCHAR2(2) | sim |  |
| NUMVENDADEV | NUMBER(10) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| VLBASEST | NUMBER(24,8) | sim |  |
| VLBASEICM | NUMBER(24,8) | sim |  |
| VLICM | NUMBER(24,8) | sim |  |
| VLBASEIPI | NUMBER(24,8) | sim |  |
| VLIPI | NUMBER(24,8) | sim |  |
| SITTRIBUT | VARCHAR2(2) | sim |  |
| NOVOPVENDA | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(24,8) | sim |  |
| VLISENTO | NUMBER(24,8) | sim |  |
| CODTRIBUT | NUMBER(4) | sim |  |
| PERBASERED | NUMBER(5,2) | sim |  |
| VLDESC | NUMBER(24,8) | sim |  |
| PERDESCIMP | NUMBER(8,4) | sim |  |
| CODBARRA | NUMBER(14) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| NUMNOTA | NUMBER(10) | sim |  |
| CODPARC | NUMBER(6) | sim |  |
| PERICMANTECIP | NUMBER(5,2) | sim |  |
| PERDESPFIN | NUMBER(18,6) | sim |  |
| PERBON | NUMBER(5,2) | sim |  |
| PERFRETECONH | NUMBER(5,2) | sim |  |
| NUMBONUS | NUMBER(10) | sim |  |
| QTPCA | NUMBER(12,3) | sim |  |
| AVARIA | VARCHAR2(1) | sim |  |
| CUSTOULTENT | NUMBER(18,6) | sim |  |
| DESCALT | VARCHAR2(120) | sim |  |
| VLPISCOFINS | NUMBER(12,2) | sim |  |
| TIPO | NUMBER(2) | sim |  |
| VLBASEPIS | NUMBER(24,8) | sim |  |
| PERPIS | NUMBER(18,6) | sim |  |
| VLPIS | NUMBER(24,8) | sim |  |
| VLBASECOFINS | NUMBER(24,8) | sim |  |
| PERCOFINS | NUMBER(18,6) | sim |  |
| VLCOFINS | NUMBER(24,8) | sim |  |
| PUNITORIG | NUMBER(24,8) | sim |  |
| NUMENTDEV | NUMBER(10) | sim |  |
| ALIQCREDSIMPLES | NUMBER(5,2) | sim |  |
| QTORIG | NUMBER(18,6) | sim |  |
| UNORIG | VARCHAR2(3) | sim |  |
| OBSADIC | VARCHAR2(400) | sim |  |
| EMBALAGEMORIG | VARCHAR2(12) | sim |  |
| CUSTOREALBLOQ | NUMBER(12,3) | sim |  |
| PERICMDEBITO | NUMBER(5,2) | sim |  |
| PERICMCREDITO | NUMBER(5,2) | sim |  |
| PERIVA | NUMBER(5,2) | sim |  |
| PRODLIBERADO | VARCHAR2(1) | sim |  |
| CSOSN | NUMBER(5) | sim |  |
| VLFRETE | NUMBER(24,8) | sim |  |
| PEROUTRASDESP | NUMBER(5,2) | sim |  |
| PERSEGURO | NUMBER(5,2) | sim |  |
| VLOUTRASDESP | NUMBER(24,8) | sim |  |
| VLSEGURO | NUMBER(24,8) | sim |  |
| SUBTOT | NUMBER(18,6) | sim |  |
| CSTPIS | VARCHAR2(3) | sim |  |
| CSTCOFINS | VARCHAR2(3) | sim |  |
| VLBCIMP | NUMBER(15,2) | sim |  |
| VLDESPADUANEIRA | NUMBER(15,2) | sim |  |
| VLIMPOSTOIMP | NUMBER(15,2) | sim |  |
| VLIOF | NUMBER(15,2) | sim |  |
| VLINSS | NUMBER(18,6) | sim |  |
| VLIR | NUMBER(18,6) | sim |  |
| VLCSLL | NUMBER(18,6) | sim |  |
| NUMNOTATRANSF | NUMBER(10) | sim |  |
| USAFATORMASTER | VARCHAR2(1) | sim |  |
| VLCONHECFRETE | NUMBER(24,8) | sim |  |
| VLICMSDES | NUMBER(24,8) | sim |  |
| VLDESPICMANTECIPADO | NUMBER(24,8) | sim |  |
| PFCPUFDEST | NUMBER(5,2) | sim |  |
| PICMSUFDEST | NUMBER(5,2) | sim |  |
| PICMSINTER | NUMBER(5,2) | sim |  |
| PICMSINTERPART | NUMBER(5,2) | sim |  |
| VFCPUFDEST | NUMBER(18,6) | sim |  |
| VICMSUFDEST | NUMBER(18,6) | sim |  |
| VICMSUFREMET | NUMBER(18,6) | sim |  |
| VLFRETECONHECIMENTO | NUMBER(24,8) | sim |  |
| VBCUFDEST | NUMBER(18,6) | sim |  |
| IDAVARIA | NUMBER(10) | sim |  |
| VLDESPFINAN | NUMBER(24,8) | sim |  |
| DTDESBLOQ | DATE | sim |  |
| CODFUNCLIB | NUMBER(5) | sim |  |
| STATUS_MOFVENC | VARCHAR2(1) | sim |  |
| QTMOF | NUMBER(18,6) | sim |  |
| QTVENC | NUMBER(18,6) | sim |  |
| STATUSPCP | VARCHAR2(1) | sim |  |
| CODPRODPAI | NUMBER(10) | sim |  |
| VLFCP | NUMBER(18,6) | sim |  |
| PERFCP | NUMBER(5,2) | sim |  |
| VLBASEFCP | NUMBER(24,8) | sim |  |
| ICMSSTRET | NUMBER(18,6) | sim |  |
| VLBASESTRET | NUMBER(18,6) | sim |  |
| NITEMPED | VARCHAR2(6) | sim |  |
| XPED | VARCHAR2(15) | sim |  |
| VLBASEFCPSTRET | NUMBER(18,6) | sim |  |
| PSTRET | NUMBER(5,2) | sim |  |
| VLFCPSTRET | NUMBER(18,6) | sim |  |
| PERFCPSTRET | NUMBER(18,6) | sim |  |
| CODHISTITEM | NUMBER(6) | sim |  |
| PERFCPST | NUMBER(5,2) | sim |  |
| VLFCPST | NUMBER(24,8) | sim |  |
| VLBASEFCPST | NUMBER(24,8) | sim |  |
| QTULTENT | NUMBER(12,3) | sim |  |
| QTULTENTANT | NUMBER(12,3) | sim |  |
| QTCANCEL | NUMBER(18,6) | sim |  |
| VLSTRET | NUMBER(24,8) | sim |  |
| CODNATPIS | VARCHAR2(4) | sim |  |
| CODNATCOFINS | VARCHAR2(4) | sim |  |
| CODNATRECFT | VARCHAR2(4) | sim |  |
| SEQREF | NUMBER(4) | sim |  |
| VICMSSUBSTITUTO | NUMBER(24,8) | sim |  |
| PRODUTOFERTA | VARCHAR2(1) | sim |  |
| GERARSALDOFLEXVENDA | VARCHAR2(1) | sim |  |
| NDRAW | VARCHAR2(11) | sim |  |
| NRE | VARCHAR2(12) | sim |  |
| CHNFE | VARCHAR2(44) | sim |  |
| QEXPORT | NUMBER(18,6) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| MOTDESICMS | VARCHAR2(2) | sim |  |
| USAFASSON | VARCHAR2(1) | sim |  |
| CODCREDESTORNOPISPF | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPF | NUMBER(3) | sim |  |
| CODCREDESTORNOPISPJ | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPJ | NUMBER(3) | sim |  |
| USADESCQTDE_DESCMISTO2 | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO3 | VARCHAR2(1) | sim |  |
| BASE_VERBAFLEX_PERDESCINI | NUMBER(5,2) | sim |  |
| BASE_VERBAFLEX_PERDESCFINAL | NUMBER(5,2) | sim |  |
| VLVERBAFLEX_CREDITO | NUMBER(12,2) | sim |  |
| VLVERBAFLEX_DEBITO | NUMBER(12,2) | sim |  |
| USAVERBAFLEX_CREDITO | VARCHAR2(1) | sim |  |
| USAVERBAFLEX_DEBITO | VARCHAR2(1) | sim |  |
| PERDIFERIMENTO | NUMBER(18,6) | sim |  |
| VLICMDIF | NUMBER(24,8) | sim |  |
| VLCIAP | NUMBER(24,8) | sim |  |
| NUMENTENTRADACIAP | NUMBER(10) | sim |  |
| QTMOFADOSTP17 | NUMBER(8) | sim |  |
| QTVENCIDOSTP17 | NUMBER(8) | sim |  |
| MOTIVOMOFVENCTP17 | VARCHAR2(1000) | sim |  |
| AGRUPCUSTO | VARCHAR2(1) | sim |  |
| AVARIADEVOL | VARCHAR2(1) | sim |  |
| ACRESCCUSTODESAG | NUMBER(18,6) | sim |  |
| CODPRODDESAGPAI | NUMBER(10) | sim |  |
| PERCUSTODESAG | NUMBER(18,6) | sim |  |
| CODFUNCALTPESO | NUMBER(10) | sim |  |
| PRODDESCQT | VARCHAR2(1) | sim |  |
| TIPOPROMOCAO | VARCHAR2(30) | sim |  |
| IDSCANNTECH | NUMBER(10) | sim |  |
| VLDESCSCANNTECH | NUMBER(24,8) | sim |  |
| VLCUSTORB | NUMBER(12,2) | sim |  |
| VL_OUT_TAXAS | NUMBER(24,8) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| SEQ_DEV | NUMBER(4) | sim |  |
| FILIALDEVORIG | VARCHAR2(2) | sim | NA DEVOLUCAO DEVERA SALVAR O CODFILIAL DO PEDIDO ORIGINAL, IMPORTANTE QUANDO ITEM E DE FILIAL RETIRA |
| ITEMPED_SEQ | NUMBER(4) | sim | CAMPO PARA RELACIONAR AS TABELAS ITEMPED.SEQ COM A MOVIMENTACAO |
| DEVOL_BLOQ | VARCHAR2(1) | sim | REALIZAR DEVOLUCAO ONDE MERCADORIA JA FOI ENTREGUE BLOQUEIA O ESTOQUE SALVA S |
| UTQTMAXOFERTA | VARCHAR2(1) | sim | CAMPO PARA MARCAR SE ABATEU QTDE MAXIMA NA VENDA DE PRODUTO COM PRECO DE OFERTA |
| QTANTECIP | NUMBER(18,6) | sim |  |
| CODTIPOOFERTA | NUMBER(10) | sim |  |
| SF_124 | VARCHAR2(1) | sim | AJUSTE DE ESTOQUE ROTINA 124 REALIZADO COMO SIMPLES FATURA |
| IDCRVENDAS | NUMBER(10) | sim | INTEGRACAO CRESCE VENDAS - RECEBE A IDENTIFICACAO UNICA DA VENDA PELO CRESCE VENDAS |
| VLDESCCRVENDAS | NUMBER(24,8) | sim | INTEGRACAO CRESCE VENDAS - RECEBE O DESCONTO CRESCE VENDAS |
| IDQTDMAXCRVENDAS | NUMBER(18,6) | sim | INTEGRACAO CRESCE VENDAS - ID PARA IDENTIFICAR A QTD MAXIMA DE ITENS PARA DESCONTO |
| PERADREM_ICMSRET | NUMBER(5,4) | sim | Alíquota AD REM do ICMS para o produto CST=61 |
| VICMSMONORET | NUMBER(18,6) | sim | Valor AD REM do ICMS para o produto CST=61 |
| SF_CONTABIL | VARCHAR2(1) | sim | GRAVAR S PARA ENTRADAS SIMPLES FATURA R736/701 |

### VAREJOANTIGO.MOVIMENTACAO (2.062.648 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| ID | NUMBER(10) | não |  |
| NUMVENDA | NUMBER(10) | sim |  |
| NUMENT | NUMBER(10) | sim |  |
| NUMOP | NUMBER(10) | sim |  |
| NUMREQ | NUMBER(10) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| DTMOV | DATE | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| CODPROD | NUMBER(10) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| SEQ | NUMBER(4) | sim |  |
| OPERACAO | VARCHAR2(2) | sim |  |
| QT | NUMBER(18,6) | sim |  |
| QTCONT | NUMBER(18,6) | sim |  |
| CUSTOCONT | NUMBER(18,6) | sim |  |
| CUSTOREAL | NUMBER(18,6) | sim |  |
| CUSTOFIN | NUMBER(18,6) | sim |  |
| CUSTOCONTANT | NUMBER(18,6) | sim |  |
| CUSTOREALANT | NUMBER(18,6) | sim |  |
| CUSTOFINANT | NUMBER(18,6) | sim |  |
| CUSTOULTENTANT | NUMBER(18,6) | sim |  |
| PTABELA | NUMBER(24,8) | sim |  |
| PUNIT | NUMBER(24,8) | sim |  |
| PUNITCONT | NUMBER(24,8) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| PERICM | NUMBER(5,2) | sim |  |
| PERST | NUMBER(18,6) | sim |  |
| PERIPI | NUMBER(5,2) | sim |  |
| PERFRETE | NUMBER(5,2) | sim |  |
| PEROUT | NUMBER(5,2) | sim |  |
| ST | NUMBER(24,8) | sim |  |
| CODFISCALITEM | NUMBER(4) | sim |  |
| NUMLOTE | VARCHAR2(20) | sim |  |
| DTFAB | DATE | sim |  |
| DTVENC | DATE | sim |  |
| STATUS | VARCHAR2(2) | sim |  |
| NUMVENDADEV | NUMBER(10) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| VLBASEST | NUMBER(24,8) | sim |  |
| VLBASEICM | NUMBER(24,8) | sim |  |
| VLICM | NUMBER(24,8) | sim |  |
| VLBASEIPI | NUMBER(24,8) | sim |  |
| VLIPI | NUMBER(24,8) | sim |  |
| SITTRIBUT | VARCHAR2(2) | sim |  |
| NOVOPVENDA | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(24,8) | sim |  |
| VLISENTO | NUMBER(24,8) | sim |  |
| CODTRIBUT | NUMBER(2) | sim |  |
| PERBASERED | NUMBER(5,2) | sim |  |
| VLDESC | NUMBER(24,8) | sim |  |
| PERDESCIMP | NUMBER(8,4) | sim |  |
| CODBARRA | NUMBER(14) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| NUMNOTA | NUMBER(10) | sim |  |
| CODPARC | NUMBER(6) | sim |  |
| PERICMANTECIP | NUMBER(5,2) | sim |  |
| PERDESPFIN | NUMBER(18,6) | sim |  |
| PERBON | NUMBER(5,2) | sim |  |
| PERFRETECONH | NUMBER(5,2) | sim |  |
| NUMBONUS | NUMBER(10) | sim |  |
| QTPCA | NUMBER(12,3) | sim |  |
| AVARIA | VARCHAR2(1) | sim |  |
| CUSTOULTENT | NUMBER(18,6) | sim |  |
| DESCALT | VARCHAR2(120) | sim |  |
| VLPISCOFINS | NUMBER(12,2) | sim |  |
| TIPO | NUMBER(2) | sim |  |
| VLBASEPIS | NUMBER(24,8) | sim |  |
| PERPIS | NUMBER(18,6) | sim |  |
| VLPIS | NUMBER(24,8) | sim |  |
| VLBASECOFINS | NUMBER(24,8) | sim |  |
| PERCOFINS | NUMBER(18,6) | sim |  |
| VLCOFINS | NUMBER(24,8) | sim |  |
| PUNITORIG | NUMBER(24,8) | sim |  |
| NUMENTDEV | NUMBER(10) | sim |  |
| ALIQCREDSIMPLES | NUMBER(5,2) | sim |  |
| QTORIG | NUMBER(18,6) | sim |  |
| UNORIG | VARCHAR2(3) | sim |  |
| OBSADIC | VARCHAR2(400) | sim |  |
| EMBALAGEMORIG | VARCHAR2(12) | sim |  |
| CUSTOREALBLOQ | NUMBER(12,3) | sim |  |
| PERICMDEBITO | NUMBER(5,2) | sim |  |
| PERICMCREDITO | NUMBER(5,2) | sim |  |
| PERIVA | NUMBER(5,2) | sim |  |
| PRODLIBERADO | VARCHAR2(1) | sim |  |
| CSOSN | NUMBER(5) | sim |  |
| VLFRETE | NUMBER(24,8) | sim |  |
| PEROUTRASDESP | NUMBER(5,2) | sim |  |
| PERSEGURO | NUMBER(5,2) | sim |  |
| VLOUTRASDESP | NUMBER(24,8) | sim |  |
| VLSEGURO | NUMBER(24,8) | sim |  |
| SUBTOT | NUMBER(18,6) | sim |  |
| CSTPIS | VARCHAR2(3) | sim |  |
| CSTCOFINS | VARCHAR2(3) | sim |  |
| VLBCIMP | NUMBER(15,2) | sim |  |
| VLDESPADUANEIRA | NUMBER(15,2) | sim |  |
| VLIMPOSTOIMP | NUMBER(15,2) | sim |  |
| VLIOF | NUMBER(15,2) | sim |  |
| VLINSS | NUMBER(18,6) | sim |  |
| VLIR | NUMBER(18,6) | sim |  |
| VLCSLL | NUMBER(18,6) | sim |  |
| NUMNOTATRANSF | NUMBER(10) | sim |  |
| USAFATORMASTER | VARCHAR2(1) | sim |  |
| VLCONHECFRETE | NUMBER(24,8) | sim |  |
| VLICMSDES | NUMBER(24,8) | sim |  |
| VLDESPICMANTECIPADO | NUMBER(24,8) | sim |  |
| PFCPUFDEST | NUMBER(5,2) | sim |  |
| PICMSUFDEST | NUMBER(5,2) | sim |  |
| PICMSINTER | NUMBER(5,2) | sim |  |
| PICMSINTERPART | NUMBER(5,2) | sim |  |
| VFCPUFDEST | NUMBER(18,6) | sim |  |
| VICMSUFDEST | NUMBER(18,6) | sim |  |
| VICMSUFREMET | NUMBER(18,6) | sim |  |
| VLFRETECONHECIMENTO | NUMBER(24,8) | sim |  |
| VBCUFDEST | NUMBER(18,6) | sim |  |
| IDAVARIA | NUMBER(10) | sim |  |
| VLDESPFINAN | NUMBER(24,8) | sim |  |
| DTDESBLOQ | DATE | sim |  |
| CODFUNCLIB | NUMBER(5) | sim |  |
| STATUS_MOFVENC | VARCHAR2(1) | sim |  |
| QTMOF | NUMBER(18,6) | sim |  |
| QTVENC | NUMBER(18,6) | sim |  |
| STATUSPCP | VARCHAR2(1) | sim |  |
| CODPRODPAI | NUMBER(10) | sim |  |
| VLFCP | NUMBER(18,6) | sim |  |
| PERFCP | NUMBER(5,2) | sim |  |
| VLBASEFCP | NUMBER(24,8) | sim |  |
| ICMSSTRET | NUMBER(18,6) | sim |  |
| VLBASESTRET | NUMBER(18,6) | sim |  |
| NITEMPED | VARCHAR2(6) | sim |  |
| XPED | VARCHAR2(15) | sim |  |
| VLBASEFCPSTRET | NUMBER(18,6) | sim |  |
| PSTRET | NUMBER(5,2) | sim |  |
| VLFCPSTRET | NUMBER(18,6) | sim |  |
| PERFCPSTRET | NUMBER(18,6) | sim |  |
| CODHISTITEM | NUMBER(6) | sim |  |
| PERFCPST | NUMBER(5,2) | sim |  |
| VLFCPST | NUMBER(24,8) | sim |  |
| VLBASEFCPST | NUMBER(24,8) | sim |  |
| QTULTENT | NUMBER(12,3) | sim |  |
| QTULTENTANT | NUMBER(12,3) | sim |  |
| QTCANCEL | NUMBER(18,6) | sim |  |
| VLSTRET | NUMBER(24,8) | sim |  |
| CODNATPIS | VARCHAR2(4) | sim |  |
| CODNATCOFINS | VARCHAR2(4) | sim |  |
| CODNATRECFT | VARCHAR2(4) | sim |  |
| SEQREF | NUMBER(4) | sim |  |
| VICMSSUBSTITUTO | NUMBER(24,8) | sim |  |
| PRODUTOFERTA | VARCHAR2(1) | sim |  |
| GERARSALDOFLEXVENDA | VARCHAR2(1) | sim |  |
| NDRAW | VARCHAR2(11) | sim |  |
| NRE | VARCHAR2(12) | sim |  |
| CHNFE | VARCHAR2(44) | sim |  |
| QEXPORT | NUMBER(18,6) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| MOTDESICMS | VARCHAR2(2) | sim |  |
| USAFASSON | VARCHAR2(1) | sim |  |
| CODCREDESTORNOPISPF | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPF | NUMBER(3) | sim |  |
| CODCREDESTORNOPISPJ | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPJ | NUMBER(3) | sim |  |
| USADESCQTDE_DESCMISTO2 | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO3 | VARCHAR2(1) | sim |  |
| BASE_VERBAFLEX_PERDESCINI | NUMBER(5,2) | sim |  |
| BASE_VERBAFLEX_PERDESCFINAL | NUMBER(5,2) | sim |  |
| VLVERBAFLEX_CREDITO | NUMBER(12,2) | sim |  |
| VLVERBAFLEX_DEBITO | NUMBER(12,2) | sim |  |
| USAVERBAFLEX_CREDITO | VARCHAR2(1) | sim |  |
| USAVERBAFLEX_DEBITO | VARCHAR2(1) | sim |  |
| PERDIFERIMENTO | NUMBER(18,6) | sim |  |
| VLICMDIF | NUMBER(24,8) | sim |  |
| VLCIAP | NUMBER(24,8) | sim |  |
| NUMENTENTRADACIAP | NUMBER(10) | sim |  |
| QTMOFADOSTP17 | NUMBER(8) | sim |  |
| QTVENCIDOSTP17 | NUMBER(8) | sim |  |
| MOTIVOMOFVENCTP17 | VARCHAR2(1000) | sim |  |
| AGRUPCUSTO | VARCHAR2(1) | sim |  |
| AVARIADEVOL | VARCHAR2(1) | sim |  |
| ACRESCCUSTODESAG | NUMBER(18,6) | sim |  |
| CODPRODDESAGPAI | NUMBER(10) | sim |  |
| PERCUSTODESAG | NUMBER(18,6) | sim |  |
| CODFUNCALTPESO | NUMBER(10) | sim |  |

### JP.NFBASE (1.848.824 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMENT | NUMBER(10) | não |  |
| CODCONT | NUMBER(10) | não |  |
| VLBASE | NUMBER(12,2) | sim |  |
| PERICM | NUMBER(5,2) | não |  |
| VLICM | NUMBER(12,2) | sim |  |
| CODFISCAL | NUMBER(4) | não |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLST | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(12,2) | sim |  |
| VLISENTO | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| VLBASEPIS | NUMBER(12,2) | sim |  |
| VLBASECOFINS | NUMBER(12,2) | sim |  |
| VLPIS | NUMBER(12,2) | sim |  |
| VLCOFINS | NUMBER(12,2) | sim |  |
| PERPIS | NUMBER(8,6) | sim |  |
| PERCOFINS | NUMBER(8,6) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| VLFCPST | NUMBER(12,2) | sim |  |
| VLBASEFCPST | NUMBER(12,2) | sim |  |
| CSTCREDITOICMS | VARCHAR2(2) | sim |  |
| CSOSN_CREDITOICMS | NUMBER(3) | sim |  |

### SEVERIANO.MOVIMENTACAO (1.188.600 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| ID | NUMBER(10) | não |  |
| NUMVENDA | NUMBER(10) | sim |  |
| NUMENT | NUMBER(10) | sim |  |
| NUMOP | NUMBER(10) | sim |  |
| NUMREQ | NUMBER(10) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| DTMOV | DATE | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| CODPROD | NUMBER(10) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| SEQ | NUMBER(4) | sim |  |
| OPERACAO | VARCHAR2(2) | sim |  |
| QT | NUMBER(18,6) | sim |  |
| QTCONT | NUMBER(18,6) | sim |  |
| CUSTOCONT | NUMBER(18,6) | sim |  |
| CUSTOREAL | NUMBER(18,6) | sim |  |
| CUSTOFIN | NUMBER(18,6) | sim |  |
| CUSTOCONTANT | NUMBER(18,6) | sim |  |
| CUSTOREALANT | NUMBER(18,6) | sim |  |
| CUSTOFINANT | NUMBER(18,6) | sim |  |
| CUSTOULTENTANT | NUMBER(18,6) | sim |  |
| PTABELA | NUMBER(24,8) | sim |  |
| PUNIT | NUMBER(24,8) | sim |  |
| PUNITCONT | NUMBER(24,8) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| PERICM | NUMBER(5,2) | sim |  |
| PERST | NUMBER(18,6) | sim |  |
| PERIPI | NUMBER(5,2) | sim |  |
| PERFRETE | NUMBER(5,2) | sim |  |
| PEROUT | NUMBER(5,2) | sim |  |
| ST | NUMBER(24,8) | sim |  |
| CODFISCALITEM | NUMBER(4) | sim |  |
| NUMLOTE | VARCHAR2(20) | sim |  |
| DTFAB | DATE | sim |  |
| DTVENC | DATE | sim |  |
| STATUS | VARCHAR2(2) | sim |  |
| NUMVENDADEV | NUMBER(10) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| VLBASEST | NUMBER(24,8) | sim |  |
| VLBASEICM | NUMBER(24,8) | sim |  |
| VLICM | NUMBER(24,8) | sim |  |
| VLBASEIPI | NUMBER(24,8) | sim |  |
| VLIPI | NUMBER(24,8) | sim |  |
| SITTRIBUT | VARCHAR2(2) | sim |  |
| NOVOPVENDA | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(24,8) | sim |  |
| VLISENTO | NUMBER(24,8) | sim |  |
| CODTRIBUT | NUMBER(2) | sim |  |
| PERBASERED | NUMBER(5,2) | sim |  |
| VLDESC | NUMBER(24,8) | sim |  |
| PERDESCIMP | NUMBER(8,4) | sim |  |
| CODBARRA | NUMBER(14) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| NUMNOTA | NUMBER(10) | sim |  |
| CODPARC | NUMBER(6) | sim |  |
| PERICMANTECIP | NUMBER(5,2) | sim |  |
| PERDESPFIN | NUMBER(18,6) | sim |  |
| PERBON | NUMBER(5,2) | sim |  |
| PERFRETECONH | NUMBER(5,2) | sim |  |
| NUMBONUS | NUMBER(10) | sim |  |
| QTPCA | NUMBER(12,3) | sim |  |
| AVARIA | VARCHAR2(1) | sim |  |
| CUSTOULTENT | NUMBER(18,6) | sim |  |
| DESCALT | VARCHAR2(120) | sim |  |
| VLPISCOFINS | NUMBER(12,2) | sim |  |
| TIPO | NUMBER(2) | sim |  |
| VLBASEPIS | NUMBER(24,8) | sim |  |
| PERPIS | NUMBER(18,6) | sim |  |
| VLPIS | NUMBER(24,8) | sim |  |
| VLBASECOFINS | NUMBER(24,8) | sim |  |
| PERCOFINS | NUMBER(18,6) | sim |  |
| VLCOFINS | NUMBER(24,8) | sim |  |
| PUNITORIG | NUMBER(24,8) | sim |  |
| NUMENTDEV | NUMBER(10) | sim |  |
| ALIQCREDSIMPLES | NUMBER(5,2) | sim |  |
| QTORIG | NUMBER(18,6) | sim |  |
| UNORIG | VARCHAR2(3) | sim |  |
| OBSADIC | VARCHAR2(400) | sim |  |
| EMBALAGEMORIG | VARCHAR2(12) | sim |  |
| CUSTOREALBLOQ | NUMBER(12,3) | sim |  |
| PERICMDEBITO | NUMBER(5,2) | sim |  |
| PERICMCREDITO | NUMBER(5,2) | sim |  |
| PERIVA | NUMBER(5,2) | sim |  |
| PRODLIBERADO | VARCHAR2(1) | sim |  |
| CSOSN | NUMBER(5) | sim |  |
| VLFRETE | NUMBER(24,8) | sim |  |
| PEROUTRASDESP | NUMBER(5,2) | sim |  |
| PERSEGURO | NUMBER(5,2) | sim |  |
| VLOUTRASDESP | NUMBER(24,8) | sim |  |
| VLSEGURO | NUMBER(24,8) | sim |  |
| SUBTOT | NUMBER(18,6) | sim |  |
| CSTPIS | VARCHAR2(3) | sim |  |
| CSTCOFINS | VARCHAR2(3) | sim |  |
| VLBCIMP | NUMBER(15,2) | sim |  |
| VLDESPADUANEIRA | NUMBER(15,2) | sim |  |
| VLIMPOSTOIMP | NUMBER(15,2) | sim |  |
| VLIOF | NUMBER(15,2) | sim |  |
| VLINSS | NUMBER(18,6) | sim |  |
| VLIR | NUMBER(18,6) | sim |  |
| VLCSLL | NUMBER(18,6) | sim |  |
| NUMNOTATRANSF | NUMBER(10) | sim |  |
| USAFATORMASTER | VARCHAR2(1) | sim |  |
| VLCONHECFRETE | NUMBER(24,8) | sim |  |
| VLICMSDES | NUMBER(24,8) | sim |  |
| VLDESPICMANTECIPADO | NUMBER(24,8) | sim |  |
| PFCPUFDEST | NUMBER(5,2) | sim |  |
| PICMSUFDEST | NUMBER(5,2) | sim |  |
| PICMSINTER | NUMBER(5,2) | sim |  |
| PICMSINTERPART | NUMBER(5,2) | sim |  |
| VFCPUFDEST | NUMBER(18,6) | sim |  |
| VICMSUFDEST | NUMBER(18,6) | sim |  |
| VICMSUFREMET | NUMBER(18,6) | sim |  |
| VLFRETECONHECIMENTO | NUMBER(24,8) | sim |  |
| VBCUFDEST | NUMBER(18,6) | sim |  |
| AAA | VARCHAR2(1) | sim |  |
| IDAVARIA | NUMBER(10) | sim |  |
| VLDESPFINAN | NUMBER(24,8) | sim |  |
| DTDESBLOQ | DATE | sim |  |
| CODFUNCLIB | NUMBER(5) | sim |  |
| STATUS_MOFVENC | VARCHAR2(1) | sim |  |
| QTMOF | NUMBER(18,6) | sim |  |
| QTVENC | NUMBER(18,6) | sim |  |
| STATUSPCP | VARCHAR2(1) | sim |  |
| CODPRODPAI | NUMBER(10) | sim |  |
| VLFCP | NUMBER(18,6) | sim |  |
| PERFCP | NUMBER(5,2) | sim |  |
| VLBASEFCP | NUMBER(24,8) | sim |  |
| ICMSSTRET | NUMBER(18,6) | sim |  |
| VLBASESTRET | NUMBER(18,6) | sim |  |
| NITEMPED | VARCHAR2(6) | sim |  |
| XPED | VARCHAR2(15) | sim |  |
| VLBASEFCPSTRET | NUMBER(18,6) | sim |  |
| PSTRET | NUMBER(5,2) | sim |  |
| VLFCPSTRET | NUMBER(18,6) | sim |  |
| PERFCPSTRET | NUMBER(18,6) | sim |  |
| CODHISTITEM | NUMBER(6) | sim |  |
| PERFCPST | NUMBER(5,2) | sim |  |
| VLFCPST | NUMBER(24,8) | sim |  |
| VLBASEFCPST | NUMBER(24,8) | sim |  |
| QTULTENT | NUMBER(12,3) | sim |  |
| QTULTENTANT | NUMBER(12,3) | sim |  |
| QTCANCEL | NUMBER(18,6) | sim |  |
| VLSTRET | NUMBER(24,8) | sim |  |
| CODNATPIS | VARCHAR2(4) | sim |  |
| CODNATCOFINS | VARCHAR2(4) | sim |  |
| CODNATRECFT | VARCHAR2(4) | sim |  |
| SEQREF | NUMBER(4) | sim |  |
| VICMSSUBSTITUTO | NUMBER(24,8) | sim |  |
| PRODUTOFERTA | VARCHAR2(1) | sim |  |
| GERARSALDOFLEXVENDA | VARCHAR2(1) | sim |  |
| NDRAW | VARCHAR2(11) | sim |  |
| NRE | VARCHAR2(12) | sim |  |
| CHNFE | VARCHAR2(44) | sim |  |
| QEXPORT | NUMBER(18,6) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| MOTDESICMS | VARCHAR2(2) | sim |  |
| USAFASSON | VARCHAR2(1) | sim |  |
| CODCREDESTORNOPISPF | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPF | NUMBER(3) | sim |  |
| CODCREDESTORNOPISPJ | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPJ | NUMBER(3) | sim |  |
| USADESCQTDE_DESCMISTO2 | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO3 | VARCHAR2(1) | sim |  |
| BASE_VERBAFLEX_PERDESCINI | NUMBER(5,2) | sim |  |
| BASE_VERBAFLEX_PERDESCFINAL | NUMBER(5,2) | sim |  |
| VLVERBAFLEX_CREDITO | NUMBER(12,2) | sim |  |
| VLVERBAFLEX_DEBITO | NUMBER(12,2) | sim |  |
| USAVERBAFLEX_CREDITO | VARCHAR2(1) | sim |  |
| USAVERBAFLEX_DEBITO | VARCHAR2(1) | sim |  |
| PERDIFERIMENTO | NUMBER(18,6) | sim |  |
| VLICMDIF | NUMBER(24,8) | sim |  |
| VLCIAP | NUMBER(24,8) | sim |  |
| NUMENTENTRADACIAP | NUMBER(10) | sim |  |
| QTMOFADOSTP17 | NUMBER(8) | sim |  |
| QTVENCIDOSTP17 | NUMBER(8) | sim |  |
| MOTIVOMOFVENCTP17 | VARCHAR2(1000) | sim |  |
| AGRUPCUSTO | VARCHAR2(1) | sim |  |
| AVARIADEVOL | VARCHAR2(1) | sim |  |
| ACRESCCUSTODESAG | NUMBER(18,6) | sim |  |
| CODPRODDESAGPAI | NUMBER(10) | sim |  |
| PERCUSTODESAG | NUMBER(18,6) | sim |  |
| CODFUNCALTPESO | NUMBER(10) | sim |  |
| PRODDESCQT | VARCHAR2(1) | sim |  |
| TIPOPROMOCAO | VARCHAR2(30) | sim |  |
| IDSCANNTECH | NUMBER(10) | sim |  |
| VLDESCSCANNTECH | NUMBER(24,8) | sim |  |

### VAREJO.NFBASE (1.150.623 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMENT | NUMBER(10) | não |  |
| CODCONT | NUMBER(10) | não |  |
| VLBASE | NUMBER(12,2) | sim |  |
| PERICM | NUMBER(5,2) | não |  |
| VLICM | NUMBER(12,2) | sim |  |
| CODFISCAL | NUMBER(4) | não |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLST | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(12,2) | sim |  |
| VLISENTO | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| VLBASEPIS | NUMBER(12,2) | sim |  |
| VLBASECOFINS | NUMBER(12,2) | sim |  |
| VLPIS | NUMBER(12,2) | sim |  |
| VLCOFINS | NUMBER(12,2) | sim |  |
| PERPIS | NUMBER(8,6) | sim |  |
| PERCOFINS | NUMBER(8,6) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| VLFCPST | NUMBER(12,2) | sim |  |
| VLBASEFCPST | NUMBER(12,2) | sim |  |
| CSTCREDITOICMS | VARCHAR2(2) | sim |  |
| CSOSN_CREDITOICMS | NUMBER(3) | sim |  |

### JP.LOG_ALTER_CRECEBER (1.045.157 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| ID | NUMBER | não |  |
| DATADOLOG | DATE | sim |  |
| USERNAME | VARCHAR2(200) | sim |  |
| MACHINE | VARCHAR2(200) | sim |  |
| PROGRAM | VARCHAR2(200) | sim |  |
| MODULE | VARCHAR2(200) | sim |  |
| TERMINAL | VARCHAR2(200) | sim |  |
| IP | VARCHAR2(200) | sim |  |
| NUMVENDA | NUMBER(10) | não |  |
| NUMNOTA | NUMBER(10) | sim |  |
| PREST | NUMBER(3) | não |  |
| CODCLI | NUMBER(6) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| DTEMISSAO | DATE | sim |  |
| DTVENC | DATE | sim |  |
| VALOR | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLJURO | NUMBER(12,2) | sim |  |
| DTPAGO | DATE | sim |  |
| VPAGO | NUMBER(12,2) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| NUMBCO | VARCHAR2(4) | sim |  |
| NUMAG | VARCHAR2(4) | sim |  |
| NUMCH | VARCHAR2(8) | sim |  |
| NUMCART | VARCHAR2(15) | sim |  |
| DTFECHA | DATE | sim |  |
| OBS | VARCHAR2(2000) | sim |  |
| CODCXBCO | NUMBER(4) | sim |  |
| CODFUNCFECHA | NUMBER(10) | sim |  |
| DTBAIXA | DATE | sim |  |
| NUMCONTA | VARCHAR2(15) | sim |  |
| CODCXBCOP | NUMBER(4) | sim |  |
| VLAUX | NUMBER(12,2) | sim |  |
| TOTPREST | NUMBER(3) | sim |  |
| DTULTALT | DATE | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| PERCOM | NUMBER(7,4) | sim |  |
| NOSSNUMBCO | VARCHAR2(14) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| DTDESD | DATE | sim |  |
| CODFUNCDESD | NUMBER(10) | sim |  |
| CODFUNCBAIXA | NUMBER(10) | sim |  |
| VALORDEV | NUMBER(12,2) | sim |  |
| OBS2 | VARCHAR2(100) | sim |  |
| NUMLANCPG | NUMBER(10) | sim |  |
| NOSSONUMBCO | VARCHAR2(20) | sim |  |
| CODBARRA | VARCHAR2(44) | sim |  |
| LINHADIG | VARCHAR2(65) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| VLTXBOLETO | NUMBER(12,2) | sim |  |
| STATUS | VARCHAR2(1) | sim |  |
| VALORORIG | NUMBER(12,2) | sim |  |
| PROTOCOLO | NUMBER(10) | sim |  |
| TURNO | VARCHAR2(1) | sim |  |
| DTVENCORIG | DATE | sim |  |
| CODCOBORIG | VARCHAR2(4) | sim |  |
| CODSUPERVISOR | NUMBER(4) | sim |  |
| PR | VARCHAR2(2) | sim |  |
| DTULTALTER | DATE | sim |  |
| DTCXMOT | DATE | sim |  |
| CODFUNCCXMOT | NUMBER(10) | sim |  |
| NUMTRANS | NUMBER(10) | sim |  |
| CODCOBCXBCO | VARCHAR2(4) | sim |  |
| CODFUNCVALE | NUMBER(10) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| OPERACAO | VARCHAR2(1) | sim |  |
| CODBAIXA | NUMBER(4) | sim |  |
| ALINEA | VARCHAR2(4) | sim |  |
| NUMVENDADESD | NUMBER(10) | sim |  |
| NUMFATURA | NUMBER(10) | sim |  |
| DTFECHAPROT | DATE | sim |  |
| DTCXMOTPROT | DATE | sim |  |
| CODFUNCFECHAPROT | NUMBER(10) | sim |  |
| TIPOPRORROG | VARCHAR2(1) | sim |  |
| DTPRORROG | DATE | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| NUMCUSTODIA | NUMBER(8) | sim |  |
| DTCUSTODIA | DATE | sim |  |
| CODCXBCOCUSTODIA | NUMBER(4) | sim |  |
| DTPREVPAGTO | DATE | sim |  |
| PRESTDESD | NUMBER(3) | sim |  |
| DTESTORNO | DATE | sim |  |
| CODFUNCESTORNO | NUMBER(10) | sim |  |
| DIGITAO | VARCHAR2(1) | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| LIBERARVENDALIMCRED | VARCHAR2(1) | sim |  |
| RETBOLTIPOREG | NUMBER(2) | sim |  |
| RETBOLCODINSC | NUMBER(3) | sim |  |
| RETBOLNUMINSC | NUMBER(20) | sim |  |
| RETBOLAGENCIA | NUMBER(6) | sim |  |
| RETBOLCONTA | NUMBER(10) | sim |  |
| RETBOLDAC | VARCHAR2(1) | sim |  |
| RETBOLCODOCORRENCIA | NUMBER(4) | sim |  |
| RETBOLDTOCORRENCIA | DATE | sim |  |
| RETBOLNOSSONUMCONF | NUMBER(15) | sim |  |
| RETBOLDTVENCIMENTO | DATE | sim |  |
| RETBOLVALORTITULO | NUMBER(15,2) | sim |  |
| RETBOLCODBCO | NUMBER(4) | sim |  |
| RETBOLAGCOB | NUMBER(6) | sim |  |
| RETBOLDACAGCOB | VARCHAR2(1) | sim |  |
| RETBOLESPECIE | NUMBER(3) | sim |  |
| RETBOLTARIFACOB | NUMBER(15,2) | sim |  |
| RETBOLVALORIOF | NUMBER(15,2) | sim |  |
| RETBOLVALORABAT | NUMBER(15,2) | sim |  |
| RETBOLDESCONTOS | NUMBER(15,2) | sim |  |
| RETBOLVALORPRINC | NUMBER(15,2) | sim |  |
| RETBOLJUROSMORAMULTA | NUMBER(15,2) | sim |  |
| RETBOLOUTROSCREDITOS | NUMBER(15,2) | sim |  |
| RETBOLDTCREDITO | DATE | sim |  |
| RETBOLINSTRCANCEL | NUMBER(6) | sim |  |
| RETBOLNOMESACADO | VARCHAR2(40) | sim |  |
| RETBOLERROS | VARCHAR2(10) | sim |  |
| RETBOLCODLIQ | VARCHAR2(4) | sim |  |
| RETBOLNUMSEQ | NUMBER(10) | sim |  |
| RETBOLBAIXADO | VARCHAR2(1) | sim |  |
| RETBOLDVAG | VARCHAR2(3) | sim |  |
| DTFECHACHECKOUT | DATE | sim |  |
| VLDESCICMPARC | NUMBER(12,2) | sim |  |
| VLDESCFIN | NUMBER(12,2) | sim |  |
| DTTRANSMISSAO | DATE | sim |  |
| PERCOMSUP | NUMBER(7,4) | sim |  |
| VLDESCTXCAR | NUMBER(12,2) | sim |  |
| NUMPROM | VARCHAR2(20) | sim |  |
| TAXA | NUMBER(12,2) | sim |  |
| CODEMITENTE | NUMBER(10) | sim |  |
| BANDEIRA | VARCHAR2(60) | sim |  |
| TIPO_TRANSACAO | VARCHAR2(15) | sim |  |
| NSU | VARCHAR2(30) | sim |  |
| AUTORIZACAO | VARCHAR2(20) | sim |  |
| ESTABELECIMENTO | VARCHAR2(20) | sim |  |
| NUMEROCARTAO | VARCHAR2(30) | sim |  |
| ORIGEM | VARCHAR2(10) | sim |  |
| MODOBAIXA | VARCHAR2(1) | sim |  |
| DTBAIXACAR | DATE | sim |  |
| TRANSBAIXAAUTO | NUMBER(15) | sim |  |
| PRESTCAR | NUMBER(3) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| LANCR28 | VARCHAR2(1) | sim |  |
| TECLACOB | VARCHAR2(6) | sim |  |
| NUMTRANSMISSAO | NUMBER(14) | sim |  |
| VLMULTA | NUMBER(12,2) | sim |  |
| PDFENVIADO | VARCHAR2(1) | sim |  |

### VAREJO.ENDERECOS (1.034.809 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CEP | VARCHAR2(10) | não |  |
| CIDADE | VARCHAR2(60) | sim |  |
| BAIRRO | VARCHAR2(120) | sim |  |
| LOGRADOURO | VARCHAR2(255) | sim |  |
| ESTADO | VARCHAR2(40) | sim |  |
| UF | VARCHAR2(2) | sim |  |
| DISTKMMATRIZ | NUMBER(5,2) | sim |  |
| CODMUNICIPIO | NUMBER(7) | sim |  |
| CODESTADO | VARCHAR2(2) | sim |  |
| CODAUX | VARCHAR2(10) | sim |  |
| SRF | VARCHAR2(10) | sim |  |
| LATITUDE | VARCHAR2(30) | sim |  |
| LONGITUDE | VARCHAR2(30) | sim |  |
| AREA_CIDADE_KM2 | VARCHAR2(20) | sim |  |
| DDD | NUMBER(3) | sim |  |

### JP.ENDERECOS (1.034.809 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CEP | VARCHAR2(10) | não |  |
| CIDADE | VARCHAR2(60) | sim |  |
| BAIRRO | VARCHAR2(120) | sim |  |
| LOGRADOURO | VARCHAR2(255) | sim |  |
| ESTADO | VARCHAR2(40) | sim |  |
| UF | VARCHAR2(2) | sim |  |
| DISTKMMATRIZ | NUMBER(5,2) | sim |  |
| CODMUNICIPIO | NUMBER(7) | sim |  |
| CODESTADO | VARCHAR2(2) | sim |  |
| CODAUX | VARCHAR2(10) | sim |  |
| SRF | VARCHAR2(10) | sim |  |
| LATITUDE | VARCHAR2(30) | sim |  |
| LONGITUDE | VARCHAR2(30) | sim |  |
| AREA_CIDADE_KM2 | VARCHAR2(20) | sim |  |
| DDD | NUMBER(3) | sim |  |

### JP.CRECEBER (1.017.872 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMNOTA | NUMBER(10) | sim |  |
| PREST | NUMBER(3) | não |  |
| CODCLI | NUMBER(6) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| DTEMISSAO | DATE | sim |  |
| DTVENC | DATE | sim |  |
| VALOR | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLJURO | NUMBER(12,2) | sim |  |
| DTPAGO | DATE | sim |  |
| VPAGO | NUMBER(12,2) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| NUMBCO | VARCHAR2(4) | sim |  |
| NUMAG | VARCHAR2(4) | sim |  |
| NUMCH | VARCHAR2(8) | sim |  |
| NUMCART | VARCHAR2(15) | sim |  |
| DTFECHA | DATE | sim |  |
| OBS | VARCHAR2(2000) | sim |  |
| CODCXBCO | NUMBER(4) | sim |  |
| CODFUNCFECHA | NUMBER(10) | sim |  |
| DTBAIXA | DATE | sim |  |
| NUMCONTA | VARCHAR2(15) | sim |  |
| CODCXBCOP | NUMBER(4) | sim |  |
| VLAUX | NUMBER(12,2) | sim |  |
| TOTPREST | NUMBER(3) | sim |  |
| DTULTALT | DATE | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| PERCOM | NUMBER(7,4) | sim |  |
| NOSSNUMBCO | VARCHAR2(14) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| DTDESD | DATE | sim |  |
| CODFUNCDESD | NUMBER(10) | sim |  |
| CODFUNCBAIXA | NUMBER(10) | sim |  |
| VALORDEV | NUMBER(12,2) | sim |  |
| OBS2 | VARCHAR2(100) | sim |  |
| NUMLANCPG | NUMBER(10) | sim |  |
| NOSSONUMBCO | VARCHAR2(20) | sim |  |
| CODBARRA | VARCHAR2(44) | sim |  |
| LINHADIG | VARCHAR2(65) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| VLTXBOLETO | NUMBER(12,2) | sim |  |
| STATUS | VARCHAR2(1) | sim |  |
| VALORORIG | NUMBER(12,2) | sim |  |
| PROTOCOLO | NUMBER(10) | sim |  |
| TURNO | VARCHAR2(1) | sim |  |
| DTVENCORIG | DATE | sim |  |
| CODCOBORIG | VARCHAR2(4) | sim |  |
| CODSUPERVISOR | NUMBER(4) | sim |  |
| PR | VARCHAR2(2) | sim |  |
| DTULTALTER | DATE | sim |  |
| DTCXMOT | DATE | sim |  |
| CODFUNCCXMOT | NUMBER(10) | sim |  |
| NUMTRANS | NUMBER(10) | sim |  |
| CODCOBCXBCO | VARCHAR2(4) | sim |  |
| CODFUNCVALE | NUMBER(10) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| OPERACAO | VARCHAR2(1) | sim |  |
| CODBAIXA | NUMBER(4) | sim |  |
| ALINEA | VARCHAR2(4) | sim |  |
| NUMVENDADESD | NUMBER(10) | sim |  |
| NUMFATURA | NUMBER(10) | sim |  |
| DTFECHAPROT | DATE | sim |  |
| DTCXMOTPROT | DATE | sim |  |
| CODFUNCFECHAPROT | NUMBER(10) | sim |  |
| TIPOPRORROG | VARCHAR2(1) | sim |  |
| DTPRORROG | DATE | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| NUMCUSTODIA | NUMBER(8) | sim |  |
| DTCUSTODIA | DATE | sim |  |
| CODCXBCOCUSTODIA | NUMBER(4) | sim |  |
| DTPREVPAGTO | DATE | sim |  |
| PRESTDESD | NUMBER(3) | sim |  |
| DTESTORNO | DATE | sim |  |
| CODFUNCESTORNO | NUMBER(10) | sim |  |
| DIGITAO | VARCHAR2(1) | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| LIBERARVENDALIMCRED | VARCHAR2(1) | sim |  |
| RETBOLTIPOREG | NUMBER(2) | sim |  |
| RETBOLCODINSC | NUMBER(3) | sim |  |
| RETBOLNUMINSC | NUMBER(20) | sim |  |
| RETBOLAGENCIA | NUMBER(6) | sim |  |
| RETBOLCONTA | NUMBER(10) | sim |  |
| RETBOLDAC | VARCHAR2(1) | sim |  |
| RETBOLCODOCORRENCIA | NUMBER(4) | sim |  |
| RETBOLDTOCORRENCIA | DATE | sim |  |
| RETBOLNOSSONUMCONF | NUMBER(15) | sim |  |
| RETBOLDTVENCIMENTO | DATE | sim |  |
| RETBOLVALORTITULO | NUMBER(15,2) | sim |  |
| RETBOLCODBCO | NUMBER(4) | sim |  |
| RETBOLAGCOB | NUMBER(6) | sim |  |
| RETBOLDACAGCOB | VARCHAR2(1) | sim |  |
| RETBOLESPECIE | NUMBER(3) | sim |  |
| RETBOLTARIFACOB | NUMBER(15,2) | sim |  |
| RETBOLVALORIOF | NUMBER(15,2) | sim |  |
| RETBOLVALORABAT | NUMBER(15,2) | sim |  |
| RETBOLDESCONTOS | NUMBER(15,2) | sim |  |
| RETBOLVALORPRINC | NUMBER(15,2) | sim |  |
| RETBOLJUROSMORAMULTA | NUMBER(15,2) | sim |  |
| RETBOLOUTROSCREDITOS | NUMBER(15,2) | sim |  |
| RETBOLDTCREDITO | DATE | sim |  |
| RETBOLINSTRCANCEL | NUMBER(6) | sim |  |
| RETBOLNOMESACADO | VARCHAR2(40) | sim |  |
| RETBOLERROS | VARCHAR2(115) | sim |  |
| RETBOLCODLIQ | VARCHAR2(4) | sim |  |
| RETBOLNUMSEQ | NUMBER(10) | sim |  |
| RETBOLBAIXADO | VARCHAR2(1) | sim |  |
| RETBOLDVAG | VARCHAR2(3) | sim |  |
| DTFECHACHECKOUT | DATE | sim |  |
| VLDESCICMPARC | NUMBER(12,2) | sim |  |
| VLDESCFIN | NUMBER(12,2) | sim |  |
| DTTRANSMISSAO | DATE | sim |  |
| PERCOMSUP | NUMBER(7,4) | sim |  |
| VLDESCTXCAR | NUMBER(12,2) | sim |  |
| NUMPROM | VARCHAR2(20) | sim |  |
| TAXA | NUMBER(12,2) | sim |  |
| CODEMITENTE | NUMBER(10) | sim |  |
| BANDEIRA | VARCHAR2(60) | sim |  |
| TIPO_TRANSACAO | VARCHAR2(15) | sim |  |
| NSU | VARCHAR2(30) | sim |  |
| AUTORIZACAO | VARCHAR2(20) | sim |  |
| ESTABELECIMENTO | VARCHAR2(20) | sim |  |
| NUMEROCARTAO | VARCHAR2(30) | sim |  |
| ORIGEM | VARCHAR2(10) | sim |  |
| MODOBAIXA | VARCHAR2(1) | sim |  |
| DTBAIXACAR | DATE | sim |  |
| TRANSBAIXAAUTO | NUMBER(15) | sim |  |
| PRESTCAR | NUMBER(3) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| LANCR28 | VARCHAR2(1) | sim |  |
| TECLACOB | VARCHAR2(6) | sim |  |
| NUMTRANSMISSAO | NUMBER(14) | sim |  |
| VLMULTA | NUMBER(12,2) | sim |  |
| PDFENVIADO | VARCHAR2(1) | sim |  |
| CODVEND2 | NUMBER(10) | sim |  |
| DTFECHAR185 | DATE | sim |  |
| DESCDEV | NUMBER(12,2) | sim |  |
| NUMVENDABK | NUMBER(10) | sim |  |
| NUMTRANSBK | NUMBER(10) | sim |  |
| CPFCNPJ | VARCHAR2(18) | sim |  |
| NUMPEDBK | NUMBER(10) | sim |  |
| CODCLIBK | NUMBER(10) | sim |  |
| VLTARIFA | NUMBER(12,2) | sim |  |
| DTPAGODESCONTO | DATE | sim |  |
| DTESTORNODESCONTO | DATE | sim |  |
| VPAGODESCONTO | NUMBER(12,2) | sim |  |
| CODFUNCPAGODESCONTO | NUMBER(10) | sim |  |
| CODFUNCESTORNODESCONTO | NUMBER(10) | sim |  |
| CODPLPAG_CR | NUMBER(4) | sim |  |
| PLACA_VEICULO | VARCHAR2(7) | sim | SALVAR INFORMAÇÃO DE PLACA NA ROTINA 0028 PARA CONSULTA NAS ROTINAS DE CRECEBER |
| SITUACAO | VARCHAR2(12) | sim | Situação do Boleto retorno API PLUGBOLETO, que pode ser (SALVO, EMITIDO, FALHA, REGISTRADO, LIQUIDADO, REJEITADO e BAIXADO) |
| NOSSONUMERO_BOLETOAPI | VARCHAR2(25) | sim | Retorno do Nosso Número do Boleto na situação "REGISTRADO" API PLUG-BOLETO |
| LINHADIGITAVEL_BOLETOAPI | VARCHAR2(70) | sim | Linha Digitável do Boleto na situação "REGISTRADO" API PLUG-BOLETO |
| CODIGOBARRAS_BOLETOAPI | VARCHAR2(70) | sim | Código de Barras do Boleto na situação "REGISTRADO" API PLUG-BOLETO |
| MOTIVO_BOLETOAPI | VARCHAR2(400) | sim | Motivo é um campo onde vem da Consulta do Boleto que diz qual é o erro no envio da API, na situação "FALHA" API PLUG-BOLETO |
| STATUS_BOLETOAPI | VARCHAR2(300) | sim | STATUS Retorno da API, na situação "FALHA" API PLUG-BOLETO |
| IDINTEGRACAO_BOLETOAPI | VARCHAR2(50) | sim | STATUS Retorno da API, na situação "SALVO" API PLUG-BOLETO |
| NUMIMPRESSAO_BOLETOAPI | VARCHAR2(50) | sim | STATUS Retorno da API, na situação "REGISTRADO" API PLUG-BOLETO |
| PROTOCOLO_IMPBOLETOAPI | VARCHAR2(20) | sim | Ao final da solicitação do PDF será devolvido pela API um protocolo que pode ser utilizado para consultar as informações da solicitação |
| NUMENT | NUMBER(10) | sim | ENTRADA PELA736/701 QUE GEROU CONTAS A RECEBER |
| TP_FORNEC_ENT | VARCHAR2(1) | sim | CONTAS A RECEBER GERADO PARA O FORNECEDOR  (F) OU TRANSPORTADOR (T) |
| PROTOCOLO_BAIXABOLETOAPI | VARCHAR2(20) | sim | BOLETOS QUE SE DESEJA OBTER REMESSA DE BAIXA, APENAS NAS SITUAÇÕES: EMITIDO E REGISTRADO QUE PERMITEM A GERAÇÃO DA REMESSA |
| TITULOPAGO_API | VARCHAR2(1) | sim | CAMPO SERÁ DESTINADO PARA CHECAR/BAIXAR BOLETOS PELA API Cefas PlugBoleto |
| URL_BOLETO | VARCHAR2(200) | sim | Plug Boleto - URL_Boleto |
| NUM_LOCACAO | NUMBER(10) | sim | Numero da proposta de locacao |

### JP.NFSAID (1.016.570 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMNOTA | NUMBER(10) | sim |  |
| SERIE | VARCHAR2(3) | sim |  |
| ESPECIE | VARCHAR2(2) | sim |  |
| DTEMISSAO | DATE | sim |  |
| CODFISCAL | NUMBER(4) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| CODCLI | NUMBER(6) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| CODPLPAG | NUMBER(4) | sim |  |
| NUMCUPOM | NUMBER(10) | sim |  |
| TIPO | NUMBER(2) | sim |  |
| VLCUSTOREAL | NUMBER(12,2) | sim |  |
| VLCUSTOFIN | NUMBER(12,2) | sim |  |
| VLFRETE | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| VLTABELA | NUMBER(12,2) | sim |  |
| TOTPESO | NUMBER(12,2) | sim |  |
| NUMITENS | NUMBER(4) | sim |  |
| OBS | VARCHAR2(40) | sim |  |
| DTCANCEL | DATE | sim |  |
| CODFUNCANCEL | NUMBER(10) | sim |  |
| VLCANCEL | NUMBER(12,2) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| TOTVOLUME | NUMBER(12,2) | sim |  |
| DTSAIDA | DATE | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLST | NUMBER(12,2) | sim |  |
| VLCUSTOCONT | NUMBER(12,2) | sim |  |
| VLTOTCONT | NUMBER(12,2) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| CODPRACA | NUMBER(4) | sim |  |
| FRETEDESPACHO | VARCHAR2(1) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| DTDEVOL | DATE | sim |  |
| VLDEVOL | NUMBER(12,2) | sim |  |
| TIPOVENDA | VARCHAR2(2) | sim |  |
| VLICM | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(12,2) | sim |  |
| VLBASEICM | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| NUMVIAS | NUMBER(2) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| CODDEVOL | NUMBER(4) | sim |  |
| DTENTREGA | DATE | sim |  |
| VLISENTO | NUMBER(12,2) | sim |  |
| NFORIGEM | NUMBER(10) | sim |  |
| VLOUTRASDESP | NUMBER(12,2) | sim |  |
| CODSUPERVISOR | NUMBER(4) | sim |  |
| NUMCOMANDA | NUMBER(10) | sim |  |
| OBS2 | VARCHAR2(40) | sim |  |
| TOTPESOLIQ | NUMBER(12,2) | sim |  |
| CODFORNECTRANSP | NUMBER(6) | sim |  |
| SUBSERIE | VARCHAR2(1) | sim |  |
| CODFUNCVEND | NUMBER(10) | sim |  |
| NUMSERVICO | NUMBER(10) | sim |  |
| VLBASEISS | NUMBER(12,2) | sim |  |
| VLISS | NUMBER(12,2) | sim |  |
| VLDESCBRINDE | NUMBER(12,2) | sim |  |
| NFETPEMIS | VARCHAR2(2) | sim |  |
| DTSTATUS | DATE | sim |  |
| NFEPLACA | VARCHAR2(7) | sim |  |
| NFEUFPLACA | VARCHAR2(2) | sim |  |
| DTNFE | DATE | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| CSTATNFE | VARCHAR2(4) | sim |  |
| RECNFE | VARCHAR2(20) | sim |  |
| NPROTNFE | VARCHAR2(20) | sim |  |
| IDLOTE | VARCHAR2(15) | sim |  |
| MODONFE | VARCHAR2(20) | sim |  |
| DTIMPNFE | DATE | sim |  |
| NFDESTINO | NUMBER(10) | sim |  |
| ENDERENT | VARCHAR2(40) | sim |  |
| BAIRROENT | VARCHAR2(30) | sim |  |
| CIDADEENT | VARCHAR2(40) | sim |  |
| ESTADOENT | VARCHAR2(2) | sim |  |
| CEPENT | VARCHAR2(10) | sim |  |
| TELENT | VARCHAR2(15) | sim |  |
| IEENT | VARCHAR2(15) | sim |  |
| CPFCNPJ | VARCHAR2(18) | sim |  |
| VLDESCICM | NUMBER(12,2) | sim |  |
| VLDESCFIN | NUMBER(12,2) | sim |  |
| VLBASEPIS | NUMBER(12,2) | sim |  |
| VLPIS | NUMBER(12,2) | sim |  |
| VLBASECOFINS | NUMBER(12,2) | sim |  |
| VLCOFINS | NUMBER(12,2) | sim |  |
| ESPECIE2 | VARCHAR2(2) | sim |  |
| STATUS | VARCHAR2(200) | sim |  |
| IMPRESSA | VARCHAR2(3) | sim |  |
| NFE | VARCHAR2(60) | sim |  |
| MSGNFE | VARCHAR2(200) | sim |  |
| NFEQTDEVOL | VARCHAR2(10) | sim |  |
| NFEESPVOL | VARCHAR2(20) | sim |  |
| NFEMARCAVOL | VARCHAR2(30) | sim |  |
| NFEOBS | VARCHAR2(4000) | sim |  |
| NUMDOCIMPORT | NUMBER(15) | sim |  |
| DTREGIMPORT | DATE | sim |  |
| DESCDESEMBARACO | VARCHAR2(100) | sim |  |
| UFDESEMBARACO | VARCHAR2(2) | sim |  |
| DTDESEMBARACO | DATE | sim |  |
| CODEXPSISTINTERNO | NUMBER(10) | sim |  |
| NFEADIC | NUMBER(3) | sim |  |
| NFESEQ | NUMBER(3) | sim |  |
| NFEFABRIC | VARCHAR2(60) | sim |  |
| VLDESCIMPOSTO | NUMBER(12,2) | sim |  |
| ANTT | VARCHAR2(20) | sim |  |
| VLCOMSUP | NUMBER(12,2) | sim |  |
| DTIMPCUPOM | DATE | sim |  |
| DATACONT | VARCHAR2(254) | sim |  |
| JUSTCONT | VARCHAR2(254) | sim |  |
| NFECHAVECONT | VARCHAR2(254) | sim |  |
| NFEUFEMBARQ | VARCHAR2(2) | sim |  |
| NFELOCEMBARQ | VARCHAR2(40) | sim |  |
| CCF | NUMBER(6) | sim |  |
| GNF | NUMBER(6) | sim |  |
| ENTNUMNFPROP | VARCHAR2(1) | sim |  |
| NFSERVICO | VARCHAR2(1) | sim |  |
| VLCANCELPARC | NUMBER(12,2) | sim |  |
| VLSEGURO | NUMBER(12,2) | sim |  |
| EMBALAGEMREGIAO | VARCHAR2(1) | sim |  |
| VLINSS | NUMBER(12,2) | sim |  |
| VLIR | NUMBER(12,2) | sim |  |
| VLCSLL | NUMBER(12,2) | sim |  |
| ORIGEM | VARCHAR2(4) | sim |  |
| CODPARIND | NUMBER(6) | sim |  |
| OBSCCE | VARCHAR2(4000) | sim |  |
| CSTATCCE | VARCHAR2(3) | sim |  |
| NPROTCCE | VARCHAR2(20) | sim |  |
| CPFCNPJCAT52 | VARCHAR2(14) | sim |  |
| VFCPUFDEST | NUMBER(12,2) | sim |  |
| VICMSUFDEST | NUMBER(12,2) | sim |  |
| VICMSUFREMET | NUMBER(12,2) | sim |  |
| CHAVEREFCOMP | VARCHAR2(60) | sim |  |
| DTACERTO | DATE | sim |  |
| OBSACERTO | VARCHAR2(80) | sim |  |
| CODFUNCACERTO | NUMBER(6) | sim |  |
| INDPRES | VARCHAR2(1) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| CSTCREDITOICMS | VARCHAR2(2) | sim |  |
| VLFCP | NUMBER(12,2) | sim |  |
| VLFCPST | NUMBER(12,2) | sim |  |
| VLFCPSTRET | NUMBER(12,2) | sim |  |
| USAMFE | CHAR(1) | sim |  |
| NFGARANTIA | VARCHAR2(1) | sim |  |
| VLBASEICMGARANTIA | NUMBER(12,2) | sim |  |
| VLICMGARANTIA | NUMBER(12,2) | sim |  |
| VLBASESTGARANTIA | NUMBER(12,2) | sim |  |
| VLSTGARANTIA | NUMBER(12,2) | sim |  |
| VLBASEIPIGARANTIA | NUMBER(12,2) | sim |  |
| VLIPIGARANTIA | NUMBER(12,2) | sim |  |
| VLBASEFCP | NUMBER(12,2) | sim |  |
| VLBASEFCPST | NUMBER(12,2) | sim |  |
| VLBASEFCPSTRET | NUMBER(12,2) | sim |  |
| CODFUNCF11LIB | NUMBER(10) | sim |  |
| CSTATNFEAUX | VARCHAR2(4) | sim |  |
| CODATEND1 | NUMBER(10) | sim |  |
| CODATEND2 | NUMBER(10) | sim |  |
| CODATEND3 | NUMBER(10) | sim |  |
| CODATEND4 | NUMBER(10) | sim |  |
| DUPLICOUTP12 | VARCHAR2(1) | sim |  |
| NFDESTINOCODCLI | NUMBER(10) | sim |  |
| XMLPDFENVIADO | VARCHAR2(1) | sim |  |
| VLICMSDES | NUMBER(12,2) | sim |  |
| TIPOCREDITOICMS | VARCHAR2(13) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| USADEVOLTRANSF | VARCHAR2(1) | sim |  |
| VLICMDIF | NUMBER(12,2) | sim |  |
| CPFCNPJSAID | VARCHAR2(18) | sim |  |
| DIFEMBREGIAO | VARCHAR2(1) | sim |  |
| VLFRETEPAGO | NUMBER(12,2) | sim |  |
| SAIDAAVARIA | VARCHAR2(1) | sim |  |
| SRSIMPLESFATURA | VARCHAR2(1) | sim |  |
| NUMLANCCPAGARDESCFIN | NUMBER(10) | sim |  |
| VLBONIFICACAO | NUMBER(12,2) | sim |  |
| FRETEBONIF | NUMBER(12,2) | sim |  |
| VLFRETECOTADO | NUMBER(12,2) | sim |  |
| CSOSN_CREDITOICMS | NUMBER(3) | sim |  |
| VLCREDUSADO | NUMBER(12,2) | sim |  |
| NCONTRATOCONSIG | NUMBER(10) | sim |  |
| VERSAOROTINA | VARCHAR2(20) | sim |  |
| CNPJINTERMEDIADOR | VARCHAR2(14) | sim |  |
| INTERMEDIADOR | VARCHAR2(60) | sim |  |
| NFTERCEIRO | VARCHAR2(1) | sim |  |
| CODIGOSTATUS_SCANNTECH | NUMBER(5) | sim |  |
| STATUSENVIO_SCANNTECH | VARCHAR2(1) | sim |  |
| VLDESCONTOSCANNTECH | NUMBER(12,2) | sim |  |
| STATUSENVIOCANCEL_SCANNTECH | VARCHAR2(1) | sim |  |
| VLTOT_OUT_TAXAS | NUMBER(12,2) | sim |  |
| FINALIDADENFE | VARCHAR2(14) | sim |  |
| CODHIST | NUMBER(6) | sim |  |
| VLBASEIRRF | NUMBER(12,2) | sim | GRAVA O VALOR DE BASE DE IMPOSTO DE RENDA RETIDO IRRF, FAZ REFERENCIA AOS CAMPOS FILIAL.DESTACAIRRFDANFE, FILIAL.PERALIQIRPJ E CLIENTE.CLIORGPUBLICO |
| VLIRRF | NUMBER(12,2) | sim | GRAVA O VALOR DE IMPOSTO DE RENDA RETIDO IRRF, FAZ REFERENCIA AOS CAMPOS NFSAID.VLBASEIRRF, FILIAL.DESTACAIRRFDANFE, FILIAL.PERALIQIRPJ E CLIENTE.CLIORGPUBLICO |
| TRANSPORTE | VARCHAR2(4) | sim | PROCESSO DE ESTIVA SALVA TIPO DO    TRANSPORTE: TE-TERCEIRIZADO EXTERNO TL ¿TERCEIRO LOCAL I-ISENTO |
| ESTORNO_QTINDENIZ | VARCHAR2(1) | sim | ESTE CAMPO IRÁ DETERMINAR NO MOMENTO DO CANCEL. DA NF-E, SE FOR (S) IRÁ VOLTAR PARA ESTOQUE.QTINDENIZ |
| NUMCOTACAO | NUMBER(12) | sim | CAMPO ALIMENTADO R.56 ABA F7 |
| DTENTREGA_RAP | DATE | sim | AO CONFIRNAR A ENTREGA NA RT 530 GRAVAR DATA DA ENTREGA |
| CODFUNCENTREGA_RAP | NUMBER(10) | sim | AO CONFIRMAR A ENTREGA NA RT 530 GRAVAR CODFUNC QUE REALIZOU A CONFIRMACAO |
| VLBONIFICACAO2 | NUMBER(12,2) | sim | VALOR DO BONIFICACAO2 SOMADO NO DESCONTO DO ITEM |
| VLBONIFICACAO3 | NUMBER(12,2) | sim | VALOR DO BONIFICACAO3 SOMADO NO DESCONTO DO ITEM |
| NPS | NUMBER(5) | sim | USADO PARA RECEBER A PONTUAÇÃO DA AVALIAÇÃO DE ATENDIMENTO NOS PDVS ATRAVES DO PINPAD |
| VICMSMONORET | NUMBER(12,2) | sim | Valor AD REM do ICMS para o produto CST=61 |
| DTCONFERIDO | DATE | sim |  |
| CSTATCVENDA | NUMBER(3) | sim | INTEGRACAO CRESCE VENDAS - RECEBE O STATUS DA VENDA COM A API |
| CSTATCVDESC | VARCHAR2(254) | sim | INTEGRACAO CRESCE VENDAS - RECEBE A DESCRICAO DO STATUS |
| ENVIOUCRVENDAS | VARCHAR2(1) | sim | INTEGRACAO CRESCE VENDAS - EXIBE SE A VENDA FOI ENVIADA PARA API |
| USACRVENDA | VARCHAR2(1) | sim | INTEGRACAO CRESCE VENDAS - DEFINE O USO DA INTEGRACAO |
| VLDESCONTOCRVENDAS | NUMBER(12,2) | sim | INTEGRACAO CRESCE VENDAS - RECEBE O DESCONTO CRESCE VENDAS |
| VLDESCONTOSUBTOTCRVENDAS | NUMBER(12,2) | sim | INTEGRACAO CRESCE VENDAS - RECEBE O DESCONTO SUBTOTAL |
| APLICAVLDESCSUBTOTCRVENDAS | VARCHAR2(1) | sim | INTEGRACAO CRESCE VENDAS - DEFINE O USO DO DESCONTO SUBTOTAL |
| ID_MARKET | VARCHAR2(80) | sim | id do pedido no Plug4Market |
| CODFUNCLIB_LIM | NUMBER(10) | sim | CODIGO DO FISCAL QUE LIBEROU VENDA ACIMA DO VALOR DE LIMINTE DISPONIVEL |
| TOT_VBC_IBSCBS | NUMBER(12,2) | sim | Valor total do IBS da UF. Recebe (MOV.VLBC_IBSCBS) |
| TOT_VIBSUF | NUMBER(12,2) | sim | Valor total do IBS da UF. Recebe (MOV.VTRIBOP_IBS_UF) |
| TOT_VIBSMUN | NUMBER(12,2) | sim | Valor total do IBS do Municipio. Recebe (MOV.VTRIBOP_IBS_MUN) |
| TOT_VCBS | NUMBER(12,2) | sim | Valor total do CBS. Recebe (MOV.VTRIBOP_CBS) |
| TOT_DIF_IBS_UF | NUMBER(12,2) | sim | Valor Total do diferimento IBS |
| TOT_DIF_CBS | NUMBER(12,2) | sim |  Valor Total do diferimento CBS |
| TOT_DIF_IBS_MUN | NUMBER(12,2) | sim |  Valor Total do diferimento IBS/MUNICIPAL |
| VLPONTUACAOFILIAL | NUMBER(12,2) | sim | Valor origem de referencia usado no processo de pontuação |
| PERC_CREDITO_PONTOS_FILIAL | NUMBER(5,2) | sim | Percentual de credito origem de referencia usado no processo de pontuação |
| NUMLANCCREDITOPONTUACAO | NUMBER(10) | sim | Numero de lancamento origem para referencia de credito de pontuação |
| TIPO_NFDEBITO | VARCHAR2(2) | sim | Tipo de Nota de Débito "06 - Pagamento Antecipado" |
| FINNFE | VARCHAR2(1) | sim | Finalidade de emissão da NF-e "6 - Nota de Débito" |
| CHAVEREF_NFEDEBITO | VARCHAR2(60) | sim | Chave da NF-e que foi feito NF-e Débito |
| NUMVENDAREF_NFEDEBITO | NUMBER(10) | sim | Numvenda da NF-e que foi feito NF-e Débito |
| TOT_ESTCRED_IBS | NUMBER(12,2) | sim | Total do Estorno de Crédito do IBS do grupo <gEstornoCred> |
| TOT_ESTCRED_CBS | NUMBER(12,2) | sim | Total do Estorno de Crédito do CBS do grupo <gEstornoCred> |
| USADEVOLREMESSA | VARCHAR2(1) | sim | DEFINIR DEVOLUCAO DE REMESSA ROTINA89 |
| NUM_LOCACAO | NUMBER(10) | sim | Numero da proposta de locacao |

### VAREJO.ITEMPED (1.000.627 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMPED | NUMBER(10) | não |  |
| CODPROD | NUMBER(10) | não |  |
| QTPEDIDA | NUMBER(12,3) | sim |  |
| PTABELA | NUMBER(24,8) | sim |  |
| PVENDA | NUMBER(24,8) | sim |  |
| VLCUSTOREAL | NUMBER(18,6) | sim |  |
| PERICM | NUMBER(5,2) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| ST | NUMBER(18,6) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| CODFISCALITEM | NUMBER(4) | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLBASEICM | NUMBER(12,2) | sim |  |
| VLICM | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(18,6) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| VLCUSTOFIN | NUMBER(18,6) | sim |  |
| SEQ | NUMBER(4) | não |  |
| CODFILIALRETIRA | VARCHAR2(2) | sim |  |
| QTFALTA | NUMBER(12,3) | sim |  |
| VLCUSTOCONT | NUMBER(18,6) | sim |  |
| OBS | VARCHAR2(40) | sim |  |
| NUMLOTE | VARCHAR2(20) | sim |  |
| DTFAB | DATE | sim |  |
| DTVENC | DATE | sim |  |
| QTPEDIDAPCA | NUMBER(12,3) | sim |  |
| CODFUNCLIB2 | NUMBER(10) | sim |  |
| CODFUNCLIB3 | NUMBER(10) | sim |  |
| AVARIA | VARCHAR2(1) | sim |  |
| CODBARRA | NUMBER(14) | sim |  |
| TPENTREGAITEM | VARCHAR2(1) | sim |  |
| CODFUNCENTREG | NUMBER(10) | sim |  |
| DTENTREG | DATE | sim |  |
| SERIGRAFIA | VARCHAR2(20) | sim |  |
| BORDADO | VARCHAR2(20) | sim |  |
| OBSERVACAO | VARCHAR2(40) | sim |  |
| PVENDAORIG | NUMBER(24,8) | sim |  |
| DESCALT | VARCHAR2(120) | sim |  |
| EXIBIRITEM | VARCHAR2(1) | sim |  |
| VLDEBCREDRCA | NUMBER(18,6) | sim |  |
| LARGURA | NUMBER(18,6) | sim |  |
| ALTURA | NUMBER(18,6) | sim |  |
| QTORIG | NUMBER(13,3) | sim |  |
| UNORIG | VARCHAR2(3) | sim |  |
| OBSADIC | VARCHAR2(400) | sim |  |
| EMBALAGEMORIG | VARCHAR2(12) | sim |  |
| QTVALE | NUMBER(12,3) | sim |  |
| QTBAIXAVALE | NUMBER(12,3) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| PVENDAST | NUMBER(18,6) | sim |  |
| VLFRETE | NUMBER(18,6) | sim |  |
| VLOUTRASDESP | NUMBER(18,6) | sim |  |
| VLDESCONTO | NUMBER(18,6) | sim |  |
| VLSEGURO | NUMBER(18,6) | sim |  |
| PRECOCLIENTE | NUMBER(18,6) | sim |  |
| QTORIGPOL | NUMBER(13,3) | sim |  |
| PVENDAEMB | NUMBER(18,6) | sim |  |
| QTENTREGA | NUMBER(12,2) | sim |  |
| QTALTERADA | NUMBER(10,2) | sim |  |
| DT_ALTERACAO | DATE | sim |  |
| CODALTERADOR | NUMBER(10) | sim |  |
| QT_ATUAL_ENTREGA | NUMBER(10,2) | sim |  |
| STATUSENT | VARCHAR2(1) | sim |  |
| STORIG | NUMBER(18,6) | sim |  |
| VLIPIORIG | NUMBER(18,6) | sim |  |
| QTUNITCX | NUMBER(18,6) | sim |  |
| PESOORIG | NUMBER(12,3) | sim |  |
| PESOAJUST | NUMBER(12,3) | sim |  |
| VLDESCONTOICMS | NUMBER(18,6) | sim |  |
| USAFATORMASTER | VARCHAR2(1) | sim |  |
| VLSTPI | NUMBER(18,6) | sim |  |
| CODFILIAL | VARCHAR2(255) | sim |  |
| QTPEDIDO | FLOAT | sim |  |
| PEDIDOITEMVLTABELA | FLOAT | sim |  |
| VLTABELA | FLOAT | sim |  |
| QTDEBANDEJA | NUMBER(18,6) | sim |  |
| VLFCPST | NUMBER(24,8) | sim |  |
| NITEMPED | VARCHAR2(6) | sim |  |
| XPED | VARCHAR2(15) | sim |  |
| FCPSTORIG | NUMBER(24,8) | sim |  |
| OBSITEM | VARCHAR2(500) | sim |  |
| QTPEDIDAORIG | NUMBER(12,3) | sim |  |
| NUMCORTE | NUMBER(10) | sim |  |
| PRODUTOFERTA | VARCHAR2(1) | sim |  |
| VLICMSDES | NUMBER(24,8) | sim |  |
| GERARSALDOFLEXVENDA | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO2 | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO3 | VARCHAR2(1) | sim |  |
| BASE_VERBAFLEX_PERDESCINI | NUMBER(5,2) | sim |  |
| BASE_VERBAFLEX_PERDESCFINAL | NUMBER(5,2) | sim |  |
| VLVERBAFLEX_CREDITO | NUMBER(12,2) | sim |  |
| VLVERBAFLEX_DEBITO | NUMBER(12,2) | sim |  |
| USAVERBAFLEX_CREDITO | VARCHAR2(1) | sim |  |
| USAVERBAFLEX_DEBITO | VARCHAR2(1) | sim |  |
| NUMENTENTRADACIAP | NUMBER(10) | sim |  |
| VLCIAP | NUMBER(24,8) | sim |  |
| QTMOFADOSTP17 | NUMBER(8) | sim |  |
| QTVENCIDOSTP17 | NUMBER(8) | sim |  |
| MOTIVOMOFVENCTP17 | VARCHAR2(1000) | sim |  |
| USADESCSUPERVISORFV | VARCHAR2(1) | sim |  |
| QTDEENTAGORA | NUMBER(12,3) | sim |  |
| QTDEAGENDAR | NUMBER(12,3) | sim |  |
| QTDESEMAGENDA | NUMBER(12,3) | sim |  |
| DTPREVENT | DATE | sim |  |
| QTDEVOLSEP | NUMBER(12,3) | sim |  |
| VL_OUT_TAXAS | NUMBER(24,8) | sim |  |
| QTDEENTREGA | NUMBER(12,3) | sim |  |
| UTQTMAXOFERTA | VARCHAR2(1) | sim | CAMPO PARA MARCAR SE ABATEU QTDE MAXIMA NA VENDA DE PRODUTO COM PRECO DE OFERTA |
| QTDESEPARADA | NUMBER(12,3) | sim | SALVA QUANTIDADE SEPARADA DA ROTINA 544 |
| VICMSMONORET | NUMBER(18,6) | sim | Valor AD REM do ICMS para o produto CST=61 |
| PERADREM_ICMSRET | NUMBER(5,4) | sim | Valor AD REM do ICMS para o produto CST=61 |
| QTTRANSF_532 | NUMBER(12,3) | sim | SALVAR QUANTIDADE TRANSFERIDA ALTERADA A FILIAL ROTINA 530 |
| ITEMCOMBO | VARCHAR2(1) | sim | SALVAR S ITEM CORRESPONDE AO PROCESSO DO COMBO ROTINA 1759 |
| NUMPEDORC | NUMBER(10) | sim |  |

### VAREJO.NUMNOTA (1.000.000 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMNOTA | NUMBER(20) | não |  |

### JP.NUMNOTA (1.000.000 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMNOTA | NUMBER(20) | não |  |

### BOLOS.NUMNOTA (1.000.000 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMNOTA | NUMBER(20) | não |  |

### JP.ITEMPED (998.053 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMPED | NUMBER(10) | não |  |
| CODPROD | NUMBER(10) | não |  |
| QTPEDIDA | NUMBER(12,3) | sim |  |
| PTABELA | NUMBER(24,8) | sim |  |
| PVENDA | NUMBER(24,8) | sim |  |
| VLCUSTOREAL | NUMBER(18,6) | sim |  |
| PERICM | NUMBER(5,2) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| ST | NUMBER(18,6) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| CODFISCALITEM | NUMBER(4) | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLBASEICM | NUMBER(12,2) | sim |  |
| VLICM | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(24,8) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| VLCUSTOFIN | NUMBER(18,6) | sim |  |
| SEQ | NUMBER(4) | não |  |
| CODFILIALRETIRA | VARCHAR2(2) | sim |  |
| QTFALTA | NUMBER(12,3) | sim |  |
| VLCUSTOCONT | NUMBER(18,6) | sim |  |
| OBS | VARCHAR2(40) | sim |  |
| NUMLOTE | VARCHAR2(20) | sim |  |
| DTFAB | DATE | sim |  |
| DTVENC | DATE | sim |  |
| QTPEDIDAPCA | NUMBER(12,3) | sim |  |
| CODFUNCLIB2 | NUMBER(10) | sim |  |
| CODFUNCLIB3 | NUMBER(10) | sim |  |
| AVARIA | VARCHAR2(1) | sim |  |
| CODBARRA | NUMBER(14) | sim |  |
| TPENTREGAITEM | VARCHAR2(1) | sim |  |
| CODFUNCENTREG | NUMBER(10) | sim |  |
| DTENTREG | DATE | sim |  |
| SERIGRAFIA | VARCHAR2(20) | sim |  |
| BORDADO | VARCHAR2(20) | sim |  |
| OBSERVACAO | VARCHAR2(40) | sim |  |
| PVENDAORIG | NUMBER(24,8) | sim |  |
| DESCALT | VARCHAR2(120) | sim |  |
| EXIBIRITEM | VARCHAR2(1) | sim |  |
| VLDEBCREDRCA | NUMBER(18,6) | sim |  |
| LARGURA | NUMBER(18,6) | sim |  |
| ALTURA | NUMBER(18,6) | sim |  |
| QTORIG | NUMBER(13,3) | sim |  |
| UNORIG | VARCHAR2(3) | sim |  |
| OBSADIC | VARCHAR2(400) | sim |  |
| EMBALAGEMORIG | VARCHAR2(12) | sim |  |
| QTVALE | NUMBER(12,3) | sim |  |
| QTBAIXAVALE | NUMBER(12,3) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| PVENDAST | NUMBER(18,6) | sim |  |
| VLFRETE | NUMBER(18,6) | sim |  |
| VLOUTRASDESP | NUMBER(18,6) | sim |  |
| VLDESCONTO | NUMBER(18,6) | sim |  |
| VLSEGURO | NUMBER(18,6) | sim |  |
| PRECOCLIENTE | NUMBER(18,6) | sim |  |
| QTORIGPOL | NUMBER(13,3) | sim |  |
| PVENDAEMB | NUMBER(18,6) | sim |  |
| QTENTREGA | NUMBER(12,2) | sim |  |
| QTALTERADA | NUMBER(10,2) | sim |  |
| DT_ALTERACAO | DATE | sim |  |
| CODALTERADOR | NUMBER(10) | sim |  |
| QT_ATUAL_ENTREGA | NUMBER(10,2) | sim |  |
| STATUSENT | VARCHAR2(1) | sim |  |
| STORIG | NUMBER(18,6) | sim |  |
| VLIPIORIG | NUMBER(24,8) | sim |  |
| QTUNITCX | NUMBER(18,6) | sim |  |
| PESOORIG | NUMBER(12,3) | sim |  |
| PESOAJUST | NUMBER(12,3) | sim |  |
| VLDESCONTOICMS | NUMBER(18,6) | sim |  |
| USAFATORMASTER | VARCHAR2(1) | sim |  |
| VLSTPI | NUMBER(18,6) | sim |  |
| CODFILIAL | VARCHAR2(255) | sim |  |
| QTPEDIDO | FLOAT | sim |  |
| PEDIDOITEMVLTABELA | FLOAT | sim |  |
| VLTABELA | FLOAT | sim |  |
| QTDEBANDEJA | NUMBER(18,6) | sim |  |
| VLFCPST | NUMBER(24,8) | sim |  |
| NITEMPED | VARCHAR2(6) | sim |  |
| XPED | VARCHAR2(15) | sim |  |
| FCPSTORIG | NUMBER(24,8) | sim |  |
| OBSITEM | VARCHAR2(500) | sim |  |
| QTPEDIDAORIG | NUMBER(12,3) | sim |  |
| NUMCORTE | NUMBER(10) | sim |  |
| PRODUTOFERTA | VARCHAR2(1) | sim |  |
| VLICMSDES | NUMBER(24,8) | sim |  |
| GERARSALDOFLEXVENDA | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO2 | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO3 | VARCHAR2(1) | sim |  |
| BASE_VERBAFLEX_PERDESCINI | NUMBER(5,2) | sim |  |
| BASE_VERBAFLEX_PERDESCFINAL | NUMBER(5,2) | sim |  |
| VLVERBAFLEX_CREDITO | NUMBER(12,2) | sim |  |
| VLVERBAFLEX_DEBITO | NUMBER(12,2) | sim |  |
| USAVERBAFLEX_CREDITO | VARCHAR2(1) | sim |  |
| USAVERBAFLEX_DEBITO | VARCHAR2(1) | sim |  |
| NUMENTENTRADACIAP | NUMBER(10) | sim |  |
| VLCIAP | NUMBER(24,8) | sim |  |
| QTMOFADOSTP17 | NUMBER(8) | sim |  |
| QTVENCIDOSTP17 | NUMBER(8) | sim |  |
| MOTIVOMOFVENCTP17 | VARCHAR2(1000) | sim |  |
| USADESCSUPERVISORFV | VARCHAR2(1) | sim |  |
| QTDEENTAGORA | NUMBER(12,3) | sim |  |
| QTDEAGENDAR | NUMBER(12,3) | sim |  |
| QTDESEMAGENDA | NUMBER(12,3) | sim |  |
| DTPREVENT | DATE | sim |  |
| QTDEVOLSEP | NUMBER(12,3) | sim |  |
| VL_OUT_TAXAS | NUMBER(24,8) | sim |  |
| QTDEENTREGA | NUMBER(12,3) | sim |  |
| UTQTMAXOFERTA | VARCHAR2(1) | sim | CAMPO PARA MARCAR SE ABATEU QTDE MAXIMA NA VENDA DE PRODUTO COM PRECO DE OFERTA |
| QTDESEPARADA | NUMBER(12,3) | sim | SALVA QUANTIDADE SEPARADA DA ROTINA 544 |
| VICMSMONORET | NUMBER(18,6) | sim | Valor AD REM do ICMS para o produto CST=61 |
| PERADREM_ICMSRET | NUMBER(5,4) | sim | Valor AD REM do ICMS para o produto CST=61 |
| QTTRANSF_532 | NUMBER(12,3) | sim | SALVAR QUANTIDADE TRANSFERIDA ALTERADA A FILIAL ROTINA 530 |
| ITEMCOMBO | VARCHAR2(1) | sim | SALVAR S ITEM CORRESPONDE AO PROCESSO DO COMBO ROTINA 1759 |
| NUMPEDORC | NUMBER(10) | sim |  |
| QTPECAS | NUMBER(18,6) | sim | Informar a quantidade de peças referente a quantidade de KG que esta lançando R.56/156 |
| PROD_PLANEJADO | VARCHAR2(1) | sim | Produto planejado  |
| PERIPI_OVERRIDE | NUMBER(5,2) | sim | Ipi Adicionado na R.56 e R.156 |
| FV_ISENCAO_MOTIVO | VARCHAR2(20) | sim | Cefas Flow Vendas: motivo pelo qual o item nao movimenta saldo flex/verba. OFERTA, DESCQTDE, COMBO, BRINDE, PRECOESPECIAL, VIP, AVARIA (isencoes definitivas) ou ORCAMENTO (tipo 3, convertido em movimentacao na promocao). NULL = item normal. |

### VAREJOANTIGO.NFBASE (770.122 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMENT | NUMBER(10) | não |  |
| CODCONT | NUMBER(10) | não |  |
| VLBASE | NUMBER(12,2) | sim |  |
| PERICM | NUMBER(5,2) | não |  |
| VLICM | NUMBER(12,2) | sim |  |
| CODFISCAL | NUMBER(4) | não |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLST | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(12,2) | sim |  |
| VLISENTO | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| VLBASEPIS | NUMBER(12,2) | sim |  |
| VLBASECOFINS | NUMBER(12,2) | sim |  |
| VLPIS | NUMBER(12,2) | sim |  |
| VLCOFINS | NUMBER(12,2) | sim |  |
| PERPIS | NUMBER(8,6) | sim |  |
| PERCOFINS | NUMBER(8,6) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| VLFCPST | NUMBER(12,2) | sim |  |
| VLBASEFCPST | NUMBER(12,2) | sim |  |
| CSTCREDITOICMS | VARCHAR2(2) | sim |  |
| CSOSN_CREDITOICMS | NUMBER(3) | sim |  |

### VAREJO.CRECEBER (655.338 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMNOTA | NUMBER(10) | sim |  |
| PREST | NUMBER(3) | não |  |
| CODCLI | NUMBER(6) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| DTEMISSAO | DATE | sim |  |
| DTVENC | DATE | sim |  |
| VALOR | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLJURO | NUMBER(12,2) | sim |  |
| DTPAGO | DATE | sim |  |
| VPAGO | NUMBER(12,2) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| NUMBCO | VARCHAR2(4) | sim |  |
| NUMAG | VARCHAR2(4) | sim |  |
| NUMCH | VARCHAR2(8) | sim |  |
| NUMCART | VARCHAR2(15) | sim |  |
| DTFECHA | DATE | sim |  |
| OBS | VARCHAR2(2000) | sim |  |
| CODCXBCO | NUMBER(4) | sim |  |
| CODFUNCFECHA | NUMBER(10) | sim |  |
| DTBAIXA | DATE | sim |  |
| NUMCONTA | VARCHAR2(15) | sim |  |
| CODCXBCOP | NUMBER(4) | sim |  |
| VLAUX | NUMBER(12,2) | sim |  |
| TOTPREST | NUMBER(3) | sim |  |
| DTULTALT | DATE | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| PERCOM | NUMBER(7,4) | sim |  |
| NOSSNUMBCO | VARCHAR2(14) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| DTDESD | DATE | sim |  |
| CODFUNCDESD | NUMBER(10) | sim |  |
| CODFUNCBAIXA | NUMBER(10) | sim |  |
| VALORDEV | NUMBER(12,2) | sim |  |
| OBS2 | VARCHAR2(100) | sim |  |
| NUMLANCPG | NUMBER(10) | sim |  |
| NOSSONUMBCO | VARCHAR2(20) | sim |  |
| CODBARRA | VARCHAR2(44) | sim |  |
| LINHADIG | VARCHAR2(65) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| VLTXBOLETO | NUMBER(12,2) | sim |  |
| STATUS | VARCHAR2(1) | sim |  |
| VALORORIG | NUMBER(12,2) | sim |  |
| PROTOCOLO | NUMBER(10) | sim |  |
| TURNO | VARCHAR2(1) | sim |  |
| DTVENCORIG | DATE | sim |  |
| CODCOBORIG | VARCHAR2(4) | sim |  |
| CODSUPERVISOR | NUMBER(4) | sim |  |
| PR | VARCHAR2(2) | sim |  |
| DTULTALTER | DATE | sim |  |
| DTCXMOT | DATE | sim |  |
| CODFUNCCXMOT | NUMBER(10) | sim |  |
| NUMTRANS | NUMBER(10) | sim |  |
| CODCOBCXBCO | VARCHAR2(4) | sim |  |
| CODFUNCVALE | NUMBER(10) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| OPERACAO | VARCHAR2(1) | sim |  |
| CODBAIXA | NUMBER(4) | sim |  |
| ALINEA | VARCHAR2(4) | sim |  |
| NUMVENDADESD | NUMBER(10) | sim |  |
| NUMFATURA | NUMBER(10) | sim |  |
| DTFECHAPROT | DATE | sim |  |
| DTCXMOTPROT | DATE | sim |  |
| CODFUNCFECHAPROT | NUMBER(10) | sim |  |
| TIPOPRORROG | VARCHAR2(1) | sim |  |
| DTPRORROG | DATE | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| NUMCUSTODIA | NUMBER(8) | sim |  |
| DTCUSTODIA | DATE | sim |  |
| CODCXBCOCUSTODIA | NUMBER(4) | sim |  |
| DTPREVPAGTO | DATE | sim |  |
| PRESTDESD | NUMBER(3) | sim |  |
| DTESTORNO | DATE | sim |  |
| CODFUNCESTORNO | NUMBER(10) | sim |  |
| DIGITAO | VARCHAR2(1) | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| LIBERARVENDALIMCRED | VARCHAR2(1) | sim |  |
| RETBOLTIPOREG | NUMBER(2) | sim |  |
| RETBOLCODINSC | NUMBER(3) | sim |  |
| RETBOLNUMINSC | NUMBER(20) | sim |  |
| RETBOLAGENCIA | NUMBER(6) | sim |  |
| RETBOLCONTA | NUMBER(10) | sim |  |
| RETBOLDAC | VARCHAR2(1) | sim |  |
| RETBOLCODOCORRENCIA | NUMBER(4) | sim |  |
| RETBOLDTOCORRENCIA | DATE | sim |  |
| RETBOLNOSSONUMCONF | NUMBER(15) | sim |  |
| RETBOLDTVENCIMENTO | DATE | sim |  |
| RETBOLVALORTITULO | NUMBER(15,2) | sim |  |
| RETBOLCODBCO | NUMBER(4) | sim |  |
| RETBOLAGCOB | NUMBER(6) | sim |  |
| RETBOLDACAGCOB | VARCHAR2(1) | sim |  |
| RETBOLESPECIE | NUMBER(3) | sim |  |
| RETBOLTARIFACOB | NUMBER(15,2) | sim |  |
| RETBOLVALORIOF | NUMBER(15,2) | sim |  |
| RETBOLVALORABAT | NUMBER(15,2) | sim |  |
| RETBOLDESCONTOS | NUMBER(15,2) | sim |  |
| RETBOLVALORPRINC | NUMBER(15,2) | sim |  |
| RETBOLJUROSMORAMULTA | NUMBER(15,2) | sim |  |
| RETBOLOUTROSCREDITOS | NUMBER(15,2) | sim |  |
| RETBOLDTCREDITO | DATE | sim |  |
| RETBOLINSTRCANCEL | NUMBER(6) | sim |  |
| RETBOLNOMESACADO | VARCHAR2(40) | sim |  |
| RETBOLERROS | VARCHAR2(115) | sim |  |
| RETBOLCODLIQ | VARCHAR2(4) | sim |  |
| RETBOLNUMSEQ | NUMBER(10) | sim |  |
| RETBOLBAIXADO | VARCHAR2(1) | sim |  |
| RETBOLDVAG | VARCHAR2(3) | sim |  |
| DTFECHACHECKOUT | DATE | sim |  |
| VLDESCICMPARC | NUMBER(12,2) | sim |  |
| VLDESCFIN | NUMBER(12,2) | sim |  |
| DTTRANSMISSAO | DATE | sim |  |
| PERCOMSUP | NUMBER(7,4) | sim |  |
| VLDESCTXCAR | NUMBER(12,2) | sim |  |
| NUMPROM | VARCHAR2(20) | sim |  |
| TAXA | NUMBER(12,2) | sim |  |
| CODEMITENTE | NUMBER(10) | sim |  |
| BANDEIRA | VARCHAR2(60) | sim |  |
| TIPO_TRANSACAO | VARCHAR2(15) | sim |  |
| NSU | VARCHAR2(30) | sim |  |
| AUTORIZACAO | VARCHAR2(20) | sim |  |
| ESTABELECIMENTO | VARCHAR2(20) | sim |  |
| NUMEROCARTAO | VARCHAR2(30) | sim |  |
| ORIGEM | VARCHAR2(10) | sim |  |
| MODOBAIXA | VARCHAR2(1) | sim |  |
| DTBAIXACAR | DATE | sim |  |
| TRANSBAIXAAUTO | NUMBER(15) | sim |  |
| PRESTCAR | NUMBER(3) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| LANCR28 | VARCHAR2(1) | sim |  |
| TECLACOB | VARCHAR2(6) | sim |  |
| NUMTRANSMISSAO | NUMBER(14) | sim |  |
| VLMULTA | NUMBER(12,2) | sim |  |
| PDFENVIADO | VARCHAR2(1) | sim |  |
| CODVEND2 | NUMBER(10) | sim |  |
| DTFECHAR185 | DATE | sim |  |
| DESCDEV | NUMBER(12,2) | sim |  |
| AAA | VARCHAR2(1) | sim |  |
| VLTARIFA | NUMBER(12,2) | sim |  |
| DTPAGODESCONTO | DATE | sim |  |
| DTESTORNODESCONTO | DATE | sim |  |
| VPAGODESCONTO | NUMBER(12,2) | sim |  |
| CODFUNCPAGODESCONTO | NUMBER(10) | sim |  |
| CODFUNCESTORNODESCONTO | NUMBER(10) | sim |  |
| CODPLPAG_CR | NUMBER(4) | sim |  |
| PLACA_VEICULO | VARCHAR2(7) | sim | SALVAR INFORMAÇÃO DE PLACA NA ROTINA 0028 PARA CONSULTA NAS ROTINAS DE CRECEBER |
| SITUACAO | VARCHAR2(12) | sim | Situação do Boleto retorno API PLUGBOLETO, que pode ser (SALVO, EMITIDO, FALHA, REGISTRADO, LIQUIDADO, REJEITADO e BAIXADO) |
| NOSSONUMERO_BOLETOAPI | VARCHAR2(25) | sim | Retorno do Nosso Número do Boleto na situação "REGISTRADO" API PLUG-BOLETO |
| LINHADIGITAVEL_BOLETOAPI | VARCHAR2(70) | sim | Linha Digitável do Boleto na situação "REGISTRADO" API PLUG-BOLETO |
| CODIGOBARRAS_BOLETOAPI | VARCHAR2(70) | sim | Código de Barras do Boleto na situação "REGISTRADO" API PLUG-BOLETO |
| MOTIVO_BOLETOAPI | VARCHAR2(300) | sim | Motivo é um campo onde vem da Consulta do Boleto que diz qual é o erro no envio da API, na situação "FALHA" API PLUG-BOLETO |
| STATUS_BOLETOAPI | VARCHAR2(300) | sim | STATUS Retorno da API, na situação "FALHA" API PLUG-BOLETO |
| IDINTEGRACAO_BOLETOAPI | VARCHAR2(50) | sim | STATUS Retorno da API, na situação "SALVO" API PLUG-BOLETO |
| NUMIMPRESSAO_BOLETOAPI | VARCHAR2(50) | sim | STATUS Retorno da API, na situação "REGISTRADO" API PLUG-BOLETO |
| PROTOCOLO_IMPBOLETOAPI | VARCHAR2(20) | sim | Ao final da solicitação do PDF será devolvido pela API um protocolo que pode ser utilizado para consultar as informações da solicitação |
| NUMENT | NUMBER(10) | sim | ENTRADA PELA736/701 QUE GEROU CONTAS A RECEBER |
| TP_FORNEC_ENT | VARCHAR2(1) | sim | CONTAS A RECEBER GERADO PARA O FORNECEDOR  (F) OU TRANSPORTADOR (T) |
| PROTOCOLO_BAIXABOLETOAPI | VARCHAR2(20) | sim | BOLETOS QUE SE DESEJA OBTER REMESSA DE BAIXA, APENAS NAS SITUAÇÕES: EMITIDO E REGISTRADO QUE PERMITEM A GERAÇÃO DA REMESSA |
| TITULOPAGO_API | VARCHAR2(1) | sim | CAMPO SERÁ DESTINADO PARA CHECAR/BAIXAR BOLETOS PELA API Cefas PlugBoleto |

### VAREJOANTIGO.ITEMPED (616.917 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMPED | NUMBER(10) | não |  |
| CODPROD | NUMBER(10) | não |  |
| QTPEDIDA | NUMBER(12,3) | sim |  |
| PTABELA | NUMBER(18,6) | sim |  |
| PVENDA | NUMBER(18,6) | sim |  |
| VLCUSTOREAL | NUMBER(18,6) | sim |  |
| PERICM | NUMBER(5,2) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| ST | NUMBER(18,6) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| CODFISCALITEM | NUMBER(4) | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLBASEICM | NUMBER(12,2) | sim |  |
| VLICM | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(18,6) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| VLCUSTOFIN | NUMBER(18,6) | sim |  |
| SEQ | NUMBER(4) | não |  |
| CODFILIALRETIRA | VARCHAR2(2) | sim |  |
| QTFALTA | NUMBER(12,3) | sim |  |
| VLCUSTOCONT | NUMBER(18,6) | sim |  |
| OBS | VARCHAR2(40) | sim |  |
| NUMLOTE | VARCHAR2(20) | sim |  |
| DTFAB | DATE | sim |  |
| DTVENC | DATE | sim |  |
| QTPEDIDAPCA | NUMBER(12,3) | sim |  |
| CODFUNCLIB2 | NUMBER(10) | sim |  |
| CODFUNCLIB3 | NUMBER(10) | sim |  |
| AVARIA | VARCHAR2(1) | sim |  |
| CODBARRA | NUMBER(14) | sim |  |
| TPENTREGAITEM | VARCHAR2(1) | sim |  |
| CODFUNCENTREG | NUMBER(10) | sim |  |
| DTENTREG | DATE | sim |  |
| SERIGRAFIA | VARCHAR2(20) | sim |  |
| BORDADO | VARCHAR2(20) | sim |  |
| OBSERVACAO | VARCHAR2(40) | sim |  |
| PVENDAORIG | NUMBER(18,6) | sim |  |
| DESCALT | VARCHAR2(120) | sim |  |
| EXIBIRITEM | VARCHAR2(1) | sim |  |
| VLDEBCREDRCA | NUMBER(18,6) | sim |  |
| LARGURA | NUMBER(18,6) | sim |  |
| ALTURA | NUMBER(18,6) | sim |  |
| QTORIG | NUMBER(13,3) | sim |  |
| UNORIG | VARCHAR2(3) | sim |  |
| OBSADIC | VARCHAR2(400) | sim |  |
| EMBALAGEMORIG | VARCHAR2(12) | sim |  |
| QTVALE | NUMBER(12,3) | sim |  |
| QTBAIXAVALE | NUMBER(12,3) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| PVENDAST | NUMBER(18,6) | sim |  |
| VLFRETE | NUMBER(18,6) | sim |  |
| VLOUTRASDESP | NUMBER(18,6) | sim |  |
| VLDESCONTO | NUMBER(18,6) | sim |  |
| VLSEGURO | NUMBER(18,6) | sim |  |
| PRECOCLIENTE | NUMBER(18,6) | sim |  |
| QTORIGPOL | NUMBER(13,3) | sim |  |
| PVENDAEMB | NUMBER(18,6) | sim |  |
| QTENTREGA | NUMBER(12,2) | sim |  |
| QTALTERADA | NUMBER(10,2) | sim |  |
| DT_ALTERACAO | DATE | sim |  |
| CODALTERADOR | NUMBER(10) | sim |  |
| QT_ATUAL_ENTREGA | NUMBER(10,2) | sim |  |
| STATUSENT | VARCHAR2(1) | sim |  |
| STORIG | NUMBER(18,6) | sim |  |
| VLIPIORIG | NUMBER(18,6) | sim |  |
| QTUNITCX | NUMBER(18,6) | sim |  |
| PESOORIG | NUMBER(12,3) | sim |  |
| PESOAJUST | NUMBER(12,3) | sim |  |
| VLDESCONTOICMS | NUMBER(18,6) | sim |  |
| USAFATORMASTER | VARCHAR2(1) | sim |  |
| VLSTPI | NUMBER(18,6) | sim |  |
| CODFILIAL | VARCHAR2(255) | sim |  |
| QTPEDIDO | FLOAT | sim |  |
| PEDIDOITEMVLTABELA | FLOAT | sim |  |
| VLTABELA | FLOAT | sim |  |
| QTDEBANDEJA | NUMBER(18,6) | sim |  |
| VLFCPST | NUMBER(24,8) | sim |  |
| NITEMPED | VARCHAR2(6) | sim |  |
| XPED | VARCHAR2(15) | sim |  |
| FCPSTORIG | NUMBER(24,8) | sim |  |
| OBSITEM | VARCHAR2(500) | sim |  |
| QTPEDIDAORIG | NUMBER(12,3) | sim |  |
| NUMCORTE | NUMBER(10) | sim |  |
| PRODUTOFERTA | VARCHAR2(1) | sim |  |
| VLICMSDES | NUMBER(24,8) | sim |  |
| GERARSALDOFLEXVENDA | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO2 | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO3 | VARCHAR2(1) | sim |  |
| BASE_VERBAFLEX_PERDESCINI | NUMBER(5,2) | sim |  |
| BASE_VERBAFLEX_PERDESCFINAL | NUMBER(5,2) | sim |  |
| VLVERBAFLEX_CREDITO | NUMBER(12,2) | sim |  |
| VLVERBAFLEX_DEBITO | NUMBER(12,2) | sim |  |
| USAVERBAFLEX_CREDITO | VARCHAR2(1) | sim |  |
| USAVERBAFLEX_DEBITO | VARCHAR2(1) | sim |  |
| NUMENTENTRADACIAP | NUMBER(10) | sim |  |
| VLCIAP | NUMBER(24,8) | sim |  |
| QTMOFADOSTP17 | NUMBER(8) | sim |  |
| QTVENCIDOSTP17 | NUMBER(8) | sim |  |
| MOTIVOMOFVENCTP17 | VARCHAR2(1000) | sim |  |
| USADESCSUPERVISORFV | VARCHAR2(1) | sim |  |

### VAREJO.NFSAID (577.483 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMNOTA | NUMBER(10) | sim |  |
| SERIE | VARCHAR2(3) | sim |  |
| ESPECIE | VARCHAR2(2) | sim |  |
| DTEMISSAO | DATE | sim |  |
| CODFISCAL | NUMBER(4) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| CODCLI | NUMBER(6) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| CODPLPAG | NUMBER(4) | sim |  |
| NUMCUPOM | NUMBER(10) | sim |  |
| TIPO | NUMBER(2) | sim |  |
| VLCUSTOREAL | NUMBER(12,2) | sim |  |
| VLCUSTOFIN | NUMBER(12,2) | sim |  |
| VLFRETE | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| VLTABELA | NUMBER(12,2) | sim |  |
| TOTPESO | NUMBER(12,2) | sim |  |
| NUMITENS | NUMBER(4) | sim |  |
| OBS | VARCHAR2(40) | sim |  |
| DTCANCEL | DATE | sim |  |
| CODFUNCANCEL | NUMBER(10) | sim |  |
| VLCANCEL | NUMBER(12,2) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| TOTVOLUME | NUMBER(12,2) | sim |  |
| DTSAIDA | DATE | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLST | NUMBER(12,2) | sim |  |
| VLCUSTOCONT | NUMBER(12,2) | sim |  |
| VLTOTCONT | NUMBER(12,2) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| CODPRACA | NUMBER(4) | sim |  |
| FRETEDESPACHO | VARCHAR2(1) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| DTDEVOL | DATE | sim |  |
| VLDEVOL | NUMBER(12,2) | sim |  |
| TIPOVENDA | VARCHAR2(2) | sim |  |
| VLICM | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(12,2) | sim |  |
| VLBASEICM | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| NUMVIAS | NUMBER(2) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| CODDEVOL | NUMBER(4) | sim |  |
| DTENTREGA | DATE | sim |  |
| VLISENTO | NUMBER(12,2) | sim |  |
| NFORIGEM | NUMBER(10) | sim |  |
| VLOUTRASDESP | NUMBER(12,2) | sim |  |
| CODSUPERVISOR | NUMBER(4) | sim |  |
| NUMCOMANDA | NUMBER(10) | sim |  |
| OBS2 | VARCHAR2(40) | sim |  |
| TOTPESOLIQ | NUMBER(12,2) | sim |  |
| CODFORNECTRANSP | NUMBER(6) | sim |  |
| SUBSERIE | VARCHAR2(1) | sim |  |
| CODFUNCVEND | NUMBER(10) | sim |  |
| NUMSERVICO | NUMBER(10) | sim |  |
| VLBASEISS | NUMBER(12,2) | sim |  |
| VLISS | NUMBER(12,2) | sim |  |
| VLDESCBRINDE | NUMBER(12,2) | sim |  |
| NFETPEMIS | VARCHAR2(2) | sim |  |
| DTSTATUS | DATE | sim |  |
| NFEPLACA | VARCHAR2(7) | sim |  |
| NFEUFPLACA | VARCHAR2(2) | sim |  |
| DTNFE | DATE | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| CSTATNFE | VARCHAR2(4) | sim |  |
| RECNFE | VARCHAR2(20) | sim |  |
| NPROTNFE | VARCHAR2(20) | sim |  |
| IDLOTE | VARCHAR2(15) | sim |  |
| MODONFE | VARCHAR2(20) | sim |  |
| DTIMPNFE | DATE | sim |  |
| NFDESTINO | NUMBER(10) | sim |  |
| ENDERENT | VARCHAR2(40) | sim |  |
| BAIRROENT | VARCHAR2(30) | sim |  |
| CIDADEENT | VARCHAR2(40) | sim |  |
| ESTADOENT | VARCHAR2(2) | sim |  |
| CEPENT | VARCHAR2(10) | sim |  |
| TELENT | VARCHAR2(15) | sim |  |
| IEENT | VARCHAR2(15) | sim |  |
| CPFCNPJ | VARCHAR2(18) | sim |  |
| VLDESCICM | NUMBER(12,2) | sim |  |
| VLDESCFIN | NUMBER(12,2) | sim |  |
| VLBASEPIS | NUMBER(12,2) | sim |  |
| VLPIS | NUMBER(12,2) | sim |  |
| VLBASECOFINS | NUMBER(12,2) | sim |  |
| VLCOFINS | NUMBER(12,2) | sim |  |
| ESPECIE2 | VARCHAR2(2) | sim |  |
| STATUS | VARCHAR2(200) | sim |  |
| IMPRESSA | VARCHAR2(3) | sim |  |
| NFE | VARCHAR2(60) | sim |  |
| MSGNFE | VARCHAR2(200) | sim |  |
| NFEQTDEVOL | VARCHAR2(10) | sim |  |
| NFEESPVOL | VARCHAR2(20) | sim |  |
| NFEMARCAVOL | VARCHAR2(30) | sim |  |
| NFEOBS | VARCHAR2(4000) | sim |  |
| NUMDOCIMPORT | NUMBER(15) | sim |  |
| DTREGIMPORT | DATE | sim |  |
| DESCDESEMBARACO | VARCHAR2(100) | sim |  |
| UFDESEMBARACO | VARCHAR2(2) | sim |  |
| DTDESEMBARACO | DATE | sim |  |
| CODEXPSISTINTERNO | NUMBER(10) | sim |  |
| NFEADIC | NUMBER(3) | sim |  |
| NFESEQ | NUMBER(3) | sim |  |
| NFEFABRIC | VARCHAR2(60) | sim |  |
| VLDESCIMPOSTO | NUMBER(12,2) | sim |  |
| ANTT | VARCHAR2(20) | sim |  |
| VLCOMSUP | NUMBER(12,2) | sim |  |
| DTIMPCUPOM | DATE | sim |  |
| DATACONT | VARCHAR2(254) | sim |  |
| JUSTCONT | VARCHAR2(254) | sim |  |
| NFECHAVECONT | VARCHAR2(254) | sim |  |
| NFEUFEMBARQ | VARCHAR2(2) | sim |  |
| NFELOCEMBARQ | VARCHAR2(40) | sim |  |
| CCF | NUMBER(6) | sim |  |
| GNF | NUMBER(6) | sim |  |
| ENTNUMNFPROP | VARCHAR2(1) | sim |  |
| NFSERVICO | VARCHAR2(1) | sim |  |
| VLCANCELPARC | NUMBER(12,2) | sim |  |
| VLSEGURO | NUMBER(12,2) | sim |  |
| EMBALAGEMREGIAO | VARCHAR2(1) | sim |  |
| VLINSS | NUMBER(12,2) | sim |  |
| VLIR | NUMBER(12,2) | sim |  |
| VLCSLL | NUMBER(12,2) | sim |  |
| ORIGEM | VARCHAR2(4) | sim |  |
| CODPARIND | NUMBER(6) | sim |  |
| OBSCCE | VARCHAR2(4000) | sim |  |
| CSTATCCE | VARCHAR2(3) | sim |  |
| NPROTCCE | VARCHAR2(20) | sim |  |
| CPFCNPJCAT52 | VARCHAR2(14) | sim |  |
| VFCPUFDEST | NUMBER(12,2) | sim |  |
| VICMSUFDEST | NUMBER(12,2) | sim |  |
| VICMSUFREMET | NUMBER(12,2) | sim |  |
| CHAVEREFCOMP | VARCHAR2(60) | sim |  |
| DTACERTO | DATE | sim |  |
| OBSACERTO | VARCHAR2(80) | sim |  |
| CODFUNCACERTO | NUMBER(6) | sim |  |
| INDPRES | VARCHAR2(1) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| CSTCREDITOICMS | VARCHAR2(2) | sim |  |
| VLFCP | NUMBER(12,2) | sim |  |
| VLFCPST | NUMBER(12,2) | sim |  |
| VLFCPSTRET | NUMBER(12,2) | sim |  |
| USAMFE | CHAR(1) | sim |  |
| NFGARANTIA | VARCHAR2(1) | sim |  |
| VLBASEICMGARANTIA | NUMBER(12,2) | sim |  |
| VLICMGARANTIA | NUMBER(12,2) | sim |  |
| VLBASESTGARANTIA | NUMBER(12,2) | sim |  |
| VLSTGARANTIA | NUMBER(12,2) | sim |  |
| VLBASEIPIGARANTIA | NUMBER(12,2) | sim |  |
| VLIPIGARANTIA | NUMBER(12,2) | sim |  |
| VLBASEFCP | NUMBER(12,2) | sim |  |
| VLBASEFCPST | NUMBER(12,2) | sim |  |
| VLBASEFCPSTRET | NUMBER(12,2) | sim |  |
| CODFUNCF11LIB | NUMBER(10) | sim |  |
| CSTATNFEAUX | VARCHAR2(4) | sim |  |
| CODATEND1 | NUMBER(10) | sim |  |
| CODATEND2 | NUMBER(10) | sim |  |
| CODATEND3 | NUMBER(10) | sim |  |
| CODATEND4 | NUMBER(10) | sim |  |
| DUPLICOUTP12 | VARCHAR2(1) | sim |  |
| NFDESTINOCODCLI | NUMBER(10) | sim |  |
| XMLPDFENVIADO | VARCHAR2(1) | sim |  |
| VLICMSDES | NUMBER(12,2) | sim |  |
| TIPOCREDITOICMS | VARCHAR2(13) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| USADEVOLTRANSF | VARCHAR2(1) | sim |  |
| VLICMDIF | NUMBER(12,2) | sim |  |
| CPFCNPJSAID | VARCHAR2(18) | sim |  |
| DIFEMBREGIAO | VARCHAR2(1) | sim |  |
| VLFRETEPAGO | NUMBER(12,2) | sim |  |
| SAIDAAVARIA | VARCHAR2(1) | sim |  |
| SRSIMPLESFATURA | VARCHAR2(1) | sim |  |
| NUMLANCCPAGARDESCFIN | NUMBER(10) | sim |  |
| VLBONIFICACAO | NUMBER(12,2) | sim |  |
| FRETEBONIF | NUMBER(12,2) | sim |  |
| VLFRETECOTADO | NUMBER(12,2) | sim |  |
| CSOSN_CREDITOICMS | NUMBER(3) | sim |  |
| VLCREDUSADO | NUMBER(12,2) | sim |  |
| NCONTRATOCONSIG | NUMBER(10) | sim |  |
| VERSAOROTINA | VARCHAR2(20) | sim |  |
| CNPJINTERMEDIADOR | VARCHAR2(14) | sim |  |
| INTERMEDIADOR | VARCHAR2(60) | sim |  |
| NFTERCEIRO | VARCHAR2(1) | sim |  |
| CODIGOSTATUS_SCANNTECH | NUMBER(5) | sim |  |
| STATUSENVIO_SCANNTECH | VARCHAR2(1) | sim |  |
| VLDESCONTOSCANNTECH | NUMBER(12,2) | sim |  |
| STATUSENVIOCANCEL_SCANNTECH | VARCHAR2(1) | sim |  |
| VLTOT_OUT_TAXAS | NUMBER(12,2) | sim |  |
| FINALIDADENFE | VARCHAR2(14) | sim |  |
| CODHIST | NUMBER(6) | sim |  |
| VLBASEIRRF | NUMBER(12,2) | sim | GRAVA O VALOR DE BASE DE IMPOSTO DE RENDA RETIDO IRRF, FAZ REFERENCIA AOS CAMPOS FILIAL.DESTACAIRRFDANFE, FILIAL.PERALIQIRPJ E CLIENTE.CLIORGPUBLICO |
| VLIRRF | NUMBER(12,2) | sim | GRAVA O VALOR DE IMPOSTO DE RENDA RETIDO IRRF, FAZ REFERENCIA AOS CAMPOS NFSAID.VLBASEIRRF, FILIAL.DESTACAIRRFDANFE, FILIAL.PERALIQIRPJ E CLIENTE.CLIORGPUBLICO |
| TRANSPORTE | VARCHAR2(4) | sim | PROCESSO DE ESTIVA SALVA TIPO DO    TRANSPORTE: TE-TERCEIRIZADO EXTERNO TL ¿TERCEIRO LOCAL I-ISENTO |
| ESTORNO_QTINDENIZ | VARCHAR2(1) | sim | ESTE CAMPO IRÁ DETERMINAR NO MOMENTO DO CANCEL. DA NF-E, SE FOR (S) IRÁ VOLTAR PARA ESTOQUE.QTINDENIZ |
| NUMCOTACAO | NUMBER(12) | sim | CAMPO ALIMENTADO R.56 ABA F7 |
| DTENTREGA_RAP | DATE | sim | AO CONFIRNAR A ENTREGA NA RT 530 GRAVAR DATA DA ENTREGA |
| CODFUNCENTREGA_RAP | NUMBER(10) | sim | AO CONFIRMAR A ENTREGA NA RT 530 GRAVAR CODFUNC QUE REALIZOU A CONFIRMACAO |
| VLBONIFICACAO2 | NUMBER(12,2) | sim | VALOR DO BONIFICACAO2 SOMADO NO DESCONTO DO ITEM |
| VLBONIFICACAO3 | NUMBER(12,2) | sim | VALOR DO BONIFICACAO3 SOMADO NO DESCONTO DO ITEM |
| NPS | NUMBER(5) | sim | USADO PARA RECEBER A PONTUAÇÃO DA AVALIAÇÃO DE ATENDIMENTO NOS PDVS ATRAVES DO PINPAD |
| CSTATCVENDA | NUMBER(3) | sim | INTEGRACAO CRESCE VENDAS - RECEBE O STATUS DA VENDA COM A API |
| CSTATCVDESC | VARCHAR2(254) | sim | INTEGRACAO CRESCE VENDAS - RECEBE A DESCRICAO DO STATUS |
| ENVIOUCRVENDAS | VARCHAR2(1) | sim | INTEGRACAO CRESCE VENDAS - EXIBE SE A VENDA FOI ENVIADA PARA API |
| USACRVENDA | VARCHAR2(1) | sim | INTEGRACAO CRESCE VENDAS - DEFINE O USO DA INTEGRACAO |
| VLDESCONTOCRVENDAS | NUMBER(12,2) | sim | INTEGRACAO CRESCE VENDAS - RECEBE O DESCONTO CRESCE VENDAS |
| VLDESCONTOSUBTOTCRVENDAS | NUMBER(12,2) | sim | INTEGRACAO CRESCE VENDAS - RECEBE O DESCONTO SUBTOTAL |
| APLICAVLDESCSUBTOTCRVENDAS | VARCHAR2(1) | sim | INTEGRACAO CRESCE VENDAS - DEFINE O USO DO DESCONTO SUBTOTAL |
| VICMSMONORET | NUMBER(12,2) | sim | Valor AD REM do ICMS para o produto CST=61 |
| ID_MARKET | VARCHAR2(80) | sim | id do pedido no Plug4Market |
| CODFUNCLIB_LIM | NUMBER(10) | sim | CODIGO DO FISCAL QUE LIBEROU VENDA ACIMA DO VALOR DE LIMINTE DISPONIVEL |
| DTCONFERIDO | DATE | sim |  |

### JP.HISTESTOQUE (570.732 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CODFILIAL | VARCHAR2(2) | não |  |
| CODPROD | NUMBER(10) | não |  |
| DATA | DATE | não |  |
| QTEST | NUMBER(18,6) | sim |  |
| QTESTGER | NUMBER(18,6) | sim |  |
| CUSTOULTENT | NUMBER(18,6) | sim |  |
| CUSTOREAL | NUMBER(18,6) | sim |  |
| CUSTOFIN | NUMBER(18,6) | sim |  |
| CUSTOCONT | NUMBER(18,6) | sim |  |
| VLCUSTOREAL | NUMBER(12,2) | sim |  |
| VLCUSTOFIN | NUMBER(12,2) | sim |  |
| QTVENDA | NUMBER(12,3) | sim |  |
| VLVENDA | NUMBER(12,2) | sim |  |
| QTRESERV | NUMBER(18,6) | sim |  |
| QTINDENIZ | NUMBER(18,6) | sim |  |
| QTBLOQUEADA | NUMBER(18,6) | sim |  |
| QTDEVOL | NUMBER(12,3) | sim |  |
| VLDEVOL | NUMBER(12,2) | sim |  |
| CODFUNCREPROC | NUMBER(10) | sim |  |
| DTREPROC | DATE | sim |  |
| PTABELA | NUMBER(18,6) | sim |  |

### SEVERIANO.LOGFATURAMENTO (560.169 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMCAR | NUMBER(10) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| DATA | DATE | sim |  |
| MENSAGEM | VARCHAR2(2000) | sim |  |

### VAREJOANTIGO.CRECEBER (498.479 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMNOTA | NUMBER(10) | sim |  |
| PREST | NUMBER(3) | não |  |
| CODCLI | NUMBER(6) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| DTEMISSAO | DATE | sim |  |
| DTVENC | DATE | sim |  |
| VALOR | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLJURO | NUMBER(12,2) | sim |  |
| DTPAGO | DATE | sim |  |
| VPAGO | NUMBER(12,2) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| NUMBCO | VARCHAR2(4) | sim |  |
| NUMAG | VARCHAR2(4) | sim |  |
| NUMCH | VARCHAR2(8) | sim |  |
| NUMCART | VARCHAR2(15) | sim |  |
| DTFECHA | DATE | sim |  |
| OBS | VARCHAR2(2000) | sim |  |
| CODCXBCO | NUMBER(4) | sim |  |
| CODFUNCFECHA | NUMBER(10) | sim |  |
| DTBAIXA | DATE | sim |  |
| NUMCONTA | VARCHAR2(15) | sim |  |
| CODCXBCOP | NUMBER(4) | sim |  |
| VLAUX | NUMBER(12,2) | sim |  |
| TOTPREST | NUMBER(3) | sim |  |
| DTULTALT | DATE | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| PERCOM | NUMBER(7,4) | sim |  |
| NOSSNUMBCO | VARCHAR2(14) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| DTDESD | DATE | sim |  |
| CODFUNCDESD | NUMBER(10) | sim |  |
| CODFUNCBAIXA | NUMBER(10) | sim |  |
| VALORDEV | NUMBER(12,2) | sim |  |
| OBS2 | VARCHAR2(100) | sim |  |
| NUMLANCPG | NUMBER(10) | sim |  |
| NOSSONUMBCO | VARCHAR2(20) | sim |  |
| CODBARRA | VARCHAR2(44) | sim |  |
| LINHADIG | VARCHAR2(65) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| VLTXBOLETO | NUMBER(12,2) | sim |  |
| STATUS | VARCHAR2(1) | sim |  |
| VALORORIG | NUMBER(12,2) | sim |  |
| PROTOCOLO | NUMBER(10) | sim |  |
| TURNO | VARCHAR2(1) | sim |  |
| DTVENCORIG | DATE | sim |  |
| CODCOBORIG | VARCHAR2(4) | sim |  |
| CODSUPERVISOR | NUMBER(4) | sim |  |
| PR | VARCHAR2(2) | sim |  |
| DTULTALTER | DATE | sim |  |
| DTCXMOT | DATE | sim |  |
| CODFUNCCXMOT | NUMBER(10) | sim |  |
| NUMTRANS | NUMBER(10) | sim |  |
| CODCOBCXBCO | VARCHAR2(4) | sim |  |
| CODFUNCVALE | NUMBER(10) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| OPERACAO | VARCHAR2(1) | sim |  |
| CODBAIXA | NUMBER(4) | sim |  |
| ALINEA | VARCHAR2(4) | sim |  |
| NUMVENDADESD | NUMBER(10) | sim |  |
| NUMFATURA | NUMBER(10) | sim |  |
| DTFECHAPROT | DATE | sim |  |
| DTCXMOTPROT | DATE | sim |  |
| CODFUNCFECHAPROT | NUMBER(10) | sim |  |
| TIPOPRORROG | VARCHAR2(1) | sim |  |
| DTPRORROG | DATE | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| NUMCUSTODIA | NUMBER(8) | sim |  |
| DTCUSTODIA | DATE | sim |  |
| CODCXBCOCUSTODIA | NUMBER(4) | sim |  |
| DTPREVPAGTO | DATE | sim |  |
| PRESTDESD | NUMBER(3) | sim |  |
| DTESTORNO | DATE | sim |  |
| CODFUNCESTORNO | NUMBER(10) | sim |  |
| DIGITAO | VARCHAR2(1) | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| LIBERARVENDALIMCRED | VARCHAR2(1) | sim |  |
| RETBOLTIPOREG | NUMBER(2) | sim |  |
| RETBOLCODINSC | NUMBER(3) | sim |  |
| RETBOLNUMINSC | NUMBER(20) | sim |  |
| RETBOLAGENCIA | NUMBER(6) | sim |  |
| RETBOLCONTA | NUMBER(10) | sim |  |
| RETBOLDAC | VARCHAR2(1) | sim |  |
| RETBOLCODOCORRENCIA | NUMBER(4) | sim |  |
| RETBOLDTOCORRENCIA | DATE | sim |  |
| RETBOLNOSSONUMCONF | NUMBER(15) | sim |  |
| RETBOLDTVENCIMENTO | DATE | sim |  |
| RETBOLVALORTITULO | NUMBER(15,2) | sim |  |
| RETBOLCODBCO | NUMBER(4) | sim |  |
| RETBOLAGCOB | NUMBER(6) | sim |  |
| RETBOLDACAGCOB | VARCHAR2(1) | sim |  |
| RETBOLESPECIE | NUMBER(3) | sim |  |
| RETBOLTARIFACOB | NUMBER(15,2) | sim |  |
| RETBOLVALORIOF | NUMBER(15,2) | sim |  |
| RETBOLVALORABAT | NUMBER(15,2) | sim |  |
| RETBOLDESCONTOS | NUMBER(15,2) | sim |  |
| RETBOLVALORPRINC | NUMBER(15,2) | sim |  |
| RETBOLJUROSMORAMULTA | NUMBER(15,2) | sim |  |
| RETBOLOUTROSCREDITOS | NUMBER(15,2) | sim |  |
| RETBOLDTCREDITO | DATE | sim |  |
| RETBOLINSTRCANCEL | NUMBER(6) | sim |  |
| RETBOLNOMESACADO | VARCHAR2(40) | sim |  |
| RETBOLERROS | VARCHAR2(10) | sim |  |
| RETBOLCODLIQ | VARCHAR2(4) | sim |  |
| RETBOLNUMSEQ | NUMBER(10) | sim |  |
| RETBOLBAIXADO | VARCHAR2(1) | sim |  |
| RETBOLDVAG | VARCHAR2(3) | sim |  |
| DTFECHACHECKOUT | DATE | sim |  |
| VLDESCICMPARC | NUMBER(12,2) | sim |  |
| VLDESCFIN | NUMBER(12,2) | sim |  |
| DTTRANSMISSAO | DATE | sim |  |
| PERCOMSUP | NUMBER(7,4) | sim |  |
| VLDESCTXCAR | NUMBER(12,2) | sim |  |
| NUMPROM | VARCHAR2(20) | sim |  |
| TAXA | NUMBER(12,2) | sim |  |
| CODEMITENTE | NUMBER(10) | sim |  |
| BANDEIRA | VARCHAR2(60) | sim |  |
| TIPO_TRANSACAO | VARCHAR2(15) | sim |  |
| NSU | VARCHAR2(30) | sim |  |
| AUTORIZACAO | VARCHAR2(20) | sim |  |
| ESTABELECIMENTO | VARCHAR2(20) | sim |  |
| NUMEROCARTAO | VARCHAR2(30) | sim |  |
| ORIGEM | VARCHAR2(10) | sim |  |
| MODOBAIXA | VARCHAR2(1) | sim |  |
| DTBAIXACAR | DATE | sim |  |
| TRANSBAIXAAUTO | NUMBER(15) | sim |  |
| PRESTCAR | NUMBER(3) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| LANCR28 | VARCHAR2(1) | sim |  |
| TECLACOB | VARCHAR2(6) | sim |  |
| NUMTRANSMISSAO | NUMBER(14) | sim |  |
| VLMULTA | NUMBER(12,2) | sim |  |
| PDFENVIADO | VARCHAR2(1) | sim |  |
| CODVEND2 | NUMBER(10) | sim |  |
| DTFECHAR185 | DATE | sim |  |
| DESCDEV | NUMBER(12,2) | sim |  |

### VAREJOANTIGO.LOG_ALTER_PARAMETRO (498.354 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| ID | NUMBER | sim |  |
| DATA | DATE | sim |  |
| USERNAME | VARCHAR2(200) | sim |  |
| MACHINE | VARCHAR2(200) | sim |  |
| PROGRAM | VARCHAR2(200) | sim |  |
| MODULE | VARCHAR2(200) | sim |  |
| TERMINAL | VARCHAR2(200) | sim |  |
| IP | VARCHAR2(200) | sim |  |
| CODFILIAL | VARCHAR2(2) | não |  |
| PROXNUMVENDA | NUMBER(10) | sim |  |
| PROXNUMENT | NUMBER(10) | sim |  |
| PROXNUMTRANS | NUMBER(10) | sim |  |
| PROXNUMLANC | NUMBER(10) | sim |  |
| PROXNUMPED | NUMBER(10) | sim |  |
| CODCONTFOR | NUMBER(10) | sim |  |
| CODCONTCLI | NUMBER(10) | sim |  |
| TXVENDA | NUMBER(5,2) | sim |  |
| VLDIFNFENT | NUMBER(12,2) | sim |  |
| VLSANGRIA | NUMBER(12,2) | sim |  |
| CAMINHODIR | VARCHAR2(30) | sim |  |
| PROXNUMCOTA | NUMBER(10) | sim |  |
| PROXNUMSANGSUP | NUMBER(10) | sim |  |
| PROXCODFORNEC | NUMBER(6) | sim |  |
| PROXCODPROD | NUMBER(10) | sim |  |
| PROXCODCLI | NUMBER(6) | sim |  |
| PROXNUMVALE | NUMBER(10) | sim |  |
| TXJURO | NUMBER(5,2) | sim |  |
| CODCXBCOBAIXA | NUMBER(4) | sim |  |
| TIPOCUSTO | VARCHAR2(1) | sim |  |
| PORTAETIQ | VARCHAR2(4) | sim |  |
| CODSETORVEND | NUMBER(4) | sim |  |
| CODSETORGEREN | NUMBER(4) | sim |  |
| CODSETORFISCALCX | NUMBER(4) | sim |  |
| CODCONTFRE | NUMBER(10) | sim |  |
| NUMCASASDECVENDA | NUMBER(2) | sim |  |
| CODCONTOUT | NUMBER(10) | sim |  |
| CODSETORCOMPRADOR | NUMBER | sim |  |
| HISTCONTFOR | VARCHAR2(60) | sim |  |
| HISTCONTFRE | VARCHAR2(60) | sim |  |
| HISTCONTOUT | VARCHAR2(60) | sim |  |
| CODSETORDIRETOR | NUMBER(4) | sim |  |
| MODELOETIQ | VARCHAR2(6) | sim |  |
| NUMMAXVIAS | NUMBER(4) | sim |  |
| PROXNUMCAR | NUMBER(10) | sim |  |
| IDSOLICITTEF | NUMBER(10) | sim |  |
| NUMCASASDECCUSTO | NUMBER(2) | sim |  |
| NUMCASASDECESTOQUE | NUMBER(2) | sim |  |
| USACODBARRA | VARCHAR2(1) | sim |  |
| VLLIMCRED | NUMBER(12,2) | sim |  |
| PERSOBRESAL | NUMBER(5,2) | sim |  |
| ACEITAVENDAABAIXODOMIN | VARCHAR2(1) | sim |  |
| COMISSAOVENDA | VARCHAR2(2) | sim |  |
| USADVCODBARRAMENOR | VARCHAR2(1) | sim |  |
| CODCONTAJUSTEEST | NUMBER(10) | sim |  |
| NUMDIASBAIXAAUTOMAT | NUMBER(4) | sim |  |
| NUMDIASTXJURO | NUMBER(4) | sim |  |
| COBRARJURODESD | VARCHAR2(1) | sim |  |
| CAMINHOSERVER | VARCHAR2(40) | sim |  |
| TX1 | NUMBER(5,2) | sim |  |
| TX2 | NUMBER(5,2) | sim |  |
| TX3 | NUMBER(5,2) | sim |  |
| TX4 | NUMBER(5,2) | sim |  |
| TX5 | NUMBER(5,2) | sim |  |
| TX6 | NUMBER(5,2) | sim |  |
| USACREDICM | VARCHAR2(1) | sim |  |
| PERPISCOFINS | NUMBER(5,2) | sim |  |
| TXOPERACIONAL | NUMBER(5,2) | sim |  |
| TPCALCULOPVENDA | VARCHAR2(1) | sim |  |
| VLMINIMOTARIFABANC | NUMBER(12,2) | sim |  |
| VLTARIFA | NUMBER(12,2) | sim |  |
| SOMATARIFABANCNF | VARCHAR2(1) | sim |  |
| CODSETORMOT | NUMBER(4) | sim |  |
| ACEITAVENDASEMEST | VARCHAR2(1) | sim |  |
| ECFCOMEREST | VARCHAR2(1) | sim |  |
| ACEITAVENDASEMESTCONT | VARCHAR2(1) | sim |  |
| PERACRESENTREGA | NUMBER(5,2) | sim |  |
| BLOQPEDIDOABAIXOPTABELA | VARCHAR2(1) | sim |  |
| PROXNUMCOMANDA | NUMBER(10) | sim |  |
| NUMCOMANDA | NUMBER(10) | sim |  |
| IMPRIMEPEDIDOTLMK | VARCHAR2(1) | sim |  |
| IMPRIMIRRESUMOCORPONF | VARCHAR2(1) | sim |  |
| QUEBRARPEDIDOFILRETIRA | VARCHAR2(1) | sim |  |
| ACEITADIVPEDIDONF | VARCHAR2(1) | sim |  |
| NUMDIASBLOQAUTOMAT | NUMBER(4) | sim |  |
| DADOSADICIONAISNFRURAL | VARCHAR2(1) | sim |  |
| USACREDPISCOFINS | VARCHAR2(1) | sim |  |
| PROXNUMFATURA | NUMBER(10) | sim |  |
| EXIBIRCRECEBERVENDA | VARCHAR2(1) | sim |  |
| CODCOBCPENT | VARCHAR2(4) | sim |  |
| HOSTFTP | VARCHAR2(60) | sim |  |
| USUARIOFTP | VARCHAR2(40) | sim |  |
| SENHAFTP | VARCHAR2(40) | sim |  |
| MARGEMMINPED | NUMBER(5,2) | sim |  |
| ACEITAGERAR1BOLETOVENDATP2 | VARCHAR2(1) | sim |  |
| PERINDICETV2 | NUMBER(5,2) | sim |  |
| USARTV6PLIQ | VARCHAR2(1) | sim |  |
| USALOTE | VARCHAR2(1) | sim |  |
| PROXNUMBORDERO | NUMBER(10) | sim |  |
| TRAVARPEDFALTA | VARCHAR2(1) | sim |  |
| VLMINVALE | NUMBER(12,2) | sim |  |
| APENASITENSESTDEF | VARCHAR2(1) | sim |  |
| CUSTOTRANSF | VARCHAR2(1) | sim |  |
| VLQUEBRAPORKG | NUMBER(12,2) | sim |  |
| CODCONTAQUEBRAKG | NUMBER(10) | sim |  |
| CODCONTFREENTREGA | NUMBER(10) | sim |  |
| CODFORNECQUEBRAKG | NUMBER(10) | sim |  |
| APLICAPRVENDATABELA | VARCHAR2(1) | sim |  |
| CODCONTANTPAG | NUMBER(10) | sim |  |
| CODCONTPAGJUR | NUMBER(10) | sim |  |
| USAFILIALRETIRA | VARCHAR2(1) | sim |  |
| USAREGPRACAPEDBALCAO | VARCHAR2(1) | sim |  |
| PERMULTA | NUMBER(5,2) | sim |  |
| PGICMTARIFABANC | VARCHAR2(1) | sim |  |
| VLVENDAMINCONSUMIDOR | NUMBER(12,2) | sim |  |
| CODCONTAICMANTECIP | NUMBER(10) | sim |  |
| CODFORNECICMANTECIP | NUMBER(6) | sim |  |
| FAZERRATEIORODAPE | VARCHAR2(1) | sim |  |
| VLMAXBOLETOFATU | NUMBER(12,2) | sim |  |
| EXIBIRLUCROVENDA | VARCHAR2(1) | sim |  |
| BLOQPEDTLMK | VARCHAR2(1) | sim |  |
| APLICCUSTOTRANSFFIL | VARCHAR2(1) | sim |  |
| EMITIRNFPF | VARCHAR2(1) | sim |  |
| CODCODTTRANSF | NUMBER(10) | sim |  |
| TPCALCST | VARCHAR2(1) | sim |  |
| GERARCPAGARPREV | VARCHAR2(1) | sim |  |
| DTULTFECHADIA | DATE | sim |  |
| DTULTFECHAMES | DATE | sim |  |
| DTULTINVENT | DATE | sim |  |
| USACREDCLIVENDA | VARCHAR2(1) | sim |  |
| ACEITAMUDARDTPEDIDO | VARCHAR2(1) | sim |  |
| CADFORNECAUT | VARCHAR2(1) | sim |  |
| PERISS | NUMBER(5,2) | sim |  |
| ATRIBUIRTIPOFJAUTO | VARCHAR2(1) | sim |  |
| TRUNCDECECF | VARCHAR2(1) | sim |  |
| USACONFCEGA | VARCHAR2(1) | sim |  |
| USABLOQCLI | VARCHAR2(2) | sim |  |
| USABLOQFOR | VARCHAR2(2) | sim |  |
| USALIVROELETRONICO | VARCHAR2(1) | sim |  |
| NFENTAJUSTERODAPE | NUMBER(12,2) | sim |  |
| PRECOEMBALAGEM | VARCHAR2(1) | sim |  |
| MAXITENSNF | NUMBER(6) | sim |  |
| ACEITAINICIAROPSEMEST | VARCHAR2(1) | sim |  |
| TRAVAREMENTREGAFUT | VARCHAR2(1) | sim |  |
| CONVERTECUSTOUNTRANSF | VARCHAR2(1) | sim |  |
| APLICARDESCPRODUTOAUTOM | VARCHAR2(1) | sim |  |
| LAYOUTCAMPODESCONTO | VARCHAR2(1) | sim |  |
| INVERTERMANIFESTO | VARCHAR2(1) | sim |  |
| FILIALEXCLUSIVA | VARCHAR2(2) | sim |  |
| BLOQPEDIMPORTFV | VARCHAR2(1) | sim |  |
| APLICPCOTRANSFVENDACUSTO | VARCHAR2(1) | sim |  |
| NUMVIASRECIBOENTMERC | NUMBER(2) | sim |  |
| HOSTSMTP | VARCHAR2(100) | sim |  |
| PORTSMTP | VARCHAR2(100) | sim |  |
| USERSMTP | VARCHAR2(100) | sim |  |
| SENHASMTP | VARCHAR2(100) | sim |  |
| TPDOCENTRADA | NUMBER(2) | sim |  |
| ALERTAENTFUTURA | VARCHAR2(1) | sim |  |
| MENSSUFRAMA1 | VARCHAR2(100) | sim |  |
| MENSSUFRAMA2 | VARCHAR2(100) | sim |  |
| SOMATARIFACRECEBER | VARCHAR2(1) | sim |  |
| DIASDTRETROATIVA | NUMBER(4) | sim |  |
| BLOQPEDTP45 | VARCHAR2(1) | sim |  |
| BLOQPEDTP45AFV | VARCHAR2(1) | sim |  |
| OBSECF1 | VARCHAR2(40) | sim |  |
| OBSECF2 | VARCHAR2(40) | sim |  |
| OBSECF3 | VARCHAR2(40) | sim |  |
| OBSECF4 | VARCHAR2(40) | sim |  |
| EXIBIRESTOQUEROT56 | VARCHAR2(1) | sim |  |
| DIRNFE | VARCHAR2(40) | sim |  |
| AMBNFE | VARCHAR2(1) | sim |  |
| TRANSAUTENTRADAS | VARCHAR2(1) | sim |  |
| BLOQPEDCOMPRA | VARCHAR2(1) | sim |  |
| ACEITADESDROBRETOATIVO | VARCHAR2(1) | sim |  |
| FRETENFE | NUMBER(1) | sim |  |
| CERTDIGITAL | VARCHAR2(500) | sim |  |
| MOVQTESTENTREGASIMPLES | VARCHAR2(1) | sim |  |
| USALOTETLMK | VARCHAR2(1) | sim |  |
| FILIALRETIRADEFAULT | VARCHAR2(2) | sim |  |
| ACEITAMANULTPEDIDOCOMISSAO | VARCHAR2(1) | sim |  |
| CODCONTTARIFABANCARIA | NUMBER(10) | sim |  |
| SOLICITANUMPEDORIG | VARCHAR2(1) | sim |  |
| TXJUROSPORPRAZOMD | VARCHAR2(1) | sim |  |
| AJUSTACUSTOPORCOMPOSICAO | VARCHAR2(1) | sim |  |
| DTSAIDATLMKDANFE | VARCHAR2(1) | sim |  |
| IMPVENDA | VARCHAR2(1) | sim |  |
| REPPRECOPLPAGVENDA | VARCHAR2(1) | sim |  |
| TPDATASINTREG53 | VARCHAR2(1) | sim |  |
| TRAVADESDCLIBLOQ | VARCHAR2(1) | sim |  |
| ACEITAQTNEGATIVA | VARCHAR2(1) | sim |  |
| CODFISCALTP22EST | NUMBER(4) | sim |  |
| CODFISCALTP22INT | NUMBER(4) | sim |  |
| AUTORIZCANCELNFQUITADA | VARCHAR2(1) | sim |  |
| MSGNFVENDACIF | VARCHAR2(40) | sim |  |
| USACODSIMILARCOMOCODFAB | VARCHAR2(1) | sim |  |
| DIRETORIOBACKUP | VARCHAR2(100) | sim |  |
| CERTIFCLASSIF | VARCHAR2(20) | sim |  |
| LOTECLASSIF | VARCHAR2(10) | sim |  |
| DTULTEXPORT | DATE | sim |  |
| DEVOLUNICA | VARCHAR2(1) | sim |  |
| USADEBCREDRCA | VARCHAR2(1) | sim |  |
| GERA1DEVOLCRECEBER | VARCHAR2(1) | sim |  |
| ENTREGARRETIRAR | VARCHAR2(1) | sim |  |
| BLOQDATAS | VARCHAR2(1) | sim |  |
| BLOQVENDABKTPDIF1 | VARCHAR2(1) | sim |  |
| ACEITAOSSEMPLACA | VARCHAR2(1) | sim |  |
| LOTEAUT | VARCHAR2(1) | sim |  |
| USAREFPROD | VARCHAR2(1) | sim |  |
| UTILIZANFE | VARCHAR2(1) | sim |  |
| BLOQENTTRANSF | VARCHAR2(1) | sim |  |
| EXIBIRAPENASCOLVENDA | VARCHAR2(1) | sim |  |
| ABATERICMPISCOFINSULTENT | VARCHAR2(1) | sim |  |
| TRAVACXBCO21 | VARCHAR2(1) | sim |  |
| TPINDICEAJUSTE | VARCHAR2(2) | sim |  |
| IMPNUMLOTENFE | VARCHAR2(1) | sim |  |
| TRAVARCODVEND | VARCHAR2(1) | sim |  |
| TRAVARDESC | VARCHAR2(1) | sim |  |
| ACEITATRANSFSEMESTSF | VARCHAR2(1) | sim |  |
| EXIBIRMENSAGEMOS | VARCHAR2(1) | sim |  |
| VLMAXCONSUMIDOR | NUMBER(15,2) | sim |  |
| TPVENDEDORAUT | VARCHAR2(1) | sim |  |
| ATIVALIBERAENTDIA | VARCHAR2(1) | sim |  |
| PERSTSOMA118 | NUMBER(5,2) | sim |  |
| MOSTRACHECKLIST | VARCHAR2(1) | sim |  |
| CALCCOMFATURA | VARCHAR2(1) | sim |  |
| BLOQUEIOVENDEDOR | VARCHAR2(1) | sim |  |
| TPFRETE56 | VARCHAR2(6) | sim |  |
| CALCULASTPFTV6 | VARCHAR2(1) | sim |  |
| CONVERTEUNIDCX | VARCHAR2(1) | sim |  |
| PRECOBALCAO | VARCHAR2(1) | sim |  |
| SOLICITASENHA | VARCHAR2(1) | sim |  |
| ALTERANUMCARDESD | VARCHAR2(1) | sim |  |
| CODSETORCRECEB1 | NUMBER(4) | sim |  |
| CODSETORCRECEB2 | NUMBER(4) | sim |  |
| DESDOBRAMENTOAUTOMATICO | VARCHAR2(1) | sim |  |
| USAOBSADICNFE | VARCHAR2(1) | sim |  |
| CODFISCALTP23EST | NUMBER(4) | sim |  |
| CODFISCALTP23INT | NUMBER(4) | sim |  |
| CODFISCALTP24EST | NUMBER(4) | sim |  |
| CODFISCALTP24INT | NUMBER(4) | sim |  |
| CODSETOR66 | NUMBER(5) | sim |  |
| CODSETOR77 | NUMBER(5) | sim |  |
| CODSETOR88 | NUMBER(5) | sim |  |
| NUMMAXVIACH | NUMBER(2) | sim |  |
| CODCONTADESCFORNEC | NUMBER(10) | sim |  |
| CODCONTAJUROFORNEC | NUMBER(10) | sim |  |
| DEFAULTAUT701 | VARCHAR2(1) | sim |  |
| CODBOICASADO | NUMBER(10) | sim |  |
| VLMINDESCDESD | NUMBER(12,2) | sim |  |
| UTCOMTON | VARCHAR2(1) | sim |  |
| ACEITARATEIOPRODOFERTA | VARCHAR2(1) | sim |  |
| VLMAXGER | NUMBER(10,2) | sim |  |
| VLMINGER | NUMBER(10,2) | sim |  |
| ACRESCIMOCOMISSAO | VARCHAR2(1) | sim |  |
| GERARCRECEBERSEMIPI | VARCHAR2(1) | sim |  |
| MOSTRARCODBARRANFE | VARCHAR2(1) | sim |  |
| USACODCONTA | VARCHAR2(1) | sim |  |
| CODHORTIFRUTI | NUMBER(10) | sim |  |
| VERIFICALIMITECRED185 | VARCHAR2(1) | sim |  |
| BLOQBOLETOMENORCEM | VARCHAR2(1) | sim |  |
| USADESCMAXPERM | VARCHAR2(1) | sim |  |
| TRAVAVENSEMESTOQPALM | VARCHAR2(1) | sim |  |
| ZERARLIMITECLIBLOQ | VARCHAR2(1) | sim |  |
| EXCECAOCOMSUMIDOR | VARCHAR2(1) | sim |  |
| DIRPALM | VARCHAR2(50) | sim |  |
| DIRIMPARQ | VARCHAR2(50) | sim |  |
| EXIBIRESTOQUENEGATIVO | VARCHAR2(1) | sim |  |
| USAPALMPOLIBRAS | VARCHAR2(1) | sim |  |
| DIRRETPALM | VARCHAR2(50) | sim |  |
| PEDIDOCANHOTO | VARCHAR2(1) | sim |  |
| EDITADTVENCIMENTO | VARCHAR2(1) | sim |  |
| ENVIAXMLAUTOMATICO | VARCHAR2(1) | sim |  |
| MANIFESTO | VARCHAR2(1) | sim |  |
| NUMDIASPRODNOVO | NUMBER(4) | sim |  |
| ACERTOCLIBLOQ | VARCHAR2(1) | sim |  |
| ATUALIZAQTUNITCX | VARCHAR2(1) | sim |  |
| APLICARDESCICMSPRODUTO | VARCHAR2(1) | sim |  |
| EXIBIRCLIENTEVENDEDOR | VARCHAR2(1) | sim |  |
| ALTERPRECOVENDA | VARCHAR2(1) | sim |  |
| VLMINIMOBOLETO | NUMBER(5,2) | sim |  |
| TPCALCIPI | VARCHAR2(1) | sim |  |
| USAPLANONEGOCIADOEXP | VARCHAR2(1) | sim |  |
| MARCARREPROCESSAMENTO | VARCHAR2(1) | sim |  |
| APLICAVLOUTDESPEMVLOUTRAS | VARCHAR2(1) | sim |  |
| EXIBIRESTOQUECONTGER | VARCHAR2(1) | sim |  |
| PERMITEALTCODCLI | VARCHAR2(1) | sim |  |
| PERMITEACERTOECF | VARCHAR2(1) | sim |  |
| CODSETORCONFERENTE | NUMBER(4) | sim |  |
| CODSETORSEPARADOR | NUMBER(4) | sim |  |
| CONTRPRODUTIVIDADEEXPED | VARCHAR2(1) | sim |  |
| APLICPCOBONIFVENDACUSTO | VARCHAR2(1) | sim |  |
| PERMITEDESCRODAPETV7 | VARCHAR2(1) | sim |  |
| DEVOLFILIALRETIRA | VARCHAR2(1) | sim |  |
| NUMREGTPV6 | NUMBER(4) | sim |  |
| CALCULOST | VARCHAR2(1) | sim |  |
| NUMREGTPV6INT | NUMBER(4) | sim |  |
| CORTEAUTROT56 | VARCHAR2(1) | sim |  |
| PERALTQTD156 | VARCHAR2(1) | sim |  |
| APENASITENSESTFILIAISDEF | VARCHAR2(1) | sim |  |
| ATALHOIMP56CTRLF5 | NUMBER(2) | sim |  |
| ATALHOIMP56SHIFTF5 | NUMBER(2) | sim |  |
| ACEITAFINALIZARENTSEMIMAGEM | VARCHAR2(1) | sim |  |
| GERACPAGARAUTFORNECTRANSP | VARCHAR2(1) | sim |  |
| CODCONTAFORNECTRANSP | NUMBER(10) | sim |  |
| USASTRECALCULOCOMISSAO | VARCHAR2(1) | sim |  |
| ATALHOIMP56F11 | NUMBER(2) | sim |  |
| GERARCPAGARFORNECICMSANT | VARCHAR2(1) | sim |  |
| EXIBIRABADADOSRECEITA | VARCHAR2(1) | sim |  |
| TRANSMITENFEVENDA | VARCHAR2(1) | sim |  |
| FECHACARGAUSUARIOLOGADO | VARCHAR2(1) | sim |  |
| EXIBIRPLANOPAGTOCLIBLOQ | VARCHAR2(1) | sim |  |
| USAAMBIENTEROT56 | VARCHAR2(1) | sim |  |
| TAXAEMBALAGEM | VARCHAR2(1) | sim |  |
| CODCONTTPVENDA17 | NUMBER(10) | sim |  |
| NUMMAXVIASMAPABALCAO | NUMBER(1) | sim |  |
| CODSETOREXECUTOR | NUMBER(4) | sim |  |
| USAEXECUTORROT300 | VARCHAR2(1) | sim |  |
| EXIBIRPVENDAMINROT56 | VARCHAR2(1) | sim |  |
| REPPRECOTRANSFORCAMENTO | VARCHAR2(1) | sim |  |
| VALIDACNPJFILIAL | VARCHAR2(1) | sim |  |
| ALTERDADOSTRANSF | VARCHAR2(1) | sim |  |
| SOLICSENHADESCITEM | VARCHAR2(1) | sim |  |
| EMAILCOTA | VARCHAR2(60) | sim |  |
| HISTCOTA | VARCHAR2(255) | sim |  |
| FONECOTA | VARCHAR2(15) | sim |  |
| ATUALIZCOTA | NUMBER(3) | sim |  |
| ATUALIZFORNECCOTA | NUMBER(3) | sim |  |
| CODSETORSUP | NUMBER(4) | sim |  |
| BAIXAPOROPERADOR185 | VARCHAR2(1) | sim |  |
| TOTSTPRIMEIRAPARC | VARCHAR2(1) | sim |  |
| ACRESCIMOTXBANCARIODESD | VARCHAR2(1) | sim |  |
| USAPROCESSOSEPARACAO | VARCHAR2(1) | sim |  |
| APLICAPTABELAPVENDAPRODSIMILAR | VARCHAR2(1) | sim |  |
| CODPRACAEST | NUMBER(4) | sim |  |
| CODPRACAINT | NUMBER(4) | sim |  |
| CODCONTADESCCH | NUMBER(10) | sim |  |
| CODCONTXCAR | NUMBER(10) | sim |  |
| TIPOCOMISSAO | VARCHAR2(1) | sim |  |
| PERALTCUSTO | NUMBER(5,2) | sim |  |
| BLOQPRODACABADO | VARCHAR2(1) | sim |  |
| PARAMETROCEFASCOMANDA | VARCHAR2(100) | sim |  |
| PERMITETROCAGARCOM | VARCHAR2(1) | sim |  |
| PRECOAUT | VARCHAR2(1) | sim |  |
| HORAUT | VARCHAR2(1) | sim |  |
| TIPOP | VARCHAR2(1) | sim |  |
| CAMINHODIRETORIOROTINAS | VARCHAR2(80) | sim |  |
| USAWMS | VARCHAR2(1) | sim |  |
| PERMITEESTDEPALOCMAX | VARCHAR2(1) | sim |  |
| NUMCASASDECST | NUMBER(2) | sim |  |
| FILIALRETIRAESTOQUEDEP | VARCHAR2(2) | sim |  |
| OBSITEMROT1747 | VARCHAR2(1) | sim |  |
| GRAVARNUMNOTATIPO6 | VARCHAR2(1) | sim |  |
| PERTAXACOMANDA | NUMBER(5,2) | sim |  |
| USADESCCOB | VARCHAR2(1) | sim |  |
| BRINDEHORAINI | VARCHAR2(2) | sim |  |
| BRINDEMININI | VARCHAR2(2) | sim |  |
| BRINDEHORAFIM | VARCHAR2(2) | sim |  |
| BRINDEMINFIM | VARCHAR2(2) | sim |  |
| CADASTROAUTOPRODUTODR736 | VARCHAR2(1) | sim |  |
| VENDACHECKOUT185 | VARCHAR2(1) | sim |  |
| SOLICSENHAFISCALF8IMP | VARCHAR2(1) | sim |  |
| PERMITEPEDIDOFORNECBLOQ | VARCHAR2(1) | sim |  |
| EXIBIRFILIALR1744 | VARCHAR2(1) | sim |  |
| PERMITINSERIRQTMANUAL | VARCHAR2(1) | sim |  |
| ACEITADESDROBRAVENDDIF | VARCHAR2(1) | sim |  |
| DIASVALPROPOSTA | NUMBER(2) | sim |  |
| USAMANIFESTOELETRONICO | VARCHAR2(1) | sim |  |
| CALCOMISSAO444 | VARCHAR2(3) | sim |  |
| HOSTSMTP_CXMALOTE | VARCHAR2(100) | sim |  |
| PORTSMTP_CXMALOTE | VARCHAR2(100) | sim |  |
| USERSMTP_CXMALOTE | VARCHAR2(100) | sim |  |
| SENHASMTP_CXMALOTE | VARCHAR2(100) | sim |  |
| DIRCEFASINVENTARIO | VARCHAR2(60) | sim |  |
| VEROUTROSCONTATOS | VARCHAR2(1) | sim |  |
| TRIBUTACAOFILIAL | VARCHAR2(1) | sim |  |
| GERACRECEBERTP16 | VARCHAR2(1) | sim |  |
| USACREDCOTACAO | VARCHAR2(1) | sim |  |
| INSERQTPRODIGUAL | VARCHAR2(1) | sim |  |
| CODCODTTRANSFENT | NUMBER(10) | sim |  |
| CONTROLABANDEJA | VARCHAR2(1) | sim |  |
| CODPRODBANDEJA | NUMBER(10) | sim |  |
| HABILITARATEIODESCTOT | VARCHAR2(1) | sim |  |
| GERACRECEBERDEVOLDESD | VARCHAR2(1) | sim |  |
| DIREXDADOSCAIXA | VARCHAR2(100) | sim |  |
| USACADRAPCLIENTE | VARCHAR2(1) | sim |  |
| PROXCODCONTABILFORNEC | NUMBER(10) | sim |  |
| BLOQPEDCREDITOCLIENTE | VARCHAR2(1) | sim |  |
| CONTRESTLOTEPROD | VARCHAR2(1) | sim |  |
| USASEPARACAOPEDIDO | VARCHAR2(1) | sim |  |
| USASEPARACAOCONTROLEPEDIDO | VARCHAR2(1) | sim |  |
| INVERTENTREGAFUT | VARCHAR2(1) | sim |  |
| DESCMISTO | VARCHAR2(1) | sim |  |
| INFCHEQUEENT | VARCHAR2(1) | sim |  |
| DIRETORIOIMGAPP | VARCHAR2(100) | sim |  |
| GRAVHIST2CONCBCO | VARCHAR2(1) | sim |  |
| CODPRODSERVICO | NUMBER(10) | sim |  |
| USASPEEDFORTES | VARCHAR2(1) | sim |  |
| OBGINFPESO | VARCHAR2(1) | sim |  |
| ATIVARBLOQPRODSESTOQUE | VARCHAR2(1) | sim |  |
| EXIBIRRELPOSICAOEST | VARCHAR2(1) | sim |  |
| PERDEGUSTACAO | NUMBER(5,2) | sim |  |
| IMPR2VIAFICHATRANSF | VARCHAR2(1) | sim |  |
| UTILIZARTXDESC | VARCHAR2(1) | sim |  |
| ZERARSTDEVOLTP44 | VARCHAR2(1) | sim |  |

### VAREJOANTIGO.NFSAID (484.872 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMNOTA | NUMBER(10) | sim |  |
| SERIE | VARCHAR2(3) | sim |  |
| ESPECIE | VARCHAR2(2) | sim |  |
| DTEMISSAO | DATE | sim |  |
| CODFISCAL | NUMBER(4) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| CODCLI | NUMBER(6) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| CODPLPAG | NUMBER(4) | sim |  |
| NUMCUPOM | NUMBER(10) | sim |  |
| TIPO | NUMBER(2) | sim |  |
| VLCUSTOREAL | NUMBER(12,2) | sim |  |
| VLCUSTOFIN | NUMBER(12,2) | sim |  |
| VLFRETE | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| VLTABELA | NUMBER(12,2) | sim |  |
| TOTPESO | NUMBER(12,2) | sim |  |
| NUMITENS | NUMBER(4) | sim |  |
| OBS | VARCHAR2(40) | sim |  |
| DTCANCEL | DATE | sim |  |
| CODFUNCANCEL | NUMBER(10) | sim |  |
| VLCANCEL | NUMBER(12,2) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| TOTVOLUME | NUMBER(12,2) | sim |  |
| DTSAIDA | DATE | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLST | NUMBER(12,2) | sim |  |
| VLCUSTOCONT | NUMBER(12,2) | sim |  |
| VLTOTCONT | NUMBER(12,2) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| CODPRACA | NUMBER(4) | sim |  |
| FRETEDESPACHO | VARCHAR2(1) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| DTDEVOL | DATE | sim |  |
| VLDEVOL | NUMBER(12,2) | sim |  |
| TIPOVENDA | VARCHAR2(2) | sim |  |
| VLICM | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(12,2) | sim |  |
| VLBASEICM | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| NUMVIAS | NUMBER(2) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| CODDEVOL | NUMBER(4) | sim |  |
| DTENTREGA | DATE | sim |  |
| VLISENTO | NUMBER(12,2) | sim |  |
| NFORIGEM | NUMBER(10) | sim |  |
| VLOUTRASDESP | NUMBER(12,2) | sim |  |
| CODSUPERVISOR | NUMBER(4) | sim |  |
| NUMCOMANDA | NUMBER(10) | sim |  |
| OBS2 | VARCHAR2(40) | sim |  |
| TOTPESOLIQ | NUMBER(12,2) | sim |  |
| CODFORNECTRANSP | NUMBER(6) | sim |  |
| SUBSERIE | VARCHAR2(1) | sim |  |
| CODFUNCVEND | NUMBER(10) | sim |  |
| NUMSERVICO | NUMBER(10) | sim |  |
| VLBASEISS | NUMBER(12,2) | sim |  |
| VLISS | NUMBER(12,2) | sim |  |
| VLDESCBRINDE | NUMBER(12,2) | sim |  |
| NFETPEMIS | VARCHAR2(2) | sim |  |
| DTSTATUS | DATE | sim |  |
| NFEPLACA | VARCHAR2(7) | sim |  |
| NFEUFPLACA | VARCHAR2(2) | sim |  |
| DTNFE | DATE | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| CSTATNFE | VARCHAR2(4) | sim |  |
| RECNFE | VARCHAR2(20) | sim |  |
| NPROTNFE | VARCHAR2(20) | sim |  |
| IDLOTE | VARCHAR2(15) | sim |  |
| MODONFE | VARCHAR2(20) | sim |  |
| DTIMPNFE | DATE | sim |  |
| NFDESTINO | NUMBER(10) | sim |  |
| ENDERENT | VARCHAR2(40) | sim |  |
| BAIRROENT | VARCHAR2(30) | sim |  |
| CIDADEENT | VARCHAR2(40) | sim |  |
| ESTADOENT | VARCHAR2(2) | sim |  |
| CEPENT | VARCHAR2(10) | sim |  |
| TELENT | VARCHAR2(15) | sim |  |
| IEENT | VARCHAR2(15) | sim |  |
| CPFCNPJ | VARCHAR2(18) | sim |  |
| VLDESCICM | NUMBER(12,2) | sim |  |
| VLDESCFIN | NUMBER(12,2) | sim |  |
| VLBASEPIS | NUMBER(12,2) | sim |  |
| VLPIS | NUMBER(12,2) | sim |  |
| VLBASECOFINS | NUMBER(12,2) | sim |  |
| VLCOFINS | NUMBER(12,2) | sim |  |
| ESPECIE2 | VARCHAR2(2) | sim |  |
| STATUS | VARCHAR2(200) | sim |  |
| IMPRESSA | VARCHAR2(3) | sim |  |
| NFE | VARCHAR2(60) | sim |  |
| MSGNFE | VARCHAR2(200) | sim |  |
| NFEQTDEVOL | VARCHAR2(10) | sim |  |
| NFEESPVOL | VARCHAR2(20) | sim |  |
| NFEMARCAVOL | VARCHAR2(30) | sim |  |
| NFEOBS | VARCHAR2(4000) | sim |  |
| NUMDOCIMPORT | NUMBER(15) | sim |  |
| DTREGIMPORT | DATE | sim |  |
| DESCDESEMBARACO | VARCHAR2(100) | sim |  |
| UFDESEMBARACO | VARCHAR2(2) | sim |  |
| DTDESEMBARACO | DATE | sim |  |
| CODEXPSISTINTERNO | NUMBER(10) | sim |  |
| NFEADIC | NUMBER(3) | sim |  |
| NFESEQ | NUMBER(3) | sim |  |
| NFEFABRIC | VARCHAR2(60) | sim |  |
| VLDESCIMPOSTO | NUMBER(12,2) | sim |  |
| ANTT | VARCHAR2(20) | sim |  |
| VLCOMSUP | NUMBER(12,2) | sim |  |
| DTIMPCUPOM | DATE | sim |  |
| DATACONT | VARCHAR2(254) | sim |  |
| JUSTCONT | VARCHAR2(254) | sim |  |
| NFECHAVECONT | VARCHAR2(254) | sim |  |
| NFEUFEMBARQ | VARCHAR2(2) | sim |  |
| NFELOCEMBARQ | VARCHAR2(40) | sim |  |
| CCF | NUMBER(6) | sim |  |
| GNF | NUMBER(6) | sim |  |
| ENTNUMNFPROP | VARCHAR2(1) | sim |  |
| NFSERVICO | VARCHAR2(1) | sim |  |
| VLCANCELPARC | NUMBER(12,2) | sim |  |
| VLSEGURO | NUMBER(12,2) | sim |  |
| EMBALAGEMREGIAO | VARCHAR2(1) | sim |  |
| VLINSS | NUMBER(12,2) | sim |  |
| VLIR | NUMBER(12,2) | sim |  |
| VLCSLL | NUMBER(12,2) | sim |  |
| ORIGEM | VARCHAR2(4) | sim |  |
| CODPARIND | NUMBER(6) | sim |  |
| OBSCCE | VARCHAR2(4000) | sim |  |
| CSTATCCE | VARCHAR2(3) | sim |  |
| NPROTCCE | VARCHAR2(20) | sim |  |
| CPFCNPJCAT52 | VARCHAR2(14) | sim |  |
| VFCPUFDEST | NUMBER(12,2) | sim |  |
| VICMSUFDEST | NUMBER(12,2) | sim |  |
| VICMSUFREMET | NUMBER(12,2) | sim |  |
| CHAVEREFCOMP | VARCHAR2(60) | sim |  |
| DTACERTO | DATE | sim |  |
| OBSACERTO | VARCHAR2(80) | sim |  |
| CODFUNCACERTO | NUMBER(6) | sim |  |
| INDPRES | VARCHAR2(1) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| CSTCREDITOICMS | VARCHAR2(2) | sim |  |
| VLFCP | NUMBER(12,2) | sim |  |
| VLFCPST | NUMBER(12,2) | sim |  |
| VLFCPSTRET | NUMBER(12,2) | sim |  |
| USAMFE | CHAR(1) | sim |  |
| NFGARANTIA | VARCHAR2(1) | sim |  |
| VLBASEICMGARANTIA | NUMBER(12,2) | sim |  |
| VLICMGARANTIA | NUMBER(12,2) | sim |  |
| VLBASESTGARANTIA | NUMBER(12,2) | sim |  |
| VLSTGARANTIA | NUMBER(12,2) | sim |  |
| VLBASEIPIGARANTIA | NUMBER(12,2) | sim |  |
| VLIPIGARANTIA | NUMBER(12,2) | sim |  |
| VLBASEFCP | NUMBER(12,2) | sim |  |
| VLBASEFCPST | NUMBER(12,2) | sim |  |
| VLBASEFCPSTRET | NUMBER(12,2) | sim |  |
| CODFUNCF11LIB | NUMBER(10) | sim |  |
| CSTATNFEAUX | VARCHAR2(4) | sim |  |
| CODATEND1 | NUMBER(10) | sim |  |
| CODATEND2 | NUMBER(10) | sim |  |
| CODATEND3 | NUMBER(10) | sim |  |
| CODATEND4 | NUMBER(10) | sim |  |
| DUPLICOUTP12 | VARCHAR2(1) | sim |  |
| NFDESTINOCODCLI | NUMBER(10) | sim |  |
| XMLPDFENVIADO | VARCHAR2(1) | sim |  |
| VLICMSDES | NUMBER(12,2) | sim |  |
| TIPOCREDITOICMS | VARCHAR2(13) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| USADEVOLTRANSF | VARCHAR2(1) | sim |  |
| VLICMDIF | NUMBER(12,2) | sim |  |
| CPFCNPJSAID | VARCHAR2(18) | sim |  |
| DIFEMBREGIAO | VARCHAR2(1) | sim |  |
| VLFRETEPAGO | NUMBER(12,2) | sim |  |
| SAIDAAVARIA | VARCHAR2(1) | sim |  |
| SRSIMPLESFATURA | VARCHAR2(1) | sim |  |
| NUMLANCCPAGARDESCFIN | NUMBER(10) | sim |  |
| VLBONIFICACAO | NUMBER(12,2) | sim |  |
| FRETEBONIF | NUMBER(12,2) | sim |  |
| VLFRETECOTADO | NUMBER(12,2) | sim |  |
| CSOSN_CREDITOICMS | NUMBER(3) | sim |  |
| VLCREDUSADO | NUMBER(12,2) | sim |  |
| NCONTRATOCONSIG | NUMBER(10) | sim |  |
| VERSAOROTINA | VARCHAR2(20) | sim |  |
| CNPJINTERMEDIADOR | VARCHAR2(14) | sim |  |
| INTERMEDIADOR | VARCHAR2(60) | sim |  |
| NFTERCEIRO | VARCHAR2(1) | sim |  |

### SEVERIANO.LOGFLEXIVEL (455.172 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| ID | NUMBER(10) | não |  |
| CODVEND | NUMBER(10) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| DATA | DATE | sim |  |
| SALDOANTERIOR | NUMBER(12,2) | sim |  |
| VLINSERIDO | NUMBER(12,2) | sim |  |
| SALDOATUAL | NUMBER(12,2) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| STATUSOBS | VARCHAR2(100) | sim |  |

### SEVERIANO.NFBASE (451.303 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMENT | NUMBER(10) | não |  |
| CODCONT | NUMBER(10) | não |  |
| VLBASE | NUMBER(12,2) | sim |  |
| PERICM | NUMBER(5,2) | não |  |
| VLICM | NUMBER(12,2) | sim |  |
| CODFISCAL | NUMBER(4) | não |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLST | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(12,2) | sim |  |
| VLISENTO | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| VLBASEPIS | NUMBER(12,2) | sim |  |
| VLBASECOFINS | NUMBER(12,2) | sim |  |
| VLPIS | NUMBER(12,2) | sim |  |
| VLCOFINS | NUMBER(12,2) | sim |  |
| PERPIS | NUMBER(8,6) | sim |  |
| PERCOFINS | NUMBER(8,6) | sim |  |
| AAA | VARCHAR2(1) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| VLFCPST | NUMBER(12,2) | sim |  |
| VLBASEFCPST | NUMBER(12,2) | sim |  |
| CSTCREDITOICMS | VARCHAR2(2) | sim |  |
| CSOSN_CREDITOICMS | NUMBER(3) | sim |  |

### JP.LOGALTCUSTO (446.318 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CODPROD | NUMBER(10) | não |  |
| CODFILIAL | VARCHAR2(2) | não |  |
| CODFUNC | NUMBER(10) | sim |  |
| DATA | DATE | não |  |
| CUSTOREALANT | NUMBER(12,3) | sim |  |
| CUSTOFINANT | NUMBER(12,3) | sim |  |
| CUSTOCONTANT | NUMBER(12,3) | sim |  |
| CUSTOREAL | NUMBER(12,3) | sim |  |
| CUSTOFIN | NUMBER(12,3) | sim |  |
| CUSTOCONT | NUMBER(12,3) | sim |  |
| MOTIVO | VARCHAR2(40) | sim |  |
| CODPROG | VARCHAR2(4) | sim |  |
| FRETEADICIONAL | NUMBER(16,4) | sim | CAMPO USADO PARA GRAVAR FRETE ADICIONAL ATUAL |
| FRETEADICIONAL_ANT | NUMBER(16,4) | sim | CAMPO USADO PARA GRAVAR FRETE ADICIONAL ANTERIOR |

### VAREJOANTIGO.LOG_ALTER_CRECEBER (393.955 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| ID | NUMBER | não |  |
| DATADOLOG | DATE | sim |  |
| USERNAME | VARCHAR2(200) | sim |  |
| MACHINE | VARCHAR2(200) | sim |  |
| PROGRAM | VARCHAR2(200) | sim |  |
| MODULE | VARCHAR2(200) | sim |  |
| TERMINAL | VARCHAR2(200) | sim |  |
| IP | VARCHAR2(200) | sim |  |
| NUMVENDA | NUMBER(10) | não |  |
| NUMNOTA | NUMBER(10) | sim |  |
| PREST | NUMBER(3) | não |  |
| CODCLI | NUMBER(6) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| DTEMISSAO | DATE | sim |  |
| DTVENC | DATE | sim |  |
| VALOR | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLJURO | NUMBER(12,2) | sim |  |
| DTPAGO | DATE | sim |  |
| VPAGO | NUMBER(12,2) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| NUMBCO | VARCHAR2(4) | sim |  |
| NUMAG | VARCHAR2(4) | sim |  |
| NUMCH | VARCHAR2(8) | sim |  |
| NUMCART | VARCHAR2(15) | sim |  |
| DTFECHA | DATE | sim |  |
| OBS | VARCHAR2(2000) | sim |  |
| CODCXBCO | NUMBER(4) | sim |  |
| CODFUNCFECHA | NUMBER(10) | sim |  |
| DTBAIXA | DATE | sim |  |
| NUMCONTA | VARCHAR2(15) | sim |  |
| CODCXBCOP | NUMBER(4) | sim |  |
| VLAUX | NUMBER(12,2) | sim |  |
| TOTPREST | NUMBER(3) | sim |  |
| DTULTALT | DATE | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| PERCOM | NUMBER(7,4) | sim |  |
| NOSSNUMBCO | VARCHAR2(14) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| DTDESD | DATE | sim |  |
| CODFUNCDESD | NUMBER(10) | sim |  |
| CODFUNCBAIXA | NUMBER(10) | sim |  |
| VALORDEV | NUMBER(12,2) | sim |  |
| OBS2 | VARCHAR2(100) | sim |  |
| NUMLANCPG | NUMBER(10) | sim |  |
| NOSSONUMBCO | VARCHAR2(20) | sim |  |
| CODBARRA | VARCHAR2(44) | sim |  |
| LINHADIG | VARCHAR2(65) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| VLTXBOLETO | NUMBER(12,2) | sim |  |
| STATUS | VARCHAR2(1) | sim |  |
| VALORORIG | NUMBER(12,2) | sim |  |
| PROTOCOLO | NUMBER(10) | sim |  |
| TURNO | VARCHAR2(1) | sim |  |
| DTVENCORIG | DATE | sim |  |
| CODCOBORIG | VARCHAR2(4) | sim |  |
| CODSUPERVISOR | NUMBER(4) | sim |  |
| PR | VARCHAR2(2) | sim |  |
| DTULTALTER | DATE | sim |  |
| DTCXMOT | DATE | sim |  |
| CODFUNCCXMOT | NUMBER(10) | sim |  |
| NUMTRANS | NUMBER(10) | sim |  |
| CODCOBCXBCO | VARCHAR2(4) | sim |  |
| CODFUNCVALE | NUMBER(10) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| OPERACAO | VARCHAR2(1) | sim |  |
| CODBAIXA | NUMBER(4) | sim |  |
| ALINEA | VARCHAR2(4) | sim |  |
| NUMVENDADESD | NUMBER(10) | sim |  |
| NUMFATURA | NUMBER(10) | sim |  |
| DTFECHAPROT | DATE | sim |  |
| DTCXMOTPROT | DATE | sim |  |
| CODFUNCFECHAPROT | NUMBER(10) | sim |  |
| TIPOPRORROG | VARCHAR2(1) | sim |  |
| DTPRORROG | DATE | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| NUMCUSTODIA | NUMBER(8) | sim |  |
| DTCUSTODIA | DATE | sim |  |
| CODCXBCOCUSTODIA | NUMBER(4) | sim |  |
| DTPREVPAGTO | DATE | sim |  |
| PRESTDESD | NUMBER(3) | sim |  |
| DTESTORNO | DATE | sim |  |
| CODFUNCESTORNO | NUMBER(10) | sim |  |
| DIGITAO | VARCHAR2(1) | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| LIBERARVENDALIMCRED | VARCHAR2(1) | sim |  |
| RETBOLTIPOREG | NUMBER(2) | sim |  |
| RETBOLCODINSC | NUMBER(3) | sim |  |
| RETBOLNUMINSC | NUMBER(20) | sim |  |
| RETBOLAGENCIA | NUMBER(6) | sim |  |
| RETBOLCONTA | NUMBER(10) | sim |  |
| RETBOLDAC | VARCHAR2(1) | sim |  |
| RETBOLCODOCORRENCIA | NUMBER(4) | sim |  |
| RETBOLDTOCORRENCIA | DATE | sim |  |
| RETBOLNOSSONUMCONF | NUMBER(15) | sim |  |
| RETBOLDTVENCIMENTO | DATE | sim |  |
| RETBOLVALORTITULO | NUMBER(15,2) | sim |  |
| RETBOLCODBCO | NUMBER(4) | sim |  |
| RETBOLAGCOB | NUMBER(6) | sim |  |
| RETBOLDACAGCOB | VARCHAR2(1) | sim |  |
| RETBOLESPECIE | NUMBER(3) | sim |  |
| RETBOLTARIFACOB | NUMBER(15,2) | sim |  |
| RETBOLVALORIOF | NUMBER(15,2) | sim |  |
| RETBOLVALORABAT | NUMBER(15,2) | sim |  |
| RETBOLDESCONTOS | NUMBER(15,2) | sim |  |
| RETBOLVALORPRINC | NUMBER(15,2) | sim |  |
| RETBOLJUROSMORAMULTA | NUMBER(15,2) | sim |  |
| RETBOLOUTROSCREDITOS | NUMBER(15,2) | sim |  |
| RETBOLDTCREDITO | DATE | sim |  |
| RETBOLINSTRCANCEL | NUMBER(6) | sim |  |
| RETBOLNOMESACADO | VARCHAR2(40) | sim |  |
| RETBOLERROS | VARCHAR2(10) | sim |  |
| RETBOLCODLIQ | VARCHAR2(4) | sim |  |
| RETBOLNUMSEQ | NUMBER(10) | sim |  |
| RETBOLBAIXADO | VARCHAR2(1) | sim |  |
| RETBOLDVAG | VARCHAR2(3) | sim |  |
| DTFECHACHECKOUT | DATE | sim |  |
| VLDESCICMPARC | NUMBER(12,2) | sim |  |
| VLDESCFIN | NUMBER(12,2) | sim |  |
| DTTRANSMISSAO | DATE | sim |  |
| PERCOMSUP | NUMBER(7,4) | sim |  |
| VLDESCTXCAR | NUMBER(12,2) | sim |  |
| NUMPROM | VARCHAR2(20) | sim |  |
| TAXA | NUMBER(12,2) | sim |  |
| CODEMITENTE | NUMBER(10) | sim |  |
| BANDEIRA | VARCHAR2(60) | sim |  |
| TIPO_TRANSACAO | VARCHAR2(15) | sim |  |
| NSU | VARCHAR2(30) | sim |  |
| AUTORIZACAO | VARCHAR2(20) | sim |  |
| ESTABELECIMENTO | VARCHAR2(20) | sim |  |
| NUMEROCARTAO | VARCHAR2(30) | sim |  |
| ORIGEM | VARCHAR2(10) | sim |  |
| MODOBAIXA | VARCHAR2(1) | sim |  |
| DTBAIXACAR | DATE | sim |  |
| TRANSBAIXAAUTO | NUMBER(15) | sim |  |
| PRESTCAR | NUMBER(3) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| LANCR28 | VARCHAR2(1) | sim |  |
| TECLACOB | VARCHAR2(6) | sim |  |
| NUMTRANSMISSAO | NUMBER(14) | sim |  |
| VLMULTA | NUMBER(12,2) | sim |  |
| PDFENVIADO | VARCHAR2(1) | sim |  |

### VAREJOANTIGO.HISTESTOQUE (305.096 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CODFILIAL | VARCHAR2(2) | não |  |
| CODPROD | NUMBER(10) | não |  |
| DATA | DATE | não |  |
| QTEST | NUMBER(18,6) | sim |  |
| QTESTGER | NUMBER(18,6) | sim |  |
| CUSTOULTENT | NUMBER(18,6) | sim |  |
| CUSTOREAL | NUMBER(18,6) | sim |  |
| CUSTOFIN | NUMBER(18,6) | sim |  |
| CUSTOCONT | NUMBER(18,6) | sim |  |
| VLCUSTOREAL | NUMBER(12,2) | sim |  |
| VLCUSTOFIN | NUMBER(12,2) | sim |  |
| QTVENDA | NUMBER(12,3) | sim |  |
| VLVENDA | NUMBER(12,2) | sim |  |
| QTRESERV | NUMBER(18,6) | sim |  |
| QTINDENIZ | NUMBER(18,6) | sim |  |
| QTBLOQUEADA | NUMBER(18,6) | sim |  |
| QTDEVOL | NUMBER(12,3) | sim |  |
| VLDEVOL | NUMBER(12,2) | sim |  |
| CODFUNCREPROC | NUMBER(10) | sim |  |
| DTREPROC | DATE | sim |  |
| PTABELA | NUMBER(18,6) | sim |  |

### SEVERIANO.CRECEBER (270.619 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMNOTA | NUMBER(10) | sim |  |
| PREST | NUMBER(3) | não |  |
| CODCLI | NUMBER(6) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| DTEMISSAO | DATE | sim |  |
| DTVENC | DATE | sim |  |
| VALOR | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLJURO | NUMBER(12,2) | sim |  |
| DTPAGO | DATE | sim |  |
| VPAGO | NUMBER(12,2) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| NUMBCO | VARCHAR2(4) | sim |  |
| NUMAG | VARCHAR2(4) | sim |  |
| NUMCH | VARCHAR2(8) | sim |  |
| NUMCART | VARCHAR2(15) | sim |  |
| DTFECHA | DATE | sim |  |
| OBS | VARCHAR2(2000) | sim |  |
| CODCXBCO | NUMBER(4) | sim |  |
| CODFUNCFECHA | NUMBER(10) | sim |  |
| DTBAIXA | DATE | sim |  |
| NUMCONTA | VARCHAR2(15) | sim |  |
| CODCXBCOP | NUMBER(4) | sim |  |
| VLAUX | NUMBER(12,2) | sim |  |
| TOTPREST | NUMBER(3) | sim |  |
| DTULTALT | DATE | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| PERCOM | NUMBER(7,4) | sim |  |
| NOSSNUMBCO | VARCHAR2(14) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| DTDESD | DATE | sim |  |
| CODFUNCDESD | NUMBER(10) | sim |  |
| CODFUNCBAIXA | NUMBER(10) | sim |  |
| VALORDEV | NUMBER(12,2) | sim |  |
| OBS2 | VARCHAR2(100) | sim |  |
| NUMLANCPG | NUMBER(10) | sim |  |
| NOSSONUMBCO | VARCHAR2(20) | sim |  |
| CODBARRA | VARCHAR2(44) | sim |  |
| LINHADIG | VARCHAR2(65) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| VLTXBOLETO | NUMBER(12,2) | sim |  |
| STATUS | VARCHAR2(1) | sim |  |
| VALORORIG | NUMBER(12,2) | sim |  |
| PROTOCOLO | NUMBER(10) | sim |  |
| TURNO | VARCHAR2(1) | sim |  |
| DTVENCORIG | DATE | sim |  |
| CODCOBORIG | VARCHAR2(4) | sim |  |
| CODSUPERVISOR | NUMBER(4) | sim |  |
| PR | VARCHAR2(2) | sim |  |
| DTULTALTER | DATE | sim |  |
| DTCXMOT | DATE | sim |  |
| CODFUNCCXMOT | NUMBER(10) | sim |  |
| NUMTRANS | NUMBER(10) | sim |  |
| CODCOBCXBCO | VARCHAR2(4) | sim |  |
| CODFUNCVALE | NUMBER(10) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| OPERACAO | VARCHAR2(1) | sim |  |
| CODBAIXA | NUMBER(4) | sim |  |
| ALINEA | VARCHAR2(4) | sim |  |
| NUMVENDADESD | NUMBER(10) | sim |  |
| NUMFATURA | NUMBER(10) | sim |  |
| DTFECHAPROT | DATE | sim |  |
| DTCXMOTPROT | DATE | sim |  |
| CODFUNCFECHAPROT | NUMBER(10) | sim |  |
| TIPOPRORROG | VARCHAR2(1) | sim |  |
| DTPRORROG | DATE | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| NUMCUSTODIA | NUMBER(8) | sim |  |
| DTCUSTODIA | DATE | sim |  |
| CODCXBCOCUSTODIA | NUMBER(4) | sim |  |
| DTPREVPAGTO | DATE | sim |  |
| PRESTDESD | NUMBER(3) | sim |  |
| DTESTORNO | DATE | sim |  |
| CODFUNCESTORNO | NUMBER(10) | sim |  |
| DIGITAO | VARCHAR2(1) | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| LIBERARVENDALIMCRED | VARCHAR2(1) | sim |  |
| RETBOLTIPOREG | NUMBER(2) | sim |  |
| RETBOLCODINSC | NUMBER(3) | sim |  |
| RETBOLNUMINSC | NUMBER(20) | sim |  |
| RETBOLAGENCIA | NUMBER(6) | sim |  |
| RETBOLCONTA | NUMBER(10) | sim |  |
| RETBOLDAC | VARCHAR2(1) | sim |  |
| RETBOLCODOCORRENCIA | NUMBER(4) | sim |  |
| RETBOLDTOCORRENCIA | DATE | sim |  |
| RETBOLNOSSONUMCONF | NUMBER(15) | sim |  |
| RETBOLDTVENCIMENTO | DATE | sim |  |
| RETBOLVALORTITULO | NUMBER(15,2) | sim |  |
| RETBOLCODBCO | NUMBER(4) | sim |  |
| RETBOLAGCOB | NUMBER(6) | sim |  |
| RETBOLDACAGCOB | VARCHAR2(1) | sim |  |
| RETBOLESPECIE | NUMBER(3) | sim |  |
| RETBOLTARIFACOB | NUMBER(15,2) | sim |  |
| RETBOLVALORIOF | NUMBER(15,2) | sim |  |
| RETBOLVALORABAT | NUMBER(15,2) | sim |  |
| RETBOLDESCONTOS | NUMBER(15,2) | sim |  |
| RETBOLVALORPRINC | NUMBER(15,2) | sim |  |
| RETBOLJUROSMORAMULTA | NUMBER(15,2) | sim |  |
| RETBOLOUTROSCREDITOS | NUMBER(15,2) | sim |  |
| RETBOLDTCREDITO | DATE | sim |  |
| RETBOLINSTRCANCEL | NUMBER(6) | sim |  |
| RETBOLNOMESACADO | VARCHAR2(40) | sim |  |
| RETBOLERROS | VARCHAR2(115) | sim |  |
| RETBOLCODLIQ | VARCHAR2(4) | sim |  |
| RETBOLNUMSEQ | NUMBER(10) | sim |  |
| RETBOLBAIXADO | VARCHAR2(1) | sim |  |
| RETBOLDVAG | VARCHAR2(3) | sim |  |
| DTFECHACHECKOUT | DATE | sim |  |
| VLDESCICMPARC | NUMBER(12,2) | sim |  |
| VLDESCFIN | NUMBER(12,2) | sim |  |
| DTTRANSMISSAO | DATE | sim |  |
| PERCOMSUP | NUMBER(7,4) | sim |  |
| VLDESCTXCAR | NUMBER(12,2) | sim |  |
| NUMPROM | VARCHAR2(20) | sim |  |
| TAXA | NUMBER(12,2) | sim |  |
| CODEMITENTE | NUMBER(10) | sim |  |
| BANDEIRA | VARCHAR2(60) | sim |  |
| TIPO_TRANSACAO | VARCHAR2(15) | sim |  |
| NSU | VARCHAR2(30) | sim |  |
| AUTORIZACAO | VARCHAR2(20) | sim |  |
| ESTABELECIMENTO | VARCHAR2(20) | sim |  |
| NUMEROCARTAO | VARCHAR2(30) | sim |  |
| ORIGEM | VARCHAR2(10) | sim |  |
| AAA | VARCHAR2(1) | sim |  |
| MODOBAIXA | VARCHAR2(1) | sim |  |
| DTBAIXACAR | DATE | sim |  |
| TRANSBAIXAAUTO | NUMBER(15) | sim |  |
| PRESTCAR | NUMBER(3) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| LANCR28 | VARCHAR2(1) | sim |  |
| TECLACOB | VARCHAR2(6) | sim |  |
| NUMTRANSMISSAO | NUMBER(14) | sim |  |
| VLMULTA | NUMBER(12,2) | sim |  |
| PDFENVIADO | VARCHAR2(1) | sim |  |
| CODVEND2 | NUMBER(10) | sim |  |
| DTFECHAR185 | DATE | sim |  |
| DESCDEV | NUMBER(12,2) | sim |  |
| VLTARIFA | NUMBER(12,2) | sim |  |
| DTPAGODESCONTO | DATE | sim |  |
| DTESTORNODESCONTO | DATE | sim |  |
| VPAGODESCONTO | NUMBER(12,2) | sim |  |
| CODFUNCPAGODESCONTO | NUMBER(10) | sim |  |
| CODFUNCESTORNODESCONTO | NUMBER(10) | sim |  |
| CODPLPAG_CR | NUMBER(4) | sim |  |

### JP.CABPED (265.104 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMPED | NUMBER(10) | não |  |
| CODCLI | NUMBER(6) | sim |  |
| CODPLPAG | NUMBER(4) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| DTEMISSAO | DATE | sim |  |
| DTPREVENT | DATE | sim |  |
| TIPO | VARCHAR2(2) | sim |  |
| OBS | VARCHAR2(1000) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| TOTPESO | NUMBER(12,2) | sim |  |
| TOTVOLUME | NUMBER(12,2) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| VLCUSTOREAL | NUMBER(12,2) | sim |  |
| VLFRETE | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| VLTABELA | NUMBER(12,2) | sim |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| POSICAO | VARCHAR2(1) | sim |  |
| TPENTREGA | VARCHAR2(1) | sim |  |
| NUMITENS | NUMBER(4) | sim |  |
| POSICAOENT | VARCHAR2(1) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| ENDERENT | VARCHAR2(60) | sim |  |
| BAIRROENT | VARCHAR2(60) | sim |  |
| CIDADEENT | VARCHAR2(40) | sim |  |
| ESTADOENT | VARCHAR2(2) | sim |  |
| CEPENT | VARCHAR2(10) | sim |  |
| TELENT | VARCHAR2(15) | sim |  |
| CODPRACA | NUMBER(4) | sim |  |
| CODFORNEC | NUMBER(6) | sim |  |
| INDICE | NUMBER(5,2) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| NUMVENDA | NUMBER(10) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| CODFUNCCAN | NUMBER(10) | sim |  |
| DTCANCEL | DATE | sim |  |
| OBS2 | VARCHAR2(1000) | sim |  |
| CLIENTE | VARCHAR2(70) | sim |  |
| CPFCNPJ | VARCHAR2(18) | sim |  |
| FRETEDESPACHO | VARCHAR2(1) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| NUMVIAS | NUMBER(2) | sim |  |
| CODVEICULO | NUMBER(6) | sim |  |
| CODTABNEGOCIACAO | NUMBER(2) | sim |  |
| DTINICIO | DATE | sim |  |
| HORAINICIO | NUMBER(2) | sim |  |
| MINUTOINICIO | NUMBER(2) | sim |  |
| DTFIM | DATE | sim |  |
| HORAFIM | NUMBER(2) | sim |  |
| MINUTOFIM | NUMBER(2) | sim |  |
| VLTOTPROD | NUMBER(12,2) | sim |  |
| PRAZO1 | NUMBER(4) | sim |  |
| PRAZO2 | NUMBER(4) | sim |  |
| PRAZO3 | NUMBER(4) | sim |  |
| PRAZO4 | NUMBER(4) | sim |  |
| PRAZO5 | NUMBER(4) | sim |  |
| PRAZO6 | NUMBER(4) | sim |  |
| PRAZO7 | NUMBER(4) | sim |  |
| PRAZO8 | NUMBER(4) | sim |  |
| PRAZO9 | NUMBER(4) | sim |  |
| PRAZO10 | NUMBER(4) | sim |  |
| PRAZO11 | NUMBER(4) | sim |  |
| PRAZO12 | NUMBER(4) | sim |  |
| PRAZOMD | NUMBER(12,2) | sim |  |
| QTVOL | NUMBER(12,2) | sim |  |
| TPBALCAOTLMK | VARCHAR2(1) | sim |  |
| OBS3 | VARCHAR2(1000) | sim |  |
| OBS4 | VARCHAR2(1000) | sim |  |
| OBSENTREGA1 | VARCHAR2(100) | sim |  |
| OBSENTREGA2 | VARCHAR2(100) | sim |  |
| OBSENTREGA3 | VARCHAR2(100) | sim |  |
| OBSENTREGA4 | VARCHAR2(100) | sim |  |
| OBSENTREGA5 | VARCHAR2(100) | sim |  |
| OBSENTREGA6 | VARCHAR2(100) | sim |  |
| OBSENTREGA7 | VARCHAR2(100) | sim |  |
| OBSENTREGA8 | VARCHAR2(100) | sim |  |
| OBSENTREGA9 | VARCHAR2(100) | sim |  |
| NUMSEQENTREGA | NUMBER(20) | sim |  |
| VLOUTRASDESP | NUMBER(12,2) | sim |  |
| VLCUSTOFIN | NUMBER(12,2) | sim |  |
| HORA | NUMBER(2) | sim |  |
| MINUTO | NUMBER(2) | sim |  |
| CODFILIALRETIRA | VARCHAR2(2) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| VLTOTALORIG | NUMBER(12,2) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| NUMCUPOM | NUMBER(10) | sim |  |
| IEENT | VARCHAR2(15) | sim |  |
| OBSENTREGA10 | VARCHAR2(75) | sim |  |
| OBSENTREGA11 | VARCHAR2(75) | sim |  |
| NUMPROCESSO | NUMBER(15) | sim |  |
| CODPARIND | NUMBER(6) | sim |  |
| NUMPEDORIG | NUMBER(10) | sim |  |
| TOTPESOLIQ | NUMBER(12,2) | sim |  |
| KMOS | NUMBER(12) | sim |  |
| NUMPEDORIGREMENTFUT | NUMBER(10) | sim |  |
| NUMVIASRECIBOENTMERC | NUMBER(4) | sim |  |
| VLDESCBRINDE | NUMBER(12,2) | sim |  |
| PRAZO13 | NUMBER(4) | sim |  |
| PRAZO14 | NUMBER(4) | sim |  |
| PRAZO15 | NUMBER(4) | sim |  |
| PRAZO16 | NUMBER(4) | sim |  |
| PRAZO17 | NUMBER(4) | sim |  |
| PRAZO18 | NUMBER(4) | sim |  |
| PRAZO19 | NUMBER(4) | sim |  |
| PRAZO20 | NUMBER(4) | sim |  |
| PRAZO21 | NUMBER(4) | sim |  |
| PRAZO22 | NUMBER(4) | sim |  |
| PRAZO23 | NUMBER(4) | sim |  |
| PRAZO24 | NUMBER(4) | sim |  |
| RESERVARESTOQUEORCAMENTO | VARCHAR2(1) | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| STATUS | VARCHAR2(2) | sim |  |
| NUMVIAGEM | NUMBER(10) | sim |  |
| NUMNOTADEST | NUMBER(10) | sim |  |
| VLTOTALNFDEST | NUMBER(12,2) | sim |  |
| PESONFDEST | NUMBER(12,2) | sim |  |
| VOLUMENFDEST | NUMBER(12,2) | sim |  |
| NUMNOTADEST2 | NUMBER(10) | sim |  |
| VLTOTALNFDEST2 | NUMBER(12,2) | sim |  |
| PESONFDEST2 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST2 | NUMBER(12,2) | sim |  |
| NUMNOTADEST3 | NUMBER(10) | sim |  |
| VLTOTALNFDEST3 | NUMBER(12,2) | sim |  |
| PESONFDEST3 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST3 | NUMBER(12,2) | sim |  |
| NUMNOTADEST4 | NUMBER(10) | sim |  |
| VLTOTALNFDEST4 | NUMBER(12,2) | sim |  |
| PESONFDEST4 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST4 | NUMBER(12,2) | sim |  |
| NUMNOTADEST5 | NUMBER(10) | sim |  |
| VLTOTALNFDEST5 | NUMBER(12,2) | sim |  |
| PESONFDEST5 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST5 | NUMBER(12,2) | sim |  |
| CODCONSIGNAT | NUMBER(6) | sim |  |
| NUMNOTATP12 | NUMBER(10) | sim |  |
| NUMPROD | NUMBER(10) | sim |  |
| NUMNOTADEST6 | NUMBER(10) | sim |  |
| VLTOTALNFDEST6 | NUMBER(12,2) | sim |  |
| PESONFDEST6 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST6 | NUMBER(12,2) | sim |  |
| NUMNOTADEST7 | NUMBER(10) | sim |  |
| VLTOTALNFDEST7 | NUMBER(12,2) | sim |  |
| PESONFDEST7 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST7 | NUMBER(12,2) | sim |  |
| NUMNOTADEST8 | NUMBER(10) | sim |  |
| VLTOTALNFDEST8 | NUMBER(12,2) | sim |  |
| PESONFDEST8 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST8 | NUMBER(12,2) | sim |  |
| NUMNOTADEST9 | NUMBER(10) | sim |  |
| VLTOTALNFDEST9 | NUMBER(12,2) | sim |  |
| PESONFDEST9 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST9 | NUMBER(12,2) | sim |  |
| NUMNOTADEST10 | NUMBER(10) | sim |  |
| VLTOTALNFDEST10 | NUMBER(12,2) | sim |  |
| PESONFDEST10 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST10 | NUMBER(12,2) | sim |  |
| NUMNOTADEST11 | NUMBER(10) | sim |  |
| VLTOTALNFDEST11 | NUMBER(12,2) | sim |  |
| PESONFDEST11 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST11 | NUMBER(12,2) | sim |  |
| NUMNOTADEST12 | NUMBER(10) | sim |  |
| VLTOTALNFDEST12 | NUMBER(12,2) | sim |  |
| PESONFDEST12 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST12 | NUMBER(12,2) | sim |  |
| NUMNOTADEST13 | NUMBER(10) | sim |  |
| VLTOTALNFDEST13 | NUMBER(12,2) | sim |  |
| PESONFDEST13 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST13 | NUMBER(12,2) | sim |  |
| NUMNOTADEST14 | NUMBER(10) | sim |  |
| VLTOTALNFDEST14 | NUMBER(12,2) | sim |  |
| PESONFDEST14 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST14 | NUMBER(12,2) | sim |  |
| NUMNOTADEST15 | NUMBER(10) | sim |  |
| VLTOTALNFDEST15 | NUMBER(12,2) | sim |  |
| PESONFDEST15 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST15 | NUMBER(12,2) | sim |  |
| NUMNOTADEST16 | NUMBER(10) | sim |  |
| VLTOTALNFDEST16 | NUMBER(12,2) | sim |  |
| PESONFDEST16 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST16 | NUMBER(12,2) | sim |  |
| NUMNOTADEST17 | NUMBER(10) | sim |  |
| VLTOTALNFDEST17 | NUMBER(12,2) | sim |  |
| PESONFDEST17 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST17 | NUMBER(12,2) | sim |  |
| NUMNOTADEST18 | NUMBER(10) | sim |  |
| VLTOTALNFDEST18 | NUMBER(12,2) | sim |  |
| PESONFDEST18 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST18 | NUMBER(12,2) | sim |  |
| NUMNOTADEST19 | NUMBER(10) | sim |  |
| VLTOTALNFDEST19 | NUMBER(12,2) | sim |  |
| PESONFDEST19 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST19 | NUMBER(12,2) | sim |  |
| NUMNOTADEST20 | NUMBER(10) | sim |  |
| VLTOTALNFDEST20 | NUMBER(12,2) | sim |  |
| PESONFDEST20 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST20 | NUMBER(12,2) | sim |  |
| POTENCIATRANSF | NUMBER(10,6) | sim |  |
| MARCATRANSF | VARCHAR2(40) | sim |  |
| NUMSERIETRANSF | VARCHAR2(25) | sim |  |
| TENSAOAT1TRANSF | VARCHAR2(6) | sim |  |
| TENSAOAT2TRANSF | VARCHAR2(6) | sim |  |
| TENSAOBT1TRANSF | VARCHAR2(3) | sim |  |
| TENSAOBT2TRANSF | VARCHAR2(3) | sim |  |
| NUMTAPETRANSF | VARCHAR2(20) | sim |  |
| TAPEATUALTRANSF | VARCHAR2(20) | sim |  |
| VOLOLEOTRANSF | NUMBER(10,6) | sim |  |
| ANOFABTRANSF | VARCHAR2(4) | sim |  |
| IMPEDANCIATRANSF | NUMBER(10,6) | sim |  |
| TIPOTRANSF | VARCHAR2(20) | sim |  |
| NUMCELGTRANSF | VARCHAR2(20) | sim |  |
| CABINEPOSTETRANSF | VARCHAR2(1) | sim |  |
| PESOTRANSF | NUMBER(10,6) | sim |  |
| CODMOTORISTA | NUMBER(6) | sim |  |
| RPMTRANSF | NUMBER(10,4) | sim |  |
| MONOFASICO | VARCHAR2(1) | sim |  |
| TIPOMOTORTRANSF | VARCHAR2(1) | sim |  |
| DESCTIPOMOTORTRANSF | VARCHAR2(255) | sim |  |
| CODAGRONOMO | NUMBER(6) | sim |  |
| LOCALAPLIC | VARCHAR2(30) | sim |  |
| CULTURA | VARCHAR2(20) | sim |  |
| DIAGNOSTICO | VARCHAR2(300) | sim |  |
| AREA | VARCHAR2(15) | sim |  |
| PRAGA | VARCHAR2(30) | sim |  |
| ANTIDOTO | VARCHAR2(30) | sim |  |
| CODMUNICIPIO | NUMBER(7) | sim |  |
| NATUREZAFRETE | VARCHAR2(30) | sim |  |
| NUMRECEITA | NUMBER(10) | sim |  |
| DTLIBPED | DATE | sim |  |
| GARANTIA | VARCHAR2(1) | sim |  |
| VLDEBCREDRCA | NUMBER(12,2) | sim |  |
| NUMTRANSPEDIDO | NUMBER(10) | sim |  |
| NUMPEDRCA0 | NUMBER(10) | sim |  |
| NUMPEDRCA | NUMBER(20) | sim |  |
| VLTOTALST | NUMBER(12,2) | sim |  |
| VLSEGURO | NUMBER(12,2) | sim |  |
| DTAUTORC | DATE | sim |  |
| CODFUNCORC | NUMBER(10) | sim |  |
| CODDIG | NUMBER(10) | sim |  |
| VLTOTCONT | NUMBER(12,2) | sim |  |
| QTTOTVOLUME | NUMBER(10) | sim |  |
| CODPARCDEST | NUMBER(6) | sim |  |
| NUMINVOICE | VARCHAR2(40) | sim |  |
| NUMPORTO | NUMBER(10) | sim |  |
| DTEMBARQUE | DATE | sim |  |
| NUMCONTAINER | VARCHAR2(40) | sim |  |
| SEALNR | NUMBER(12) | sim |  |
| BLNR | NUMBER(12) | sim |  |
| NAVIO | VARCHAR2(30) | sim |  |
| ARMADOR | VARCHAR2(40) | sim |  |
| NRRE | VARCHAR2(40) | sim |  |
| NRSD | VARCHAR2(40) | sim |  |
| DEBNOTE | VARCHAR2(100) | sim |  |
| STO | VARCHAR2(40) | sim |  |
| NUMPORTODEST | NUMBER(10) | sim |  |
| CODQUARTO | NUMBER(6) | sim |  |
| NUMPROM | VARCHAR2(20) | sim |  |
| GERARFALTA | VARCHAR2(1) | sim |  |
| ESF_ODLONGE | VARCHAR2(6) | sim |  |
| ESF_OELONGE | VARCHAR2(6) | sim |  |
| ESF_ODPERTO | VARCHAR2(6) | sim |  |
| ESF_OEPERTO | VARCHAR2(6) | sim |  |
| CIL_ODLONGE | VARCHAR2(6) | sim |  |
| CIL_OELONGE | VARCHAR2(6) | sim |  |
| CIL_ODPERTO | VARCHAR2(6) | sim |  |
| CIL_OEPERTO | VARCHAR2(6) | sim |  |
| EIXO_ODLONGE | VARCHAR2(6) | sim |  |
| EIXO_OELONGE | VARCHAR2(6) | sim |  |
| EIXO_ODPERTO | VARCHAR2(6) | sim |  |
| EIXO_OEPERTO | VARCHAR2(6) | sim |  |
| ADICAO | VARCHAR2(6) | sim |  |
| DNP_OD | VARCHAR2(6) | sim |  |
| DNP_OE | VARCHAR2(6) | sim |  |
| ALTURA | VARCHAR2(6) | sim |  |
| COLORACAO | VARCHAR2(3) | sim |  |
| INTENSIDADE | VARCHAR2(3) | sim |  |
| SITUACAO | VARCHAR2(3) | sim |  |
| CODMEDICO | NUMBER(10) | sim |  |
| OBSRECEITA | VARCHAR2(200) | sim |  |
| EANENTEDI | NUMBER(13) | sim |  |
| NUMVIASMAPABALCAO | NUMBER(1) | sim |  |
| AIDF_FORTES | VARCHAR2(25) | sim |  |
| NUMOP | NUMBER(10) | sim |  |
| NFSERVICO | VARCHAR2(1) | sim |  |
| NUMVENDATP21 | NUMBER(10) | sim |  |
| OBSACERTO | VARCHAR2(80) | sim |  |
| CODFUNCACERTO | NUMBER(6) | sim |  |
| DTACERTO | DATE | sim |  |
| CODANIMAL | NUMBER(10) | sim |  |
| DIAGANIMAL | VARCHAR2(240) | sim |  |
| NUMPEDMESCLAR | NUMBER(10) | sim |  |
| PARC1 | NUMBER(12,2) | sim |  |
| PARC2 | NUMBER(12,2) | sim |  |
| PARC3 | NUMBER(12,2) | sim |  |
| PARC4 | NUMBER(12,2) | sim |  |
| PARC5 | NUMBER(12,2) | sim |  |
| PARC6 | NUMBER(12,2) | sim |  |
| PARC7 | NUMBER(12,2) | sim |  |
| PARC8 | NUMBER(12,2) | sim |  |
| PARC9 | NUMBER(12,2) | sim |  |
| PARC10 | NUMBER(12,2) | sim |  |
| PARC11 | NUMBER(12,2) | sim |  |
| PARC12 | NUMBER(12,2) | sim |  |
| VLTOTALPARC | NUMBER(12,2) | sim |  |
| NUMCAR44 | NUMBER(10) | sim |  |
| NUMSERIE | VARCHAR2(255) | sim |  |
| NUMSERIE44 | VARCHAR2(255) | sim |  |
| INFORMANOTA | VARCHAR2(1) | sim |  |
| LISTADECOMPRA | VARCHAR2(1) | sim |  |
| DTVENCLISTA | DATE | sim |  |
| NUMPEDLISTACOMP | NUMBER(10) | sim |  |
| QTDHOSPEDE | NUMBER(3) | sim |  |
| PLACA | VARCHAR2(8) | sim |  |
| CARRO | VARCHAR2(20) | sim |  |
| VENDADIRETA | VARCHAR2(1) | sim |  |
| IMPPEDIDO | VARCHAR2(1) | sim |  |
| DUPLICOUTP12 | VARCHAR2(1) | sim |  |
| ESTPCP | VARCHAR2(1) | sim |  |
| TEMTROCA | VARCHAR2(1) | sim |  |
| QTDEBANDEJARECOLHER | NUMBER(18,6) | sim |  |
| PEDFVBLOQ | VARCHAR2(1) | sim |  |
| STATUSPEDIDOINSERIDO | VARCHAR2(1) | sim |  |
| CODMTPARAMETRO | VARCHAR2(20) | sim |  |
| CODMTLIMCRED | VARCHAR2(20) | sim |  |
| CODMTESTOQUE | VARCHAR2(20) | sim |  |
| CODMTFMARGEM | VARCHAR2(20) | sim |  |
| CODMTPMINIMO | VARCHAR2(20) | sim |  |
| STATUS_APP | VARCHAR2(5) | sim |  |
| ISVENDAPP | VARCHAR2(1) | sim |  |
| TROCOAPP | NUMBER(10,2) | sim |  |
| CPFNOTA | VARCHAR2(1) | sim |  |
| PERIODOENT | VARCHAR2(1) | sim |  |
| PERACREGIRO | NUMBER(5,2) | sim |  |
| IMPORTOUCX | NUMBER(4) | sim |  |
| VLICMSDES | NUMBER(12,2) | sim |  |
| DTVALIDADEOS | DATE | sim |  |
| CRO | VARCHAR2(20) | sim |  |
| SERVICOCONCLUIDO | VARCHAR2(1) | sim |  |
| DTENVIOFV | DATE | sim |  |
| IMPRESSOROT79 | VARCHAR2(1) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| SEQCARREGAMENTO | NUMBER(4) | sim |  |
| CPFCNPJSAID | VARCHAR2(18) | sim |  |
| MODELO | VARCHAR2(250) | sim |  |
| IMEI | VARCHAR2(50) | sim |  |
| TECNICO | VARCHAR2(60) | sim |  |
| DATATECN | DATE | sim |  |
| RELATO | VARCHAR2(1000) | sim |  |
| ACESSORIOS | VARCHAR2(500) | sim |  |
| SENHA | VARCHAR2(200) | sim |  |
| CONDICAOFISICA | VARCHAR2(1000) | sim |  |
| AVARIA | VARCHAR2(1) | sim | A=ABERTA, R=REALIZADA |
| VLBONIFICACAO | NUMBER(12,2) | sim |  |
| FRETEBONIF | NUMBER(12,2) | sim |  |
| VLFRETECOTADO | NUMBER(12,2) | sim |  |
| NUMCOTACAO | NUMBER(12) | sim |  |
| INFOPEDIDO | VARCHAR2(1) | sim |  |
| NUMVIASMODELO4 | NUMBER(2) | sim |  |
| NUMLACREAVARIA | NUMBER(10) | sim |  |
| MOTIVOAVARIA | VARCHAR2(1000) | sim |  |
| PEDPRINCAVARIA | NUMBER(10) | sim |  |
| CODFUNCIMPRESROT79 | NUMBER(10) | sim |  |
| NCONTRATOCONSIG | NUMBER(10) | sim |  |
| CODETAPAECOMMERCE | VARCHAR2(10) | sim |  |
| CODCOBESPEC | VARCHAR2(1) | sim |  |
| VLCREDCLIENTEUSADO | NUMBER(12,2) | sim |  |
| VERSAOROTINA | VARCHAR2(20) | sim |  |
| SITE | VARCHAR2(1) | sim |  |
| DTSTATUSENTREGA_ECOMMERCE | DATE | sim |  |
| USADESCSUPERVISORFV | VARCHAR2(1) | sim |  |
| CODSUPERVLIB | NUMBER(10) | sim |  |
| TPENTPED | VARCHAR2(2) | sim |  |
| PEDEXPRESS | VARCHAR2(1) | sim |  |
| TPCONTATO | VARCHAR2(1) | sim |  |
| CPAGARSERV | VARCHAR2(1) | sim |  |
| NUMTOTCONS | NUMBER(6) | sim |  |
| CPAGARTRANSP | VARCHAR2(1) | sim |  |
| VENCTOCPTRANSP | DATE | sim |  |
| CODLUCROMINIMO | VARCHAR2(20) | sim |  |
| OS | VARCHAR2(1) | sim |  |
| CODFUNCMEC | NUMBER(10) | sim |  |
| CODOPDESCROD | VARCHAR2(20) | sim |  |
| OBS5 | VARCHAR2(1000) | sim |  |
| CODLOG | NUMBER(10) | sim |  |
| VLTOT_OUT_TAXAS | NUMBER(12,2) | sim |  |
| CODPLPAG_ORIGINAL | NUMBER(4) | sim |  |
| CODCOB_ORIGINAL | VARCHAR2(4) | sim |  |
| VALORFRETEMOTORISTA | NUMBER(12,2) | sim |  |
| CABNFEESPVOL | VARCHAR2(20) | sim |  |
| TRANSPORTE | VARCHAR2(4) | sim | PROCESSO DE ESTIVA SALVA TIPO DO TRANSPORTE: TE-TERCEIRIZADO EXTERNO TL ¿TERCEIRO LOCAL I-ISENTO |
| DTBLOQENTREGA | DATE | sim | GRAVAR DATA BLOQUEIO PARA BLOQUEAR A ENTREGA  DO PEDIDO E NAO PERMITIR MONTAR NA 512 |
| VLBONIFICACAO2 | NUMBER(12,2) | sim | VALOR DO BONIFICACAO2 SOMADO NO DESCONTO DO ITEM |
| VLBONIFICACAO3 | NUMBER(12,2) | sim | VALOR DO BONIFICACAO3 SOMADO NO DESCONTO DO ITEM |
| NUMPED_ORIGTP7 | NUMBER(10) | sim | NA R.1436 NAS VENDAS TIPO 7 GERADAS E GRAVADO O NUMPED DE ORIGEM |
| DTGERAR_TP7 | DATE | sim | GRAVAR DATA QUE FOI GERADO TIPO 7 |
| NAOUSARPOFERTA | VARCHAR2(1) | sim | GRAVAR NA VENDA QUE UTILIZOU A FLAG NAO UTILIZAR POFERTA R.56 |
| VICMSMONORET | NUMBER(12,2) | sim | Valor AD REM do ICMS para o produto CST=61 |
| CODFUNCLIB_VLMINPAGTO | NUMBER(10) | sim | FUNC LIBEROU O PEDIDOS ONDE O PLANO DE PAGAMENTO UTILIZAR O VALOR MININO |
| ID_MARKET | VARCHAR2(80) | sim | id do pedido no Plug4Market |
| IDCV_MARKET | VARCHAR2(80) | sim | CANAL DE VENDA DO PEDIDO NA Plug4Market |
| OS300 | VARCHAR2(1) | sim | Pedido nao consolidado rotina 300 OS |
| NUMTRANSPEDELETAR | VARCHAR2(30) | sim | GRAVAR O NUMTRANSPEDIDO AO CONSOLIDAR ORCAMENTOS PARA PODER DELETAR |
| CODGRUPO_OS_CPAGAR | NUMBER(4) | sim | GRUPO SELECIONADO PARA GERAR CPAGAR AO REALIZAR SERVIÇO RT.300 |
| CODCONTA_OS_CPAGAR | NUMBER(10) | sim | CONTA SELECIONADO PARA GERAR CPAGAR AO REALIZAR SERVIÇO RT.300 |
| DATAIMPRESSOROT79 | DATE | sim | ROTINA 79 SALVAR DATA E HORA DA IMPRESSAO |
| MANUT_PLANEJADA | VARCHAR2(1) | sim | Quando a flag estiver ativa, salvar como "S"  |
| KM_MANUT | NUMBER(15) | sim | Quilometragem da manutenção |
| MOSKITSYNC | VARCHAR2(1) | sim | Cefas Moskit: S = sincronizado com o Moskit, N = pendente. |
| MOSKIT_ID | NUMBER(15) | sim | Cefas Moskit: ID do deal/negócio correspondente na API Moskit CRM. |
| NUM_LOCACAO | NUMBER(10) | sim | Numero da proposta de locacao |
| TIPO_SERVICO | VARCHAR2(1) | sim | Tipo de serviço da locação: P=Preventiva, C=Corretiva, R=Proativa |

### SEVERIANO.NFSAID (263.472 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMVENDA | NUMBER(10) | não |  |
| NUMNOTA | NUMBER(10) | sim |  |
| SERIE | VARCHAR2(3) | sim |  |
| ESPECIE | VARCHAR2(2) | sim |  |
| DTEMISSAO | DATE | sim |  |
| CODFISCAL | NUMBER(4) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| CODCONT | NUMBER(10) | sim |  |
| CODCLI | NUMBER(6) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| CODPLPAG | NUMBER(4) | sim |  |
| NUMCUPOM | NUMBER(10) | sim |  |
| TIPO | NUMBER(2) | sim |  |
| VLCUSTOREAL | NUMBER(12,2) | sim |  |
| VLCUSTOFIN | NUMBER(12,2) | sim |  |
| VLFRETE | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| VLTABELA | NUMBER(12,2) | sim |  |
| TOTPESO | NUMBER(12,2) | sim |  |
| NUMITENS | NUMBER(4) | sim |  |
| OBS | VARCHAR2(40) | sim |  |
| DTCANCEL | DATE | sim |  |
| CODFUNCANCEL | NUMBER(10) | sim |  |
| VLCANCEL | NUMBER(12,2) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| TOTVOLUME | NUMBER(12,2) | sim |  |
| DTSAIDA | DATE | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLST | NUMBER(12,2) | sim |  |
| VLCUSTOCONT | NUMBER(12,2) | sim |  |
| VLTOTCONT | NUMBER(12,2) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| CODPRACA | NUMBER(4) | sim |  |
| FRETEDESPACHO | VARCHAR2(1) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| DTDEVOL | DATE | sim |  |
| VLDEVOL | NUMBER(12,2) | sim |  |
| TIPOVENDA | VARCHAR2(2) | sim |  |
| VLICM | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(12,2) | sim |  |
| VLBASEICM | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| NUMVIAS | NUMBER(2) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| CODDEVOL | NUMBER(4) | sim |  |
| DTENTREGA | DATE | sim |  |
| VLISENTO | NUMBER(12,2) | sim |  |
| NFORIGEM | NUMBER(10) | sim |  |
| VLOUTRASDESP | NUMBER(12,2) | sim |  |
| CODSUPERVISOR | NUMBER(4) | sim |  |
| NUMCOMANDA | NUMBER(10) | sim |  |
| OBS2 | VARCHAR2(40) | sim |  |
| TOTPESOLIQ | NUMBER(12,2) | sim |  |
| CODFORNECTRANSP | NUMBER(6) | sim |  |
| SUBSERIE | VARCHAR2(1) | sim |  |
| CODFUNCVEND | NUMBER(10) | sim |  |
| NUMSERVICO | NUMBER(10) | sim |  |
| VLBASEISS | NUMBER(12,2) | sim |  |
| VLISS | NUMBER(12,2) | sim |  |
| VLDESCBRINDE | NUMBER(12,2) | sim |  |
| NFETPEMIS | VARCHAR2(2) | sim |  |
| DTSTATUS | DATE | sim |  |
| NFEPLACA | VARCHAR2(7) | sim |  |
| NFEUFPLACA | VARCHAR2(2) | sim |  |
| DTNFE | DATE | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| CSTATNFE | VARCHAR2(4) | sim |  |
| RECNFE | VARCHAR2(20) | sim |  |
| NPROTNFE | VARCHAR2(20) | sim |  |
| IDLOTE | VARCHAR2(15) | sim |  |
| MODONFE | VARCHAR2(20) | sim |  |
| DTIMPNFE | DATE | sim |  |
| NFDESTINO | NUMBER(10) | sim |  |
| ENDERENT | VARCHAR2(40) | sim |  |
| BAIRROENT | VARCHAR2(30) | sim |  |
| CIDADEENT | VARCHAR2(40) | sim |  |
| ESTADOENT | VARCHAR2(2) | sim |  |
| CEPENT | VARCHAR2(10) | sim |  |
| TELENT | VARCHAR2(15) | sim |  |
| IEENT | VARCHAR2(15) | sim |  |
| CPFCNPJ | VARCHAR2(18) | sim |  |
| VLDESCICM | NUMBER(12,2) | sim |  |
| VLDESCFIN | NUMBER(12,2) | sim |  |
| VLBASEPIS | NUMBER(12,2) | sim |  |
| VLPIS | NUMBER(12,2) | sim |  |
| VLBASECOFINS | NUMBER(12,2) | sim |  |
| VLCOFINS | NUMBER(12,2) | sim |  |
| ESPECIE2 | VARCHAR2(2) | sim |  |
| STATUS | VARCHAR2(200) | sim |  |
| IMPRESSA | VARCHAR2(3) | sim |  |
| NFE | VARCHAR2(60) | sim |  |
| MSGNFE | VARCHAR2(200) | sim |  |
| NFEQTDEVOL | VARCHAR2(10) | sim |  |
| NFEESPVOL | VARCHAR2(20) | sim |  |
| NFEMARCAVOL | VARCHAR2(30) | sim |  |
| NFEOBS | VARCHAR2(4000) | sim |  |
| NUMDOCIMPORT | NUMBER(15) | sim |  |
| DTREGIMPORT | DATE | sim |  |
| DESCDESEMBARACO | VARCHAR2(100) | sim |  |
| UFDESEMBARACO | VARCHAR2(2) | sim |  |
| DTDESEMBARACO | DATE | sim |  |
| CODEXPSISTINTERNO | NUMBER(10) | sim |  |
| NFEADIC | NUMBER(3) | sim |  |
| NFESEQ | NUMBER(3) | sim |  |
| NFEFABRIC | VARCHAR2(60) | sim |  |
| VLDESCIMPOSTO | NUMBER(12,2) | sim |  |
| ANTT | VARCHAR2(20) | sim |  |
| VLCOMSUP | NUMBER(12,2) | sim |  |
| DTIMPCUPOM | DATE | sim |  |
| DATACONT | VARCHAR2(254) | sim |  |
| JUSTCONT | VARCHAR2(254) | sim |  |
| NFECHAVECONT | VARCHAR2(254) | sim |  |
| NFEUFEMBARQ | VARCHAR2(2) | sim |  |
| NFELOCEMBARQ | VARCHAR2(40) | sim |  |
| CCF | NUMBER(6) | sim |  |
| GNF | NUMBER(6) | sim |  |
| ENTNUMNFPROP | VARCHAR2(1) | sim |  |
| NFSERVICO | VARCHAR2(1) | sim |  |
| VLCANCELPARC | NUMBER(12,2) | sim |  |
| VLSEGURO | NUMBER(12,2) | sim |  |
| EMBALAGEMREGIAO | VARCHAR2(1) | sim |  |
| VLINSS | NUMBER(12,2) | sim |  |
| VLIR | NUMBER(12,2) | sim |  |
| VLCSLL | NUMBER(12,2) | sim |  |
| ORIGEM | VARCHAR2(4) | sim |  |
| CODPARIND | NUMBER(6) | sim |  |
| OBSCCE | VARCHAR2(4000) | sim |  |
| CSTATCCE | VARCHAR2(3) | sim |  |
| NPROTCCE | VARCHAR2(20) | sim |  |
| CPFCNPJCAT52 | VARCHAR2(14) | sim |  |
| VFCPUFDEST | NUMBER(12,2) | sim |  |
| VICMSUFDEST | NUMBER(12,2) | sim |  |
| VICMSUFREMET | NUMBER(12,2) | sim |  |
| CHAVEREFCOMP | VARCHAR2(60) | sim |  |
| AAA | VARCHAR2(1) | sim |  |
| DTACERTO | DATE | sim |  |
| OBSACERTO | VARCHAR2(80) | sim |  |
| CODFUNCACERTO | NUMBER(6) | sim |  |
| ENVIOU | VARCHAR2(1) | sim |  |
| INDPRES | VARCHAR2(1) | sim |  |
| CSTCREDITOICMS | VARCHAR2(2) | sim |  |
| VLFCP | NUMBER(12,2) | sim |  |
| VLFCPST | NUMBER(12,2) | sim |  |
| VLFCPSTRET | NUMBER(12,2) | sim |  |
| USAMFE | CHAR(1) | sim |  |
| NFGARANTIA | VARCHAR2(1) | sim |  |
| VLBASEICMGARANTIA | NUMBER(12,2) | sim |  |
| VLICMGARANTIA | NUMBER(12,2) | sim |  |
| VLBASESTGARANTIA | NUMBER(12,2) | sim |  |
| VLSTGARANTIA | NUMBER(12,2) | sim |  |
| VLBASEIPIGARANTIA | NUMBER(12,2) | sim |  |
| VLIPIGARANTIA | NUMBER(12,2) | sim |  |
| VLBASEFCP | NUMBER(12,2) | sim |  |
| VLBASEFCPST | NUMBER(12,2) | sim |  |
| VLBASEFCPSTRET | NUMBER(12,2) | sim |  |
| CODFUNCF11LIB | NUMBER(10) | sim |  |
| CSTATNFEAUX | VARCHAR2(4) | sim |  |
| CODATEND1 | NUMBER(10) | sim |  |
| CODATEND2 | NUMBER(10) | sim |  |
| CODATEND3 | NUMBER(10) | sim |  |
| CODATEND4 | NUMBER(10) | sim |  |
| DUPLICOUTP12 | VARCHAR2(1) | sim |  |
| NFDESTINOCODCLI | NUMBER(10) | sim |  |
| XMLPDFENVIADO | VARCHAR2(1) | sim |  |
| VLICMSDES | NUMBER(12,2) | sim |  |
| TIPOCREDITOICMS | VARCHAR2(13) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| USADEVOLTRANSF | VARCHAR2(1) | sim |  |
| VLICMDIF | NUMBER(12,2) | sim |  |
| CPFCNPJSAID | VARCHAR2(18) | sim |  |
| DIFEMBREGIAO | VARCHAR2(1) | sim |  |
| VLFRETEPAGO | NUMBER(12,2) | sim |  |
| SAIDAAVARIA | VARCHAR2(1) | sim |  |
| SRSIMPLESFATURA | VARCHAR2(1) | sim |  |
| NUMLANCCPAGARDESCFIN | NUMBER(10) | sim |  |
| VLBONIFICACAO | NUMBER(12,2) | sim |  |
| FRETEBONIF | NUMBER(12,2) | sim |  |
| VLFRETECOTADO | NUMBER(12,2) | sim |  |
| CSOSN_CREDITOICMS | NUMBER(3) | sim |  |
| VLCREDUSADO | NUMBER(12,2) | sim |  |
| NCONTRATOCONSIG | NUMBER(10) | sim |  |
| VERSAOROTINA | VARCHAR2(20) | sim |  |
| CNPJINTERMEDIADOR | VARCHAR2(14) | sim |  |
| INTERMEDIADOR | VARCHAR2(60) | sim |  |
| NFTERCEIRO | VARCHAR2(1) | sim |  |
| CODIGOSTATUS_SCANNTECH | NUMBER(5) | sim |  |
| STATUSENVIO_SCANNTECH | VARCHAR2(1) | sim |  |
| VLDESCONTOSCANNTECH | NUMBER(12,2) | sim |  |

### SEVERIANO.CADNCMPISCOFINS16MAR17 (263.385 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CODPROD | NUMBER(10) | sim |  |
| COD_NCM | VARCHAR2(15) | sim |  |
| OPERACAO | VARCHAR2(2) | sim |  |
| CSTPIS | VARCHAR2(2) | sim |  |
| CSTCOFINS | VARCHAR2(2) | sim |  |
| PERPIS | NUMBER(8,6) | sim |  |
| PERCOFINS | NUMBER(8,6) | sim |  |
| PISCOFINS | VARCHAR2(1) | sim |  |
| CODNATPIS | VARCHAR2(4) | sim |  |
| CODNATCOFINS | VARCHAR2(4) | sim |  |
| CODNATRECFT | VARCHAR2(4) | sim |  |
| CSTPISPF | VARCHAR2(2) | sim |  |
| CSTCOFINSPF | VARCHAR2(2) | sim |  |
| PERPISPF | NUMBER(8,6) | sim |  |
| PERCOFINSPF | NUMBER(8,6) | sim |  |
| PISCOFINSPF | VARCHAR2(1) | sim |  |
| CODNATPISPF | VARCHAR2(4) | sim |  |
| CODNATCOFINSPF | VARCHAR2(4) | sim |  |
| CODNATRECFTPF | VARCHAR2(4) | sim |  |
| REGTRIBUT | NUMBER(1) | sim |  |
| CEST | VARCHAR2(7) | sim |  |
| ALIQFED | NUMBER(8,6) | sim |  |
| ALIQEST | NUMBER(8,6) | sim |  |
| DTVENCALIQ | DATE | sim |  |
| CODCONTABIL | NUMBER(15) | sim |  |

### VAREJO.CABPED (259.266 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMPED | NUMBER(10) | não |  |
| CODCLI | NUMBER(6) | sim |  |
| CODPLPAG | NUMBER(4) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| DTEMISSAO | DATE | sim |  |
| DTPREVENT | DATE | sim |  |
| TIPO | VARCHAR2(2) | sim |  |
| OBS | VARCHAR2(1000) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| TOTPESO | NUMBER(12,2) | sim |  |
| TOTVOLUME | NUMBER(12,2) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| VLCUSTOREAL | NUMBER(12,2) | sim |  |
| VLFRETE | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| VLTABELA | NUMBER(12,2) | sim |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| POSICAO | VARCHAR2(1) | sim |  |
| TPENTREGA | VARCHAR2(1) | sim |  |
| NUMITENS | NUMBER(4) | sim |  |
| POSICAOENT | VARCHAR2(1) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| ENDERENT | VARCHAR2(60) | sim |  |
| BAIRROENT | VARCHAR2(60) | sim |  |
| CIDADEENT | VARCHAR2(40) | sim |  |
| ESTADOENT | VARCHAR2(2) | sim |  |
| CEPENT | VARCHAR2(10) | sim |  |
| TELENT | VARCHAR2(15) | sim |  |
| CODPRACA | NUMBER(4) | sim |  |
| CODFORNEC | NUMBER(6) | sim |  |
| INDICE | NUMBER(5,2) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| NUMVENDA | NUMBER(10) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| CODFUNCCAN | NUMBER(10) | sim |  |
| DTCANCEL | DATE | sim |  |
| OBS2 | VARCHAR2(1000) | sim |  |
| CLIENTE | VARCHAR2(70) | sim |  |
| CPFCNPJ | VARCHAR2(18) | sim |  |
| FRETEDESPACHO | VARCHAR2(1) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| NUMVIAS | NUMBER(2) | sim |  |
| CODVEICULO | NUMBER(6) | sim |  |
| CODTABNEGOCIACAO | NUMBER(2) | sim |  |
| DTINICIO | DATE | sim |  |
| HORAINICIO | NUMBER(2) | sim |  |
| MINUTOINICIO | NUMBER(2) | sim |  |
| DTFIM | DATE | sim |  |
| HORAFIM | NUMBER(2) | sim |  |
| MINUTOFIM | NUMBER(2) | sim |  |
| VLTOTPROD | NUMBER(12,2) | sim |  |
| PRAZO1 | NUMBER(4) | sim |  |
| PRAZO2 | NUMBER(4) | sim |  |
| PRAZO3 | NUMBER(4) | sim |  |
| PRAZO4 | NUMBER(4) | sim |  |
| PRAZO5 | NUMBER(4) | sim |  |
| PRAZO6 | NUMBER(4) | sim |  |
| PRAZO7 | NUMBER(4) | sim |  |
| PRAZO8 | NUMBER(4) | sim |  |
| PRAZO9 | NUMBER(4) | sim |  |
| PRAZO10 | NUMBER(4) | sim |  |
| PRAZO11 | NUMBER(4) | sim |  |
| PRAZO12 | NUMBER(4) | sim |  |
| PRAZOMD | NUMBER(12,2) | sim |  |
| QTVOL | NUMBER(12,2) | sim |  |
| TPBALCAOTLMK | VARCHAR2(1) | sim |  |
| OBS3 | VARCHAR2(1000) | sim |  |
| OBS4 | VARCHAR2(1000) | sim |  |
| OBSENTREGA1 | VARCHAR2(100) | sim |  |
| OBSENTREGA2 | VARCHAR2(100) | sim |  |
| OBSENTREGA3 | VARCHAR2(100) | sim |  |
| OBSENTREGA4 | VARCHAR2(100) | sim |  |
| OBSENTREGA5 | VARCHAR2(100) | sim |  |
| OBSENTREGA6 | VARCHAR2(100) | sim |  |
| OBSENTREGA7 | VARCHAR2(100) | sim |  |
| OBSENTREGA8 | VARCHAR2(100) | sim |  |
| OBSENTREGA9 | VARCHAR2(100) | sim |  |
| NUMSEQENTREGA | NUMBER(20) | sim |  |
| VLOUTRASDESP | NUMBER(12,2) | sim |  |
| VLCUSTOFIN | NUMBER(12,2) | sim |  |
| HORA | NUMBER(2) | sim |  |
| MINUTO | NUMBER(2) | sim |  |
| CODFILIALRETIRA | VARCHAR2(2) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| VLTOTALORIG | NUMBER(12,2) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| NUMCUPOM | NUMBER(10) | sim |  |
| IEENT | VARCHAR2(15) | sim |  |
| OBSENTREGA10 | VARCHAR2(75) | sim |  |
| OBSENTREGA11 | VARCHAR2(75) | sim |  |
| NUMPROCESSO | NUMBER(15) | sim |  |
| CODPARIND | NUMBER(6) | sim |  |
| NUMPEDORIG | NUMBER(10) | sim |  |
| TOTPESOLIQ | NUMBER(12,2) | sim |  |
| KMOS | NUMBER(12) | sim |  |
| NUMPEDORIGREMENTFUT | NUMBER(10) | sim |  |
| NUMVIASRECIBOENTMERC | NUMBER(4) | sim |  |
| VLDESCBRINDE | NUMBER(12,2) | sim |  |
| PRAZO13 | NUMBER(4) | sim |  |
| PRAZO14 | NUMBER(4) | sim |  |
| PRAZO15 | NUMBER(4) | sim |  |
| PRAZO16 | NUMBER(4) | sim |  |
| PRAZO17 | NUMBER(4) | sim |  |
| PRAZO18 | NUMBER(4) | sim |  |
| PRAZO19 | NUMBER(4) | sim |  |
| PRAZO20 | NUMBER(4) | sim |  |
| PRAZO21 | NUMBER(4) | sim |  |
| PRAZO22 | NUMBER(4) | sim |  |
| PRAZO23 | NUMBER(4) | sim |  |
| PRAZO24 | NUMBER(4) | sim |  |
| RESERVARESTOQUEORCAMENTO | VARCHAR2(1) | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| STATUS | VARCHAR2(2) | sim |  |
| NUMVIAGEM | NUMBER(10) | sim |  |
| NUMNOTADEST | NUMBER(10) | sim |  |
| VLTOTALNFDEST | NUMBER(12,2) | sim |  |
| PESONFDEST | NUMBER(12,2) | sim |  |
| VOLUMENFDEST | NUMBER(12,2) | sim |  |
| NUMNOTADEST2 | NUMBER(10) | sim |  |
| VLTOTALNFDEST2 | NUMBER(12,2) | sim |  |
| PESONFDEST2 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST2 | NUMBER(12,2) | sim |  |
| NUMNOTADEST3 | NUMBER(10) | sim |  |
| VLTOTALNFDEST3 | NUMBER(12,2) | sim |  |
| PESONFDEST3 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST3 | NUMBER(12,2) | sim |  |
| NUMNOTADEST4 | NUMBER(10) | sim |  |
| VLTOTALNFDEST4 | NUMBER(12,2) | sim |  |
| PESONFDEST4 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST4 | NUMBER(12,2) | sim |  |
| NUMNOTADEST5 | NUMBER(10) | sim |  |
| VLTOTALNFDEST5 | NUMBER(12,2) | sim |  |
| PESONFDEST5 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST5 | NUMBER(12,2) | sim |  |
| CODCONSIGNAT | NUMBER(6) | sim |  |
| NUMNOTATP12 | NUMBER(10) | sim |  |
| NUMPROD | NUMBER(10) | sim |  |
| NUMNOTADEST6 | NUMBER(10) | sim |  |
| VLTOTALNFDEST6 | NUMBER(12,2) | sim |  |
| PESONFDEST6 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST6 | NUMBER(12,2) | sim |  |
| NUMNOTADEST7 | NUMBER(10) | sim |  |
| VLTOTALNFDEST7 | NUMBER(12,2) | sim |  |
| PESONFDEST7 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST7 | NUMBER(12,2) | sim |  |
| NUMNOTADEST8 | NUMBER(10) | sim |  |
| VLTOTALNFDEST8 | NUMBER(12,2) | sim |  |
| PESONFDEST8 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST8 | NUMBER(12,2) | sim |  |
| NUMNOTADEST9 | NUMBER(10) | sim |  |
| VLTOTALNFDEST9 | NUMBER(12,2) | sim |  |
| PESONFDEST9 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST9 | NUMBER(12,2) | sim |  |
| NUMNOTADEST10 | NUMBER(10) | sim |  |
| VLTOTALNFDEST10 | NUMBER(12,2) | sim |  |
| PESONFDEST10 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST10 | NUMBER(12,2) | sim |  |
| NUMNOTADEST11 | NUMBER(10) | sim |  |
| VLTOTALNFDEST11 | NUMBER(12,2) | sim |  |
| PESONFDEST11 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST11 | NUMBER(12,2) | sim |  |
| NUMNOTADEST12 | NUMBER(10) | sim |  |
| VLTOTALNFDEST12 | NUMBER(12,2) | sim |  |
| PESONFDEST12 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST12 | NUMBER(12,2) | sim |  |
| NUMNOTADEST13 | NUMBER(10) | sim |  |
| VLTOTALNFDEST13 | NUMBER(12,2) | sim |  |
| PESONFDEST13 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST13 | NUMBER(12,2) | sim |  |
| NUMNOTADEST14 | NUMBER(10) | sim |  |
| VLTOTALNFDEST14 | NUMBER(12,2) | sim |  |
| PESONFDEST14 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST14 | NUMBER(12,2) | sim |  |
| NUMNOTADEST15 | NUMBER(10) | sim |  |
| VLTOTALNFDEST15 | NUMBER(12,2) | sim |  |
| PESONFDEST15 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST15 | NUMBER(12,2) | sim |  |
| NUMNOTADEST16 | NUMBER(10) | sim |  |
| VLTOTALNFDEST16 | NUMBER(12,2) | sim |  |
| PESONFDEST16 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST16 | NUMBER(12,2) | sim |  |
| NUMNOTADEST17 | NUMBER(10) | sim |  |
| VLTOTALNFDEST17 | NUMBER(12,2) | sim |  |
| PESONFDEST17 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST17 | NUMBER(12,2) | sim |  |
| NUMNOTADEST18 | NUMBER(10) | sim |  |
| VLTOTALNFDEST18 | NUMBER(12,2) | sim |  |
| PESONFDEST18 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST18 | NUMBER(12,2) | sim |  |
| NUMNOTADEST19 | NUMBER(10) | sim |  |
| VLTOTALNFDEST19 | NUMBER(12,2) | sim |  |
| PESONFDEST19 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST19 | NUMBER(12,2) | sim |  |
| NUMNOTADEST20 | NUMBER(10) | sim |  |
| VLTOTALNFDEST20 | NUMBER(12,2) | sim |  |
| PESONFDEST20 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST20 | NUMBER(12,2) | sim |  |
| POTENCIATRANSF | NUMBER(10,6) | sim |  |
| MARCATRANSF | VARCHAR2(40) | sim |  |
| NUMSERIETRANSF | VARCHAR2(25) | sim |  |
| TENSAOAT1TRANSF | VARCHAR2(6) | sim |  |
| TENSAOAT2TRANSF | VARCHAR2(6) | sim |  |
| TENSAOBT1TRANSF | VARCHAR2(3) | sim |  |
| TENSAOBT2TRANSF | VARCHAR2(3) | sim |  |
| NUMTAPETRANSF | VARCHAR2(20) | sim |  |
| TAPEATUALTRANSF | VARCHAR2(20) | sim |  |
| VOLOLEOTRANSF | NUMBER(10,6) | sim |  |
| ANOFABTRANSF | VARCHAR2(4) | sim |  |
| IMPEDANCIATRANSF | NUMBER(10,6) | sim |  |
| TIPOTRANSF | VARCHAR2(20) | sim |  |
| NUMCELGTRANSF | VARCHAR2(20) | sim |  |
| CABINEPOSTETRANSF | VARCHAR2(1) | sim |  |
| PESOTRANSF | NUMBER(10,6) | sim |  |
| CODMOTORISTA | NUMBER(6) | sim |  |
| RPMTRANSF | NUMBER(10,4) | sim |  |
| MONOFASICO | VARCHAR2(1) | sim |  |
| TIPOMOTORTRANSF | VARCHAR2(1) | sim |  |
| DESCTIPOMOTORTRANSF | VARCHAR2(255) | sim |  |
| CODAGRONOMO | NUMBER(6) | sim |  |
| LOCALAPLIC | VARCHAR2(30) | sim |  |
| CULTURA | VARCHAR2(20) | sim |  |
| DIAGNOSTICO | VARCHAR2(300) | sim |  |
| AREA | VARCHAR2(15) | sim |  |
| PRAGA | VARCHAR2(30) | sim |  |
| ANTIDOTO | VARCHAR2(30) | sim |  |
| CODMUNICIPIO | NUMBER(7) | sim |  |
| NATUREZAFRETE | VARCHAR2(30) | sim |  |
| NUMRECEITA | NUMBER(10) | sim |  |
| DTLIBPED | DATE | sim |  |
| GARANTIA | VARCHAR2(1) | sim |  |
| VLDEBCREDRCA | NUMBER(12,2) | sim |  |
| NUMTRANSPEDIDO | NUMBER(10) | sim |  |
| NUMPEDRCA0 | NUMBER(10) | sim |  |
| NUMPEDRCA | NUMBER(20) | sim |  |
| VLTOTALST | NUMBER(12,2) | sim |  |
| VLSEGURO | NUMBER(12,2) | sim |  |
| DTAUTORC | DATE | sim |  |
| CODFUNCORC | NUMBER(10) | sim |  |
| CODDIG | NUMBER(10) | sim |  |
| VLTOTCONT | NUMBER(12,2) | sim |  |
| QTTOTVOLUME | NUMBER(10) | sim |  |
| CODPARCDEST | NUMBER(6) | sim |  |
| NUMINVOICE | VARCHAR2(40) | sim |  |
| NUMPORTO | NUMBER(10) | sim |  |
| DTEMBARQUE | DATE | sim |  |
| NUMCONTAINER | VARCHAR2(40) | sim |  |
| SEALNR | NUMBER(12) | sim |  |
| BLNR | NUMBER(12) | sim |  |
| NAVIO | VARCHAR2(30) | sim |  |
| ARMADOR | VARCHAR2(40) | sim |  |
| NRRE | VARCHAR2(40) | sim |  |
| NRSD | VARCHAR2(40) | sim |  |
| DEBNOTE | VARCHAR2(100) | sim |  |
| STO | VARCHAR2(40) | sim |  |
| NUMPORTODEST | NUMBER(10) | sim |  |
| CODQUARTO | NUMBER(6) | sim |  |
| NUMPROM | VARCHAR2(20) | sim |  |
| GERARFALTA | VARCHAR2(1) | sim |  |
| ESF_ODLONGE | VARCHAR2(6) | sim |  |
| ESF_OELONGE | VARCHAR2(6) | sim |  |
| ESF_ODPERTO | VARCHAR2(6) | sim |  |
| ESF_OEPERTO | VARCHAR2(6) | sim |  |
| CIL_ODLONGE | VARCHAR2(6) | sim |  |
| CIL_OELONGE | VARCHAR2(6) | sim |  |
| CIL_ODPERTO | VARCHAR2(6) | sim |  |
| CIL_OEPERTO | VARCHAR2(6) | sim |  |
| EIXO_ODLONGE | VARCHAR2(6) | sim |  |
| EIXO_OELONGE | VARCHAR2(6) | sim |  |
| EIXO_ODPERTO | VARCHAR2(6) | sim |  |
| EIXO_OEPERTO | VARCHAR2(6) | sim |  |
| ADICAO | VARCHAR2(6) | sim |  |
| DNP_OD | VARCHAR2(6) | sim |  |
| DNP_OE | VARCHAR2(6) | sim |  |
| ALTURA | VARCHAR2(6) | sim |  |
| COLORACAO | VARCHAR2(3) | sim |  |
| INTENSIDADE | VARCHAR2(3) | sim |  |
| SITUACAO | VARCHAR2(3) | sim |  |
| CODMEDICO | NUMBER(10) | sim |  |
| OBSRECEITA | VARCHAR2(200) | sim |  |
| EANENTEDI | NUMBER(13) | sim |  |
| NUMVIASMAPABALCAO | NUMBER(1) | sim |  |
| AIDF_FORTES | VARCHAR2(25) | sim |  |
| NUMOP | NUMBER(10) | sim |  |
| NFSERVICO | VARCHAR2(1) | sim |  |
| NUMVENDATP21 | NUMBER(10) | sim |  |
| OBSACERTO | VARCHAR2(80) | sim |  |
| CODFUNCACERTO | NUMBER(6) | sim |  |
| DTACERTO | DATE | sim |  |
| CODANIMAL | NUMBER(10) | sim |  |
| DIAGANIMAL | VARCHAR2(240) | sim |  |
| NUMPEDMESCLAR | NUMBER(10) | sim |  |
| PARC1 | NUMBER(12,2) | sim |  |
| PARC2 | NUMBER(12,2) | sim |  |
| PARC3 | NUMBER(12,2) | sim |  |
| PARC4 | NUMBER(12,2) | sim |  |
| PARC5 | NUMBER(12,2) | sim |  |
| PARC6 | NUMBER(12,2) | sim |  |
| PARC7 | NUMBER(12,2) | sim |  |
| PARC8 | NUMBER(12,2) | sim |  |
| PARC9 | NUMBER(12,2) | sim |  |
| PARC10 | NUMBER(12,2) | sim |  |
| PARC11 | NUMBER(12,2) | sim |  |
| PARC12 | NUMBER(12,2) | sim |  |
| VLTOTALPARC | NUMBER(12,2) | sim |  |
| NUMCAR44 | NUMBER(10) | sim |  |
| NUMSERIE | VARCHAR2(255) | sim |  |
| NUMSERIE44 | VARCHAR2(255) | sim |  |
| INFORMANOTA | VARCHAR2(1) | sim |  |
| LISTADECOMPRA | VARCHAR2(1) | sim |  |
| DTVENCLISTA | DATE | sim |  |
| NUMPEDLISTACOMP | NUMBER(10) | sim |  |
| QTDHOSPEDE | NUMBER(3) | sim |  |
| PLACA | VARCHAR2(8) | sim |  |
| CARRO | VARCHAR2(20) | sim |  |
| VENDADIRETA | VARCHAR2(1) | sim |  |
| IMPPEDIDO | VARCHAR2(1) | sim |  |
| DUPLICOUTP12 | VARCHAR2(1) | sim |  |
| ESTPCP | VARCHAR2(1) | sim |  |
| TEMTROCA | VARCHAR2(1) | sim |  |
| QTDEBANDEJARECOLHER | NUMBER(18,6) | sim |  |
| PEDFVBLOQ | VARCHAR2(1) | sim |  |
| STATUSPEDIDOINSERIDO | VARCHAR2(1) | sim |  |
| CODMTPARAMETRO | VARCHAR2(20) | sim |  |
| CODMTLIMCRED | VARCHAR2(20) | sim |  |
| CODMTESTOQUE | VARCHAR2(20) | sim |  |
| CODMTFMARGEM | VARCHAR2(20) | sim |  |
| CODMTPMINIMO | VARCHAR2(20) | sim |  |
| STATUS_APP | VARCHAR2(5) | sim |  |
| ISVENDAPP | VARCHAR2(1) | sim |  |
| TROCOAPP | NUMBER(10,2) | sim |  |
| CPFNOTA | VARCHAR2(1) | sim |  |
| PERIODOENT | VARCHAR2(1) | sim |  |
| PERACREGIRO | NUMBER(5,2) | sim |  |
| IMPORTOUCX | NUMBER(4) | sim |  |
| VLICMSDES | NUMBER(12,2) | sim |  |
| DTVALIDADEOS | DATE | sim |  |
| CRO | VARCHAR2(20) | sim |  |
| SERVICOCONCLUIDO | VARCHAR2(1) | sim |  |
| DTENVIOFV | DATE | sim |  |
| IMPRESSOROT79 | VARCHAR2(1) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| SEQCARREGAMENTO | NUMBER(4) | sim |  |
| CPFCNPJSAID | VARCHAR2(18) | sim |  |
| MODELO | VARCHAR2(250) | sim |  |
| IMEI | VARCHAR2(50) | sim |  |
| TECNICO | VARCHAR2(60) | sim |  |
| DATATECN | DATE | sim |  |
| RELATO | VARCHAR2(1000) | sim |  |
| ACESSORIOS | VARCHAR2(500) | sim |  |
| SENHA | VARCHAR2(200) | sim |  |
| CONDICAOFISICA | VARCHAR2(1000) | sim |  |
| AVARIA | VARCHAR2(1) | sim | A=ABERTA, R=REALIZADA |
| VLBONIFICACAO | NUMBER(12,2) | sim |  |
| FRETEBONIF | NUMBER(12,2) | sim |  |
| VLFRETECOTADO | NUMBER(12,2) | sim |  |
| NUMCOTACAO | NUMBER(12) | sim |  |
| INFOPEDIDO | VARCHAR2(1) | sim |  |
| NUMVIASMODELO4 | NUMBER(2) | sim |  |
| NUMLACREAVARIA | NUMBER(10) | sim |  |
| MOTIVOAVARIA | VARCHAR2(1000) | sim |  |
| PEDPRINCAVARIA | NUMBER(10) | sim |  |
| CODFUNCIMPRESROT79 | NUMBER(10) | sim |  |
| NCONTRATOCONSIG | NUMBER(10) | sim |  |
| CODETAPAECOMMERCE | VARCHAR2(10) | sim |  |
| CODCOBESPEC | VARCHAR2(1) | sim |  |
| VLCREDCLIENTEUSADO | NUMBER(12,2) | sim |  |
| VERSAOROTINA | VARCHAR2(20) | sim |  |
| SITE | VARCHAR2(1) | sim |  |
| DTSTATUSENTREGA_ECOMMERCE | DATE | sim |  |
| USADESCSUPERVISORFV | VARCHAR2(1) | sim |  |
| CODSUPERVLIB | NUMBER(10) | sim |  |
| TPENTPED | VARCHAR2(2) | sim |  |
| PEDEXPRESS | VARCHAR2(1) | sim |  |
| TPCONTATO | VARCHAR2(1) | sim |  |
| CPAGARSERV | VARCHAR2(1) | sim |  |
| NUMTOTCONS | NUMBER(6) | sim |  |
| CPAGARTRANSP | VARCHAR2(1) | sim |  |
| VENCTOCPTRANSP | DATE | sim |  |
| CODLUCROMINIMO | VARCHAR2(20) | sim |  |
| OS | VARCHAR2(1) | sim |  |
| CODFUNCMEC | NUMBER(10) | sim |  |
| CODOPDESCROD | VARCHAR2(20) | sim |  |
| OBS5 | VARCHAR2(1000) | sim |  |
| CODLOG | NUMBER(10) | sim |  |
| VLTOT_OUT_TAXAS | NUMBER(12,2) | sim |  |
| CODPLPAG_ORIGINAL | NUMBER(4) | sim |  |
| CODCOB_ORIGINAL | VARCHAR2(4) | sim |  |
| VALORFRETEMOTORISTA | NUMBER(12,2) | sim |  |
| CABNFEESPVOL | VARCHAR2(20) | sim |  |
| TRANSPORTE | VARCHAR2(4) | sim | PROCESSO DE ESTIVA SALVA TIPO DO TRANSPORTE: TE-TERCEIRIZADO EXTERNO TL ¿TERCEIRO LOCAL I-ISENTO |
| DTBLOQENTREGA | DATE | sim | GRAVAR DATA BLOQUEIO PARA BLOQUEAR A ENTREGA  DO PEDIDO E NAO PERMITIR MONTAR NA 512 |
| VLBONIFICACAO2 | NUMBER(12,2) | sim | VALOR DO BONIFICACAO2 SOMADO NO DESCONTO DO ITEM |
| VLBONIFICACAO3 | NUMBER(12,2) | sim | VALOR DO BONIFICACAO3 SOMADO NO DESCONTO DO ITEM |
| NUMPED_ORIGTP7 | NUMBER(10) | sim | NA R.1436 NAS VENDAS TIPO 7 GERADAS E GRAVADO O NUMPED DE ORIGEM |
| DTGERAR_TP7 | DATE | sim | GRAVAR DATA QUE FOI GERADO TIPO 7 |
| NAOUSARPOFERTA | VARCHAR2(1) | sim | GRAVAR NA VENDA QUE UTILIZOU A FLAG NAO UTILIZAR POFERTA R.56 |
| VICMSMONORET | NUMBER(12,2) | sim | Valor AD REM do ICMS para o produto CST=61 |
| CODFUNCLIB_VLMINPAGTO | NUMBER(10) | sim | FUNC LIBEROU O PEDIDOS ONDE O PLANO DE PAGAMENTO UTILIZAR O VALOR MININO |
| ID_MARKET | VARCHAR2(80) | sim | id do pedido no Plug4Market |
| IDCV_MARKET | VARCHAR2(80) | sim | CANAL DE VENDA DO PEDIDO NA Plug4Market |
| OS300 | VARCHAR2(1) | sim | Pedido nao consolidado rotina 300 OS |
| NUMTRANSPEDELETAR | VARCHAR2(30) | sim | GRAVAR O NUMTRANSPEDIDO AO CONSOLIDAR ORCAMENTOS PARA PODER DELETAR |

### VAREJO.CARREGAMENTO (259.026 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMCAR | NUMBER(10) | não |  |
| DATAMON | DATE | sim |  |
| CODFUNCMON | NUMBER(10) | sim |  |
| DTSAIDA | DATE | sim |  |
| CODMOTORISTA | NUMBER(10) | sim |  |
| CODVEICULO | NUMBER(6) | sim |  |
| TOTPESO | NUMBER(12,2) | sim |  |
| TOTVOLUME | NUMBER(12,2) | sim |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| DTFECHA | DATE | sim |  |
| DESTINO | VARCHAR2(40) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| DTPREVCHEG | DATE | sim |  |
| DTRETORNO | DATE | sim |  |
| DTCANCEL | DATE | sim |  |
| CODFUNCCANCEL | NUMBER(10) | sim |  |
| NUMVIASMAPA | NUMBER(2) | sim |  |
| DTFAT | DATE | sim |  |
| CODFUNCFATURA | NUMBER(10) | sim |  |
| OBSFATURA | VARCHAR2(255) | sim |  |
| TIPOCARGA | VARCHAR2(1) | sim |  |
| KMINICIAL | NUMBER(12,2) | sim |  |
| KMFINAL | NUMBER(12,2) | sim |  |
| DTSAIDAVEICULO | DATE | sim |  |
| CODROTAPRINC | NUMBER(4) | sim |  |
| NUMDIARIAS | NUMBER(4) | sim |  |
| VLVALERETENCAO | NUMBER(12,2) | sim |  |
| DTFECHACOMISSMOT | DATE | sim |  |
| QTCOMBUSTIVEL | NUMBER(18,6) | sim |  |
| OBSDESTINO | VARCHAR2(80) | sim |  |
| CODFUNCFECHA | NUMBER(10) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| FRETETERCEIRO | VARCHAR2(1) | sim |  |
| MOTIVO | VARCHAR2(40) | sim |  |
| CODFUNCCONF | NUMBER(10) | sim |  |
| STATUSPEDCAR | VARCHAR2(1) | sim |  |
| VLTOTALBNF | NUMBER(12,2) | sim |  |
| QTTOTVOLUME | NUMBER(10) | sim |  |

### JP.CARREGAMENTO (257.828 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMCAR | NUMBER(10) | não |  |
| DATAMON | DATE | sim |  |
| CODFUNCMON | NUMBER(10) | sim |  |
| DTSAIDA | DATE | sim |  |
| CODMOTORISTA | NUMBER(10) | sim |  |
| CODVEICULO | NUMBER(6) | sim |  |
| TOTPESO | NUMBER(12,2) | sim |  |
| TOTVOLUME | NUMBER(12,2) | sim |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| DTFECHA | DATE | sim |  |
| DESTINO | VARCHAR2(40) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| DTPREVCHEG | DATE | sim |  |
| DTRETORNO | DATE | sim |  |
| DTCANCEL | DATE | sim |  |
| CODFUNCCANCEL | NUMBER(10) | sim |  |
| NUMVIASMAPA | NUMBER(2) | sim |  |
| DTFAT | DATE | sim |  |
| CODFUNCFATURA | NUMBER(10) | sim |  |
| OBSFATURA | VARCHAR2(255) | sim |  |
| TIPOCARGA | VARCHAR2(1) | sim |  |
| KMINICIAL | NUMBER(12,2) | sim |  |
| KMFINAL | NUMBER(12,2) | sim |  |
| DTSAIDAVEICULO | DATE | sim |  |
| CODROTAPRINC | NUMBER(4) | sim |  |
| NUMDIARIAS | NUMBER(4) | sim |  |
| VLVALERETENCAO | NUMBER(12,2) | sim |  |
| DTFECHACOMISSMOT | DATE | sim |  |
| QTCOMBUSTIVEL | NUMBER(18,6) | sim |  |
| OBSDESTINO | VARCHAR2(80) | sim |  |
| CODFUNCFECHA | NUMBER(10) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| FRETETERCEIRO | VARCHAR2(1) | sim |  |
| MOTIVO | VARCHAR2(40) | sim |  |
| CODFUNCCONF | NUMBER(10) | sim |  |
| STATUSPEDCAR | VARCHAR2(1) | sim |  |
| VLTOTALBNF | NUMBER(12,2) | sim |  |
| QTTOTVOLUME | NUMBER(10) | sim |  |

### JP.LOGFATURAMENTO (252.304 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMCAR | NUMBER(10) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| DATA | DATE | sim |  |
| MENSAGEM | VARCHAR2(2000) | sim |  |

### VAREJO.LOGFATURAMENTO (244.541 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMCAR | NUMBER(10) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| DATA | DATE | sim |  |
| MENSAGEM | VARCHAR2(2000) | sim |  |

### JP.CADNCMPISCOFINS (223.983 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CODPROD | NUMBER(10) | não |  |
| COD_NCM | VARCHAR2(15) | não |  |
| OPERACAO | VARCHAR2(2) | não |  |
| CSTPIS | VARCHAR2(2) | não |  |
| CSTCOFINS | VARCHAR2(2) | não |  |
| PERPIS | NUMBER(8,6) | sim |  |
| PERCOFINS | NUMBER(8,6) | sim |  |
| PISCOFINS | VARCHAR2(1) | sim |  |
| CODNATPIS | VARCHAR2(4) | sim |  |
| CODNATCOFINS | VARCHAR2(4) | sim |  |
| CODNATRECFT | VARCHAR2(4) | sim |  |
| CSTPISPF | VARCHAR2(2) | sim |  |
| CSTCOFINSPF | VARCHAR2(2) | sim |  |
| PERPISPF | NUMBER(8,6) | sim |  |
| PERCOFINSPF | NUMBER(8,6) | sim |  |
| PISCOFINSPF | VARCHAR2(1) | sim |  |
| CODNATPISPF | VARCHAR2(4) | sim |  |
| CODNATCOFINSPF | VARCHAR2(4) | sim |  |
| CODNATRECFTPF | VARCHAR2(4) | sim |  |
| REGTRIBUT | NUMBER(1) | não |  |
| CEST | VARCHAR2(7) | sim |  |
| ALIQFED | NUMBER(8,6) | sim |  |
| ALIQEST | NUMBER(8,6) | sim |  |
| DTVENCALIQ | DATE | sim |  |
| CODCONTABIL | NUMBER(15) | sim |  |
| CODCREDESTORNOPISPF | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPF | NUMBER(3) | sim |  |
| CODCREDESTORNOPISPJ | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPJ | NUMBER(3) | sim |  |
| PERPISLP | NUMBER(8,6) | sim |  |
| PERCOFINSLP | NUMBER(8,6) | sim |  |
| USALIQESP | VARCHAR2(1) | sim |  |
| USA_RECEITUARIO | VARCHAR2(1) | não | Indica se o NCM regra fiscal vigente exige receituário/documento na emissão. S N. |
| REDLINE_PERPIS_SPED | NUMBER(8,6) | sim | Redução linear – Lei Complementar nº 224, de 2025 – EFD-Contribuições, Alíquotas somente no Sped Contribuições |
| REDLINE_PERCOFINS_SPED | NUMBER(8,6) | sim | Redução linear – Lei Complementar nº 224, de 2025 – EFD-Contribuições, Alíquotas somente no Sped Contribuições |

### VAREJO.CLI12MESES (218.482 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CODFILIAL | VARCHAR2(2) | não |  |
| ANO | NUMBER(4) | não |  |
| CODCLI | NUMBER(6) | não |  |
| CODVEND | NUMBER(10) | não |  |
| VLJAN | NUMBER(12,2) | sim |  |
| VLFEV | NUMBER(12,2) | sim |  |
| VLMAR | NUMBER(12,2) | sim |  |
| VLABR | NUMBER(12,2) | sim |  |
| VLMAI | NUMBER(12,2) | sim |  |
| VLJUN | NUMBER(12,2) | sim |  |
| VLJUL | NUMBER(12,2) | sim |  |
| VLAGO | NUMBER(12,2) | sim |  |
| VLSET | NUMBER(12,2) | sim |  |
| VLOUT | NUMBER(12,2) | sim |  |
| VLNOV | NUMBER(12,2) | sim |  |
| VLDEZ | NUMBER(12,2) | sim |  |
| CODPROD | NUMBER(10) | não |  |
| PESOJAN | NUMBER(12,2) | sim |  |
| PESOFEV | NUMBER(12,2) | sim |  |
| PESOMAR | NUMBER(12,2) | sim |  |
| PESOABR | NUMBER(12,2) | sim |  |
| PESOMAI | NUMBER(12,2) | sim |  |
| PESOJUN | NUMBER(12,2) | sim |  |
| PESOJUL | NUMBER(12,2) | sim |  |
| PESOAGO | NUMBER(12,2) | sim |  |
| PESOSET | NUMBER(12,2) | sim |  |
| PESOOUT | NUMBER(12,2) | sim |  |
| PESONOV | NUMBER(12,2) | sim |  |
| PESODEZ | NUMBER(12,2) | sim |  |
| LUCROJAN | NUMBER(12,2) | sim |  |
| LUCROFEV | NUMBER(12,2) | sim |  |
| LUCROMAR | NUMBER(12,2) | sim |  |
| LUCROABR | NUMBER(12,2) | sim |  |
| LUCROMAI | NUMBER(12,2) | sim |  |
| LUCROJUN | NUMBER(12,2) | sim |  |
| LUCROJUL | NUMBER(12,2) | sim |  |
| LUCROAGO | NUMBER(12,2) | sim |  |
| LUCROSET | NUMBER(12,2) | sim |  |
| LUCROOUT | NUMBER(12,2) | sim |  |
| LUCRONOV | NUMBER(12,2) | sim |  |
| LUCRODEZ | NUMBER(12,2) | sim |  |
| VLDEVOLJAN | NUMBER(12,2) | sim |  |
| VLDEVOLFEV | NUMBER(12,2) | sim |  |
| VLDEVOLMAR | NUMBER(12,2) | sim |  |
| VLDEVOLABR | NUMBER(12,2) | sim |  |
| VLDEVOLMAI | NUMBER(12,2) | sim |  |
| VLDEVOLJUN | NUMBER(12,2) | sim |  |
| VLDEVOLJUL | NUMBER(12,2) | sim |  |
| VLDEVOLAGO | NUMBER(12,2) | sim |  |
| VLDEVOLSET | NUMBER(12,2) | sim |  |
| VLDEVOLOUT | NUMBER(12,2) | sim |  |
| VLDEVOLNOV | NUMBER(12,2) | sim |  |
| VLDEVOLDEZ | NUMBER(12,2) | sim |  |

### JP.CLI12MESES (214.832 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CODFILIAL | VARCHAR2(2) | não |  |
| ANO | NUMBER(4) | não |  |
| CODCLI | NUMBER(6) | não |  |
| CODVEND | NUMBER(10) | não |  |
| VLJAN | NUMBER(12,2) | sim |  |
| VLFEV | NUMBER(12,2) | sim |  |
| VLMAR | NUMBER(12,2) | sim |  |
| VLABR | NUMBER(12,2) | sim |  |
| VLMAI | NUMBER(12,2) | sim |  |
| VLJUN | NUMBER(12,2) | sim |  |
| VLJUL | NUMBER(12,2) | sim |  |
| VLAGO | NUMBER(12,2) | sim |  |
| VLSET | NUMBER(12,2) | sim |  |
| VLOUT | NUMBER(12,2) | sim |  |
| VLNOV | NUMBER(12,2) | sim |  |
| VLDEZ | NUMBER(12,2) | sim |  |
| CODPROD | NUMBER(10) | não |  |
| PESOJAN | NUMBER(12,2) | sim |  |
| PESOFEV | NUMBER(12,2) | sim |  |
| PESOMAR | NUMBER(12,2) | sim |  |
| PESOABR | NUMBER(12,2) | sim |  |
| PESOMAI | NUMBER(12,2) | sim |  |
| PESOJUN | NUMBER(12,2) | sim |  |
| PESOJUL | NUMBER(12,2) | sim |  |
| PESOAGO | NUMBER(12,2) | sim |  |
| PESOSET | NUMBER(12,2) | sim |  |
| PESOOUT | NUMBER(12,2) | sim |  |
| PESONOV | NUMBER(12,2) | sim |  |
| PESODEZ | NUMBER(12,2) | sim |  |
| LUCROJAN | NUMBER(12,2) | sim |  |
| LUCROFEV | NUMBER(12,2) | sim |  |
| LUCROMAR | NUMBER(12,2) | sim |  |
| LUCROABR | NUMBER(12,2) | sim |  |
| LUCROMAI | NUMBER(12,2) | sim |  |
| LUCROJUN | NUMBER(12,2) | sim |  |
| LUCROJUL | NUMBER(12,2) | sim |  |
| LUCROAGO | NUMBER(12,2) | sim |  |
| LUCROSET | NUMBER(12,2) | sim |  |
| LUCROOUT | NUMBER(12,2) | sim |  |
| LUCRONOV | NUMBER(12,2) | sim |  |
| LUCRODEZ | NUMBER(12,2) | sim |  |
| VLDEVOLJAN | NUMBER(12,2) | sim |  |
| VLDEVOLFEV | NUMBER(12,2) | sim |  |
| VLDEVOLMAR | NUMBER(12,2) | sim |  |
| VLDEVOLABR | NUMBER(12,2) | sim |  |
| VLDEVOLMAI | NUMBER(12,2) | sim |  |
| VLDEVOLJUN | NUMBER(12,2) | sim |  |
| VLDEVOLJUL | NUMBER(12,2) | sim |  |
| VLDEVOLAGO | NUMBER(12,2) | sim |  |
| VLDEVOLSET | NUMBER(12,2) | sim |  |
| VLDEVOLOUT | NUMBER(12,2) | sim |  |
| VLDEVOLNOV | NUMBER(12,2) | sim |  |
| VLDEVOLDEZ | NUMBER(12,2) | sim |  |

### VAREJOANTIGO.LOGFATURAMENTO (186.847 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMCAR | NUMBER(10) | sim |  |
| NUMPED | NUMBER(10) | sim |  |
| DATA | DATE | sim |  |
| MENSAGEM | VARCHAR2(2000) | sim |  |

### VAREJOANTIGO.CABPED (186.841 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMPED | NUMBER(10) | não |  |
| CODCLI | NUMBER(6) | sim |  |
| CODPLPAG | NUMBER(4) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| DTEMISSAO | DATE | sim |  |
| DTPREVENT | DATE | sim |  |
| TIPO | VARCHAR2(2) | sim |  |
| OBS | VARCHAR2(1000) | sim |  |
| CODFUNC | NUMBER(10) | sim |  |
| TOTPESO | NUMBER(12,2) | sim |  |
| TOTVOLUME | NUMBER(12,2) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| VLCUSTOREAL | NUMBER(12,2) | sim |  |
| VLFRETE | NUMBER(12,2) | sim |  |
| VLDESCONTO | NUMBER(12,2) | sim |  |
| VLOUTRAS | NUMBER(12,2) | sim |  |
| VLTABELA | NUMBER(12,2) | sim |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| POSICAO | VARCHAR2(1) | sim |  |
| TPENTREGA | VARCHAR2(1) | sim |  |
| NUMITENS | NUMBER(4) | sim |  |
| POSICAOENT | VARCHAR2(1) | sim |  |
| NUMCAR | NUMBER(10) | sim |  |
| ENDERENT | VARCHAR2(40) | sim |  |
| BAIRROENT | VARCHAR2(30) | sim |  |
| CIDADEENT | VARCHAR2(40) | sim |  |
| ESTADOENT | VARCHAR2(2) | sim |  |
| CEPENT | VARCHAR2(10) | sim |  |
| TELENT | VARCHAR2(15) | sim |  |
| CODPRACA | NUMBER(4) | sim |  |
| CODFORNEC | NUMBER(6) | sim |  |
| INDICE | NUMBER(5,2) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| NUMVENDA | NUMBER(10) | sim |  |
| CODVEND | NUMBER(10) | sim |  |
| CODFUNCCAN | NUMBER(10) | sim |  |
| DTCANCEL | DATE | sim |  |
| OBS2 | VARCHAR2(1000) | sim |  |
| CLIENTE | VARCHAR2(70) | sim |  |
| CPFCNPJ | VARCHAR2(18) | sim |  |
| FRETEDESPACHO | VARCHAR2(1) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| NUMVIAS | NUMBER(2) | sim |  |
| CODVEICULO | NUMBER(6) | sim |  |
| CODTABNEGOCIACAO | NUMBER(2) | sim |  |
| DTINICIO | DATE | sim |  |
| HORAINICIO | NUMBER(2) | sim |  |
| MINUTOINICIO | NUMBER(2) | sim |  |
| DTFIM | DATE | sim |  |
| HORAFIM | NUMBER(2) | sim |  |
| MINUTOFIM | NUMBER(2) | sim |  |
| VLTOTPROD | NUMBER(12,2) | sim |  |
| PRAZO1 | NUMBER(4) | sim |  |
| PRAZO2 | NUMBER(4) | sim |  |
| PRAZO3 | NUMBER(4) | sim |  |
| PRAZO4 | NUMBER(4) | sim |  |
| PRAZO5 | NUMBER(4) | sim |  |
| PRAZO6 | NUMBER(4) | sim |  |
| PRAZO7 | NUMBER(4) | sim |  |
| PRAZO8 | NUMBER(4) | sim |  |
| PRAZO9 | NUMBER(4) | sim |  |
| PRAZO10 | NUMBER(4) | sim |  |
| PRAZO11 | NUMBER(4) | sim |  |
| PRAZO12 | NUMBER(4) | sim |  |
| PRAZOMD | NUMBER(12,2) | sim |  |
| QTVOL | NUMBER(12,2) | sim |  |
| TPBALCAOTLMK | VARCHAR2(1) | sim |  |
| OBS3 | VARCHAR2(1000) | sim |  |
| OBS4 | VARCHAR2(1000) | sim |  |
| OBSENTREGA1 | VARCHAR2(100) | sim |  |
| OBSENTREGA2 | VARCHAR2(100) | sim |  |
| OBSENTREGA3 | VARCHAR2(100) | sim |  |
| OBSENTREGA4 | VARCHAR2(100) | sim |  |
| OBSENTREGA5 | VARCHAR2(100) | sim |  |
| OBSENTREGA6 | VARCHAR2(100) | sim |  |
| OBSENTREGA7 | VARCHAR2(100) | sim |  |
| OBSENTREGA8 | VARCHAR2(100) | sim |  |
| OBSENTREGA9 | VARCHAR2(100) | sim |  |
| NUMSEQENTREGA | NUMBER(20) | sim |  |
| VLOUTRASDESP | NUMBER(12,2) | sim |  |
| VLCUSTOFIN | NUMBER(12,2) | sim |  |
| HORA | NUMBER(2) | sim |  |
| MINUTO | NUMBER(2) | sim |  |
| CODFILIALRETIRA | VARCHAR2(2) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| VLTOTALORIG | NUMBER(12,2) | sim |  |
| NUMCX | NUMBER(4) | sim |  |
| NUMCUPOM | NUMBER(10) | sim |  |
| IEENT | VARCHAR2(15) | sim |  |
| OBSENTREGA10 | VARCHAR2(75) | sim |  |
| OBSENTREGA11 | VARCHAR2(75) | sim |  |
| NUMPROCESSO | NUMBER(15) | sim |  |
| CODPARIND | NUMBER(6) | sim |  |
| NUMPEDORIG | NUMBER(10) | sim |  |
| TOTPESOLIQ | NUMBER(12,2) | sim |  |
| KMOS | NUMBER(12) | sim |  |
| NUMPEDORIGREMENTFUT | NUMBER(10) | sim |  |
| NUMVIASRECIBOENTMERC | NUMBER(4) | sim |  |
| VLDESCBRINDE | NUMBER(12,2) | sim |  |
| PRAZO13 | NUMBER(4) | sim |  |
| PRAZO14 | NUMBER(4) | sim |  |
| PRAZO15 | NUMBER(4) | sim |  |
| PRAZO16 | NUMBER(4) | sim |  |
| PRAZO17 | NUMBER(4) | sim |  |
| PRAZO18 | NUMBER(4) | sim |  |
| PRAZO19 | NUMBER(4) | sim |  |
| PRAZO20 | NUMBER(4) | sim |  |
| PRAZO21 | NUMBER(4) | sim |  |
| PRAZO22 | NUMBER(4) | sim |  |
| PRAZO23 | NUMBER(4) | sim |  |
| PRAZO24 | NUMBER(4) | sim |  |
| RESERVARESTOQUEORCAMENTO | VARCHAR2(1) | sim |  |
| VLAVARIA | NUMBER(18,6) | sim |  |
| STATUS | VARCHAR2(2) | sim |  |
| NUMVIAGEM | NUMBER(10) | sim |  |
| NUMNOTADEST | NUMBER(10) | sim |  |
| VLTOTALNFDEST | NUMBER(12,2) | sim |  |
| PESONFDEST | NUMBER(12,2) | sim |  |
| VOLUMENFDEST | NUMBER(12,2) | sim |  |
| NUMNOTADEST2 | NUMBER(10) | sim |  |
| VLTOTALNFDEST2 | NUMBER(12,2) | sim |  |
| PESONFDEST2 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST2 | NUMBER(12,2) | sim |  |
| NUMNOTADEST3 | NUMBER(10) | sim |  |
| VLTOTALNFDEST3 | NUMBER(12,2) | sim |  |
| PESONFDEST3 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST3 | NUMBER(12,2) | sim |  |
| NUMNOTADEST4 | NUMBER(10) | sim |  |
| VLTOTALNFDEST4 | NUMBER(12,2) | sim |  |
| PESONFDEST4 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST4 | NUMBER(12,2) | sim |  |
| NUMNOTADEST5 | NUMBER(10) | sim |  |
| VLTOTALNFDEST5 | NUMBER(12,2) | sim |  |
| PESONFDEST5 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST5 | NUMBER(12,2) | sim |  |
| CODCONSIGNAT | NUMBER(6) | sim |  |
| NUMNOTATP12 | NUMBER(10) | sim |  |
| NUMPROD | NUMBER(10) | sim |  |
| NUMNOTADEST6 | NUMBER(10) | sim |  |
| VLTOTALNFDEST6 | NUMBER(12,2) | sim |  |
| PESONFDEST6 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST6 | NUMBER(12,2) | sim |  |
| NUMNOTADEST7 | NUMBER(10) | sim |  |
| VLTOTALNFDEST7 | NUMBER(12,2) | sim |  |
| PESONFDEST7 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST7 | NUMBER(12,2) | sim |  |
| NUMNOTADEST8 | NUMBER(10) | sim |  |
| VLTOTALNFDEST8 | NUMBER(12,2) | sim |  |
| PESONFDEST8 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST8 | NUMBER(12,2) | sim |  |
| NUMNOTADEST9 | NUMBER(10) | sim |  |
| VLTOTALNFDEST9 | NUMBER(12,2) | sim |  |
| PESONFDEST9 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST9 | NUMBER(12,2) | sim |  |
| NUMNOTADEST10 | NUMBER(10) | sim |  |
| VLTOTALNFDEST10 | NUMBER(12,2) | sim |  |
| PESONFDEST10 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST10 | NUMBER(12,2) | sim |  |
| NUMNOTADEST11 | NUMBER(10) | sim |  |
| VLTOTALNFDEST11 | NUMBER(12,2) | sim |  |
| PESONFDEST11 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST11 | NUMBER(12,2) | sim |  |
| NUMNOTADEST12 | NUMBER(10) | sim |  |
| VLTOTALNFDEST12 | NUMBER(12,2) | sim |  |
| PESONFDEST12 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST12 | NUMBER(12,2) | sim |  |
| NUMNOTADEST13 | NUMBER(10) | sim |  |
| VLTOTALNFDEST13 | NUMBER(12,2) | sim |  |
| PESONFDEST13 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST13 | NUMBER(12,2) | sim |  |
| NUMNOTADEST14 | NUMBER(10) | sim |  |
| VLTOTALNFDEST14 | NUMBER(12,2) | sim |  |
| PESONFDEST14 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST14 | NUMBER(12,2) | sim |  |
| NUMNOTADEST15 | NUMBER(10) | sim |  |
| VLTOTALNFDEST15 | NUMBER(12,2) | sim |  |
| PESONFDEST15 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST15 | NUMBER(12,2) | sim |  |
| NUMNOTADEST16 | NUMBER(10) | sim |  |
| VLTOTALNFDEST16 | NUMBER(12,2) | sim |  |
| PESONFDEST16 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST16 | NUMBER(12,2) | sim |  |
| NUMNOTADEST17 | NUMBER(10) | sim |  |
| VLTOTALNFDEST17 | NUMBER(12,2) | sim |  |
| PESONFDEST17 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST17 | NUMBER(12,2) | sim |  |
| NUMNOTADEST18 | NUMBER(10) | sim |  |
| VLTOTALNFDEST18 | NUMBER(12,2) | sim |  |
| PESONFDEST18 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST18 | NUMBER(12,2) | sim |  |
| NUMNOTADEST19 | NUMBER(10) | sim |  |
| VLTOTALNFDEST19 | NUMBER(12,2) | sim |  |
| PESONFDEST19 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST19 | NUMBER(12,2) | sim |  |
| NUMNOTADEST20 | NUMBER(10) | sim |  |
| VLTOTALNFDEST20 | NUMBER(12,2) | sim |  |
| PESONFDEST20 | NUMBER(12,2) | sim |  |
| VOLUMENFDEST20 | NUMBER(12,2) | sim |  |
| POTENCIATRANSF | NUMBER(10,6) | sim |  |
| MARCATRANSF | VARCHAR2(40) | sim |  |
| NUMSERIETRANSF | VARCHAR2(25) | sim |  |
| TENSAOAT1TRANSF | VARCHAR2(6) | sim |  |
| TENSAOAT2TRANSF | VARCHAR2(6) | sim |  |
| TENSAOBT1TRANSF | VARCHAR2(3) | sim |  |
| TENSAOBT2TRANSF | VARCHAR2(3) | sim |  |
| NUMTAPETRANSF | VARCHAR2(20) | sim |  |
| TAPEATUALTRANSF | VARCHAR2(20) | sim |  |
| VOLOLEOTRANSF | NUMBER(10,6) | sim |  |
| ANOFABTRANSF | VARCHAR2(4) | sim |  |
| IMPEDANCIATRANSF | NUMBER(10,6) | sim |  |
| TIPOTRANSF | VARCHAR2(20) | sim |  |
| NUMCELGTRANSF | VARCHAR2(20) | sim |  |
| CABINEPOSTETRANSF | VARCHAR2(1) | sim |  |
| PESOTRANSF | NUMBER(10,6) | sim |  |
| CODMOTORISTA | NUMBER(6) | sim |  |
| RPMTRANSF | NUMBER(10,4) | sim |  |
| MONOFASICO | VARCHAR2(1) | sim |  |
| TIPOMOTORTRANSF | VARCHAR2(1) | sim |  |
| DESCTIPOMOTORTRANSF | VARCHAR2(255) | sim |  |
| CODAGRONOMO | NUMBER(6) | sim |  |
| LOCALAPLIC | VARCHAR2(30) | sim |  |
| CULTURA | VARCHAR2(20) | sim |  |
| DIAGNOSTICO | VARCHAR2(300) | sim |  |
| AREA | VARCHAR2(15) | sim |  |
| PRAGA | VARCHAR2(30) | sim |  |
| ANTIDOTO | VARCHAR2(30) | sim |  |
| CODMUNICIPIO | NUMBER(7) | sim |  |
| NATUREZAFRETE | VARCHAR2(30) | sim |  |
| NUMRECEITA | NUMBER(10) | sim |  |
| DTLIBPED | DATE | sim |  |
| GARANTIA | VARCHAR2(1) | sim |  |
| VLDEBCREDRCA | NUMBER(12,2) | sim |  |
| NUMTRANSPEDIDO | NUMBER(10) | sim |  |
| NUMPEDRCA0 | NUMBER(10) | sim |  |
| NUMPEDRCA | NUMBER(20) | sim |  |
| VLTOTALST | NUMBER(12,2) | sim |  |
| VLSEGURO | NUMBER(12,2) | sim |  |
| DTAUTORC | DATE | sim |  |
| CODFUNCORC | NUMBER(10) | sim |  |
| CODDIG | NUMBER(10) | sim |  |
| VLTOTCONT | NUMBER(12,2) | sim |  |
| QTTOTVOLUME | NUMBER(10) | sim |  |
| CODPARCDEST | NUMBER(6) | sim |  |
| NUMINVOICE | VARCHAR2(40) | sim |  |
| NUMPORTO | NUMBER(10) | sim |  |
| DTEMBARQUE | DATE | sim |  |
| NUMCONTAINER | VARCHAR2(40) | sim |  |
| SEALNR | NUMBER(12) | sim |  |
| BLNR | NUMBER(12) | sim |  |
| NAVIO | VARCHAR2(30) | sim |  |
| ARMADOR | VARCHAR2(40) | sim |  |
| NRRE | VARCHAR2(40) | sim |  |
| NRSD | VARCHAR2(40) | sim |  |
| DEBNOTE | VARCHAR2(100) | sim |  |
| STO | VARCHAR2(40) | sim |  |
| NUMPORTODEST | NUMBER(10) | sim |  |
| CODQUARTO | NUMBER(6) | sim |  |
| NUMPROM | VARCHAR2(20) | sim |  |
| GERARFALTA | VARCHAR2(1) | sim |  |
| ESF_ODLONGE | VARCHAR2(6) | sim |  |
| ESF_OELONGE | VARCHAR2(6) | sim |  |
| ESF_ODPERTO | VARCHAR2(6) | sim |  |
| ESF_OEPERTO | VARCHAR2(6) | sim |  |
| CIL_ODLONGE | VARCHAR2(6) | sim |  |
| CIL_OELONGE | VARCHAR2(6) | sim |  |
| CIL_ODPERTO | VARCHAR2(6) | sim |  |
| CIL_OEPERTO | VARCHAR2(6) | sim |  |
| EIXO_ODLONGE | VARCHAR2(6) | sim |  |
| EIXO_OELONGE | VARCHAR2(6) | sim |  |
| EIXO_ODPERTO | VARCHAR2(6) | sim |  |
| EIXO_OEPERTO | VARCHAR2(6) | sim |  |
| ADICAO | VARCHAR2(6) | sim |  |
| DNP_OD | VARCHAR2(6) | sim |  |
| DNP_OE | VARCHAR2(6) | sim |  |
| ALTURA | VARCHAR2(6) | sim |  |
| COLORACAO | VARCHAR2(3) | sim |  |
| INTENSIDADE | VARCHAR2(3) | sim |  |
| SITUACAO | VARCHAR2(3) | sim |  |
| CODMEDICO | NUMBER(10) | sim |  |
| OBSRECEITA | VARCHAR2(200) | sim |  |
| EANENTEDI | NUMBER(13) | sim |  |
| NUMVIASMAPABALCAO | NUMBER(1) | sim |  |
| AIDF_FORTES | VARCHAR2(25) | sim |  |
| NUMOP | NUMBER(10) | sim |  |
| NFSERVICO | VARCHAR2(1) | sim |  |
| NUMVENDATP21 | NUMBER(10) | sim |  |
| OBSACERTO | VARCHAR2(80) | sim |  |
| CODFUNCACERTO | NUMBER(6) | sim |  |
| DTACERTO | DATE | sim |  |
| CODANIMAL | NUMBER(10) | sim |  |
| DIAGANIMAL | VARCHAR2(240) | sim |  |
| NUMPEDMESCLAR | NUMBER(10) | sim |  |
| PARC1 | NUMBER(12,2) | sim |  |
| PARC2 | NUMBER(12,2) | sim |  |
| PARC3 | NUMBER(12,2) | sim |  |
| PARC4 | NUMBER(12,2) | sim |  |
| PARC5 | NUMBER(12,2) | sim |  |
| PARC6 | NUMBER(12,2) | sim |  |
| PARC7 | NUMBER(12,2) | sim |  |
| PARC8 | NUMBER(12,2) | sim |  |
| PARC9 | NUMBER(12,2) | sim |  |
| PARC10 | NUMBER(12,2) | sim |  |
| PARC11 | NUMBER(12,2) | sim |  |
| PARC12 | NUMBER(12,2) | sim |  |
| VLTOTALPARC | NUMBER(12,2) | sim |  |
| NUMCAR44 | NUMBER(10) | sim |  |
| NUMSERIE | VARCHAR2(255) | sim |  |
| NUMSERIE44 | VARCHAR2(255) | sim |  |
| INFORMANOTA | VARCHAR2(1) | sim |  |
| LISTADECOMPRA | VARCHAR2(1) | sim |  |
| DTVENCLISTA | DATE | sim |  |
| NUMPEDLISTACOMP | NUMBER(10) | sim |  |
| QTDHOSPEDE | NUMBER(3) | sim |  |
| PLACA | VARCHAR2(8) | sim |  |
| CARRO | VARCHAR2(20) | sim |  |
| VENDADIRETA | VARCHAR2(1) | sim |  |
| IMPPEDIDO | VARCHAR2(1) | sim |  |
| DUPLICOUTP12 | VARCHAR2(1) | sim |  |
| ESTPCP | VARCHAR2(1) | sim |  |
| TEMTROCA | VARCHAR2(1) | sim |  |
| QTDEBANDEJARECOLHER | NUMBER(18,6) | sim |  |
| PEDFVBLOQ | VARCHAR2(1) | sim |  |
| STATUSPEDIDOINSERIDO | VARCHAR2(1) | sim |  |
| CODMTPARAMETRO | VARCHAR2(20) | sim |  |
| CODMTLIMCRED | VARCHAR2(20) | sim |  |
| CODMTESTOQUE | VARCHAR2(20) | sim |  |
| CODMTFMARGEM | VARCHAR2(20) | sim |  |
| CODMTPMINIMO | VARCHAR2(20) | sim |  |
| STATUS_APP | VARCHAR2(5) | sim |  |
| ISVENDAPP | VARCHAR2(1) | sim |  |
| TROCOAPP | NUMBER(10,2) | sim |  |
| CPFNOTA | VARCHAR2(1) | sim |  |
| PERIODOENT | VARCHAR2(1) | sim |  |
| PERACREGIRO | NUMBER(5,2) | sim |  |
| IMPORTOUCX | NUMBER(4) | sim |  |
| VLICMSDES | NUMBER(12,2) | sim |  |
| DTVALIDADEOS | DATE | sim |  |
| CRO | VARCHAR2(20) | sim |  |
| SERVICOCONCLUIDO | VARCHAR2(1) | sim |  |
| DTENVIOFV | DATE | sim |  |
| IMPRESSOROT79 | VARCHAR2(1) | sim |  |
| NUMCONT | NUMBER(10) | sim |  |
| SEQCARREGAMENTO | NUMBER(4) | sim |  |
| CPFCNPJSAID | VARCHAR2(18) | sim |  |
| MODELO | VARCHAR2(250) | sim |  |
| IMEI | VARCHAR2(50) | sim |  |
| TECNICO | VARCHAR2(60) | sim |  |
| DATATECN | DATE | sim |  |
| RELATO | VARCHAR2(1000) | sim |  |
| ACESSORIOS | VARCHAR2(500) | sim |  |
| SENHA | VARCHAR2(200) | sim |  |
| CONDICAOFISICA | VARCHAR2(1000) | sim |  |
| AVARIA | VARCHAR2(1) | sim | A=ABERTA, R=REALIZADA |
| VLBONIFICACAO | NUMBER(12,2) | sim |  |
| FRETEBONIF | NUMBER(12,2) | sim |  |
| VLFRETECOTADO | NUMBER(12,2) | sim |  |
| NUMCOTACAO | NUMBER(12) | sim |  |
| INFOPEDIDO | VARCHAR2(1) | sim |  |
| NUMVIASMODELO4 | NUMBER(2) | sim |  |
| NUMLACREAVARIA | NUMBER(10) | sim |  |
| MOTIVOAVARIA | VARCHAR2(1000) | sim |  |
| PEDPRINCAVARIA | NUMBER(10) | sim |  |
| CODFUNCIMPRESROT79 | NUMBER(10) | sim |  |
| NCONTRATOCONSIG | NUMBER(10) | sim |  |
| CODETAPAECOMMERCE | VARCHAR2(10) | sim |  |
| CODCOBESPEC | VARCHAR2(1) | sim |  |
| VLCREDCLIENTEUSADO | NUMBER(12,2) | sim |  |
| VERSAOROTINA | VARCHAR2(20) | sim |  |
| SITE | VARCHAR2(1) | sim |  |
| DTSTATUSENTREGA_ECOMMERCE | DATE | sim |  |
| USADESCSUPERVISORFV | VARCHAR2(1) | sim |  |
| CODSUPERVLIB | NUMBER(10) | sim |  |

### VAREJOANTIGO.CARREGAMENTO (186.839 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMCAR | NUMBER(10) | não |  |
| DATAMON | DATE | sim |  |
| CODFUNCMON | NUMBER(10) | sim |  |
| DTSAIDA | DATE | sim |  |
| CODMOTORISTA | NUMBER(10) | sim |  |
| CODVEICULO | NUMBER(6) | sim |  |
| TOTPESO | NUMBER(12,2) | sim |  |
| TOTVOLUME | NUMBER(12,2) | sim |  |
| VLTOTAL | NUMBER(12,2) | sim |  |
| DTFECHA | DATE | sim |  |
| DESTINO | VARCHAR2(40) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| DTPREVCHEG | DATE | sim |  |
| DTRETORNO | DATE | sim |  |
| DTCANCEL | DATE | sim |  |
| CODFUNCCANCEL | NUMBER(10) | sim |  |
| NUMVIASMAPA | NUMBER(2) | sim |  |
| DTFAT | DATE | sim |  |
| CODFUNCFATURA | NUMBER(10) | sim |  |
| OBSFATURA | VARCHAR2(255) | sim |  |
| TIPOCARGA | VARCHAR2(1) | sim |  |
| KMINICIAL | NUMBER(12,2) | sim |  |
| KMFINAL | NUMBER(12,2) | sim |  |
| DTSAIDAVEICULO | DATE | sim |  |
| CODROTAPRINC | NUMBER(4) | sim |  |
| NUMDIARIAS | NUMBER(4) | sim |  |
| VLVALERETENCAO | NUMBER(12,2) | sim |  |
| DTFECHACOMISSMOT | DATE | sim |  |
| QTCOMBUSTIVEL | NUMBER(18,6) | sim |  |
| OBSDESTINO | VARCHAR2(80) | sim |  |
| CODFUNCFECHA | NUMBER(10) | sim |  |
| CODCOB | VARCHAR2(4) | sim |  |
| FRETETERCEIRO | VARCHAR2(1) | sim |  |
| MOTIVO | VARCHAR2(40) | sim |  |
| CODFUNCCONF | NUMBER(10) | sim |  |
| STATUSPEDCAR | VARCHAR2(1) | sim |  |
| VLTOTALBNF | NUMBER(12,2) | sim |  |
| QTTOTVOLUME | NUMBER(10) | sim |  |

### SEVERIANO.ITEMPED (174.236 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMPED | NUMBER(10) | não |  |
| CODPROD | NUMBER(10) | não |  |
| QTPEDIDA | NUMBER(12,3) | sim |  |
| PTABELA | NUMBER(18,6) | sim |  |
| PVENDA | NUMBER(18,6) | sim |  |
| VLCUSTOREAL | NUMBER(18,6) | sim |  |
| PERICM | NUMBER(5,2) | sim |  |
| PERDESC | NUMBER(5,2) | sim |  |
| ST | NUMBER(18,6) | sim |  |
| PERCOM | NUMBER(5,2) | sim |  |
| CODFISCALITEM | NUMBER(4) | sim |  |
| VLBASEST | NUMBER(12,2) | sim |  |
| VLBASEICM | NUMBER(12,2) | sim |  |
| VLICM | NUMBER(12,2) | sim |  |
| VLBASEIPI | NUMBER(12,2) | sim |  |
| VLIPI | NUMBER(18,6) | sim |  |
| CODFUNCLIB | NUMBER(10) | sim |  |
| VLCUSTOFIN | NUMBER(18,6) | sim |  |
| SEQ | NUMBER(4) | não |  |
| CODFILIALRETIRA | VARCHAR2(2) | sim |  |
| QTFALTA | NUMBER(12,3) | sim |  |
| VLCUSTOCONT | NUMBER(18,6) | sim |  |
| OBS | VARCHAR2(40) | sim |  |
| NUMLOTE | VARCHAR2(20) | sim |  |
| DTFAB | DATE | sim |  |
| DTVENC | DATE | sim |  |
| QTPEDIDAPCA | NUMBER(12,3) | sim |  |
| CODFUNCLIB2 | NUMBER(10) | sim |  |
| CODFUNCLIB3 | NUMBER(10) | sim |  |
| AVARIA | VARCHAR2(1) | sim |  |
| CODBARRA | NUMBER(14) | sim |  |
| TPENTREGAITEM | VARCHAR2(1) | sim |  |
| CODFUNCENTREG | NUMBER(10) | sim |  |
| DTENTREG | DATE | sim |  |
| SERIGRAFIA | VARCHAR2(20) | sim |  |
| BORDADO | VARCHAR2(20) | sim |  |
| OBSERVACAO | VARCHAR2(40) | sim |  |
| PVENDAORIG | NUMBER(18,6) | sim |  |
| DESCALT | VARCHAR2(120) | sim |  |
| EXIBIRITEM | VARCHAR2(1) | sim |  |
| VLDEBCREDRCA | NUMBER(18,6) | sim |  |
| LARGURA | NUMBER(18,6) | sim |  |
| ALTURA | NUMBER(18,6) | sim |  |
| QTORIG | NUMBER(13,3) | sim |  |
| UNORIG | VARCHAR2(3) | sim |  |
| OBSADIC | VARCHAR2(400) | sim |  |
| EMBALAGEMORIG | VARCHAR2(12) | sim |  |
| QTVALE | NUMBER(12,3) | sim |  |
| QTBAIXAVALE | NUMBER(12,3) | sim |  |
| VLCOMISSAO | NUMBER(12,2) | sim |  |
| PVENDAST | NUMBER(18,6) | sim |  |
| VLFRETE | NUMBER(18,6) | sim |  |
| VLOUTRASDESP | NUMBER(18,6) | sim |  |
| VLDESCONTO | NUMBER(18,6) | sim |  |
| VLSEGURO | NUMBER(18,6) | sim |  |
| PRECOCLIENTE | NUMBER(18,6) | sim |  |
| QTORIGPOL | NUMBER(13,3) | sim |  |
| PVENDAEMB | NUMBER(18,6) | sim |  |
| QTENTREGA | NUMBER(12,2) | sim |  |
| QTALTERADA | NUMBER(10,2) | sim |  |
| DT_ALTERACAO | DATE | sim |  |
| CODALTERADOR | NUMBER(10) | sim |  |
| QT_ATUAL_ENTREGA | NUMBER(10,2) | sim |  |
| STATUSENT | VARCHAR2(1) | sim |  |
| STORIG | NUMBER(18,6) | sim |  |
| VLIPIORIG | NUMBER(18,6) | sim |  |
| QTUNITCX | NUMBER(18,6) | sim |  |
| PESOORIG | NUMBER(12,3) | sim |  |
| PESOAJUST | NUMBER(12,3) | sim |  |
| VLDESCONTOICMS | NUMBER(18,6) | sim |  |
| USAFATORMASTER | VARCHAR2(1) | sim |  |
| VLSTPI | NUMBER(18,6) | sim |  |
| AAA | VARCHAR2(1) | sim |  |
| QTDEBANDEJA | NUMBER(18,6) | sim |  |
| VLFCPST | NUMBER(24,8) | sim |  |
| NITEMPED | VARCHAR2(6) | sim |  |
| XPED | VARCHAR2(15) | sim |  |
| FCPSTORIG | NUMBER(24,8) | sim |  |
| CODFILIAL | VARCHAR2(255) | sim |  |
| QTPEDIDO | FLOAT | sim |  |
| PEDIDOITEMVLTABELA | FLOAT | sim |  |
| VLTABELA | FLOAT | sim |  |
| OBSITEM | VARCHAR2(500) | sim |  |
| QTPEDIDAORIG | NUMBER(12,3) | sim |  |
| NUMCORTE | NUMBER(10) | sim |  |
| PRODUTOFERTA | VARCHAR2(1) | sim |  |
| VLICMSDES | NUMBER(24,8) | sim |  |
| GERARSALDOFLEXVENDA | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO2 | VARCHAR2(1) | sim |  |
| USADESCQTDE_DESCMISTO3 | VARCHAR2(1) | sim |  |
| BASE_VERBAFLEX_PERDESCINI | NUMBER(5,2) | sim |  |
| BASE_VERBAFLEX_PERDESCFINAL | NUMBER(5,2) | sim |  |
| VLVERBAFLEX_CREDITO | NUMBER(12,2) | sim |  |
| VLVERBAFLEX_DEBITO | NUMBER(12,2) | sim |  |
| USAVERBAFLEX_CREDITO | VARCHAR2(1) | sim |  |
| USAVERBAFLEX_DEBITO | VARCHAR2(1) | sim |  |
| NUMENTENTRADACIAP | NUMBER(10) | sim |  |
| VLCIAP | NUMBER(24,8) | sim |  |
| QTMOFADOSTP17 | NUMBER(8) | sim |  |
| QTVENCIDOSTP17 | NUMBER(8) | sim |  |
| MOTIVOMOFVENCTP17 | VARCHAR2(1000) | sim |  |
| USADESCSUPERVISORFV | VARCHAR2(1) | sim |  |
| QTDEENTAGORA | NUMBER(12,3) | sim |  |
| QTDEAGENDAR | NUMBER(12,3) | sim |  |
| QTDESEMAGENDA | NUMBER(12,3) | sim |  |

### VAREJO.CADNCMPISCOFINS (170.334 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CODPROD | NUMBER(10) | não |  |
| COD_NCM | VARCHAR2(15) | não |  |
| OPERACAO | VARCHAR2(2) | não |  |
| CSTPIS | VARCHAR2(2) | não |  |
| CSTCOFINS | VARCHAR2(2) | não |  |
| PERPIS | NUMBER(8,6) | sim |  |
| PERCOFINS | NUMBER(8,6) | sim |  |
| PISCOFINS | VARCHAR2(1) | sim |  |
| CODNATPIS | VARCHAR2(4) | sim |  |
| CODNATCOFINS | VARCHAR2(4) | sim |  |
| CODNATRECFT | VARCHAR2(4) | sim |  |
| CSTPISPF | VARCHAR2(2) | sim |  |
| CSTCOFINSPF | VARCHAR2(2) | sim |  |
| PERPISPF | NUMBER(8,6) | sim |  |
| PERCOFINSPF | NUMBER(8,6) | sim |  |
| PISCOFINSPF | VARCHAR2(1) | sim |  |
| CODNATPISPF | VARCHAR2(4) | sim |  |
| CODNATCOFINSPF | VARCHAR2(4) | sim |  |
| CODNATRECFTPF | VARCHAR2(4) | sim |  |
| REGTRIBUT | NUMBER(1) | não |  |
| CEST | VARCHAR2(7) | sim |  |
| ALIQFED | NUMBER(8,6) | sim |  |
| ALIQEST | NUMBER(8,6) | sim |  |
| DTVENCALIQ | DATE | sim |  |
| CODCONTABIL | NUMBER(15) | sim |  |
| CODCREDESTORNOPISPF | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPF | NUMBER(3) | sim |  |
| CODCREDESTORNOPISPJ | NUMBER(3) | sim |  |
| CODCREDESTORNOCOFINSPJ | NUMBER(3) | sim |  |
| PERPISLP | NUMBER(8,6) | sim |  |
| PERCOFINSLP | NUMBER(8,6) | sim |  |

### JP.DADOSTEMPENT (169.804 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| NUMENT | NUMBER(10) | sim |  |
| CODFILIAL | VARCHAR2(2) | sim |  |
| QTULTENT | NUMBER(12,3) | sim |  |
| CUSTOCONT | NUMBER(18,6) | sim |  |
| CUSTOMEDIO | NUMBER(18,6) | sim |  |
| CODFORNECULTENT | NUMBER(6) | sim |  |
| CODPROD | NUMBER(10) | sim |  |
| PTABELAULTENT | NUMBER(12,3) | sim |  |

### VAREJOANTIGO.CLI12MESES (165.121 linhas)

| Coluna | Tipo | Aceita nulo | Comentário |
|---|---|---|---|
| CODFILIAL | VARCHAR2(2) | não |  |
| ANO | NUMBER(4) | não |  |
| CODCLI | NUMBER(6) | não |  |
| CODVEND | NUMBER(10) | não |  |
| VLJAN | NUMBER(12,2) | sim |  |
| VLFEV | NUMBER(12,2) | sim |  |
| VLMAR | NUMBER(12,2) | sim |  |
| VLABR | NUMBER(12,2) | sim |  |
| VLMAI | NUMBER(12,2) | sim |  |
| VLJUN | NUMBER(12,2) | sim |  |
| VLJUL | NUMBER(12,2) | sim |  |
| VLAGO | NUMBER(12,2) | sim |  |
| VLSET | NUMBER(12,2) | sim |  |
| VLOUT | NUMBER(12,2) | sim |  |
| VLNOV | NUMBER(12,2) | sim |  |
| VLDEZ | NUMBER(12,2) | sim |  |
| CODPROD | NUMBER(10) | não |  |


## 5. Tabelas candidatas por tema

Busca por palavras-chave nos nomes das tabelas e das colunas. Ordem: primeiro as tabelas cujo NOME bate, depois as com mais colunas que batem, depois as maiores. Até 40 por tema.

### Vendas

Palavras: VENDA, CUPOM, PDV, MOVIMENTO, ITEM, NFCE, CAIXA — 701 tabelas encontradas.

| Owner | Tabela | Nome bate? | Linhas (aprox.) | Colunas que batem |
|---|---|---|---|---|
| VAREJO | ITEMPED | sim | 1.000.627 | PVENDA, CODFISCALITEM, TPENTREGAITEM, PVENDAORIG, EXIBIRITEM, PVENDAST … |
| JP | ITEMPED | sim | 998.053 | PVENDA, CODFISCALITEM, TPENTREGAITEM, PVENDAORIG, EXIBIRITEM, PVENDAST … |
| VAREJOANTIGO | ITEMPED | sim | 616.917 | PVENDA, CODFISCALITEM, TPENTREGAITEM, PVENDAORIG, EXIBIRITEM, PVENDAST … |
| SEVERIANO | ITEMPED | sim | 174.236 | PVENDA, CODFISCALITEM, TPENTREGAITEM, PVENDAORIG, EXIBIRITEM, PVENDAST … |
| BOLOS | ITEMPED | sim | 264 | PVENDA, CODFISCALITEM, TPENTREGAITEM, PVENDAORIG, EXIBIRITEM, PVENDAST … |
| JP | LOCACAO_MOVIMENTO | sim | 0 | ID_MOVIMENTO, TIPO_MOVIMENTO, DATA_MOVIMENTO, OBS_MOVIMENTO |
| JP | LOGFECHDIARIO_CRVENDAS | sim | 0 | DTENVIO_CRVENDAS, CODIGOSTATUS_CRVENDAS, STATUSENVIO_CRVENDAS |
| VAREJO | LOGFECHDIARIO_CRVENDAS | sim | 0 | DTENVIO_CRVENDAS, CODIGOSTATUS_CRVENDAS, STATUSENVIO_CRVENDAS |
| JP | LOGCANCELITEM | sim | 64.080 | NUMVENDA, NUMCUPOM |
| VAREJO | LOGCANCELITEM | sim | 43.767 | NUMVENDA, NUMCUPOM |
| VAREJOANTIGO | LOGCANCELITEM | sim | 31.848 | NUMVENDA, NUMCUPOM |
| SEVERIANO | LOGCANCELITEM | sim | 19.053 | NUMVENDA, NUMCUPOM |
| BOLOS | LOGCANCELITEM | sim | 0 | NUMVENDA, NUMCUPOM |
| BOLOS | CUPOMFISCALZ | sim | 0 | NUMCUPOMINICIO, NUMCUPOMFIM |
| VAREJO | CUPOMFISCALZ | sim | 0 | NUMCUPOMINICIO, NUMCUPOMFIM |
| SEVERIANO | CUPOMFISCALZ | sim | 0 | NUMCUPOMINICIO, NUMCUPOMFIM |
| VAREJOANTIGO | CUPOMFISCALZ | sim | 0 | NUMCUPOMINICIO, NUMCUPOMFIM |
| JP | CUPOMFISCALZ | sim | 0 | NUMCUPOMINICIO, NUMCUPOMFIM |
| JP | ITEMXML | sim | 32.955 | CODFISCALITEM |
| VAREJOANTIGO | ITEMXML | sim | 29.539 | CODFISCALITEM |
| JP | LOGNFCANCELITEM | sim | 21.392 | NUMVENDA |
| VAREJO | LOGNFCANCELITEM | sim | 8.040 | NUMVENDA |
| JP | LOGPEDCANCELITEM | sim | 3.513 | PVENDA |
| BOLOS | ITEMXML | sim | 95 | CODFISCALITEM |
| BOLOS | LOGPESOBALITEM | sim | 0 | CODLOGPESOITEM |
| BOLOS | CUPOMFISCALITEM | sim | 0 | NUMITEM |
| BOLOS | ENTREGAITEM | sim | 0 | PVENDA |
| BOLOS | ITEMESCOLAR | sim | 0 | PVENDA |
| BOLOS | ITEMPEDAUX | sim | 0 | PVENDA |
| VAREJO | CUPOMFISCALITEM | sim | 0 | NUMITEM |
| VAREJO | ENTREGAITEM | sim | 0 | PVENDA |
| VAREJOANTIGO | ENTREGAITEM | sim | 0 | PVENDA |
| VAREJOANTIGO | ITEMESCOLAR | sim | 0 | PVENDA |
| VAREJOANTIGO | ITEMPEDAUX | sim | 0 | PVENDA |
| VAREJO | ITEMESCOLAR | sim | 0 | PVENDA |
| VAREJO | ITEMPEDAUX | sim | 0 | PVENDA |
| VAREJO | ITEMXML | sim | 0 | CODFISCALITEM |
| VAREJO | LOGPESOBALITEM | sim | 0 | CODLOGPESOITEM |
| BOLOS | LOGNFCANCELITEM | sim | 0 | NUMVENDA |
| SEVERIANO | LOGPESOBALITEM | sim | 0 | CODLOGPESOITEM |

### Produtos

Palavras: PRODUTO, EAN, MERCADORIA, ITEM, DESCRICAO — 639 tabelas encontradas.

| Owner | Tabela | Nome bate? | Linhas (aprox.) | Colunas que batem |
|---|---|---|---|---|
| VAREJO | ITEMPED | sim | 1.000.627 | CODFISCALITEM, TPENTREGAITEM, EXIBIRITEM, PEDIDOITEMVLTABELA, NITEMPED, OBSITEM … |
| JP | ITEMPED | sim | 998.053 | CODFISCALITEM, TPENTREGAITEM, EXIBIRITEM, PEDIDOITEMVLTABELA, NITEMPED, OBSITEM … |
| VAREJOANTIGO | ITEMPED | sim | 616.917 | CODFISCALITEM, TPENTREGAITEM, EXIBIRITEM, PEDIDOITEMVLTABELA, NITEMPED, OBSITEM … |
| SEVERIANO | ITEMPED | sim | 174.236 | CODFISCALITEM, TPENTREGAITEM, EXIBIRITEM, NITEMPED, PEDIDOITEMVLTABELA, OBSITEM … |
| BOLOS | ITEMPED | sim | 264 | CODFISCALITEM, TPENTREGAITEM, EXIBIRITEM, PEDIDOITEMVLTABELA, NITEMPED, OBSITEM … |
| JP | PRODUTO | sim | 25.000 | DESCRICAO, PRODUTOPESO, TAMANHOPRODUTO, PRODUTOPROMO |
| VAREJO | PRODUTO | sim | 19.320 | DESCRICAO, PRODUTOPESO, TAMANHOPRODUTO |
| SEVERIANO | PRODUTO | sim | 13.551 | PRODUTOPESO, TAMANHOPRODUTO, DESCRICAO |
| VAREJOANTIGO | PRODUTO | sim | 11.932 | DESCRICAO, PRODUTOPESO, TAMANHOPRODUTO |
| BOLOS | PRODUTO | sim | 37 | DESCRICAO, PRODUTOPESO, TAMANHOPRODUTO |
| JP | ITEMXML | sim | 32.955 | DESCRICAO, CODFISCALITEM |
| VAREJOANTIGO | ITEMXML | sim | 29.539 | DESCRICAO, CODFISCALITEM |
| SEVERIANO | PRODUTOBKPCSOSN | sim | 4.163 | DESCRICAO, PRODUTOPESO |
| BOLOS | LOG_ALTER_PRODUTO | sim | 313 | DESCRICAO, PRODUTOPESO |
| BOLOS | ITEMXML | sim | 95 | DESCRICAO, CODFISCALITEM |
| VAREJO | ITEMXML | sim | 0 | DESCRICAO, CODFISCALITEM |
| VAREJO | LOG_ALTER_PRODUTO | sim | 0 | PRODUTOPESO, DESCRICAO |
| SEVERIANO | LOG_ALTER_PRODUTO | sim | 0 | DESCRICAO, PRODUTOPESO |
| SEVERIANO | ITEMXML | sim | 0 | DESCRICAO, CODFISCALITEM |
| VAREJOANTIGO | LOG_ALTER_PRODUTO | sim | 0 | DESCRICAO, PRODUTOPESO |
| JP | LOG_ALTER_PRODUTO | sim | 0 | DESCRICAO, PRODUTOPESO |
| JP | ITEMXMLIMPORTADO | sim | 128.725 | DESCRICAO |
| VAREJO | ITEMXMLIMPORTADO | sim | 87.730 | DESCRICAO |
| VAREJOANTIGO | ITEMXMLIMPORTADO | sim | 49.136 | DESCRICAO |
| SEVERIANO | ITEMXMLIMPORTADO | sim | 38.082 | DESCRICAO |
| BOLOS | ITEMXMLIMPORTADO | sim | 95 | DESCRICAO |
| BOLOS | LOGPESOBALITEM | sim | 0 | CODLOGPESOITEM |
| BOLOS | CUPOMFISCALITEM | sim | 0 | NUMITEM |
| BOLOS | ITEMESCOLAR | sim | 0 | DESCRICAO |
| VAREJO | CUPOMFISCALITEM | sim | 0 | NUMITEM |
| VAREJOANTIGO | ITEMESCOLAR | sim | 0 | DESCRICAO |
| VAREJO | ITEMESCOLAR | sim | 0 | DESCRICAO |
| VAREJO | LOGPESOBALITEM | sim | 0 | CODLOGPESOITEM |
| SEVERIANO | LOGPESOBALITEM | sim | 0 | CODLOGPESOITEM |
| SEVERIANO | CUPOMFISCALITEM | sim | 0 | NUMITEM |
| SEVERIANO | ITEMESCOLAR | sim | 0 | DESCRICAO |
| VAREJOANTIGO | CUPOMFISCALITEM | sim | 0 | NUMITEM |
| VAREJOANTIGO | LOGPESOBALITEM | sim | 0 | CODLOGPESOITEM |
| VAREJO | PROMOCONDICAOITEMSCANNTECH | sim | 0 | DESCRICAOCOND |
| VAREJO | PROMOBENEFICIOITEMSCANNTECH | sim | 0 | DESCRICAOBENEF |

### Departamentos

Palavras: DEPARTAMENTO, SECAO, GRUPO, CATEGORIA, FAMILIA — 60 tabelas encontradas.

| Owner | Tabela | Nome bate? | Linhas (aprox.) | Colunas que batem |
|---|---|---|---|---|
| BOLOS | GRUPO | sim | 15 | CODGRUPO, GRUPO |
| SEVERIANO | GRUPO | sim | 14 | CODGRUPO, GRUPO |
| JP | GRUPO | sim | 12 | CODGRUPO, GRUPO |
| VAREJO | GRUPO | sim | 11 | CODGRUPO, GRUPO |
| VAREJOANTIGO | GRUPO | sim | 10 | CODGRUPO, GRUPO |
| VAREJOANTIGO | SECAO | sim | 327 | SECAO |
| JP | SECAO | sim | 269 | SECAO |
| VAREJO | SECAO | sim | 264 | SECAO |
| SEVERIANO | SECAO | sim | 101 | SECAO |
| BOLOS | SECAO | sim | 0 | SECAO |
| JP | CATEGORIAS_MARKET | sim | 0 |  |
| VAREJO | CATEGORIAS_MARKET | sim | 0 |  |
| JP | PARAMETRO | não | 1 | USADEPARTAMENTO, ANALISEGRUPO_R0148 |
| JP | CABPED | não | 265.104 | CODGRUPO_OS_CPAGAR |
| JP | LOG_ALTER_CPAGAR | não | 22.839 | CODGRUPO |
| VAREJO | CPAGAR | não | 20.309 | CODGRUPO |
| JP | CPAGAR | não | 19.362 | CODGRUPO |
| SEVERIANO | CPAGAR | não | 15.012 | CODGRUPO |
| VAREJOANTIGO | CPAGAR | não | 7.314 | CODGRUPO |
| VAREJOANTIGO | LOG_DELETE_CPAGAR | não | 1.013 | CODGRUPO |
| JP | CLIENTE | não | 950 | CNAE_GRUPO |
| JP | LOG_DELETE_CPAGAR | não | 773 | CODGRUPO |
| SEVERIANO | CATEG | não | 386 | CATEGORIA |
| BOLOS | CONTA | não | 375 | CODGRUPO |
| VAREJO | EMPREGADO | não | 160 | SALARIOFAMILIA |
| JP | EMPREGADO | não | 141 | SALARIOFAMILIA |
| JP | CONTA | não | 136 | CODGRUPO |
| VAREJO | CONTA | não | 133 | CODGRUPO |
| SEVERIANO | CONTA | não | 109 | CODGRUPO |
| VAREJOANTIGO | CONTA | não | 86 | CODGRUPO |
| SEVERIANO | EMPREGADO | não | 61 | SALARIOFAMILIA |
| VAREJO | LOG_DELETE_CPAGAR | não | 46 | CODGRUPO |
| JP | DEPTO | não | 42 | DEPARTAMENTO |
| BOLOS | CPAGAR | não | 38 | CODGRUPO |
| VAREJO | DEPTO | não | 34 | DEPARTAMENTO |
| VAREJOANTIGO | EMPREGADO | não | 31 | SALARIOFAMILIA |
| VAREJOANTIGO | DEPTO | não | 29 | DEPARTAMENTO |
| VAREJOANTIGO | LOG_ALTER_CPAGAR | não | 27 | CODGRUPO |
| VAREJO | CATEG | não | 22 | CATEGORIA |
| JP | CATEG | não | 22 | CATEGORIA |

### Fornecedores

Palavras: FORNECEDOR, PARCEIRO — 51 tabelas encontradas.

| Owner | Tabela | Nome bate? | Linhas (aprox.) | Colunas que batem |
|---|---|---|---|---|
| JP | FORNECEDOR | sim | 616 | FORNECEDOR, FORNECEDORCOLETA |
| VAREJO | FORNECEDOR | sim | 412 | FORNECEDOR, FORNECEDORCOLETA |
| SEVERIANO | FORNECEDOR | sim | 276 | FORNECEDOR, FORNECEDORCOLETA |
| VAREJOANTIGO | FORNECEDOR | sim | 261 | FORNECEDOR, FORNECEDORCOLETA |
| BOLOS | FORNECEDOR | sim | 5 | FORNECEDOR, FORNECEDORCOLETA |
| SEVERIANO | COTACAOW_FORNECEDORES | sim | 6 |  |
| BOLOS | COTACAOW_FORNECEDORES | sim | 0 |  |
| VAREJO | COTACAOW_FORNECEDORES | sim | 0 |  |
| VAREJOANTIGO | COTACAOW_FORNECEDORES | sim | 0 |  |
| VAREJO | FORNECEDORCONTCONTABIL | sim | 0 |  |
| BOLOS | FORNECEDORCONTCONTABIL | sim | 0 |  |
| SEVERIANO | FORNECEDORCONTCONTABIL | sim | 0 |  |
| JP | FORNECEDORCONTCONTABIL | sim | 0 |  |
| JP | COTACAOW_FORNECEDORES | sim | 0 |  |
| VAREJO | PARAMETRO | não | 1 | MIN_METAGERALFORNECEDOR, VLBONUS_METAGERALFORNECEDOR |
| JP | PARAMETRO | não | 1 | MIN_METAGERALFORNECEDOR, VLBONUS_METAGERALFORNECEDOR |
| BOLOS | PROTOCOLO | não | 0 | TPPARCEIRO, CODPARCEIRO |
| SEVERIANO | PROTOCOLO | não | 0 | TPPARCEIRO, CODPARCEIRO |
| VAREJO | PROTOCOLO | não | 0 | TPPARCEIRO, CODPARCEIRO |
| VAREJOANTIGO | PROTOCOLO | não | 0 | TPPARCEIRO, CODPARCEIRO |
| JP | PROTOCOLO | não | 0 | TPPARCEIRO, CODPARCEIRO |
| JP | LOG_ALTER_CPAGAR | não | 22.839 | TIPOPARCEIRO |
| VAREJO | CPAGAR | não | 20.309 | TIPOPARCEIRO |
| JP | CPAGAR | não | 19.362 | TIPOPARCEIRO |
| SEVERIANO | CPAGAR | não | 15.012 | TIPOPARCEIRO |
| JP | VALE | não | 9.339 | TIPOPARCEIRO |
| SEVERIANO | CCORREN | não | 8.129 | TPPARCEIRO |
| VAREJOANTIGO | CPAGAR | não | 7.314 | TIPOPARCEIRO |
| VAREJO | VALE | não | 6.233 | TIPOPARCEIRO |
| VAREJOANTIGO | VALE | não | 4.693 | TIPOPARCEIRO |
| SEVERIANO | VALE | não | 2.143 | TIPOPARCEIRO |
| VAREJO | CCORREN | não | 1.731 | TPPARCEIRO |
| JP | CCORREN | não | 1.171 | TPPARCEIRO |
| VAREJOANTIGO | LOG_DELETE_CPAGAR | não | 1.013 | TIPOPARCEIRO |
| JP | LOG_DELETE_CPAGAR | não | 773 | TIPOPARCEIRO |
| VAREJO | LOGCANCELCPAGAR | não | 281 | TIPOPARCEIRO |
| SEVERIANO | LOGCANCELCPAGAR | não | 190 | TIPOPARCEIRO |
| JP | LOGCANCELCPAGAR | não | 73 | TIPOPARCEIRO |
| VAREJO | LOG_DELETE_CPAGAR | não | 46 | TIPOPARCEIRO |
| BOLOS | CPAGAR | não | 38 | TIPOPARCEIRO |


## 6. Chaves estrangeiras

Chaves estrangeiras em que pelo menos uma das tabelas é candidata.

Se aparecer pouca coisa: muitos ERPs não declaram chaves estrangeiras no banco. Nesse caso, os relacionamentos aparecem por colunas com o mesmo nome (ex.: COD_PRODUTO em várias tabelas) — veja a seção 4.

| Owner | Tabela | Coluna | → Owner | → Tabela | → Coluna | Nome da chave |
|---|---|---|---|---|---|---|
| BOLOS | CADEQUIPAMENTOPOS | CODFORNEC | BOLOS | FORNECEDOR | CODFORNEC | CADEQUIPAMENTOPOS_FK002 |
| BOLOS | CADOPERADORACARTAO | CODFORNEC | BOLOS | FORNECEDOR | CODFORNEC | CADOPERADORACARTAO_FK002 |
| BOLOS | COTACAOW_FORNECEDORES | NUMCOTA | BOLOS | COTACAOW | NUMCOTA | FK978E5713E86F175E |
| BOLOS | COTACAOW_FORNECEDORES | IDFORNEC | BOLOS | COTACAOWF | ID | FK978E57138F7C7A25 |
| JP | CADEQUIPAMENTOPOS | CODFORNEC | JP | FORNECEDOR | CODFORNEC | CADEQUIPAMENTOPOS_FK002 |
| JP | CADOPERADORACARTAO | CODFORNEC | JP | FORNECEDOR | CODFORNEC | CADOPERADORACARTAO_FK002 |
| JP | COTACAOW_FORNECEDORES | NUMCOTA | JP | COTACAOW | NUMCOTA | FK978E5713E86F175E |
| JP | COTACAOW_FORNECEDORES | IDFORNEC | JP | COTACAOWF | ID | FK978E57138F7C7A25 |
| JP | FLOWVENDAS_DISPOSITIVO | CODFUNC | JP | EMPREGADO | CODFUNC | FK_FLOWVENDAS_DISPOSITIVO_FUNC |
| JP | FLOWVENDAS_EMPREGADO | CODFUNC | JP | EMPREGADO | CODFUNC | FK_FLOWVENDAS_EMPREGADO_FUNC |
| JP | LOCACAO_MOVIMENTO | NUM_LOCACAO | JP | LOCACAO_ITEM | NUM_LOCACAO | FK_LOCMOV_ITEM |
| JP | LOCACAO_MOVIMENTO | SEQ | JP | LOCACAO_ITEM | SEQ | FK_LOCMOV_ITEM |
| JP | ROTADIA_CLIENTE | CLI_ID | JP | CLIENTE | CODCLI | FK788A054D6D3750AC |
| JP | ROTADIASEMANAL_CLIENTE | CLI_ID | JP | CLIENTE | CODCLI | FKB85B007C6D3750AC |
| SEVERIANO | CADEQUIPAMENTOPOS | CODFORNEC | SEVERIANO | FORNECEDOR | CODFORNEC | CADEQUIPAMENTOPOS_FK002 |
| SEVERIANO | CADOPERADORACARTAO | CODFORNEC | SEVERIANO | FORNECEDOR | CODFORNEC | CADOPERADORACARTAO_FK002 |
| SEVERIANO | COTACAOW_FORNECEDORES | IDFORNEC | SEVERIANO | COTACAOWF | ID | FK978E5713AA6D108C |
| SEVERIANO | COTACAOW_FORNECEDORES | NUMCOTA | SEVERIANO | COTACAOW | NUMCOTA | FK978E57136D6E9817 |
| VAREJO | CADEQUIPAMENTOPOS | CODFORNEC | VAREJO | FORNECEDOR | CODFORNEC | CADEQUIPAMENTOPOS_FK002 |
| VAREJO | CADOPERADORACARTAO | CODFORNEC | VAREJO | FORNECEDOR | CODFORNEC | CADOPERADORACARTAO_FK002 |
| VAREJO | COTACAOW_FORNECEDORES | NUMCOTA | VAREJO | COTACAOW | NUMCOTA | FK978E5713E86F175E |
| VAREJO | COTACAOW_FORNECEDORES | IDFORNEC | VAREJO | COTACAOWF | ID | FK978E57138F7C7A25 |
| VAREJOANTIGO | CADEQUIPAMENTOPOS | CODFORNEC | VAREJOANTIGO | FORNECEDOR | CODFORNEC | CADEQUIPAMENTOPOS_FK002 |
| VAREJOANTIGO | CADOPERADORACARTAO | CODFORNEC | VAREJOANTIGO | FORNECEDOR | CODFORNEC | CADOPERADORACARTAO_FK002 |
| VAREJOANTIGO | COTACAOW_FORNECEDORES | NUMCOTA | VAREJOANTIGO | COTACAOW | NUMCOTA | FK978E5713E86F175E |
| VAREJOANTIGO | COTACAOW_FORNECEDORES | IDFORNEC | VAREJOANTIGO | COTACAOWF | ID | FK978E57138F7C7A25 |


## 7. Views

19 views encontradas. A coluna "Tema provável" usa as mesmas palavras-chave.

| Owner | View | Tema provável |
|---|---|---|
| BOLOS | CLIENTEIMP |  |
| BOLOS | CPAGAS_12MESES |  |
| BOLOS | VPROD |  |
| JP | ATUALIZACAO |  |
| JP | CLIENTEIMP |  |
| JP | CPAGAS_12MESES |  |
| JP | FLOWVENDAS_ESTOQUE_MANIFESTO | Vendas |
| JP | VPROD |  |
| JP | VW_PEDIDOS_ITENS |  |
| JP | VW_PEDIDOS_LISTAGEM |  |
| SEVERIANO | CLIENTEIMP |  |
| SEVERIANO | CPAGAS_12MESES |  |
| SEVERIANO | VPROD |  |
| VAREJO | CLIENTEIMP |  |
| VAREJO | CPAGAS_12MESES |  |
| VAREJO | VPROD |  |
| VAREJOANTIGO | CLIENTEIMP |  |
| VAREJOANTIGO | CPAGAS_12MESES |  |
| VAREJOANTIGO | VPROD |  |
