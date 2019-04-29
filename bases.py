class urls_set:
    def __init__(self):
        pass

    bacen_get_url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda=XX&DATAINI=ii/ii/iiii&DATAFIM=ff/ff/ffff"

    bmf_get_url = "http://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-taxas-referenciais-bmf-ptBR.asp?Data=02/04/2019&slcTaxa=ACC"

    bacen_urls = {
        "AFEGANE AFEGANIST": 1,
        "ARIARY MADAGASCAR": 2331,
        "AUSTRAL": 4,
        "BALBOA/PANAMA": 6,
        "BATH/TAILANDIA": 5,
        "BIRR": 2,
        "BIRR/ETIOPIA": 3,
        "BOLIVAR SOBERANO VENEZUELANO": 2472,
        "BOLIVAR VENEZUELANO": 8,
        "BOLIVAR/VENZUELA": 7,
        "BOLIVIANO/BOLIVIA": 9,
        "BUA": 234,
        "CEDI GANA": 10,
        "COLON/COSTA RICA": 11,
        "COLON/EL SALVADOR": 12,
        "CORDOBA OURO": 14,
        "CORDOBA/NICARAGUA": 13,
        "COROA DINAMARQUESA": 15,
        "COROA ESLOVACA": 17,
        "COROA ESTONIA": 16,
        "COROA ISLND/ISLAN": 18,
        "COROA NORUEGUESA": 19,
        "COROA SUECA": 20,
        "COROA TCHECA": 21,
        "CRUZADO": 23,
        "CRUZADO NOVO": 22,
        "CRUZEIRO": 24,
        "CRUZEIRO": 25,
        "CRUZEIRO REAL": 26,
        "CUPON GEORGIANO": 27,
        "DALASI/GAMBIA": 28,
        "DINAR ARGELINO": 29,
        "DINAR IEMENITA": 32,
        "DINAR IUGOSLAVO": 34,
        "DINAR SERVIO SERVIA": 38,
        "DINAR/BAHREIN": 31,
        "DINAR/IRAQUE": 33,
        "DINAR/JORDANIA": 35,
        "DINAR/KWAIT": 30,
        "DINAR/LIBIA": 36,
        "DINAR/MACEDONIA": 37,
        "DINAR/TUNISIA": 40,
        "DIREITO ESPECIAL": 41,
        "DIRHAM/EMIR.ARABE": 43,
        "DIRHAM/MARROCOS": 42,
        "DOBRA S TOME PRIN": 44,
        "DOLAR AUSTRALIANO": 45,
        "DOLAR BRUNEI": 53,
        "DOLAR CANADENSE": 48,
        "DOLAR CARIBE ORIENTAL": 59,
        "DOLAR CAYMAN": 54,
        "DOLAR CINGAPURA": 55,
        "DOLAR DA GUIANA": 49,
        "DOLAR DA NAMIBIA": 50,
        "DOLAR DOS EUA": 61,
        "DOLAR FIJI": 56,
        "DOLAR HONG KONG": 57,
        "DOLAR IL SALOMAO": 67,
        "DOLAR LIBERIA": 64,
        "DOLAR MALAIO": 65,
        "DOLAR NOVA ZELANDIA": 66,
        "DOLAR ZIMBABUE": 60,
        "DOLAR-BULGARIA": 224,
        "DOLAR-EX-ALEM.ORI": 223,
        "DOLAR-GRECIA": 225,
        "DOLAR-HUNGRIA": 226,
        "DOLAR-ISRAEL": 227,
        "DOLAR-IUGOSLAVIA": 228,
        "DOLAR-POLONIA": 229,
        "DOLAR-ROMENIA": 231,
        "DOLAR/BAHAMAS": 46,
        "DOLAR/BARBADOS": 51,
        "DOLAR/BELIZE": 52,
        "DOLAR/BERMUDAS": 47,
        "DOLAR/ETIOPIA": 62,
        "DOLAR/JAMAICA": 63,
        "DOLAR/SURINAME": 68,
        "DOLAR/SURINAME": 78,
        "DOLAR/TRIN. TOBAG": 58,
        "DONGUE/VIETNAN": 69,
        "DRACMA/GRECIA": 70,
        "DRAM ARMENIA REP": 71,
        "ESCUDO CABO VERDE": 72,
        "ESCUDO PORTUGUES": 73,
        "ESCUDO TIMOR LESTE": 74,
        "EURO": 222,
        "FLORIM HOLANDES": 79,
        "FLORIM/ARUBA": 76,
        "FLORIM/SURINAME": 77,
        "FORINT/HUNGRIA": 80,
        "FRANCO BELGA FINA": 82,
        "FRANCO BELGA/BELG": 81,
        "FRANCO CFA BCEAO": 87,
        "FRANCO CFA BEAC": 86,
        "FRANCO CFP": 88,
        "FRANCO CONGOLES": 83,
        "FRANCO FRANCES": 91,
        "FRANCO LUXEMBURGO": 93,
        "FRANCO MALGAXE MADAGA": 94,
        "FRANCO MALI": 95,
        "FRANCO SUICO": 97,
        "FRANCO/BURUNDI": 84,
        "FRANCO/BURUNDI": 89,
        "FRANCO/COMORES": 85,
        "FRANCO/DJIBUTI": 90,
        "FRANCO/GUINE": 92,
        "FRANCO/RUANDA": 96,
        "FUA": 235,
        "GOURDE/HAITI": 98,
        "GUARANI/PARAGUAI": 99,
        "GUILDER ANTILHAS HOLANDESAS": 75,
        "HRYVNIA UCRANIA": 100,
        "IENE": 101,
        "INTI PERUANO": 102,
        "KARBOVANETS": 172,
        "KINA/PAPUA N GUIN": 173,
        "KUNA/CROACIA": 174,
        "KWANZA/ANGOLA": 139,
        "LARI GEORGIA": 103,
        "LAT LETONIA REP": 104,
        "LEK ALBANIA REP": 105,
        "LEMPIRA/HONDURAS": 106,
        "LEONE/SERRA LEOA": 107,
        "LEU/MOLDAVIA REP": 108,
        "LEU/ROMENIA": 109,
        "LEV/BULGARIA REP": 111,
        "LIBRA CIP/CHIPRE": 112,
        "LIBRA ESTERLINA": 115,
        "LIBRA ISRAELENSE": 118,
        "LIBRA SUDANESA": 123,
        "LIBRA SUL SUDANESA": 2372,
        "LIBRA/EGITO": 114,
        "LIBRA/FALKLAND": 116,
        "LIBRA/GIBRALTAR": 113,
        "LIBRA/IRLANDA": 117,
        "LIBRA/LIBANO": 119,
        "LIBRA/SIRIA REP": 122,
        "LIBRA/STA HELENA": 121,
        "LILANGENI/SUAZIL": 124,
        "LIRA ITALIANA": 125,
        "LIRA TURCA": 142,
        "LIRA TURQUIA": 126,
        "LIRA/MALTA": 120,
        "LITA LITUANIA": 127,
        "LOTI/LESOTO": 128,
        "MANAT ARZEBAIJAO": 130,
        "MARCO": 129,
        "MARCO ALEMAO": 132,
        "MARCO CONV BOSNIA": 133,
        "MARCO FINLANDES": 134,
        "METICAL MOCAMBIQ": 135,
        "NAIRA/NIGERIA": 138,
        "NAKFA ERITREIA": 137,
        "NGULTRUM/BUTAO": 149,
        "NOVA LIBRA SUDANESA": 39,
        "NOVA METICAL/MOCA": 136,
        "NOVO DINAR IUGOSLAVO": 140,
        "NOVO DOLAR/TAIWAN": 141,
        "NOVO LEU/ROMENIA": 110,
        "NOVO MANAT TURCOM": 131,
        "NOVO PESO URUGUAI": 145,
        "NOVO PESO URUGUAI": 146,
        "NOVO PESO/MEXICO": 143,
        "NOVO PESO/MEXICO": 144,
        "NOVO SOL/PERU": 147,
        "NOVO ZAIRE ZAIRE": 219,
        "NOVO ZAIRE/ZAIRE": 148,
        "NOVO ZAIRE/ZAIRE": 220,
        "OURO": 236,
        "PAANGA/TONGA": 151,
        "PALADIO": 232,
        "PATACA/MACAU": 152,
        "PESETA ESPANHOLA": 154,
        "PESETA/ANDORA": 153,
        "PESO ARGENTINO": 155,
        "PESO ARGENTINO": 156,
        "PESO BOLIVIANO": 157,
        "PESO CHILE": 158,
        "PESO MEXICANO": 164,
        "PESO/COLOMBIA": 159,
        "PESO/CUBA": 160,
        "PESO/FILIPINAS": 162,
        "PESO/GUINE BISSAU": 163,
        "PESO/MEXICO": 165,
        "PESO/REP. DOMINIC": 161,
        "PESO/URUGUAIO": 166,
        "PLATINA": 233,
        "PRATA-DEAFI": 230,
        "PULA/BOTSWANA": 167,
        "QUACHA ZAMBIA": 169,
        "QUACHA ZAMBIA": 2352,
        "QUACHA/MALAVI": 168,
        "QUETZAL/GUATEMALA": 170,
        "QUIATE/BIRMANIA": 171,
        "QUIPE/LAOS REP": 175,
        "RANDE/AFRICA SUL": 176,
        "REAL BRASIL": 177,
        "RENMINBI CHINES": 178,
        "RENMINBI HONG KONG": 2332,
        "RIAL/ARAB SAUDITA": 183,
        "RIAL/CATAR": 179,
        "RIAL/IEMEN": 181,
        "RIAL/IRAN REP": 182,
        "RIAL/OMA": 180,
        "RIEL/CAMBOJA": 184,
        "RINGGIT/MALASIA": 185,
        "RUBLO BELARUS": 186,
        "RUBLO BELARUS": 2432,
        "RUBLO/RUSSIA": 187,
        "RUFIA/MALDIVAS": 195,
        "RUPIA/INDIA": 193,
        "RUPIA/INDONESIA": 194,
        "RUPIA/MAURICIO": 189,
        "RUPIA/NEPAL": 190,
        "RUPIA/PAQUISTAO": 196,
        "RUPIA/SEYCHELES": 191,
        "RUPIA/SRI LANKA": 192,
        "SHEKEL/ISRAEL": 197,
        "SOL PERUANO": 198,
        "SOM QUIRGUISTAO": 199,
        "SOM UZBEQUISTAO": 200,
        "SOMONI TADJIQUISTAO": 188,
        "SUCRE EQUADOR": 201,
        "TACA/BANGLADESH": 202,
        "TALA": 203,
        "TALA SAMOA": 2412,
        "TALA SAMOA OC": 204,
        "TENGE CAZAQUISTAO": 205,
        "TOLAR/ESLOVENIA": 206,
        "TUGRIK/MONGOLIA": 207,
        "UGUIA MAURITANIA": 150,
        "UGUIA MAURITANIA": 2452,
        "UNID FOMENTO CHIL": 208,
        "UNID.MONET.EUROP.": 209,
        "UNIDADE DE FOMENTO DO CHILE": 2392,
        "VATU VANUATU": 210,
        "WON COREIA SUL": 212,
        "WON/COREIA NORTE": 211,
        "XELIM AUSTRIACO": 213,
        "XELIM DA TANZANIA": 214,
        "XELIM/QUENIA": 216,
        "XELIM/SOMALIA": 218,
        "XELIM/TANZANIA": 215,
        "XELIM/UGANDA": 217,
        "ZLOTY/POLONIA": 221,
    }

    bmf_options = {
        "Ajuste cupom": "ACC",
        "Alumínio": "ALD",
        "DI x Anbid": "AN",
        "Anbid x pré": "ANP",
        "Ajuste pré": "APR",
        "IBrX-50": "BRP",
        "Cobre": "CBD",
        "Cupom Cambial OC1": "DCO",
        "DI x IPCA": "DIC",
        "DI x IGP-M": "DIM",
        "Cupom limpo": "DOC",
        "DI x dólar": "DOL",
        "Dólar x pré": "DP",
        "DI x euro": "EUC",
        "Real x euro": "EUR",
        "IPCA": "IAP",
        "Ibovespa": "INP",
        "IGP-M": "IPR",
        "Real x iene": "JPY",
        "Libor": "LIB",
        "Níquel": "NID",
        "Chumbo": "PBD",
        "Prob. não default": "PDN",
        "DI x pré": "PRE",
        "Real x dólar": "PTX",
        "Spread Libor Euro x Dólar": "SDE",
        "Selic x pré": "SLP",
        "Estanho": "SND",
        "TBF x pré": "TFP",
        "TR x pré": "TP",
        "DI x TR": "TR ",
        "Zinco": "ZND"}