from jinja2 import Environment, FileSystemLoader
import requests

# テンプレートファイルが置かれているディレクトリを指定
file_loader = FileSystemLoader('generator/templates')
env = Environment(loader=file_loader)

# テンプレートファイルの読み込み
template = env.get_template('zenn.jinja')

# テンプレートに埋め込むデータ
endpoint = "https://zenn.dev/api/articles?username=nanikore"
response = requests.get(endpoint).json()

# テンプレートをレンダリング（データを埋め込んでHTMLを生成）
output = template.render(datas=response['articles'][:3])  # 最新の3記事を表示

# 生成されたHTMLをファイルに保存
with open('fragment/zenn.html', 'w', encoding='utf-8') as f:
    f.write(output)
