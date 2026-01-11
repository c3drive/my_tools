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
docker run -it -p 8888:8888 --rm jupyter/datascience-notebook bash jupyter notebook
```
2. ブラウザからlocalhost:8888でアクセスする。