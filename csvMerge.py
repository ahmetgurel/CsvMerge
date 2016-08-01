#  -*- coding=utf-8 -*-
import csv

#print 'ADA-DH-D001'.lower() == 'ada-dh-d001'    #lower fonksiyonunun denenmesi küçük harfe çevirmeye yarıyor.

def csv_to_dict(file_name):   #bu metod csv dosyalarını alıp parse edip yeni bir listeye atmamıza yarıyor
    dict = []

    item = {}
    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            for i, name in enumerate(header):
                item[name] = row[i]
            dict.append(item.copy())
    return dict


def join_dicts(dicts):    #Name değişkenine göre gezerek aynı olanları tek sütüna aynı yoksa bir alt satıra yazmaya yarıyor
    joined_dict = {}
    for dict_list in dicts:
        for item in dict_list:
            if item['Name'] != '':  # Name sütununda ' işareti bulunanları atlamamıza yarıyor
                if item['Name'] in joined_dict or item['Name'].lower() in joined_dict:  #Hepsini küçük harfe çeviriyor
                    joined_dict[item['Name'].lower()].update(item)
                else:
                    joined_dict[item['Name'].lower()] = item
    return joined_dict

#Dosyaları okumamıza yarayan metoda gönderiyor ve bunları değişkene aktarıyoruz.
sysaid = csv_to_dict('Sysaid1.csv')
sep = csv_to_dict('SEP2.csv')
bigfix = csv_to_dict('Bigfix1.csv')
qRadar = csv_to_dict('QRadar1.csv')
ad = csv_to_dict('AD.csv')

#Her bir okuyup değişkene atadığımız dosyayı Name değişkenine göre kontrol eden metoda gönderiyoruz
sum = join_dicts([sysaid,sep,bigfix,qRadar,ad])


maxLen = 0
baseIndex = ''
for rowName in sum:
    if maxLen < (len(sum[rowName].values())):
        maxLen = len(sum[rowName].values())
        baseIndex = rowName

#Son olarak sum adındakı dosyayı csv olarak yazdırıyoruz.

with open('sum.csv', 'wb') as csvfile:
    w = csv.DictWriter(csvfile, sum[baseIndex].keys())
    w.writeheader()
    for rowName in sum:
        w.writerow(sum[rowName])
