import datetime
import PyPDF2
import spacy
import re

def read_donator_pdf(file):
    page_content = PyPDF2.PdfReader(file).pages[0].extract_text()
    parsed = "".join(page_content)
    parsed = re.sub('n', '', parsed)
    
    print(page_content)

    correspondencia_localidade = re.search(r'Hosp. Notificate: (\w+)', parsed)
    # print(correspondencia_localidade)
    correspondencia_data = re.search(r'Data: (\d{2}/\d{2}/\d{4})', parsed)
    correspondencia_rgct = re.search(r'RGCT :(\w+-\w+)', parsed)
    correspondencia_idade = re.search(r'Idade:(\s+)(\w+)', parsed)
    correspondencia_sexo = re.search(r'Sexo: (\w+)', parsed)
    correspondencia_causa = re.search(r'Causa da morte ecefálica: (\w+)', parsed)
    correspondencia_peso = re.search(r'Peso: (\d+),00', parsed)
    correspondencia_altura = re.search(r'Altura: (\d+) cm', parsed)
    correspondencia_opo = re.search(r'OPO(\s+)(\w+\s+\w+)', parsed)

    localidade = correspondencia_localidade.group(1) if correspondencia_localidade else ""
    data_oferta = datetime.datetime.strptime(correspondencia_data.group(1), '%d/%m/%Y').date() if correspondencia_data else ""
    rgct = correspondencia_rgct.group(1) if correspondencia_rgct else ""
    idade = correspondencia_idade.group(2) if correspondencia_idade else ""
    sexo = correspondencia_sexo.group(1) if correspondencia_sexo else ""
    peso = correspondencia_peso.group(1) if correspondencia_peso else ""
    altura = correspondencia_altura.group(1) if correspondencia_altura else ""
    opo = correspondencia_opo.group(2) if correspondencia_opo else ""
    causa_obito = correspondencia_causa.group(1) if correspondencia_causa else ""

    context = {'last_rgct': rgct, 'last_opo': opo, 'last_date': data_oferta,
                'last_location': localidade, 'last_height': altura,
                'last_age': idade, 'last_gender': sexo,'last_death_cause': causa_obito}


# read_donator_pdf("doador.pdf")

