#全てのファイル取得
import glob

print("allファイル取得")
files = glob.glob('C:\\Users\\moika\\OneDrive\\Documents\\GitHub\\Nutanix\\*')
for file in files:
    print(file)

print("")
#特定の拡張子のみ取得する
import glob

print(".pyファイルのみ取得")

files = glob.glob('C:\\Users\\moika\\OneDrive\\Documents\\GitHub\\Nutanix\\*.py')
for file in files:
    print(file)

#サブディレクトリ内のファイル一覧を取得する
import glob

print("サブディレクトリallファイル取得")
files = glob.glob('C:\\Users\\moika\\OneDrive\\画像\\*\\*')
for file in files:
    print(file)

   