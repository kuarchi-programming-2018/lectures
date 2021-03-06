* johoshori181019
    * # 今回の位置づけ
        * python`.py`ファイルの実行方法，jupyter notobookでの実行方法の復習
        * pythonの文法の復習
        * フィボナッチ数列を利用したpython文法の復習
        * 標準ライブラリ，外部ライブラリの使用
        * `math`や`numpy`を用いた数理的処理
    * # 今回まででできていること
        * プログラミング学習サイトPaizaを利用して**一通りの文法の学習**
            * まだ終わっていない人はこの文法の学習を一通りやりましょう。
                * 一通りやってわからない人は，以下のような勉強方法があります。
                    * 他のプログラミング学習サイトでの学習（Progateやドットインストールなど）
                    * 書籍を買ってやってみる。（『みんなのPython』や指定教科書など）
                    * 何かやりたいことを設定して本を買ってわからないことを調べながら進める。（『デザイン・コンピューティング入門』，『Rhino x Python コンピューテーショナル・デザイン』など。また，深層学習，機械学習，最適化，統計などのPython処理練習本があります。）
        * GitHubの使用
        * 自分のPCでのPython実行環境の構築
            * Anacondaインストール
            * jupyter notobook
            * spyder
        * まだできていない人はTAさんに質問してやってみよう。
    * # 前回の課題の復習
        * 拡張子，ファイル名のつけ方
            * pythonは`.py`，jupyter notebookは`ipynb`
            * 正しい拡張子を付けるとシンタックスハイライトもつく。
            * このハンドアウト後半に記してある「181019出席中の課題」のURLにアクセスして課題をやろう。
            * jupyter notebook でfibonacci_tutrialのファイルをやる。
            * 「fib-to-revise」フォルダの中のファイルを修正する。
            * fibonacci_ans.pyにいろいろなfibonacci数を算出するための関数を載せています。
    * # 今回学ぶこと
        * ## GitHubに慣れる必要がある理由
            * 新しい概念を理解するのは大変だが・・
            * 自分自身のプロジェクト管理 リビジョン
            * プログラミングの標準ツールなので，自学自習に必須。
            * 研究室やチームでの管理　秘伝のタレ化を防ぐ
            * 公開されているものを利用する　ゼロから書く（スクラッチという）より，できる限り利用できる資産を使うことが労力の節約になる。
            * それを公開すればまた世界への貢献になる。
            * ### なぜGitHubを使うのか，ということの建築設計における意味
                * [マリオ・カルポ: 『アルファベット そして アルゴリズム: 表記法による建築-- ルネサンスからデジタル革命へ』, 鹿島出版会, 2014](https://www.amazon.co.jp/%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A1%E3%83%99%E3%83%83%E3%83%88-%E3%81%9D%E3%81%97%E3%81%A6-%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0-%E8%A1%A8%E8%A8%98%E6%B3%95%E3%81%AB%E3%82%88%E3%82%8B%E5%BB%BA%E7%AF%89%E2%80%95%E2%80%95%E3%83%AB%E3%83%8D%E3%82%B5%E3%83%B3%E3%82%B9%E3%81%8B%E3%82%89%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E9%9D%A9%E5%91%BD%E3%81%B8-%E3%83%9E%E3%83%AA%E3%82%AA/dp/4306046117)
                * **digital turn** デジタルターン
                    * デジタルなものが「パラダイム・シフト」であるならば，どのようなパラダイムがシフトしているのか？
                    * 前機械時代 手仕事によるゆらぎ・可変性
                    * 印刷術 近代初期 同一コピーの需要 産業による規格化
                    * レオン・バティスタ・アルベルティによるデザインの発見。建物は建築家によるデザインのコピーである。デザインと作ることの分離。原作者としての建築家という現代的な定義が生まれた。
                    * 同一性に基づいた近代的な力はデジタルテクノロジーの興盛で終わる。
                    * 前機械時代における手仕事によるものにおける可変性との共通点
                * 藤村龍至　超線形設計プロセス論
                    * http://db.10plus1.jp/backnumber/article/articleid/782/
        * ## ライブラリimport
            * `import hoge`
            * `from hoge import fuga`
            * 標準ライブラリ https://docs.python.jp/3/library/
                * こういうライブラリは隅から隅まで覚える必要はないが，基礎的な例題をこなしたり，写経をしているうちにどのようなライブラリが用意されているのかわかってくる。つかうときはリファレンスをググりながらつかえばよい。
                    * random
                    * math
                    * turtle
                * 組み込み関数も同様（rangeとか）
            * 外部ライブラリ紹介
                * インストールが必要 anacondaならば主要なものはすでに用意されている。
                    * numpy http://www.numpy.org/
                    * scipy https://www.scipy.org/
                    * matplotlib https://matplotlib.org/
                    * networkx https://networkx.github.io/documentation/stable/tutorial.html
                * もしインストールする必要あれば，そのライブラリの指示に従う。`pip install hogehoge`が多い
            * デザインコンピューティング入門のpython入門をやる
                * 181025までの課題に『デザインコンピューティング入門』の2章のpdfが入っています。(課題のところに書いてあるURLに行こう)
                * デザインコンピューティング入門のリポジトリをやってみよう。
                * https://github.com/o-kei/design-computing-aij
                * ch2_1に入っているファイルを実行してみよう。
                * 例えばplotrose_1.pyとか実行してみよう。
                * ライブラリを使った基礎的な説明も簡潔に書いてある
    * # 課題
        * ## 181019出席中の課題
            * 提出方法
                * https://classroom.github.com/a/ib32KfnR
                * 上記URLにアクセスし，「kuarchi-programming-2018/181019attendance-自分のアカウント」というリポジトリを自動作成する。
                * そのリポジトリをクローンして課題を行い，コミット・プッシュを行って提出。
                * 提出できたか確認するためには，「kuarchi-programming-2018/181019attendance-自分のアカウント」のリポジトリをブラウザ上で見てできているか確認する。フォークなどして「自分のアカウント/181019attendance-自分のアカウント」や「自分のアカウント/181019attendance」を変更しているとこちらでは確認できません。（初回授業と変わっています。シンプルにしました。フォークとプルリクエストを送っていません。）
            * やること
                * jupyter notebook でfibonacci_tutrialのファイルをやる。
                * 「fib-to-revise」フォルダの中のファイルを修正する。
        * ## 181025までの課題
            * https://classroom.github.com/a/lT6Ne2XC
            * (プリントに記載間違えたのでこちらを参照)
            * 『デザインコンピューティング入門』の2章を一通り実行して復習する。
                * `rose.py``plotrose_1.py`などのプログラムがあるが，その中の変数を変更して，自分のオリジナルの画像を作る。
                * それらのスクリプトを`recursion-practice`フォルダに入れる。
                * わからないのは飛ばす。
                * 意欲的な人はぜひ購入して他の章をやると面白いです。
        * ### 過去の課題（出席課題・翌週までの課題）をやってない人はやっておきましょう。
            * とくにPaiza はやりましょう。