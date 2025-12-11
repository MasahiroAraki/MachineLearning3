import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    import numpy as np
    import pandas as pd
    import altair as alt
    from sklearn.datasets import load_iris, load_digits, load_wine, load_breast_cancer
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.metrics import confusion_matrix, classification_report
    from sklearn.pipeline import make_pipeline

    np.set_printoptions(precision=3, suppress=True)
    pd.set_option('display.precision', 3)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Setup cell
    - 上のセルは Setup cell です。このセル左側の `+` ボタンを cmd キーを押しながらクリックして選択することで作成できます。Setup cell は、すべてのセルの実行に先立って実行されるもので、作成は任意です。

    /// attention | Attention!

    Setup cell は必ずページ先頭に固定されるというレイアウト上の問題があります。また、ページをロードした後に、右下の "Run all slate cells" ボタンを押して（またはブラウザ下部メニューの "on startup" を autorun にして）必ず DAG を作成してからコーディングすることにしておけば、特別扱いのセルを作成する必要はありません。これらから、Setup cell のメリットはあまりないように思います。

    現に marimo のチュートリアルでも、`import` 文は通常のコードセルでノートブックの一番下に配置されています。
    ///
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # 機械学習の基本的な手順

    - 2章「機械学習の基本的な手順」から、探索的データ解析と、評価法の選択・学習の内容を用いて、marimo の特徴を紹介します。
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.mermaid(
    """
    flowchart LR
        A[データの収集・整理]
        B[探索的データ解析]
        C[前処理]
        D[評価法の選択]
        E[学習]
        F[結果の表示]
        A --> B --> C --> D --> E --> F
        style A stroke-dasharray: 5 5,stroke:#333,fill:#ffffff
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## 探索的データ解析

    - `marimo.ui` ライブラリには、ボタンやメニューなど、web インタフェースでよく見かける入力コンポーネントが用意されています。ここでは、探索的データ解析の手順を、いくつかのコンポーネントを使いながら説明します。
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### dropdown メニュー
    - 探索的データ解析の対象として、scikit-learn の toydata set のうち、4つの識別用データセットから1つを選ぶ dropdown メニューを作成します。
    - 選択するデータを変更すると、この変数を参照しているセルが自動的に再実行されます（DAGを作成している場合）。
    """)
    return


