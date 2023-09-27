import os
from git import Repo
from datetime import datetime as dt

def push(   file_name : str, 
                title : str,
                date  : str = str(dt.now()),
                tags : list = ['general'], 
                categories : list = ['others'], 
                banner : str = '', 
                authors : str = [''] , 
                member : str = ['']):

    format='+++\n' \
    f'title = "{title}"\n'\
    f'date = "{date}"\n'\
    f'tags = {tags}\n'\
    f'categories = {categories}\n'\
    f'banner = "{banner}"\n'\
    f'authors = {authors}\n'\
    '+++\n'\
    '\n'\
    'Supatsara Wattanakriengkrai, Koki Okai, and Atsuhito Yamaoka attended at the software engineering symposium (SES), a symposium on software. Supatsara Wattanakriengkrai received two SIGSE Distinguished Research Award.\n'\
    '\n'\
    'ソフトウェア工学に関する国内最大級のシンポジウムである，ソフトウェアエンジニアリングシンポジウム(Software Engineering Symposium : SES)にて，M2の岡井 光輝さんとM2の山岡 厚仁さんが発表を行いました．また，D2のSupatsara Wattanakriengkraiさんがソフトウェア工学研究会卓越研究賞(SIGSE Distinguished Research Award)を2件受賞されました．\n'\
    '\n'\
    '\n'\
    '**TITLE OF RESEARCH**\n'\
    '\n'\
    '**Supatsara Wattanakriengkrai**\n'\
    '”Understanding the Role of External Pull Requests in the NPM Ecosystem  Giving Back: Contributions Congruent to Library Dependency Changes in a Software Ecosystem”\n'\
    '**Koki Okai** \n'\
    '”型とスコープに着目した一文字変数の利用状況の調査”\n'\
    '**Atsuhito Yamaoka**\n'\
    '”実行トレースの差分を用いたライブラリ非互換性の分析支援”\n'\
    '\n'\
    '\n'\
    '**Location:** <br>\n'\
    'Waseda University, Tokyo, Japan\n'\
    '\n'\
    '{{< figure src="/img/news/2023-08-29-ses-1.jpg" height=".3" title="A presentation at CSEE&T and Aworded! [CSEE&T での発表および受賞]" >}}\n'\
    '{{< figure src="/img/news/2023-08-29-ses-2.jpg" height=".3" >}}\n'\
    '{{< figure src="/img/news/2023-08-29-ses-3.jpg" height=".3" >}}\n'

    repo = Repo(os.getcwd())
    upload_file = 'push_files/'+file_name+'.md'

    with open(upload_file , 'w') as f:
        # f.write('title = "'+ title + '"\n')
        # f.write('member = "'+ member + '"\n')
        f.write(format)
    
    add_file = [upload_file]
    repo.index.add(add_file)
    repo.index.commit("update from python")
    repo.remotes.origin.push()