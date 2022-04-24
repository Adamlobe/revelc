from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

print('\n\tAutomação inicializada!')
#login = input('\nInforme seu usuário: ')
#senha = getpass.getpass('\nInforme sua senha: ')

driver = webdriver.Chrome('/home/adam/Documentos/programação/SerCAE/chromedriver')
driver.get('https://brasil.sercaeone.com/sercae/pages/core/login.jsf')

#login
driver.find_element_by_xpath('//*[@id="j_username"]').send_keys("ACCNA034")
#senha
driver.find_element_by_xpath('//*[@id="j_password"]').send_keys("Powerockao123," + Keys.ENTER)
time.sleep(2)
#Adentrar como Cliente
driver.find_element_by_xpath('//*[@id="frmMiPanelMiEmpresa:btnCliente"]').click()
time.sleep(2)
#Home
driver.find_element_by_xpath('//*[@id="cabeceraSecundariaBtnMenu"]/img').click()
time.sleep(2)
#Controle de Acesso
driver.find_element_by_xpath('//*[@id="iconform:MENU_CLI_CONTROL_ACCESO"]').click()
#Historico de acesso
driver.find_element_by_xpath('//*[@id="iconform:MENU_CLI_CONTROL_ACCESO_HISTORIAL_ACCESOS"]').click()
#Filtros
#Today
driver.find_element_by_xpath('//*[@id="frmFiltroBusqueda:dtFechaInicioPopupButton"]').click()
driver.find_element_by_xpath('//*[@id="frmFiltroBusqueda:dtFechaInicioFooter"]/table/tbody/tr/td[5]/div').click()
time.sleep(2)

table = pd.read_excel('/home/adam/Documentos/programação/SerCAE/Controle_de_acesso/portarias.xlsx')
for i, Portaria in enumerate(table['Portaria']):
    terminal = table.loc[i,'Portaria']
    
    #Terminal
    driver.find_element_by_xpath('//*[@id="frmFiltroBusqueda:inEleDes"]').send_keys(terminal)
    #Buscar
    buscar = driver.find_element_by_xpath('//*[@id="frmFiltroBusqueda:j_id190"]').click()
    time.sleep(1)
    #resultado
    ache = driver.find_elements_by_xpath('//*[@id="formListadoRegistroDeAccesos:dtAccesos"]/tfoot/tr/td/table/tbody/tr/td/table')[0].text
    print(terminal + ' ' + ache)
    #Limpar
    driver.find_element_by_xpath('//*[@id="frmFiltroBusqueda:inEleDes"]').clear()

print('\n\tFim da automação')
time.sleep(5)