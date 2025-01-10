# 擬似の株価変動
![test](https://github.com/yuuya1086/mypkg/actions/workflows/test.yml/badge.svg)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

## 概要

これは、株価の変動を擬似的に体験することができるROS 2のパッケージです。

## ノード

10000円分の株を買ったときの株価が変動します。<br>

※値の増減はランダムなので、実際の株価の増減方法とは異なります。

※listener.pyはテスト用で残してあります。

## トピック

- トピック名：kabuka

- 2秒ごとに株価が送信されています。

## 実行方法

- 送信側
```bash
   $ ros2 run mypkg kabu
```

- 受信側：もう一つの端末で入力してください。
```bash
   $ ros2 topic echo /kabuka
```

## 実行例

```bash
   $ ros2 topic echo /kabuka
   data: 10000.05
   ---
   data: 10000.46
   ---
   data: 10000.51
   ---
   data: 10000.81
   ---
   data: 10000.02
   ---
   data: 9999.57
   ---
```

## 必要なソフトウェア

- Python
  - テスト済みバージョン：3.10<br>

- ROS 2 のバージョン： foxy

- Ubuntu のバージョン： 20.04
　
## ライセンス

- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布及び使用が許可されます。

- © 2024 Yuuya Tanaka

