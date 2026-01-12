# my_anthropic
stdy https://anthropic.com/

# Using my dockerfile
1. 以下のコマンドを実行する
```
docker compose up --build
docker compose up
```
2. ブラウザからlocalhost:2718
この際、パスワード入力画面になるので実行画面のtokenを入力する

```
claude_learning_env  |         ➜  URL: http://0.0.0.0:2718?access_token=Oqnp8lF99Ehjm9ElDMN-9A
claude_learning_env  |         ➜  Network: http://172.19.0.2:2718?access_token=Oqnp8lF99Ehjm9ElDMN-9A
```

# .ipynb ファイルを marimo 形式（.py）に変換
```
# claude_learning_envはコンテナ名
docker exec -it claude_learning_env marimo convert ./anthropic/001_prompt_evals.ipynb -o ./anthropic/001_prompt_evals.py

```