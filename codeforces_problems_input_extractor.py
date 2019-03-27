
import urllib2
from bs4 import BeautifulSoup
import time

start = time.time()

f_url="https://codeforces.com/";
a_url=raw_input("Enter the problem link : ");
f_url+=a_url;

print("Extracting problem inputs from "+f_url);

#get the web page content
page=urllib2.urlopen(f_url)
#print(page)

# parse the html using beautiful soup
f_page=BeautifulSoup(page, 'html.parser')
#print(f_page)

k=0;
para=''
for input_s in f_page.find_all('div', attrs={'class':'input'}):
	#print(input_s)

	for f_text in input_s.find_all('pre'):
		test=str(f_text)
		#print("test = "+test)
		#print(len(test))
		s=''
		f=0
		g=0
		o='0'
		for c in test:
			if c=='>':
				f=1
				g=1
			elif c=='<':
				f=0
				if ord(o)>47 and ord(o)<=57:
					s+='\n'
			if f==1 and c!='>':
				s+=c
			o=c
		#print(str(k)+" "+s)
		#para+="Input :"+str(k)+'\n'
		s.replace('\n','',10)
		#print(s)
		para+=(s)
	k+=1

f_string=str(k)+para;
print(f_string)

f=open('newinput.txt','w')
f.write(f_string)
f.close()
#print(input_data)
