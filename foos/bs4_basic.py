from bs4 import BeautifulSoup as bs
import requests, re

root_url = 'https://www.sialparis.com'
first_url = 'https://www.sialparis.com/Exhibitors-list-SIAL-2014/Exhibitors-list/(page)/1'

r = requests.get(first_url)
rt = r.text
soup = bs(rt, 'html.parser')

##         <div class="esf-exhibitor-item" id="exhibitor_2044750">
##          <div class="esf-ei-image esf-ei-empty">
##          </div>
##          <div class="esf-ei-description">
##           <h4 class="esf-ei-title direct">
##            <a href="/Exhibitors-list-SIAL-2014/Exhibitors-list/A-a-Z-do-Cafe">
##             A a Z do Café
##            </a>
##           </h4>
##           <p class="esf-ei-country">
##            PORTUGAL
##           </p>
##           <p class="esf-ei-stand">
##            5A T 157
##           </p>
##          </div>
##         </div>
for a in soup.find_all(href=re.compile(r'^/Exhibitors-list-SIAL-2014/Exhibitors-list/\w+')):
    print(root_url + a.get('href'))

r2 = requests.get('https://www.sialparis.com/Exhibitors-list-SIAL-2014/Exhibitors-list/GRANA-Ltd')
r2 = r2.text
soup2 = bs(r2, 'html.parser')
# print(soup2.prettify())
soup3 = soup2.find('div', class_='exhibitor-content')
print(soup3.find('h2').get_text())
