# Report for Model: norallm/normistral-7b-warm-instruct

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        311 |        190 |         116 |     617 |      50.4052 |      30.7942 |      18.8006 |
| ageism      | positive      |        198 |        160 |          54 |     412 |      48.0583 |      38.835  |      13.1068 |
| ableism     | positive      |        120 |         88 |          84 |     292 |      41.0959 |      30.137  |      28.7671 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        248 |        245 |          99 |     592 |      41.8919 |      41.3851 |      16.723  |
| ageism      | negative      |        184 |        174 |          50 |     408 |      45.098  |      42.6471 |      12.2549 |
| ableism     | negative      |        125 |        121 |          50 |     296 |      42.2297 |      40.8784 |      16.8919 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        559 |        435 |         215 |    1209 | 46.2366 | 35.9801 | 17.7833 |
| ageism      |        382 |        334 |         104 |     820 | 46.5854 | 40.7317 | 12.6829 |
| ableism     |        245 |        209 |         134 |     588 | 41.6667 | 35.5442 | 22.7891 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        119 |        122 |         119 |     360 |      33.0556 |      33.8889 |      33.0556 |
| ageism      | positive      |        167 |        135 |         346 |     648 |      25.7716 |      20.8333 |      53.3951 |
| ableism     | positive      |         75 |         24 |          61 |     160 |      46.875  |      15      |      38.125  |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        102 |        169 |         102 |     373 |      27.3458 |      45.3083 |      27.3458 |
| ageism      | negative      |        160 |        155 |         333 |     648 |      24.6914 |      23.9198 |      51.3889 |
| ableism     | negative      |         65 |         61 |          60 |     186 |      34.9462 |      32.7957 |      32.2581 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        221 |        291 |         221 |     733 | 30.1501 | 39.6999 | 30.1501 |
| ageism      |        327 |        290 |         679 |    1296 | 25.2315 | 22.3765 | 52.392  |
| ableism     |        140 |         85 |         121 |     346 | 40.4624 | 24.5665 | 34.9711 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         95 |         61 |          41 |     197 |      48.2234 |      30.9645 |     20.8122  |
| nationality | positive      | female        |        101 |         63 |          35 |     199 |      50.7538 |      31.6583 |     17.5879  |
| nationality | positive      | not_spacified |        115 |         66 |          40 |     221 |      52.0362 |      29.8643 |     18.0995  |
| ageism      | positive      | male          |         58 |         61 |          20 |     139 |      41.7266 |      43.8849 |     14.3885  |
| ageism      | positive      | female        |         65 |         50 |          21 |     136 |      47.7941 |      36.7647 |     15.4412  |
| ageism      | positive      | not_spacified |         75 |         49 |          13 |     137 |      54.7445 |      35.7664 |      9.48905 |
| ableism     | positive      | male          |         38 |         29 |          30 |      97 |      39.1753 |      29.8969 |     30.9278  |
| ableism     | positive      | female        |         37 |         29 |          28 |      94 |      39.3617 |      30.8511 |     29.7872  |
| ableism     | positive      | not_spacified |         45 |         30 |          26 |     101 |      44.5545 |      29.703  |     25.7426  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        191 |        151 |          91 |     433 |      44.1109 |      34.873  |      21.0162 |
| female        |        203 |        142 |          84 |     429 |      47.3193 |      33.1002 |      19.5804 |
| not_spacified |        235 |        145 |          79 |     459 |      51.1983 |      31.5904 |      17.2113 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         72 |         79 |          34 |     185 |      38.9189 |      42.7027 |      18.3784 |
| nationality | negative      | female        |         84 |         79 |          36 |     199 |      42.2111 |      39.6985 |      18.0905 |
| nationality | negative      | not_spacified |         92 |         87 |          29 |     208 |      44.2308 |      41.8269 |      13.9423 |
| ageism      | negative      | male          |         61 |         58 |          18 |     137 |      44.5255 |      42.3358 |      13.1387 |
| ageism      | negative      | female        |         60 |         55 |          18 |     133 |      45.1128 |      41.3534 |      13.5338 |
| ageism      | negative      | not_spacified |         63 |         61 |          14 |     138 |      45.6522 |      44.2029 |      10.1449 |
| ableism     | negative      | male          |         33 |         40 |          19 |      92 |      35.8696 |      43.4783 |      20.6522 |
| ableism     | negative      | female        |         44 |         39 |          17 |     100 |      44      |      39      |      17      |
| ableism     | negative      | not_spacified |         48 |         42 |          14 |     104 |      46.1538 |      40.3846 |      13.4615 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        166 |        177 |          71 |     414 |      40.0966 |      42.7536 |      17.1498 |
| female        |        188 |        173 |          71 |     432 |      43.5185 |      40.0463 |      16.4352 |
| not_spacified |        203 |        190 |          57 |     450 |      45.1111 |      42.2222 |      12.6667 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         44 |         39 |          38 |     121 |      36.3636 |      32.2314 |      31.405  |
| nationality | positive      | female        |         35 |         41 |          41 |     117 |      29.9145 |      35.0427 |      35.0427 |
| nationality | positive      | not_spacified |         40 |         42 |          40 |     122 |      32.7869 |      34.4262 |      32.7869 |
| ageism      | positive      | male          |         57 |         44 |         115 |     216 |      26.3889 |      20.3704 |      53.2407 |
| ageism      | positive      | female        |         65 |         46 |         105 |     216 |      30.0926 |      21.2963 |      48.6111 |
| ageism      | positive      | not_spacified |         45 |         45 |         126 |     216 |      20.8333 |      20.8333 |      58.3333 |
| ableism     | positive      | male          |         26 |          7 |          20 |      53 |      49.0566 |      13.2075 |      37.7358 |
| ableism     | positive      | female        |         28 |         11 |          18 |      57 |      49.1228 |      19.2982 |      31.5789 |
| ableism     | positive      | not_spacified |         21 |          6 |          23 |      50 |      42      |      12      |      46      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        127 |         90 |         173 |     390 |      32.5641 |      23.0769 |      44.359  |
| female        |        128 |         98 |         164 |     390 |      32.8205 |      25.1282 |      42.0513 |
| not_spacified |        106 |         93 |         189 |     388 |      27.3196 |      23.9691 |      48.7113 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         32 |         60 |          34 |     126 |      25.3968 |      47.619  |      26.9841 |
| nationality | negative      | female        |         33 |         52 |          39 |     124 |      26.6129 |      41.9355 |      31.4516 |
| nationality | negative      | not_spacified |         37 |         57 |          29 |     123 |      30.0813 |      46.3415 |      23.5772 |
| ageism      | negative      | male          |         52 |         63 |         101 |     216 |      24.0741 |      29.1667 |      46.7593 |
| ageism      | negative      | female        |         58 |         46 |         112 |     216 |      26.8519 |      21.2963 |      51.8519 |
| ageism      | negative      | not_spacified |         50 |         46 |         120 |     216 |      23.1481 |      21.2963 |      55.5556 |
| ableism     | negative      | male          |         19 |         25 |          20 |      64 |      29.6875 |      39.0625 |      31.25   |
| ableism     | negative      | female        |         27 |         17 |          17 |      61 |      44.2623 |      27.8689 |      27.8689 |
| ableism     | negative      | not_spacified |         19 |         19 |          23 |      61 |      31.1475 |      31.1475 |      37.7049 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        103 |        148 |         155 |     406 |      25.3695 |      36.4532 |      38.1773 |
| female        |        118 |        115 |         168 |     401 |      29.4264 |      28.6783 |      41.8953 |
| not_spacified |        106 |        122 |         172 |     400 |      26.5    |      30.5    |      43      |



## Kendall Tau Calculation

Total data: 3230

Kendall's Tau Correlation for type 1: 0.07041263694658245

P-Value: 0.00023352348459128007

Total data: 2441

Kendall's Tau Correlation for type 2: 0.08167987780778356

P-Value: 0.00017783593077257365

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 3230

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.019288692501605496

P-Value: 0.21700379954969695

Total data: 2441

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.024360571091860492

P-Value: 0.1709537426904657

