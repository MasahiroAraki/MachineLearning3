# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.17.0",
#     "matplotlib==3.10.7",
#     "numpy==2.3.5",
#     "pandas==2.3.3",
#     "pyzmq",
#     "scikit-learn==1.7.2",
#     "seaborn==0.13.2",
# ]
# ///

import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium", layout_file="layouts/chap02.grid.json")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    return


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.metrics import confusion_matrix, classification_report
    from sklearn.pipeline import make_pipeline
    return (
        KNeighborsClassifier,
        StandardScaler,
        classification_report,
        confusion_matrix,
        cross_val_score,
        load_iris,
        make_pipeline,
        np,
        pd,
        plt,
        sns,
        train_test_split,
    )


@app.cell
def _(np, pd, sns):
    np.set_printoptions(precision=3, suppress=True)
    pd.set_option('display.precision', 3)
    sns.set_theme()
    return


@app.cell
def _(load_iris):
    iris = load_iris(as_frame=True)
    X = iris.data
    y = iris.target
    return X, iris, y


@app.cell
def _(iris):
    print(iris.DESCR)
    return


@app.cell
def _(mo):
    # クイズの挿入
    options = ["2", "3", "4"]
    radio1 = mo.ui.radio(options=options)
    radio2 = mo.ui.radio(options=options)
    mo.md(f"""
    iris データのクラス数は？ {radio1}

    iris データの特徴の次元数は？ {radio2}
    """)
    return radio1, radio2


@app.cell
def _(answer):
    print(answer)
    return


@app.cell
def _(radio1, radio2):
    # クイズの正解（本当はもっと下の見えにくいところに配置）
    answer = "good" if radio1.value == "3" and radio2.value == "4" else "bad"
    return (answer,)


@app.cell
def _(X, iris, y):
    print(f"Shape of the dataset: {X.shape}")
    print(f"Feature names: {iris.feature_names}")
    print(f"Shape of the target: {y.shape}")
    print(f"Target class names: {iris.target_names}")
    return


@app.cell
def _(sns):
    df = sns.load_dataset('iris')
    df
    return (df,)


@app.cell
def _(df, mo):
    mo.ui.dataframe(df)
    return


@app.cell
def _(df, mo):
    mo.ui.data_explorer(df)
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df, plt, sns):
    markers = ['o', '^', 's']
    sns.pairplot(df, hue='species', markers=markers)
    plt.show()
    return


@app.cell
def _(StandardScaler, X, np):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print('mean:', np.mean(X_scaled, axis=0))
    print('std :', np.std(X_scaled, axis=0))
    return (X_scaled,)


@app.cell
def _(X_scaled, train_test_split, y):
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.33, random_state=7)
    return X_test, X_train, y_test, y_train


@app.cell
def _(KNeighborsClassifier, X_test, X_train, y_test, y_train):
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = sum(y_pred == y_test) / len(y_test)
    print(f'Accuracy: {acc:0.2f}')
    return clf, y_pred


@app.cell
def _(X_scaled, clf, cross_val_score, y):
    scores = cross_val_score(clf, X_scaled, y, cv=10)
    print(f'Accuracy: {scores.mean():0.2f} (+/- {scores.std()*2:0.2f})')
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(start=2, stop=10, label="Select CV folds", value=5)
    slider
    return (slider,)


@app.cell
def _(
    KNeighborsClassifier,
    StandardScaler,
    X,
    X_test,
    X_train,
    cross_val_score,
    make_pipeline,
    slider,
    y,
    y_test,
    y_train,
):
    pipe = make_pipeline(StandardScaler(), KNeighborsClassifier())

    # 分割学習法の場合
    score_div = pipe.fit(X_train, y_train).score(X_test, y_test)
    print(f'Split Accuracy: {score_div:0.2f}')

    # 交差確認法の場合
    score_cross = cross_val_score(pipe, X, y, cv=slider.value)
    print(f'Cross-val Accuracy: {score_cross.mean():0.2f} (+/- {score_cross.std()*2:0.2f})')
    return (pipe,)


@app.cell
def _(X_test, classification_report, pipe, y_test):
    y_pred2 = pipe.predict(X_test)
    print(classification_report(y_test, y_pred2))
    return


@app.cell
def _(confusion_matrix, plt, sns, y_pred, y_test):
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, cmap='Blues')
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.show()
    return


if __name__ == "__main__":
    app.run()
