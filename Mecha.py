#!/usr/bin/env python3.6
# -*- coding: utf-8 -*

import mechanize

url = 'https://facebook.com'
loggedin_title = 'Facebook'
# isto vai servir para confirmarmos que estamos loggedin,
# vendo o titulo da pagina para onde fomos redirecionados

username = 'seuemail@seudominio.com'
password = 'SuaPassword'

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-Agent', 'Firefox/68.0 (Windows; U; Linux; en-US; rv:19.0.6)')]

browser.open(url)
browser.select_form(nr=0)
browser.form["email"] = username
browser.form["pass"] = password
browser.submit()

if browser.title() == loggedin_title:
    print ('[+] SUCCESS')
    print ('Username: {}\nPassword: {}'.format(username, password))
else:
    print ('[-] LOGIN FAILED')

