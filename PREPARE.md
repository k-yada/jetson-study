# 事前準備

## macOS で OpenMP を利用するための準備

  OpenMP は gcc で利用可能です。mac に Xcode をインストールすることで標準的に利用可能な gcc/g++ は clang のラッパーなので、本物の gcc をインストールする必要があります。

  1. 事前準備

    - Xcode のインストール

      Homebrew からパッケージをインストールするときに、コンパイラが必要になるので AppStore から Xcode をインストールしておきます。

      Xcode を起動すると、コマンドラインツールをインストールするかどうか聞かれますので、コマンドラインツールもインストールしておきます。

      複数のバージョンの Xcode をインストールしているときには、```xcode-select```で選択することができます。


      ```
      sudo xcode-select -s /Applications/Xcode.app
      ```

    - Homebrew のインストール

      https://brew.sh を参照して、インストールスクリプトを実行して Homebrew が利用できるようにしてください。

  1. gcc/g++ のインストール

    mac で利用可能な gcc/g++ は、Xcode でインストールされている clang のラッパーであり、OpenMP が使えません。OpenMP が使えるように本物の gcc/g++ をインストールします。

    ```
    brew update
    brew install gcc@9
    ln -s /usr/local/bin/gcc-9 /usr/local/bin/gcc
    ln -s /usr/local/bin/g++-9 /usr/local/bin/g++
    rehash
    ```

    ```
    % gcc --version
    gcc (Homebrew GCC 9.3.0) 9.3.0
    Copyright (C) 2019 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    ```
