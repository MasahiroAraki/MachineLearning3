import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", layout_file="layouts/slide2.slides.json")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # <span style="color: blue;">marimo ノートブックで機械学習 (2)</span>

    <img src="https://raw.githubusercontent.com/MasahiroAraki/MachineLearning3/refs/heads/main/images/notebook.svg" width="600" />"
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">はじめに</span>
    - このスライドは、marimo（アプリのスライドモード）で作成したものです
     - 1つのマークダウンセルが1ページのスライドになります
      - 印刷は PDF で1ページずつで出力して貼り合わせています
    - 元になった文章は note で公開しています
      -  [marimo ノートブックで機械学習 (2)](https://note.com/mas_araki/n/n77f80aa1e672)
    - 【注意】 marimo を用いたコードは、荒木雅弘 : 『Pythonではじめる機械学習』（森北出版, 2025）には含まれておりません。本ドキュメントは、同書の補足資料です。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">インストールと設定</span>
    - marimo プロジェクトで動かす方法
    1. プロジェクトディレクトリを作成
    2. uv でディレクトリを初期化し、marimo をインストール
       ```
       $ uv init -p 3.13
       $ uv add marimo
       ```
    3. marimo の実行
        ```
        $ uv run marimo edit ファイル名.py
        ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">ブラウザインターフェース</span>

    <img src="https://raw.githubusercontent.com/MasahiroAraki/MachineLearning3/refs/heads/main/images/notebook.svg" width="600" />"
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">セルについて（コードセルを中心に）</span>
    - セルの種類は、Python（コード）、マークダウン、SQL がある
    - コードセルは、Python のコードを書いて、Ctrl + Enter キーまたは黄色で表示されているセル右上の '▶' ボタンをクリックして実行
    - コードセルの追加は、セル左側上下の '+' をクリック
      - 追加したセルは、セル右下のアイコンで、SQL セルやマークダウンセルに変更可能
      - セルの内容は、AI による生成も可能
    - セルの削除は、セル右下のゴミ箱アイコンをクリック
    - セルの移動は、セル右側下の `⠿` の印をドラッグアンドドロップ
    - セル右上の Open cell actions ボタン `…` から開くメニューでは、セルに関するさまざまな操作が可能
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">マークダウンセル</span>
    - マークダウン形式で、見出し、箇条書き、番号付きリスト、太字、斜体、コードブロック、数式（LaTeX 形式）、画像の挿入などが可能
    - r と f のチェックボックスはそれぞれ、raw文字列、f文字列を意味する
      - 数式を書くときは r をオンにする
      - マークダウン内に Python の変数値やインスタンスの値を埋め込むときは、 f をオンにする
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">SQL セル</span>
    - データベースを指定して接続し、SQL クエリを実行して、その結果を得る
    - 接続するデータベースや、結果を格納する変数はセルの下側で指定
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">セルの外部</span>

    - 補助的な情報の表示
      - 画面左側のアイコンをクリックすることで、その横にサイドバーが開いて、ディレクトリ構成、変数エクスプローラ、DAG 、AIチャットなどが表示される
    - アプリ画面の設計
      - 画面右側のボタンから、marimo ノートブックをアプリとして起動したときの画面設計が行える
      - スライドやグリッドで設計した場合は、`layouts` ディレクトリに画面構成情報が保存される
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">marimo のコマンド</span>

    - `uv run marimo edit <notebook_file>`
      - 指定したノートブックファイルを開き、ブラウザで編集できるようにする。ノートブックファイルが存在しない場合は、新しいノートブックを作成
    - `uv run marimo run <notebook_file>`
      - 指定したノートブックファイルを web アプリとして実行
    - `uv run marimo convert <ipynb_file> -o <marimo_file>`
      - Jupyter Notebook 形式の .ipynb ファイルを marimo ノートブック形式の .py ファイルに変換
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">marimo のモード</span>

    - edit : `marimo edit ファイル名` で起動して、notebook を編集するときのモード
    - run : `marimo run ファイル名` でアプリとして実行したときのモード
    - script : `python ファイル名` で実行したときのモード
    - test : `pytest ファイル名` でテストを実行するときのモード。edit モードで `pytest` をインポートし、特定のセルを `test_` で始まる関数だけにすると、テストが自動実行される
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">チュートリアル</span>

    - `uv run marimo tutorial 種類名` でチュートリアルを起動
    - チュートリアルの種類
      - intro, dataflow, ui, markdown, plots, sql, layout, fileformat, markdown-format, for-jupyter-users
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