def test(file):
    page_content = PyPDF2.PdfReader(file).pages[0].extract_text()
    parsed = "".join(page_content)
    parsed = re.sub('n', '', parsed)
    
    rgct_match = re.search(r'RGCT\s*:\s*([\w-]+)', parsed)
    idade_match = re.search(r'Idade:\s*(\d+)', parsed)
    sexo_match = re.search(r'Sexo:\s*(\w+)', parsed)
    cor_match = re.search(r'Cor:\s*([\w\s]+)', parsed)
    abo_match = re.search(r'ABO:\s*(\w)', parsed)
    peso_match = re.search(r'Peso:\s*([\d.]+)', parsed)
    altura_match = re.search(r'Altura:\s*(\d+)', parsed)
    death_cause_match = re.search(r'Causa da morte encefálica:\s*([\w\s]+)', parsed)
    hb_match = re.search(r'HB\s*([\d.,]+)', parsed)
    tgo_match = re.search(r'TGO\s*([\d.,]+)', parsed)
    ht_match = re.search(r'HT\s*([\d.,]+)', parsed)
    tgp_match = re.search(r'TGP\s*([\d.,]+)', parsed)
    gb_match = re.search(r'GB\s*([\d.,]+)', parsed)
    fos_alc_match = re.search(r'Fos Alc\s*([\d.,]+)', parsed)
    plts_match = re.search(r'PLTS\s*([\d.,]+)', parsed)
    gama_gt_match = re.search(r'GamaGT\s*([\d.,]+)', parsed)
    ureia_match = re.search(r'Uréia\s*([\d.,]+)', parsed)
    bil_total_match = re.search(r'Bil Total\s*([\d.,]+)', parsed)
    creat_match = re.search(r'Creat\s*([\d.,]+)', parsed)
    bil_direta_match = re.search(r'Bil Direta\s*([\d.,]+)', parsed)
    na_match = re.search(r'Na\s*([\d.,]+)', parsed)
    fio2_match = re.search(r'FiO2\s*([\d.,]+)', parsed)
    k_match = re.search(r'K\s*([\d.,]+)', parsed)
    ph_match = re.search(r'Ph\s*([\d.,]+)', parsed)
    glic_match = re.search(r'Glic\s*([\d.,]+)', parsed)
    po2_match = re.search(r'PO2\s*([\d.,]+)', parsed)
    cpk_match = re.search(r'CPK\s*([\d.,]+)', parsed)
    pco2_match = re.search(r'PCO2\s*([\d.,]+)', parsed)
    ck_mb_match = re.search(r'CK-MB\s*([\d.,]+)', parsed)
    sat_o2_match = re.search(r'SatO2\s*([\d.,]+)', parsed)
    amilase_match = re.search(r'Amilase\s*([\d.,]+)', parsed)

    # Retrieve the extracted information
    rgct = rgct_match.group(1).replace('-', '') if rgct_match else None
    idade = idade_match.group(1) if idade_match else None
    sexo = sexo_match.group(1)[0] if sexo_match else None
    cor = cor_match.group(1)[0] if cor_match else None
    abo = abo_match.group(1)[0] if abo_match else None
    peso = peso_match.group(1) if peso_match else None
    altura = altura_match.group(1) if altura_match else None
    death_cause = death_cause_match.group(1).strip() if death_cause_match else None
    hb = hb_match.group(1).strip() if hb_match else None
    tgo = tgo_match.group(1).strip() if tgo_match else None
    ht = ht_match.group(1).strip() if ht_match else None
    tgp = tgp_match.group(1).strip() if tgp_match else None
    gb = gb_match.group(1).strip() if gb_match else None
    fos_alc = fos_alc_match.group(1).strip() if fos_alc_match else None
    plts = plts_match.group(1).strip() if plts_match else None
    gama_gt = gama_gt_match.group(1).strip() if gama_gt_match else None
    ureia = ureia_match.group(1).strip() if ureia_match else None
    bil_total = bil_total_match.group(1).strip() if bil_total_match else None
    creat = creat_match.group(1).strip() if creat_match else None
    bil_direta = bil_direta_match.group(1).strip() if bil_direta_match else None
    na = na_match.group(1).strip() if na_match else None
    fio2 = fio2_match.group(1).strip() if fio2_match else None
    k = k_match.group(1).strip() if k_match else None
    ph = ph_match.group(1).strip() if ph_match else None
    glic = glic_match.group(1).strip() if glic_match else None
    po2 = po2_match.group(1).strip() if po2_match else None
    cpk = cpk_match.group(1).strip() if cpk_match else None
    pco2 = pco2_match.group(1).strip() if pco2_match else None
    ck_mb = ck_mb_match.group(1).strip() if ck_mb_match else None
    sat_o2 = sat_o2_match.group(1).strip() if sat_o2_match else None
    amilase = amilase_match.group(1).strip() if amilase_match else None

    print(rgct, idade, sexo, cor, abo, peso, altura)
    print("death_cause =", death_cause)
    print("HB =", hb)
    print("TGO =", tgo)
    print("HT =", ht)
    print("TGP =", tgp)
    print("GB =", gb)
    print("Fos_Alc =", fos_alc)
    print("PLTS =", plts)
    print("GamaGT =", gama_gt)
    print("Ureia =", ureia)
    print("Bil_Total =", bil_total)
    print("Creat =", creat)
    print("Bil_Direta =", bil_direta)
    print("Na =", na)
    print("FiO2 =", fio2)
    print("K =", k)
    print("Ph =", ph)
    print("Glic =", glic)
    print("PO2 =", po2)
    print("CPK =", cpk)
    print("PCO2 =", pco2)
    print("CK-MB =", ck_mb)
    print("SatO2 =", sat_o2)
    print("Amilase =", amilase)
    causa_da_morte_encefalica_match = re.search(r'Causa da morte encefálica:\s*([\w\s]+)', parsed)
    causa_da_morte_encefalica = causa_da_morte_encefalica_match.group(1).strip() if causa_da_morte_encefalica_match else None

    print("causa_da_morte_encefalica =", causa_da_morte_encefalica)


test("doador.pdf")