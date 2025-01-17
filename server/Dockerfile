# ベースイメージ
FROM python:3.10.11-slim

# 作業ディレクトリを作成
WORKDIR /server

# 必要なファイルをコピー
COPY requirements.txt .
COPY app /server/app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-dev \
    pkg-config \
    bluez \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# 依存パッケージをインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# アプリケーションを起動
CMD ["python", "app/main.py"]