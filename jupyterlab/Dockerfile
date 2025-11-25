FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
	sudo \
	wget \
	vim \
	build-essential
WORKDIR /opt
RUN wget https://repo.continuum.io/archive/Anaconda3-2025.06-1-Linux-x86_64.sh && \
	sh /opt/Anaconda3-2025.06-1-Linux-x86_64.sh -b -p /opt/anaconda3 && \
	rm -f /opt/Anaconda3-2025.06-1-Linux-x86_64.sh
ENV PATH=/opt/anaconda3/bin:$PATH

# Pythonのpakage管理ツール
RUN pip install --upgrade 'pip<24.1'
RUN pip install boto3

# 構成図作画
RUN pip install diagrams
RUN apt install -y graphviz

# web上の色々な情報をAPIを使って簡単に取得するライブラリ
RUN pip install pandas_datareader
# さまざまなテクニカル指標を計算するためのPythonのライブラリ
# RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
# RUN wget https://sourceforge.net/projects/ta-lib/files/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz && \
#   tar -xvzf ta-lib-0.4.0-src.tar.gz && \
#   cd ta-lib/ && \
#   ./configure --prefix=/usr && \
#   make && \
#   make install
# RUN conda install conda-forge::ta-lib
# RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz

# ローソク足チャートを作成
RUN pip install mplfinance

WORKDIR /
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]