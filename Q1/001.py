import urllib.request
import zipfile
import csv
url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip"
zip_name = "ubike_rent"
urllib.request.urlretrieve(url, zip_name)
File = zipfile.ZipFile(zip_name)
file_dir = './'
for file_name in File.namelist():
    File.extract(file_name, file_dir)
    print(file_name)
File.close()
File = open(file_name, 'r', encoding='utf8')
plots = csv.reader(File, delimiter=',')
t = 0
lst = []
for row in plots:
    if t == 0:
        t = 1
        continue
    lst.append([row[0], row[1], row[12]])
lstf = sorted(lst, key=lambda x: (int(x[2]), int(x[0])), reverse=True)
# print(lstf)
lstf = sorted(lstf[:5], key=lambda x: int(x[0]))
print("sno sna bemp")
for i in range(5):
    print(f'{lstf[i][0]}, {lstf[i][1]}, {lstf[i][2]}')
N = int(input())
lst = [i for i in lst if int(i[2]) >= N]
lst.sort(key=lambda x: int(x[0]))
print("sno sna bemp")
for i in lst:
    print(f'{i[0]}, {i[1]}, {i[2]}')
File.close()
