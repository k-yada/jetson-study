# PythonからCUDAを実行する

## PyCuda とは

  CUDAのPythonバインディング。Pythonのプログラムの中にCUDAプログラムを記述することができ、実行時にコンパイルが行われる。面倒な Makefile などは不要。

## pycuda のインストール

    ```text
    $ pip3 install --user -U pycuda
    ```

  ```-U``` は、既にインストールされていて新しいバージョンが存在すればアップグレードされるオプション。

