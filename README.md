# 擬似の株価変動
![test](https://github.com/yuuya1086/mypkg/actions/workflows/test.yml/badge.svg)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)


## ノード

これは、10000円分の株を買ったときの株価の変動を擬似的に体験することができるプログラムです。<br>

※値の増減はランダムなので、実際の株価の増減方法とは異なります。

※listener.pyはテスト用で残してあります。

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

![スクリーンショット 2025-01-04 235214](https://github.com/user-attachments/assets/ce0dd84d-e58d-48bf-9fdd-8d3e7f96802a)

## 必要なソフトウェア

- Python
  - テスト済みバージョン： 3.7~3.10<br>
　
[テストで利用したコンテナ](https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2)

## ライセンス

- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布及び使用が許可されます。

- © 2024 Yuuya Tanaka

## テスト環境
- Ubuntu 22.04 LTS



　　　　　
　
　　　　
