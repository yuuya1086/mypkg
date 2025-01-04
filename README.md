# 擬似の株価変動
![test](https://github.com/yuuya1086/mypkg/actions/workflows/test.yml/badge.svg)

## ノード

これは、10000円分の株を買ったときの株価の変動を擬似的に体験することができるプログラムです。<br>

※値の増減はランダムなので、実際の株価の増減方法とは異なります。

## トピック

このプログラムでは、株価の値がやり取りされます。

## 実行方法

- 送信側
```bash
   $ ros2 run mypkg kabu
```

- 受信側
```bash
   $ ros2 topic echo /kabuka
```

## 実行例

## 必要なソフトウェア

- Python
  - テスト済みバージョン： 3.7~3.10<br>
　
　[テストで利用したコンテナ](https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2)

## ライセンス

- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布及び使用が許可されます。

- © 2024 Yuuya Tanaka

## テスト環境
- Ubuntu 22.04 LTS



　　　　　
　
　　　　
