import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", layout_file="layouts/slide1.slides.json")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # <span style="color: blue;">marimo ノートブックで機械学習 (1)</span>

    <img src="https://raw.githubusercontent.com/MasahiroAraki/MachineLearning3/refs/heads/main/images/marimo.svg" width="400" />
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
      -  [marimo ノートブックで機械学習 (1)](https://note.com/mas_araki/n/n4fbcc8a74b08)
    - 【注意】 marimo を用いたコードは、荒木雅弘 : 『Pythonではじめる機械学習』（森北出版, 2025）には含まれておりません。本ドキュメントは、同書の補足資料です。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">marimo とは</span>

    * 次世代の Python notebook 環境
    * コードセル間の関係を DAG（有向非巡回グラフ）として管理することで、ある変数の値を変更すると、その変数に依存するセルが自動的に再実行される
      - この機能によって、変数の値をスライダーやドロップダウンリストでインタラクティブに変更すると、その値を利用して計算したデータやグラフ表示が自動的に更新される
    * notebook は Python のコードとして保存されるので、Git やコーディングエージェントとの相性がよい
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">marimo に至る道</span>

    * Jupyter notebook で十分なのでは？
      * Jupyter notebook は、Python の試行錯誤的コーディングに適しているので、初学者の学習に特に有用
      * しかし、基本設計が 2010 年代初頭のものであり、最新の Python エコシステムや生成 AI が十分に活用できているとはいえない
    * Python のノートブック環境を、現状の技術を前提に再設計してみては？
      * marimo は、そのようなアプローチのひとつ
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### <span style="color: blue;">REPL から Jupyter notebook まで</span>
    - Python の試行錯誤的なコーディング環境は、できることが増える方向に発展してきた
    <img src="https://raw.githubusercontent.com/MasahiroAraki/MachineLearning3/refs/heads/main/images/repl2marimo.svg" width="800" />
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### <span style="color: blue;">REPL</span>
    - Read（読み込み）、Eval（評価）、Print（表示）、Loop（繰り返し）
    - 履歴は上下の矢印キーでたどる
    - 多くの新しい言語で実装されており、文法の確認などに用いる
    ```console
    >>> data = [6, 1, 8]
    >>> sum(data)
    15
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### <span style="color: blue;">IPython</span>
    - REPL の拡張版
    - 入出力が In[1]:/Out[1] 形式の番号付きになるので、特定の出力を Out[1] のように番号で参照できる
    - マジックコマンドはコード実行に対してメタ的に働く（例 : 実行時間を計測する `%time`）
    - シェルコマンドは Python が動いている OS の機能を呼び出す(例 : `!ls`)

    ```console
    In [1]: a = !date
    In [2]: a[0].split(' ')[1:3]
    ['Nov', '24']
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### <span style="color: blue;">Jupyter notebook</span>
    - 当初は、IPython に対するブラウザーインターフェース IPython notebook として開発された
      - 後に Julia, Python, R を主要なターゲットとする Jupyter notebook プロジェクトに発展
    - プログラムを書くコードセルと、Markdown 文書を書くマークダウンセルを組み合わせて、ドキュメントを作成
    - コード、Markdown, 出力画像などをひとつの JSON 形式のファイルとして保存

    <img src="https://raw.githubusercontent.com/MasahiroAraki/MachineLearning3/refs/heads/main/images/jb.svg" width="500" />
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">なぜ marimo か</span>

    - marimo の特徴
      - 「AI-native で reactive な notebook であり、Git-friendly である」
      - これらは裏返すと、Jupyter notebook の欠点と見ることができる
    - Jupyter notebook でも、これらの欠点へ対処する方法は試みられている。しかし、継ぎ足しを続けて複雑な構造物を作るのではなく、現状の技術をベースに Python のノートブック環境をゼロから考えたらどうなるか、という試みのひとつが marimo だと考えられる
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### <span style="color: blue;">AI-native である</span>
    - marimo の処理系が直接 LLM を使っているので、現在の LLM が得意なことを、最大限に引き出すようになっている
      - notebook のコードが LLM にコンテキストとして渡されているので、高精度なコード生成・補完が可能
      - メモリに保持された変数の値を `@変数名` を使って参照できるので、現在の変数の内容を踏まえた質問が可能
    - ファイルが Python のコードなので、コーディングエージェントの使用が容易
    - MCP server, client の機能を持っている

    <img src="https://raw.githubusercontent.com/MasahiroAraki/MachineLearning3/refs/heads/main/images/AInative.svg" width="400" />
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### <span style="color: blue;">reactive である</span>
    - セルの依存関係が DAG (有向非巡回グラフ) で管理されている
      - あるセルで変数値を変更すると、それに影響を受ける他のセル（のみ）が自動的に再実行される
      - これが「同じ名前を持つ変数や関数を、異なるセルで定義することができない」という marimo 独自のルールにつながる
    <img src="https://raw.githubusercontent.com/MasahiroAraki/MachineLearning3/refs/heads/main/images/DAG.svg" width="300" />
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### <span style="color: blue;">Git-friendly である</span>
    - marimo notebook は実行可能な Python コード
      - Git でのバージョン管理に適している
      - コーディングエージェントを用いるときに、GitHub でのプルリクエストが読みやすい
    - プロジェクトとしての管理が容易
      - 実行結果は `__marimo__` ディレクトリに書かれるが、ここをリポジトリで管理する必要はない
      - エディタとしてのブラウザの設定は、`~/.config/marimo/marimo.toml` に保存されるので、プロジェクトをまたいで利用できる
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">まとめ</span>
    - marimo への道
      - REPL, IPython, Jupyter notebook から marimo へ
    - marimo の特徴
    　　- AI-native で reactive な notebook であり、Git-friendly である」
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
