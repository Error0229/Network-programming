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
for row in plots:
    if t == 0:
        t = 1
        continue
    if int(row[2]) - int(row[3]) > 5:
        print(
            f'{row[0]:\u3000<5}, {row[1]:\u3000<20}, {row[2]:5s}, {row[3]:5s}, {row[8]:20s}, {row[12]:5s}')
File.close()
