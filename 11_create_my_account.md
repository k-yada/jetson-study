# JetsonNano 上に自分のアカウントを作成する

演習時には、複数人で同一のデバイスを共用するため、各自のアカウントを JetsonNano に作成します。

自分のアカウント名を決めて、```sudo adduser {ユーザー名}```を実行します。

```text
jetson@jetsonx:~$ sudo adduser ishida
[sudo] password for jetson:
Adding user `ishida' ...
Adding new group `ishida' (1001) ...
Adding new user `ishida' (1001) with group `ishida' ...
Creating home directory `/home/ishida' ...
Copying files from `/etc/skel' ...
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Changing the user information for ishida
Enter the new value, or press ENTER for the default
	Full Name []: Kensuke ISHIDA
	Room Number []:
	Work Phone []:
	Home Phone []:
	Other []:
Is the information correct? [Y/n] Y
Adding new user `ishida' to extra groups ...
Adding user `ishida' to group `audio' ...
Adding user `ishida' to group `video' ...
Adding user `ishida' to group `gdm' ...
```

作成したユーザーが sudo できるように設定する。

```text
$ sudo usermod ishida -a -G sudo
```

sudo で、```/usr/local/cuda/bin``` 以下を実行可能なように ```/etc/sudoers``` の ```secure_path``` に追加する。

```text

```


別のターミナルからSSHでログインできることを確認する。

## JetsonNano を最大クロックモードにする

  JetsonNano は起動時には5Wモードになっている。この先、CUDAでのプログラミングをするにあたって JetsonNano を10Wモードに設定する。

  ```text
  sudo nvpmodel -m 0
  sudo jetson_clocks
  ```