@app.cell
def _():
    dropdown_dict = mo.ui.dropdown(
        options={"iris":load_iris, "digits":load_digits, "wine":load_wine, "breast_cancer":load_breast_cancer},
        value="iris", # initial value
        label="Choose dataset")

    dropdown_dict
    return (dropdown_dict,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### DataFrame の扱い
    - dropdown メニューで選んだ値は、UIコンポーネントインスタンスの `value` 属性で取得できます。
      -  下記のコード例は、辞書の値として関数を持っているので、少し特殊な振る舞いをしています。
    - この例のように、pandas や polars の `DataFrame` を marimo で出力すると、いくつかの特別な操作が可能になります。
      - デフォルトの表示では、列名をクリックすることで、列ごとの並べ替えやフィルタリングが可能です。
      - 表示最下行のアイコンから Chart builder を選んで、表の上部の Table 横の `+` をクリックすると、何種類かのチャートをインタラクティブに作成できます。
      - `mo.ui.dataframe(データフレーム)` で DataFrame を表示すると、GUI でデータの変換操作が可能で、その操作を行う Python コードを得ることができます。
      - 詳細は [marimo での DataFrame の扱いのページ](https://docs.marimo.io/guides/working_with_data/dataframes/) を参照してください。
    """)
    return


@app.cell
def _(dropdown_dict):
    toydata = dropdown_dict.value()

    df = pd.DataFrame(
        data=toydata.data,
        columns=toydata.feature_names
    )
    df["target"] = toydata.target
    df
    return df, toydata


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### データの可視化

    - marimo では、データ可視化ライブラリ Altair や、Plotly を用いたグラフ表示が行えます。以下では、高次元のデータを PCA（本文11.2節で説明）で2次元に削減して散布図を描画しており、マウスオーバーで、各点の値が表示されます。

    - `mo.ui.altair_chart()` で作成したコンポーネントは、`value` 属性で選択範囲の DataFrame が取得できます。このようにグラフ表示をインタラクティブな部品として扱う方法は、[marimo の plotting のページ](https://docs.marimo.io/guides/working_with_data/plotting/) を参照してください。
    """)
    return


@app.cell
def _(toydata):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(toydata.data) 

    df2 = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
    df2["target"] = toydata.target
    df2["target_name"] = [toydata.target_names[i] for i in toydata.target]

    chart = mo.ui.altair_chart(
              alt.Chart(df2)
              .mark_point()
              .encode(
                x="PC1", y="PC2", color="target_name:N", tooltip=["PC1", "PC2", "target_name"]
              )
              .properties(
                width=400, height=300, title="PCA (2D)"
              )
            )
    return (chart,)


@app.cell
def _(chart):
    mo.vstack([chart, mo.ui.table(chart.value)])
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### tab を用いた表示の切り替え

    - タブは、ユーザーの選択によって表示内容を切り替えるUI部品です。
    - 通常は、ユーザに見せるべき情報を見せ、他の情報は隠すために使われます。
    - ここでは、異なる対象に向けてデータの説明を LLM で生成します。
    - 使用する LLM を、dummy, LMStudio 経由でローカルモデル、OpenAI API から選択してください。
      - LMStudio や OpenAI API の使用については、それぞれ設定が必要です。また、OpenAI API は有料のサービスです。
    - タブで初学者・中級者・上級者を切り替えると、それぞれの対象に向けた説明が出力されます。
    """)
    return


@app.cell(hide_code=True)
def _(LLMselect):
    mo.md(f"""
    {LLMselect}
    """)
    return


@app.cell
def _(explain_data, toydata):
    prompt = [
        "以下の内容を日本語で100字程度にまとめてください。やさしいお姉さんが中学生に説明するように。",
        "以下の内容を日本語で200字程度にまとめてください。男子大学生が、タメ口で友達に説明するように。",
        "以下の内容を、専門用語を交えながら、機械学習を実行する観点で日本語で300字程度にまとめてください。教師がぶっきらぼうに学生に説明するように。"
    ]


    tabs = mo.ui.tabs({
        "初学者": explain_data(prompt[0]+"\n"+toydata.DESCR),
        "中級者": explain_data(prompt[1]+"\n"+toydata.DESCR),
        "上級者": explain_data(prompt[2]+"\n"+toydata.DESCR),
    })
    tabs
    return


@app.cell
def _():
    LLMselect = mo.ui.dropdown(
        options=["dummy", "LMStudio", "OpenAI API"],
        value="dummy", # initial value
        label="使用するLLM")
    return (LLMselect,)


@app.cell
def _(LLMselect):
    LOCAL_MODEL = "llm-jp-3.1-1.8b-instruct4"
    OPENAI_MODEL = "gpt-5-mini"

    def explain_data(descr):
        if LLMselect.value == "dummy":
            if "iris" in descr:
                response = "アヤメのデータです。"
            elif "digits" in descr:
                response = "手書き数字のデータです。"
            elif "wine" in descr:
                response = "ワインの化学成分のデータです。"
            elif "breast cancer" in descr:
                response = "乳がんの診断データです。"
            else:
                response = "不明なデータセットです。"

        elif LLMselect.value == "LMStudio":
            import lmstudio as lms
            model = lms.llm(LOCAL_MODEL)
            response = model.respond(descr)

        elif LLMselect.value == "OpenAI API":
            from openai import OpenAI
            client = OpenAI()
            res = client.responses.create(
                model=OPENAI_MODEL,
                input=descr
            )
            response = res.output_text
        else:
            response = "不明なLLMが選択されました。"
        return response
    return (explain_data,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## 評価法の選択と学習
    - 機械学習の評価法は、分割学習法と交差確認法があります。
      - 分割学習法では、どのような割合でデータを学習用と評価用に分けるのかを考えます
      - 交差確認法では、データをいくつに分割して学習と評価を繰り返すのかを考えます
    - 学習には k-NN法を用います。
      - 識別したいデータに近い k 個のデータの多数決でクラスを決定します。k の値によって性能が変わります。
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### slider による値の設定
    - slider は、左端の値（最小値）、右端の値（最大値）、初期値、ステップ幅、左側に表示するラベルを指定して作成します。
    - 選んだ値は、UIコンポーネントインスタンスの value 属性で取得できます。
    """)
    return


@app.cell
def _():
    eval_ratio = mo.ui.slider(start=10, stop=90, value=30, step=10, label="評価用データの割合")
    eval_ratio
    return (eval_ratio,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    上で設定した割合で学習用と評価用にデータを分割したあと、これらの分布がどれだけ異なるかを、もっとも分散が大きい特徴のヒストグラムで確認します。
    """)
    return


@app.cell
def _(df, eval_ratio):
    train_df, test_df = train_test_split(df, test_size=eval_ratio.value/100)

    # もっとも分散の大きい特徴量を見つける
    numeric_df = df.select_dtypes(include="number")
    variances = numeric_df.var()
    feature_name = variances.idxmax()

    # 分布を比較
    def plot_hist(data, title):
        return (
            alt.Chart(data, title=title)
            .mark_bar(opacity=0.7)
            .encode(
                x=alt.X(f"{feature_name}:Q", bin=alt.Bin(maxbins=20)),
                y="count()",
            )
            .properties(width=300, height=200)
        )

    chart2 = alt.hconcat(
        plot_hist(train_df, "Train distribution"),
        plot_hist(test_df, "Test distribution")
    )

    chart2
    return


if __name__ == "__main__":
    app.run()
