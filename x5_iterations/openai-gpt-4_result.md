# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        690 |         10 |         151 |     851 |      81.0811 |      1.17509 |      17.7438 |
| ageism      | positive      |        343 |         17 |          67 |     427 |      80.3279 |      3.98126 |      15.6909 |
| ableism     | positive      |        293 |         15 |          88 |     396 |      73.9899 |      3.78788 |      22.2222 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        618 |         65 |         169 |     852 |      72.5352 |      7.62911 |      19.8357 |
| ageism      | negative      |        263 |         77 |          71 |     411 |      63.9903 |     18.7348  |      17.2749 |
| ableism     | negative      |        249 |         38 |         106 |     393 |      63.3588 |      9.66921 |      26.972  |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |       1308 |         75 |         320 |    1703 | 76.8056 |  4.40399 | 18.7904 |
| ageism      |        606 |         94 |         138 |     838 | 72.315  | 11.2172  | 16.4678 |
| ableism     |        542 |         53 |         194 |     789 | 68.6946 |  6.71736 | 24.5881 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        300 |         24 |          68 |     392 |      76.5306 |      6.12245 |      17.3469 |
| ageism      | positive      |        322 |        109 |         215 |     646 |      49.8452 |     16.8731  |      33.2817 |
| ableism     | positive      |         23 |         50 |         125 |     198 |      11.6162 |     25.2525  |      63.1313 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        209 |         90 |          68 |     367 |      56.9482 |      24.5232 |      18.5286 |
| ageism      | negative      |        224 |        257 |         164 |     645 |      34.7287 |      39.845  |      25.4264 |
| ableism     | negative      |         26 |        105 |          96 |     227 |      11.4537 |      46.2555 |      42.2907 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        509 |        114 |         136 |     759 | 67.0619 | 15.0198 | 17.9183 |
| ageism      |        546 |        366 |         379 |    1291 | 42.2928 | 28.3501 | 29.3571 |
| ableism     |         49 |        155 |         221 |     425 | 11.5294 | 36.4706 | 52      |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        227 |          3 |          52 |     282 |      80.4965 |      1.06383 |      18.4397 |
| nationality | positive      | female        |        231 |          4 |          49 |     284 |      81.338  |      1.40845 |      17.2535 |
| nationality | positive      | not_spacified |        232 |          3 |          50 |     285 |      81.4035 |      1.05263 |      17.5439 |
| ageism      | positive      | male          |        115 |          4 |          24 |     143 |      80.4196 |      2.7972  |      16.7832 |
| ageism      | positive      | female        |        116 |          4 |          23 |     143 |      81.1189 |      2.7972  |      16.0839 |
| ageism      | positive      | not_spacified |        112 |          9 |          20 |     141 |      79.4326 |      6.38298 |      14.1844 |
| ableism     | positive      | male          |         92 |          5 |          35 |     132 |      69.697  |      3.78788 |      26.5152 |
| ableism     | positive      | female        |        107 |          2 |          23 |     132 |      81.0606 |      1.51515 |      17.4242 |
| ableism     | positive      | not_spacified |         94 |          8 |          30 |     132 |      71.2121 |      6.06061 |      22.7273 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        434 |         12 |         111 |     557 |      77.9174 |      2.1544  |      19.9282 |
| female        |        454 |         10 |          95 |     559 |      81.2165 |      1.78891 |      16.9946 |
| not_spacified |        438 |         20 |         100 |     558 |      78.4946 |      3.58423 |      17.9211 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |        205 |         21 |          57 |     283 |      72.4382 |      7.42049 |      20.1413 |
| nationality | negative      | female        |        212 |         17 |          55 |     284 |      74.6479 |      5.98592 |      19.3662 |
| nationality | negative      | not_spacified |        201 |         27 |          57 |     285 |      70.5263 |      9.47368 |      20      |
| ageism      | negative      | male          |         85 |         28 |          25 |     138 |      61.5942 |     20.2899  |      18.1159 |
| ageism      | negative      | female        |         91 |         23 |          23 |     137 |      66.4234 |     16.7883  |      16.7883 |
| ageism      | negative      | not_spacified |         87 |         26 |          23 |     136 |      63.9706 |     19.1176  |      16.9118 |
| ableism     | negative      | male          |         74 |         15 |          42 |     131 |      56.4885 |     11.4504  |      32.0611 |
| ableism     | negative      | female        |         90 |         12 |          30 |     132 |      68.1818 |      9.09091 |      22.7273 |
| ableism     | negative      | not_spacified |         85 |         11 |          34 |     130 |      65.3846 |      8.46154 |      26.1538 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        364 |         64 |         124 |     552 |      65.942  |     11.5942  |      22.4638 |
| female        |        393 |         52 |         108 |     553 |      71.0669 |      9.40325 |      19.5298 |
| not_spacified |        373 |         64 |         114 |     551 |      67.6951 |     11.6152  |      20.6897 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        100 |         11 |          21 |     132 |     75.7576  |      8.33333 |      15.9091 |
| nationality | positive      | female        |        105 |          5 |          22 |     132 |     79.5455  |      3.78788 |      16.6667 |
| nationality | positive      | not_spacified |         95 |          8 |          25 |     128 |     74.2188  |      6.25    |      19.5312 |
| ageism      | positive      | male          |         87 |         45 |          84 |     216 |     40.2778  |     20.8333  |      38.8889 |
| ageism      | positive      | female        |        117 |         28 |          69 |     214 |     54.6729  |     13.0841  |      32.243  |
| ageism      | positive      | not_spacified |        118 |         36 |          62 |     216 |     54.6296  |     16.6667  |      28.7037 |
| ableism     | positive      | male          |          8 |         15 |          43 |      66 |     12.1212  |     22.7273  |      65.1515 |
| ableism     | positive      | female        |          5 |         19 |          42 |      66 |      7.57576 |     28.7879  |      63.6364 |
| ableism     | positive      | not_spacified |         10 |         16 |          40 |      66 |     15.1515  |     24.2424  |      60.6061 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        195 |         71 |         148 |     414 |      47.1014 |      17.1498 |      35.7488 |
| female        |        227 |         52 |         133 |     412 |      55.0971 |      12.6214 |      32.2816 |
| not_spacified |        223 |         60 |         127 |     410 |      54.3902 |      14.6341 |      30.9756 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         74 |         30 |          20 |     124 |     59.6774  |      24.1935 |      16.129  |
| nationality | negative      | female        |         73 |         21 |          29 |     123 |     59.3496  |      17.0732 |      23.5772 |
| nationality | negative      | not_spacified |         62 |         39 |          19 |     120 |     51.6667  |      32.5    |      15.8333 |
| ageism      | negative      | male          |         51 |         96 |          68 |     215 |     23.7209  |      44.6512 |      31.6279 |
| ageism      | negative      | female        |         82 |         73 |          60 |     215 |     38.1395  |      33.9535 |      27.907  |
| ageism      | negative      | not_spacified |         91 |         88 |          36 |     215 |     42.3256  |      40.9302 |      16.7442 |
| ableism     | negative      | male          |          9 |         34 |          33 |      76 |     11.8421  |      44.7368 |      43.4211 |
| ableism     | negative      | female        |          7 |         36 |          32 |      75 |      9.33333 |      48      |      42.6667 |
| ableism     | negative      | not_spacified |         10 |         35 |          31 |      76 |     13.1579  |      46.0526 |      40.7895 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        134 |        160 |         121 |     415 |      32.2892 |      38.5542 |      29.1566 |
| female        |        162 |        130 |         121 |     413 |      39.2252 |      31.477  |      29.2978 |
| not_spacified |        163 |        162 |          86 |     411 |      39.6594 |      39.4161 |      20.9246 |



## Kendall Tau Calculation

Total data: 3330

Kendall's Tau Correlation for type 1: 0.12437085734383031

P-Value: 6.276816379314295e-16

Total data: 2475

Kendall's Tau Correlation for type 2: 0.23261169268441995

P-Value: 5.6486827690857274e-27

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 3330

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.02841246652057463

P-Value: 0.023712516532652758

Total data: 2475

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.05812451790633609

P-Value: 0.0009974848877181495

