# Report for Model: NorwAI/NorwAI-Llama2-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        574 |         56 |         164 |     794 |      72.2922 |      7.0529  |     20.6549  |
| ageism      | positive      |        317 |         31 |          31 |     379 |      83.6412 |      8.17942 |      8.17942 |
| ableism     | positive      |        208 |         67 |          72 |     347 |      59.9424 |     19.3084  |     20.7493  |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        412 |        214 |         163 |     789 |      52.218  |      27.1229 |      20.6591 |
| ageism      | negative      |        269 |         43 |          58 |     370 |      72.7027 |      11.6216 |      15.6757 |
| ableism     | negative      |        191 |         87 |          52 |     330 |      57.8788 |      26.3636 |      15.7576 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |        986 |        270 |         327 |    1583 | 62.2868 | 17.0562  | 20.657  |
| ageism      |        586 |         74 |          89 |     749 | 78.2377 |  9.87984 | 11.8825 |
| ableism     |        399 |        154 |         124 |     677 | 58.9365 | 22.7474  | 18.3161 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        189 |         74 |          45 |     308 |      61.3636 |      24.026  |      14.6104 |
| ageism      | positive      |        188 |        216 |         243 |     647 |      29.0572 |      33.3849 |      37.558  |
| ableism     | positive      |         62 |         47 |          77 |     186 |      33.3333 |      25.2688 |      41.3978 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        178 |         95 |          54 |     327 |      54.4343 |      29.052  |      16.5138 |
| ageism      | negative      |        174 |        253 |         221 |     648 |      26.8519 |      39.0432 |      34.1049 |
| ableism     | negative      |         63 |         71 |          74 |     208 |      30.2885 |      34.1346 |      35.5769 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        367 |        169 |          99 |     635 | 57.7953 | 26.6142 | 15.5906 |
| ageism      |        362 |        469 |         464 |    1295 | 27.9537 | 36.2162 | 35.8301 |
| ableism     |        125 |        118 |         151 |     394 | 31.7259 | 29.9492 | 38.3249 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        191 |         23 |          53 |     267 |      71.5356 |      8.61423 |     19.8502  |
| nationality | positive      | female        |        191 |         13 |          58 |     262 |      72.9008 |      4.96183 |     22.1374  |
| nationality | positive      | not_spacified |        192 |         20 |          53 |     265 |      72.4528 |      7.54717 |     20       |
| ageism      | positive      | male          |        106 |         11 |          12 |     129 |      82.1705 |      8.52713 |      9.30233 |
| ageism      | positive      | female        |        108 |         11 |           8 |     127 |      85.0394 |      8.66142 |      6.29921 |
| ageism      | positive      | not_spacified |        103 |          9 |          11 |     123 |      83.7398 |      7.31707 |      8.94309 |
| ableism     | positive      | male          |         73 |         22 |          26 |     121 |      60.3306 |     18.1818  |     21.4876  |
| ableism     | positive      | female        |         63 |         26 |          23 |     112 |      56.25   |     23.2143  |     20.5357  |
| ableism     | positive      | not_spacified |         72 |         19 |          23 |     114 |      63.1579 |     16.6667  |     20.1754  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        370 |         56 |          91 |     517 |      71.5667 |     10.8317  |      17.6015 |
| female        |        362 |         50 |          89 |     501 |      72.2555 |      9.98004 |      17.7645 |
| not_spacified |        367 |         48 |          87 |     502 |      73.1076 |      9.56175 |      17.3307 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |        135 |         70 |          58 |     263 |      51.3308 |     26.616   |      22.0532 |
| nationality | negative      | female        |        150 |         64 |          52 |     266 |      56.391  |     24.0602  |      19.5489 |
| nationality | negative      | not_spacified |        127 |         80 |          53 |     260 |      48.8462 |     30.7692  |      20.3846 |
| ageism      | negative      | male          |        100 |         10 |          17 |     127 |      78.7402 |      7.87402 |      13.3858 |
| ageism      | negative      | female        |         80 |         16 |          25 |     121 |      66.1157 |     13.2231  |      20.6612 |
| ageism      | negative      | not_spacified |         89 |         17 |          16 |     122 |      72.9508 |     13.9344  |      13.1148 |
| ableism     | negative      | male          |         61 |         33 |          21 |     115 |      53.0435 |     28.6957  |      18.2609 |
| ableism     | negative      | female        |         63 |         29 |          14 |     106 |      59.434  |     27.3585  |      13.2075 |
| ableism     | negative      | not_spacified |         67 |         25 |          17 |     109 |      61.4679 |     22.9358  |      15.5963 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        296 |        113 |          96 |     505 |      58.6139 |      22.3762 |      19.0099 |
| female        |        293 |        109 |          91 |     493 |      59.432  |      22.1095 |      18.4584 |
| not_spacified |        283 |        122 |          86 |     491 |      57.6375 |      24.8473 |      17.5153 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         59 |         28 |          13 |     100 |      59      |      28      |      13      |
| nationality | positive      | female        |         66 |         23 |          15 |     104 |      63.4615 |      22.1154 |      14.4231 |
| nationality | positive      | not_spacified |         64 |         23 |          17 |     104 |      61.5385 |      22.1154 |      16.3462 |
| ageism      | positive      | male          |         60 |         75 |          81 |     216 |      27.7778 |      34.7222 |      37.5    |
| ageism      | positive      | female        |         64 |         70 |          81 |     215 |      29.7674 |      32.5581 |      37.6744 |
| ageism      | positive      | not_spacified |         64 |         71 |          81 |     216 |      29.6296 |      32.8704 |      37.5    |
| ableism     | positive      | male          |         22 |         18 |          23 |      63 |      34.9206 |      28.5714 |      36.5079 |
| ableism     | positive      | female        |         21 |         16 |          24 |      61 |      34.4262 |      26.2295 |      39.3443 |
| ableism     | positive      | not_spacified |         19 |         13 |          30 |      62 |      30.6452 |      20.9677 |      48.3871 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        141 |        121 |         117 |     379 |      37.2032 |      31.9261 |      30.8707 |
| female        |        151 |        109 |         120 |     380 |      39.7368 |      28.6842 |      31.5789 |
| not_spacified |        147 |        107 |         128 |     382 |      38.4817 |      28.0105 |      33.5079 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         60 |         32 |          16 |     108 |      55.5556 |      29.6296 |      14.8148 |
| nationality | negative      | female        |         56 |         33 |          16 |     105 |      53.3333 |      31.4286 |      15.2381 |
| nationality | negative      | not_spacified |         62 |         30 |          22 |     114 |      54.386  |      26.3158 |      19.2982 |
| ageism      | negative      | male          |         53 |         90 |          73 |     216 |      24.537  |      41.6667 |      33.7963 |
| ageism      | negative      | female        |         59 |         92 |          65 |     216 |      27.3148 |      42.5926 |      30.0926 |
| ageism      | negative      | not_spacified |         62 |         71 |          83 |     216 |      28.7037 |      32.8704 |      38.4259 |
| ableism     | negative      | male          |         20 |         24 |          25 |      69 |      28.9855 |      34.7826 |      36.2319 |
| ableism     | negative      | female        |         18 |         24 |          26 |      68 |      26.4706 |      35.2941 |      38.2353 |
| ableism     | negative      | not_spacified |         25 |         23 |          23 |      71 |      35.2113 |      32.3944 |      32.3944 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        133 |        146 |         114 |     393 |      33.8422 |      37.1501 |      29.0076 |
| female        |        133 |        149 |         107 |     389 |      34.1902 |      38.3033 |      27.5064 |
| not_spacified |        149 |        124 |         128 |     401 |      37.1571 |      30.9227 |      31.9202 |



## Kendall Tau Calculation

Total data: 3009

Kendall's Tau Correlation for type 1: 0.15938757340474421

P-Value: 2.3910135778437434e-19

Total data: 2324

Kendall's Tau Correlation for type 2: 0.06009580490637248

P-Value: 0.007723864393657757

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 3009

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.005271655952713478

P-Value: 0.7156300385794645

Total data: 2324

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.01091524939196175

P-Value: 0.5535184541701128

