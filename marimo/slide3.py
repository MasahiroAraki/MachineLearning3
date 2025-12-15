import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", layout_file="layouts/slide3.slides.json")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # <span style="color: blue;">marimo ノートブックで機械学習 (3)</span>

    <img src="https://raw.githubusercontent.com/MasahiroAraki/MachineLearning3/refs/heads/main/images/PCA.svg" width="600" />
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
      -  [marimo ノートブックで機械学習 (3)](https://note.com/mas_araki/n/n5917741fd6a9)
    - 【注意】 marimo を用いたコードは、荒木雅弘 : 『Pythonではじめる機械学習』（森北出版, 2025）には含まれておりません。本ドキュメントは、同書の補足資料です。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <span style="color: blue;">内容</span>
    - ページ下部のリンク先のノートブックでは、2章「機械学習の基本的な手順」をベースに、評価法の選択・学習の内容を用いて、marimo の特徴を説明
    - 本スライドでは、上記内容を marimo の機能ごとに並べ替えて紹介
      - 基本的な UI 部品
      - DataFrame の扱い
      - データの可視化

    [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_NxypaRkCLTPYbCWmb4zyEJ)
    """)
    return


@app.cell(hide_code=True)
def _(load_breast_cancer, load_digits, load_iris, load_wine, mo):
    dropdown_doc1 = mo.md(f'## <span style="color: blue;">基本的な UI 部品</span>')
    dropdown_doc2 = mo.md(f'### <span style="color: blue;">dropdown メニュー</span>')
    dropdown_doc3 = mo.md("""- dropdown メニューは、マウスによってメニューを下方向に開き、そのうちのひとつを選択するもの
      - options : 選択肢をリストまたは辞書で定義
      - value : 初期値
      - label : メニューの左に表示する文字列
    - 以下の例は scikit-learn の toydata set のうち、4つの識別用データセットから1つを選択するもの""")
    dropdown_doc4 = mo.md("""    ```python
        dropdown_dict = mo.ui.dropdown(
            options={"iris": load_iris, "digits": load_digits, "wine": load_wine, "breast_cancer": load_breast_cancer},
            value="iris",
            label="Choose dataset",
        )
        ```""")
    dropdown_dict = mo.ui.dropdown(
        options={
            "iris": load_iris,
            "digits": load_digits,
            "wine": load_wine,
            "breast_cancer": load_breast_cancer,
        },
        value="iris",  # initial value
        label="Choose dataset",
    )
    return (
        dropdown_dict,
        dropdown_doc1,
        dropdown_doc2,
        dropdown_doc3,
        dropdown_doc4,
    )


@app.cell(hide_code=True)
def _(
    dropdown_dict,
    dropdown_doc1,
    dropdown_doc2,
    dropdown_doc3,
    dropdown_doc4,
    mo,
):
    mo.md(rf"""
    {dropdown_doc1}
    {dropdown_doc2}
    {dropdown_doc3}
    {dropdown_doc4}

    {dropdown_dict}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    LLMselect = mo.ui.dropdown(
        options=["dummy", "LMStudio", "OpenAI API"],
        value="dummy", # initial value
        label="使用するLLM")
    return (LLMselect,)


@app.cell(hide_code=True)
def _(LLMselect, mo, toydata):
    tab_doc1 = mo.md(f'### <span style="color: blue;">tab を用いた表示の切り替え</span>')
    tab_doc2 = mo.md("""- tab は、ユーザーの選択によって表示内容を切り替えるもの
      - 引数は辞書形式で、キーがタブのラベル、値が各タブで表示する内容になる
    - 以下の例は、レベルが異なるユーザに向けてデータの説明を LLM で生成するもの
      - 使用する LLM を dropdown メニューで選択（LMStudio, OpenAI API を使う場合は、それぞれ設定が必要）
      - タブで初学者・中級者・上級者を切り替えると、それぞれの対象に向けた説明が出力される
    """)
    tab_doc3 = mo.md("""    ```python
        prompt = [
          "以下の内容を日本語で100字程度にまとめてください。やさしいお姉さんが...",
          "以下の内容を日本語で200字程度にまとめてください。男子大学生が...",
          "以下の内容を、専門用語を交えながら、機械学習を実行する観点で..."
        ]
        tabs = mo.ui.tabs({
          "初学者": explain_data(prompt[0]+"\\n"+toydata.DESCR),
          "中級者": explain_data(prompt[1]+"\\n"+toydata.DESCR),
          "上級者": explain_data(prompt[2]+"\\n"+toydata.DESCR)
        })
        ```""")

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

    return tab_doc1, tab_doc2, tab_doc3, tabs


@app.cell(hide_code=True)
def _(mo, tab_doc1, tab_doc2, tab_doc3):
    mo.md(rf"""
    {tab_doc1}
    {tab_doc2}

    {tab_doc3}
    """)
    return


@app.cell(hide_code=True)
def _(LLMselect, mo, tabs):
    mo.md(rf"""
    ### <span style="color: blue;">tab を用いた表示の切り替えの動作例</span>

    {LLMselect}

    {tabs}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ### <span style="color: blue;">slider による値の設定</span>
    - slider は、マウスでツマミ（ハンドル）を動かして、数値の範囲（最小値〜最大値）を設定するもの
      - start : 左端の値（最小値）
      - stop : 右端の値（最大値）
      - value : 初期値
      - step : ステップ幅
      - label : slider の左に表示する文字列

    ```python
    eval_ratio = mo.ui.slider(start=10, stop=90, value=30, step=10, label="評価用データの割合")
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    slider_doc1=mo.md(f"""
    ### <span style="color: blue;">slider による値の設定の動作例</span>
    """)
    return (slider_doc1,)


@app.cell(hide_code=True)
def _(mo):
    eval_ratio = mo.ui.slider(start=10, stop=90, value=30, step=10, label="評価用データの割合")
    return (eval_ratio,)


@app.cell(hide_code=True)
def _(alt, df, eval_ratio, mo, train_test_split):
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

    chart2 = mo.ui.altair_chart(alt.hconcat(
        plot_hist(train_df, "Train distribution"),
        plot_hist(test_df, "Test distribution")
    ))
    return (chart2,)


@app.cell(hide_code=True)
def _(chart2, eval_ratio, mo, slider_doc1):
    mo.md(rf"""
    {slider_doc1}

    {eval_ratio}

    {chart2}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ### <span style="color: blue;">DataFrame の扱い</span>
    - pandas や polars の DataFrame を marimo で出力すると、いくつかの特別な操作が可能になる
      - 例： 列ごとの並べ替えやフィルタリング

    ```python
    toydata = dropdown_dict.value()

    df = pd.DataFrame(
        data=toydata.data,
        columns=toydata.feature_names
    )
    df["target"] = toydata.target
    df
    ```
    """)
    return


@app.cell(hide_code=True)
def _(dropdown_dict, pd):
    toydata = dropdown_dict.value()

    df = pd.DataFrame(
        data=toydata.data,
        columns=toydata.feature_names
    )
    df["target"] = toydata.target
    df
    return df, toydata


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### <span style="color: blue;">データの可視化</span>

    - データ可視化ライブラリ Altair や、Plotly を用いたインタラクティブなグラフ表示が行える
    - 以下の例は、上記 dropdown メニューで選択した高次元のデータを PCA（本文11.2節で説明）で2次元に削減して散布図を描画
      - マウスオーバーで、各点の値が表示される
      - mo.ui.altair_chart() で作成したコンポーネントは、value 属性で選択範囲の DataFrame が取得できる

    ```python
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
    ```
    """)
    return


@app.cell(hide_code=True)
def _(PCA, alt, mo, pd, toydata):
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


@app.cell(hide_code=True)
def _(chart, mo):
    mo.vstack([chart, mo.ui.table(chart.value)])
    return


@app.cell
def _():
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
    return (
        PCA,
        alt,
        load_breast_cancer,
        load_digits,
        load_iris,
        load_wine,
        mo,
        pd,
        train_test_split,
    )


if __name__ == "__main__":
    app.run()
