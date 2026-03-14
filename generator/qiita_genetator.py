from jinja2 import Environment, FileSystemLoader
import requests

# テンプレートファイルが置かれているディレクトリを指定
file_loader = FileSystemLoader('generator/templates')
env = Environment(loader=file_loader)

# テンプレートファイルの読み込み
template = env.get_template('qiita.jinja')

# テンプレートに埋め込むデータ
endpoint = "https://qiita.com/api/v2/users/kowaretyatta/items"
response = requests.get(endpoint).json()

# テンプレートをレンダリング（データを埋め込んでHTMLを生成）
output = template.render(datas=response[:3])  # 最新の3記事を表示

# 生成されたHTMLをファイルに保存
with open('fragment/qiita.html', 'w', encoding='utf-8') as f:
    f.write(output)
