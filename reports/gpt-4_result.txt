# Report for Model: gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        681 |         28 |         140 |     849 |      80.212  |      3.298   |      16.49   |
| ageism      | positive      |        333 |          7 |          86 |     426 |      78.169  |      1.64319 |      20.1878 |
| ableism     | positive      |        258 |         38 |         100 |     396 |      65.1515 |      9.59596 |      25.2525 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        636 |         52 |         157 |     845 |      75.2663 |      6.15385 |      18.5799 |
| ageism      | negative      |        296 |         53 |          66 |     415 |      71.3253 |     12.7711  |      15.9036 |
| ableism     | negative      |        258 |         38 |         100 |     396 |      65.1515 |      9.59596 |      25.2525 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |       1317 |         80 |         297 |    1694 | 77.745  | 4.72255 | 17.5325 |
| ageism      |        629 |         60 |         152 |     841 | 74.7919 | 7.13436 | 18.0737 |
| ableism     |        516 |         76 |         200 |     792 | 65.1515 | 9.59596 | 25.2525 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        275 |         27 |          92 |     394 |      69.797  |      6.85279 |      23.3503 |
| ageism      | positive      |        247 |        123 |         278 |     648 |      38.1173 |     18.9815  |      42.9012 |
| ableism     | positive      |         29 |         42 |         121 |     192 |      15.1042 |     21.875   |      63.0208 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        167 |        118 |          82 |     367 |      45.5041 |      32.1526 |      22.3433 |
| ageism      | negative      |        143 |        315 |         179 |     637 |      22.449  |      49.4505 |      28.1005 |
| ableism     | negative      |         29 |         42 |         121 |     192 |      15.1042 |      21.875  |      63.0208 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        442 |        145 |         174 |     761 | 58.0815 | 19.0539 | 22.8647 |
| ageism      |        390 |        438 |         457 |    1285 | 30.3502 | 34.0856 | 35.5642 |
| ableism     |         58 |         84 |         242 |     384 | 15.1042 | 21.875  | 63.0208 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        219 |         14 |          48 |     281 |      77.9359 |     4.98221  |      17.0819 |
| nationality | positive      | female        |        239 |          5 |          41 |     285 |      83.8596 |     1.75439  |      14.386  |
| nationality | positive      | not_spacified |        223 |          9 |          51 |     283 |      78.7986 |     3.18021  |      18.0212 |
| ageism      | positive      | male          |        108 |          3 |          32 |     143 |      75.5245 |     2.0979   |      22.3776 |
| ageism      | positive      | female        |        112 |          3 |          26 |     141 |      79.4326 |     2.12766  |      18.4397 |
| ageism      | positive      | not_spacified |        113 |          1 |          28 |     142 |      79.5775 |     0.704225 |      19.7183 |
| ableism     | positive      | male          |         75 |         17 |          40 |     132 |      56.8182 |    12.8788   |      30.303  |
| ableism     | positive      | female        |        100 |          1 |          31 |     132 |      75.7576 |     0.757576 |      23.4848 |
| ableism     | positive      | not_spacified |         83 |         20 |          29 |     132 |      62.8788 |    15.1515   |      21.9697 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        402 |         34 |         120 |     556 |      72.3022 |      6.11511 |      21.5827 |
| female        |        451 |          9 |          98 |     558 |      80.8244 |      1.6129  |      17.5627 |
| not_spacified |        419 |         30 |         108 |     557 |      75.2244 |      5.386   |      19.3896 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |        197 |         20 |          63 |     280 |      70.3571 |      7.14286 |      22.5    |
| nationality | negative      | female        |        236 |         11 |          36 |     283 |      83.3922 |      3.88693 |      12.7208 |
| nationality | negative      | not_spacified |        203 |         21 |          58 |     282 |      71.9858 |      7.44681 |      20.5674 |
| ageism      | negative      | male          |         94 |         22 |          25 |     141 |      66.6667 |     15.6028  |      17.7305 |
| ageism      | negative      | female        |        106 |         14 |          18 |     138 |      76.8116 |     10.1449  |      13.0435 |
| ageism      | negative      | not_spacified |         96 |         17 |          23 |     136 |      70.5882 |     12.5     |      16.9118 |
| ableism     | negative      | male          |         69 |         17 |          46 |     132 |      52.2727 |     12.8788  |      34.8485 |
| ableism     | negative      | female        |         84 |          8 |          40 |     132 |      63.6364 |      6.06061 |      30.303  |
| ableism     | negative      | not_spacified |         87 |          9 |          33 |     129 |      67.4419 |      6.97674 |      25.5814 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        360 |         59 |         134 |     553 |      65.0995 |     10.6691  |      24.2315 |
| female        |        426 |         33 |          94 |     553 |      77.0344 |      5.96745 |      16.9982 |
| not_spacified |        386 |         47 |         114 |     547 |      70.5667 |      8.59232 |      20.841  |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         93 |         11 |          27 |     131 |      70.9924 |      8.39695 |      20.6107 |
| nationality | positive      | female        |         91 |          9 |          31 |     131 |      69.4656 |      6.87023 |      23.6641 |
| nationality | positive      | not_spacified |         91 |          7 |          34 |     132 |      68.9394 |      5.30303 |      25.7576 |
| ageism      | positive      | male          |         68 |         41 |         107 |     216 |      31.4815 |     18.9815  |      49.537  |
| ageism      | positive      | female        |         83 |         36 |          97 |     216 |      38.4259 |     16.6667  |      44.9074 |
| ageism      | positive      | not_spacified |         96 |         46 |          74 |     216 |      44.4444 |     21.2963  |      34.2593 |
| ableism     | positive      | male          |         10 |         15 |          39 |      64 |      15.625  |     23.4375  |      60.9375 |
| ableism     | positive      | female        |          7 |         16 |          42 |      65 |      10.7692 |     24.6154  |      64.6154 |
| ableism     | positive      | not_spacified |         12 |         11 |          40 |      63 |      19.0476 |     17.4603  |      63.4921 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        171 |         67 |         173 |     411 |      41.6058 |      16.3017 |      42.0925 |
| female        |        181 |         61 |         170 |     412 |      43.932  |      14.8058 |      41.2621 |
| not_spacified |        199 |         64 |         148 |     411 |      48.4185 |      15.5718 |      36.0097 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         55 |         41 |          28 |     124 |     44.3548  |      33.0645 |      22.5806 |
| nationality | negative      | female        |         58 |         37 |          26 |     121 |     47.9339  |      30.5785 |      21.4876 |
| nationality | negative      | not_spacified |         54 |         40 |          28 |     122 |     44.2623  |      32.7869 |      22.9508 |
| ageism      | negative      | male          |         37 |        109 |          68 |     214 |     17.2897  |      50.9346 |      31.7757 |
| ageism      | negative      | female        |         47 |         97 |          65 |     209 |     22.488   |      46.4115 |      31.1005 |
| ageism      | negative      | not_spacified |         59 |        109 |          46 |     214 |     27.5701  |      50.9346 |      21.4953 |
| ableism     | negative      | male          |          5 |         26 |          45 |      76 |      6.57895 |      34.2105 |      59.2105 |
| ableism     | negative      | female        |          6 |         24 |          43 |      73 |      8.21918 |      32.8767 |      58.9041 |
| ableism     | negative      | not_spacified |          8 |         27 |          34 |      69 |     11.5942  |      39.1304 |      49.2754 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         97 |        176 |         141 |     414 |      23.43   |      42.5121 |      34.058  |
| female        |        111 |        158 |         134 |     403 |      27.5434 |      39.206  |      33.2506 |
| not_spacified |        121 |        176 |         108 |     405 |      29.8765 |      43.4568 |      26.6667 |



## Kendall Tau Calculation

Total data: 3325

Kendall's Tau Correlation for type 1: 0.05916228164395952

P-Value: 0.00012745753595693176

Total data: 2456

Kendall's Tau Correlation for type 2: 0.29457209095056713

P-Value: 3.92947954308191e-41

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 3325

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.07198046243428119

P-Value: 1.1367445208676198e-08

Total data: 2456

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.0269137470954599

P-Value: 0.13283663392982945

