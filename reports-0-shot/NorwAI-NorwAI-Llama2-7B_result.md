# Report for Model: NorwAI/NorwAI-Llama2-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        227 |        240 |         117 |     584 |      38.8699 |      41.0959 |     20.0342  |
| ageism      | positive      |        257 |         58 |          25 |     340 |      75.5882 |      17.0588 |      7.35294 |
| ableism     | positive      |        109 |        109 |          50 |     268 |      40.6716 |      40.6716 |     18.6567  |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        225 |        235 |         128 |     588 |      38.2653 |      39.966  |      21.7687 |
| ageism      | negative      |        221 |         48 |          49 |     318 |      69.4969 |      15.0943 |      15.4088 |
| ableism     | negative      |        131 |         84 |          39 |     254 |      51.5748 |      33.0709 |      15.3543 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        452 |        475 |         245 |    1172 | 38.5666 | 40.529  | 20.9044 |
| ageism      |        478 |        106 |          74 |     658 | 72.6444 | 16.1094 | 11.2462 |
| ableism     |        240 |        193 |          89 |     522 | 45.977  | 36.9732 | 17.0498 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        182 |         73 |          36 |     291 |      62.543  |      25.0859 |      12.3711 |
| ageism      | positive      |        109 |        351 |         188 |     648 |      16.821  |      54.1667 |      29.0123 |
| ableism     | positive      |         57 |         54 |          40 |     151 |      37.7483 |      35.7616 |      26.4901 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        200 |         60 |          36 |     296 |      67.5676 |      20.2703 |      12.1622 |
| ageism      | negative      |        129 |        320 |         199 |     648 |      19.9074 |      49.3827 |      30.7099 |
| ableism     | negative      |         56 |         65 |          63 |     184 |      30.4348 |      35.3261 |      34.2391 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        382 |        133 |          72 |     587 | 65.0767 | 22.6576 | 12.2658 |
| ageism      |        238 |        671 |         387 |    1296 | 18.3642 | 51.7747 | 29.8611 |
| ableism     |        113 |        119 |         103 |     335 | 33.7313 | 35.5224 | 30.7463 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         83 |         79 |          41 |     203 |      40.8867 |      38.9163 |     20.197   |
| nationality | positive      | female        |         73 |         76 |          37 |     186 |      39.2473 |      40.8602 |     19.8925  |
| nationality | positive      | not_spacified |         71 |         85 |          39 |     195 |      36.4103 |      43.5897 |     20       |
| ageism      | positive      | male          |         94 |         15 |          11 |     120 |      78.3333 |      12.5    |      9.16667 |
| ageism      | positive      | female        |         80 |         23 |          10 |     113 |      70.7965 |      20.354  |      8.84956 |
| ageism      | positive      | not_spacified |         83 |         20 |           4 |     107 |      77.5701 |      18.6916 |      3.73832 |
| ableism     | positive      | male          |         41 |         37 |          11 |      89 |      46.0674 |      41.573  |     12.3596  |
| ableism     | positive      | female        |         32 |         39 |          22 |      93 |      34.4086 |      41.9355 |     23.6559  |
| ableism     | positive      | not_spacified |         36 |         33 |          17 |      86 |      41.8605 |      38.3721 |     19.7674  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        218 |        131 |          63 |     412 |      52.9126 |      31.7961 |      15.2913 |
| female        |        185 |        138 |          69 |     392 |      47.1939 |      35.2041 |      17.602  |
| not_spacified |        190 |        138 |          60 |     388 |      48.9691 |      35.567  |      15.4639 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         69 |         79 |          44 |     192 |      35.9375 |      41.1458 |      22.9167 |
| nationality | negative      | female        |         84 |         69 |          42 |     195 |      43.0769 |      35.3846 |      21.5385 |
| nationality | negative      | not_spacified |         72 |         87 |          42 |     201 |      35.8209 |      43.2836 |      20.8955 |
| ageism      | negative      | male          |         75 |         15 |          15 |     105 |      71.4286 |      14.2857 |      14.2857 |
| ageism      | negative      | female        |         74 |         16 |          15 |     105 |      70.4762 |      15.2381 |      14.2857 |
| ageism      | negative      | not_spacified |         72 |         17 |          19 |     108 |      66.6667 |      15.7407 |      17.5926 |
| ableism     | negative      | male          |         46 |         31 |          16 |      93 |      49.4624 |      33.3333 |      17.2043 |
| ableism     | negative      | female        |         43 |         26 |          15 |      84 |      51.1905 |      30.9524 |      17.8571 |
| ableism     | negative      | not_spacified |         42 |         27 |           8 |      77 |      54.5455 |      35.0649 |      10.3896 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        190 |        125 |          75 |     390 |      48.7179 |      32.0513 |      19.2308 |
| female        |        201 |        111 |          72 |     384 |      52.3438 |      28.9062 |      18.75   |
| not_spacified |        186 |        131 |          69 |     386 |      48.1865 |      33.9378 |      17.8756 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         67 |         24 |           9 |     100 |      67      |      24      |       9      |
| nationality | positive      | female        |         57 |         26 |          13 |      96 |      59.375  |      27.0833 |      13.5417 |
| nationality | positive      | not_spacified |         58 |         23 |          14 |      95 |      61.0526 |      24.2105 |      14.7368 |
| ageism      | positive      | male          |         31 |        117 |          68 |     216 |      14.3519 |      54.1667 |      31.4815 |
| ageism      | positive      | female        |         37 |        118 |          61 |     216 |      17.1296 |      54.6296 |      28.2407 |
| ageism      | positive      | not_spacified |         41 |        116 |          59 |     216 |      18.9815 |      53.7037 |      27.3148 |
| ableism     | positive      | male          |         19 |         16 |          12 |      47 |      40.4255 |      34.0426 |      25.5319 |
| ableism     | positive      | female        |         21 |         15 |          12 |      48 |      43.75   |      31.25   |      25      |
| ableism     | positive      | not_spacified |         17 |         23 |          16 |      56 |      30.3571 |      41.0714 |      28.5714 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        117 |        157 |          89 |     363 |      32.2314 |      43.2507 |      24.5179 |
| female        |        115 |        159 |          86 |     360 |      31.9444 |      44.1667 |      23.8889 |
| not_spacified |        116 |        162 |          89 |     367 |      31.6076 |      44.1417 |      24.2507 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         67 |         23 |          11 |     101 |      66.3366 |      22.7723 |      10.8911 |
| nationality | negative      | female        |         66 |         21 |          13 |     100 |      66      |      21      |      13      |
| nationality | negative      | not_spacified |         67 |         16 |          12 |      95 |      70.5263 |      16.8421 |      12.6316 |
| ageism      | negative      | male          |         45 |        109 |          62 |     216 |      20.8333 |      50.463  |      28.7037 |
| ageism      | negative      | female        |         42 |         93 |          81 |     216 |      19.4444 |      43.0556 |      37.5    |
| ageism      | negative      | not_spacified |         42 |        118 |          56 |     216 |      19.4444 |      54.6296 |      25.9259 |
| ableism     | negative      | male          |         18 |         23 |          19 |      60 |      30      |      38.3333 |      31.6667 |
| ableism     | negative      | female        |         19 |         22 |          20 |      61 |      31.1475 |      36.0656 |      32.7869 |
| ableism     | negative      | not_spacified |         19 |         20 |          24 |      63 |      30.1587 |      31.746  |      38.0952 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        130 |        155 |          92 |     377 |      34.4828 |      41.1141 |      24.4032 |
| female        |        127 |        136 |         114 |     377 |      33.687  |      36.0743 |      30.2387 |
| not_spacified |        128 |        154 |          92 |     374 |      34.2246 |      41.1765 |      24.5989 |



## Kendall Tau Calculation

Total data: 2352

Kendall's Tau Correlation for type 1: -0.012546855476884632

P-Value: 0.5644407582507176

Total data: 2218

Kendall's Tau Correlation for type 2: -0.042337429393575474

P-Value: 0.06500123880518434

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 2352

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.005880796196029432

P-Value: 0.7408085276683847

Total data: 2218

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.00741169267595808

P-Value: 0.6924195321909039

