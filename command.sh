
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ~/Miniconda3-latest-Linux-x86_64.sh
conda create -n "test" python=3.11
conda activate test
pip install "modin[dask]" dask-cuda
pip install cudf-cu12 --extra-index-url=https://pypi.nvidia.com
pip install pandas, pyspark, polars,dask
curl -L -o 100million_steam_reviews.zip\
  https://www.kaggle.com/api/v1/datasets/download/kieranpoc/steam-reviews
curl -L -o 6million_steam_revies.zip\
  https://www.kaggle.com/api/v1/datasets/download/andrewmvd/steam-reviews
apt install openjdk-11-jre-headless
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64