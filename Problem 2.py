import requests
from bs4 import BeautifulSoup

url = input()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
html=requests.get(url,headers=headers)
soup=BeautifulSoup(html.content,'html.parser')
social_Cont=soup.find('div',{'class' : 'flex my-2 -mx-1 justify-center' }).find_all('a')
social = []
for anchor in social_Cont:
    social.append(anchor['href'])
E = soup.find('a',{'class' : 'hover:text-gray-500 text-base leading-4 mt-2 lg:mt-4 text-white cursor-pointer flex items-center justify-center md:justify-start mb-4' }).contents
email = E[1:]
PhNo = soup.find('p',{'class' : 'hover:text-gray-500 text-base leading-4 text-white cursor-pointer flex items-center justify-center md:justify-start mb-4'}).find('a').contents

print("Social links -")
for i in social:
    print(i)
print("\nEmail/s-") 
for i in email:
    print(i)
print("\nContact:")
for i in PhNo:
    print(i)
    