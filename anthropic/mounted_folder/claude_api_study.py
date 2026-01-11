import marimo

__generated_with = "0.19.2"
app = marimo.App(width="medium")


@app.cell
def _():
    # md用
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # 環境変数を読み込み
    """)
    return


@app.cell
def _():
    # read envs
    from dotenv import load_dotenv
    load_dotenv()

    from anthropic import Anthropic

    client = Anthropic()
    model = "claude-sonnet-4-0"
    return client, model


@app.cell
def _():
    # claudeは解答を暗記しないため暗記する仕組み
    messages = []
    def add_user_message(messages, text):
        user_message = {"role": "user", "content": text}
        messages.append(user_message)

    def add_assistant_message(messages, text):
        assistant_message = {"role": "assistant", "content": text}
        messages.append(assistant_message)

    # def chat(messages):
    #     message = client.messages.create(
    #         model=model,
    #         max_tokens=1000,
    #         messages=messages,
    #     )
    #     return message.content[0].text
    return (messages,)


@app.cell
def _(client, model):
    # システムプロンプトを設定
    def chat(messages, system=None, temperature=1.0):
        params = {
            "model": model,
            "max_tokens": 1000,
            "messages": messages,
            "temperature": temperature
        }

        if system:
            params["system"] = system

        message = client.messages.create(**params)
        return message.content[0].text
    return (chat,)


@app.cell
def _(chat, messages):
    # Without system prompt
    answer = chat(messages)

    # With system prompt
    system = """
    You are a patient math tutor.
    Do not directly answer a student's questions.
    Guide them to a solution step by step.
    """
    answer = chat(messages, system=system)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # temperature
    **低温（0.0～0.3）**
    - 事実に基づく回答
    - コーディング支援
    - データ抽出
    - コンテンツのモデレーション

    **中温（0.4～0.7）**
    - 要約
    - 教育コンテンツ
    - 問題解決
    - 制約のある創作

    **高温（0.8～1.0）**
    - ブレインストーミング
    - 創作文
    - マーケティングコンテンツ
    - ジョーク世代
    """)
    return


@app.cell
def _(chat, messages):
    # Low temperature - more predictable
    answer = chat(messages, temperature=0.0)

    # High temperature - more creative  
    answer = chat(messages, temperature=1.0)
    return


if __name__ == "__main__":
    app.run()
