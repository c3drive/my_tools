import marimo

__generated_with = "0.19.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import os
    import marimo as mo
    from dotenv import load_dotenv
    import anthropic

    # .envの読み込み確認
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if api_key:
        print("APIキーの読み込みに成功したぞ。準備万端だ。")
    else:
        print("APIキーが見当たらない。 .env ファイルを確認しろ。")
    return


if __name__ == "__main__":
    app.run()
