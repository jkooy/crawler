################  icliniq
import numpy as np
from bs4 import BeautifulSoup


# import xlwt

# x_test = np.load("x_test.npy")
# # key =x_test['COVID-19']
# y_test = np.load("y_test.npy")
# x_train = np.load("x_train.npy")
# y_train = np.load("y_train.npy")

def get_source():
    WAIT.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#server-search-app > div.contain > div.body-contain > div > div.result-wrap.clearfix')))
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    save_to_excel(soup)


import requests
from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
    # 'Cookie': '__cfduid=d62d573efb23893f3979148a6dad5738f1585330452; _fbp=fb.1.1585330455580.666176081; _ga=GA1.2.92032256.1585330459; _gid=GA1.2.1577716045.1585330459; driftt_aid=dca78e43-d946-49ca-a293-3923af58eed0; _hjid=95d195dd-5d0e-4374-92dd-05793d25df41; _hjIncludedInSample=1; DFTT_END_USER_PREV_BOOTSTRAPPED=true; acceptedGuestPolicy=true; _gac_UA-128822047-1=1.1585335236.EAIaIQobChMItOf7vam76AIVpRx9Ch3uvg74EAAYASAAEgJeJvD_BwE; htua={%22browser%22:%22Chrome%22%2C%22mobile%22:false%2C%22webview%22:false%2C%22os%22:%22Mac%22%2C%22app%22:false}; langLocale=en-US; htuid=919d3437de46c7f177909759ed0bda43; lang_locale=en-US; next_web=true; __utmc=174474555; __utmz=174474555.1585335452.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); hopes_version=HOPES-Web%2F1.2.1-ht.member%2B696; session_id=bc8344bda4ecc77998adce2b3488bd4c; __utma=174474555.92032256.1585330459.1585347131.1585350961.4; __utmt=1; _gat_UA-128822047-1=1; __utmb=174474555.3.10.1585350961; _gat_gtag_UA_128822047_6=1; previous_page_url=https%3A%2F%2Fwww.healthtap.com%2Fsearch%2Fcovid%3Fcontent_only%3D1%26next%3D1%26device_lang%3Den-US%26hopes_version%3DHOPES-Web%252F1.2.1-ht.member%252B696; previous_generic_page_visited=https%3A%2F%2Fwww.healthtap.com%2Fsearch%2Fcovidhttps%3A%2F%2Fwww.healthtap.com%2Fmember%2Ffg%3Fcontent_only%3D1%26page%3D%2Fsearch%2Fcovid%26next%3D1%26device_lang%3Den-US%26hopes_version%3DHOPES-Web%252F1.2.1-ht.member%252B696; noredirect=1; _healthTap_session=BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiJWJjODM0NGJkYTRlY2M3Nzk5OGFkY2UyYjM0ODhiZDRjBjsAVEkiD2dtdF9vZmZzZXQGOwBGaQBJIhFjdXJyZW50X3BhZ2UGOwBGSSISdXNlcl9xdWVzdGlvbgY7AFQ%3D--71c61bb3ac4992e07dc1dee81e9b3f1fa5180da0; turl=/member/fg?page=/search/covid; expires_at=1585358502; access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkYXRhIjp7InJhbmRvbSI6ImViYjE4YjlmLWY1NGQtNDVjNC05OTExLTAzZmIzNjIwN2E2NiIsInBlcnNvbiI6eyJhdXRoX3Rva2VuIjoidnhOc2VJSVJNSUREWGMwYkwyZm8iLCJpZCI6NDA1MTU5MjZ9fSwidHlwIjoiSldUIiwiZXhwIjoxNTg1MzU4NTMyLCJpc3MiOiJodHRwczovL25leHQuaGVhbHRodGFwLmNvbSJ9.6I9ikDM0huE6ajxOXEU4A-zCyVl-4oOKRCZo-bweLSyXAcQXL35DRclfGU2lnU_CberJuIyFFgzXyKVtHBt4iQ; refresh_token=6793c9f1be358012651eaf3506f7e1c99b52078e2d6fdfa39a42c9d7b126bfa5; token_type=bearer; scope=member_write%20member_read',
}


def getHtmlCode(url):
    url1 = request.Request(url, headers=headers)
    page = request.urlopen(url1).read().decode()
    return page


def save_d(soup):
    f = open('page.txt', 'a+')
    f.write(str(soup))
    f.write('\n')
    f.close()


def save_q(soup):
    f = open('page.txt', 'a+')
    f.write(str(soup))
    f.write('\n')
    f.close()


def save_a(soup):
    f = open('page.txt', 'a+')
    f.write(str(soup))
    f.write('\n\n')
    f.close()


# mainurls = []
# session = requests.Session()
# for i in range(1000):
#     response = session.get(f'https://www.icliniq.com/qa?page={i}', headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     tags = soup.find_all(attrs={"class": "card-title"})
#     for tag in tags:
#         linkfind = tag.find('a')
#         mainurls.append('https://www.icliniq.com' + linkfind.get('href'))
#     # print(mainurls)
#     print(i)
#
# f = open('url.txt', 'a+')
# f.write(str(mainurls))

####################### crawl icliniq
import requests
from urllib import request

session = requests.Session()
f = open('url.txt')
mainurls = f.read().strip("[").strip("]").strip("'").split(',')
index = 0
for i, u in enumerate(mainurls):
    # print('u',u)
    u = u.strip().strip("'")

    mainurl = u
    #     print(u)
    print(mainurl)

    response = session.get(u, headers=headers)
    subsoup = BeautifulSoup(response.text, 'lxml')
    #     print(subsoup)

    try:
        description = subsoup.find(attrs={"class": "article-details-heading"}).text.strip()
        #     print(description)

        question = subsoup.find(attrs={"class": "alert alert-default border corner qContent"}).text.strip()
        question = 'Patient:\n' + question
        #     print(question)
        answer_str = subsoup.find(attrs={"class": "ansExtCon"}).find_all('p')
        answer = " ".join([i.text for i in answer_str])
        #     print(" ".join([i.text for i in answer]))
        #         if 'pneumonia' in description or 'coronavirus' in description:
        f = open('icliniq.txt', 'a+')
        f.write('id=')
        f.write(str(index))
        f.write('\n')
        f.write(str(u))
        f.write('\n\n')
        f.write('Description')
        f.write('\n')
        f.write(str(description))
        f.write('\n')
        f.write('\n')
        f.write('Dialogue')
        #     f.write('Patient:')
        f.write('\n')
        f.write(str(question))
        f.write('\n')
        #     f.write('Doctor:')
        answer = 'Doctor:\n' + str(answer)
        f.write(answer)
        f.write('\n\n')
        f.close()
        index = index + 1
    except:
        print('undecode',u)
