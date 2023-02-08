# BeautyInlet2

## 用意すべきもの
### Pythonモジュール
* TensorFlow
* cv2
* PIL
* requests

### サーバー立ち上げ
1. `Server/`内のソースコードをGAS上に展開し，
2. GAS上でWebアプリのデプロイを行う．
3. WebアプリへのURLを`Environments/detectiondbservice_url.txt`(gitignoreされている)に書き込む．

### モデル用意
以下のような要件を満たすモデルを用意する．

* Shapeが`(classifier.consts.IMG_HEIGHT, classifier.consts.IMG_WIDTH, classifier.consts.IMG_CHANNELS)`である入力
* Shapeが`(3,)`である出力
* 入力のそれぞれの要素が$[0,1]$の範囲内にある
* 出力のArgmaxがそれぞれ`classifier.consts.UNCLEAR, classifier.consts.NOTSEEN, classifier.consts.SEEN`を表す．

モデルを`Models/`などに入れておく．