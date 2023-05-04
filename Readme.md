# Pythonプロジェクトテンプレート

Projectで汎用的に活用可能なテンレートです。

# 前提ソフトウェア

以下のソフトウェアを使用しますので、事前にインストールしてください。

pyenv
poetry
python 3.10+ ※pyenvでインストールします
pre-commit


# How to use

envファイルをコピーして作成する。

```bash
cp .env.example .env
```

必要パッケージ等をインストールする。

```bash
make install
```

動作確認のために、main.pyを実行します。

```bash
make run_main
```
