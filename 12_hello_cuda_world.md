# はじめての CUDA プログラミング

## CUDA プログラミングの準備

Jetson Nano では、OSイメージに CUDA がインストール済みなので、パスを通すだけで利用可能です。

```~/.bashrc``` に、以下の設定を追加します。

```text
export PATH=$PATH:/usr/local/cuda/bin:/usr/sbin
export LD_LIBRARY_PATH=/usr/local/cuda/lib
```

```~/.bashrc``` の編集を読み込み、CUDAのコンパイラ(nvcc)が利用可能であることを確認します。

```text
ishida@jetson:~$ source ~/.bashrc
ishida@jetson:~$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2018 NVIDIA Corporation
Built on Sun_Sep_30_21:09:22_CDT_2018
Cuda compilation tools, release 10.0, V10.0.166
```

## GPU で行列の加算を実行する

<https://github.com/nebosuke/hello_cuda_world>
