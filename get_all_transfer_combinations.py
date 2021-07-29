pi = False

import requests, re, html, pickle
from bs4 import BeautifulSoup


def form_link(year, page_number) :
    return 'https://www.fifacm.com/'+str(year)+'/players?page='+str(page_number)

def scrape(link) :
        page = requests.get(link)
        soup = html.unescape(str(BeautifulSoup(page.content, 'html.parser')))
        return soup

def get_average(array) :
        length = len(array)
        return int(sum(array)/length)

print(list(range(20, 22)))

pages_number = {
    20:653,
    21:636,
}

def main() :
    transfer_combinations = {}
    for year in range(20, 22) :
                for page_number in range(1, pages_number[year]) :
                        soup = scrape(form_link(year, page_number))
                        print(page_number)
                        names = [name for name in re.findall('>[^<>]+</a> </div>', soup)[4:][:-2] if name != '> </a> </div>']
                        for i in range(len(names)) :
                                try :
                                        section_of_code = soup.split(names[i])[1].split(names[i+1])[0]
                                except :
                                        section_of_code = soup.split(names[i])[1].split('Exclude Results')[0]
                                displayed = [dis.replace(' ', '').replace('>', '').replace('<', '') for dis in re.findall('>[^<>]+<', section_of_code) if not dis in ['> <', '> | <', '> R.Face<', '>|<']]
                                displayed[0] = displayed[0].split(',')[0]
                                value = displayed[6][1:]
                                k_replaced = '000'
                                m_replaced = '000000'
                                if '.' in value :
                                        point = value.split('.')[1][:-1]
                                        k_replaced = k_replaced[:-(len(point))]
                                        m_replaced = m_replaced[:-(len(point))]
                                value = value.replace('K', k_replaced).replace('M', m_replaced).replace('.', '')
                                displayed[6] = int(value)
                                position, rating, age, value = displayed[0], int(displayed[2]), int(displayed[5]), int(displayed[6])
                                key = '|'.join([position, str(rating), str(age)])
                                if key in transfer_combinations :
                                        transfer_combinations[key].append(value)
                                else :
                                        transfer_combinations[key] = [value]

    return {transfer_key:get_average(transfer_combinations[transfer_key]) for transfer_key in transfer_combinations}

transfer_combinations = main()
file_path = 'C:\\Users\\rhyde23\\Desktop\\Project\\TransferCombinations.dat'
if pi :
        file_path = convert_path(file_path)
output_file = open(file_path, 'wb')
pickle.dump(transfer_combinations, output_file)
print(transfer_combinations)

