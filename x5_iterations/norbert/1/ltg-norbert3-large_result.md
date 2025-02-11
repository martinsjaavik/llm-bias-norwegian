# Report for Model: ltg/norbert3-large

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         67 |         14 |          58 |     139 |      48.2014 |     10.0719  |      41.7266 |
| ageism      | positive      |         54 |          1 |          26 |      81 |      66.6667 |      1.23457 |      32.0988 |
| ableism     | positive      |         17 |         24 |          24 |      65 |      26.1538 |     36.9231  |      36.9231 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         46 |         27 |          51 |     124 |      37.0968 |      21.7742 |      41.129  |
| ageism      | negative      |         38 |         19 |          19 |      76 |      50      |      25      |      25      |
| ableism     | negative      |         27 |         20 |          21 |      68 |      39.7059 |      29.4118 |      30.8824 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        113 |         41 |         109 |     263 | 42.9658 | 15.5894 | 41.4449 |
| ageism      |         92 |         20 |          45 |     157 | 58.5987 | 12.7389 | 28.6624 |
| ableism     |         44 |         44 |          45 |     133 | 33.0827 | 33.0827 | 33.8346 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         23 |         18 |          24 |      65 |      35.3846 |      27.6923 |      36.9231 |
| ageism      | positive      |         25 |         52 |          37 |     114 |      21.9298 |      45.614  |      32.4561 |
| ableism     | positive      |         15 |         13 |           6 |      34 |      44.1176 |      38.2353 |      17.6471 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         20 |         28 |          27 |      75 |      26.6667 |      37.3333 |      36      |
| ageism      | negative      |         41 |         41 |          38 |     120 |      34.1667 |      34.1667 |      31.6667 |
| ableism     | negative      |         18 |         14 |           7 |      39 |      46.1538 |      35.8974 |      17.9487 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         43 |         46 |          51 |     140 | 30.7143 | 32.8571 | 36.4286 |
| ageism      |         66 |         93 |          75 |     234 | 28.2051 | 39.7436 | 32.0513 |
| ableism     |         33 |         27 |          13 |      73 | 45.2055 | 36.9863 | 17.8082 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         20 |          6 |          11 |      37 |      54.0541 |     16.2162  |      29.7297 |
| nationality | positive      | female        |         23 |          4 |          25 |      52 |      44.2308 |      7.69231 |      48.0769 |
| nationality | positive      | not_spacified |         24 |          4 |          22 |      50 |      48      |      8       |      44      |
| ageism      | positive      | male          |         22 |          0 |          11 |      33 |      66.6667 |      0       |      33.3333 |
| ageism      | positive      | female        |         11 |          1 |           5 |      17 |      64.7059 |      5.88235 |      29.4118 |
| ageism      | positive      | not_spacified |         21 |          0 |          10 |      31 |      67.7419 |      0       |      32.2581 |
| ableism     | positive      | male          |          6 |          5 |           8 |      19 |      31.5789 |     26.3158  |      42.1053 |
| ableism     | positive      | female        |          8 |          5 |           8 |      21 |      38.0952 |     23.8095  |      38.0952 |
| ableism     | positive      | not_spacified |          3 |         14 |           8 |      25 |      12      |     56       |      32      |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         48 |         11 |          30 |      89 |      53.9326 |      12.3596 |      33.7079 |
| female        |         42 |         10 |          38 |      90 |      46.6667 |      11.1111 |      42.2222 |
| not_spacified |         48 |         18 |          40 |     106 |      45.283  |      16.9811 |      37.7358 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         12 |         10 |          15 |      37 |      32.4324 |      27.027  |      40.5405 |
| nationality | negative      | female        |         17 |         11 |          21 |      49 |      34.6939 |      22.449  |      42.8571 |
| nationality | negative      | not_spacified |         17 |          6 |          15 |      38 |      44.7368 |      15.7895 |      39.4737 |
| ageism      | negative      | male          |         14 |          8 |           6 |      28 |      50      |      28.5714 |      21.4286 |
| ageism      | negative      | female        |         13 |          7 |           6 |      26 |      50      |      26.9231 |      23.0769 |
| ageism      | negative      | not_spacified |         11 |          4 |           7 |      22 |      50      |      18.1818 |      31.8182 |
| ableism     | negative      | male          |          5 |          8 |           6 |      19 |      26.3158 |      42.1053 |      31.5789 |
| ableism     | negative      | female        |         13 |          6 |          11 |      30 |      43.3333 |      20      |      36.6667 |
| ableism     | negative      | not_spacified |          9 |          6 |           4 |      19 |      47.3684 |      31.5789 |      21.0526 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         31 |         26 |          27 |      84 |      36.9048 |      30.9524 |      32.1429 |
| female        |         43 |         24 |          38 |     105 |      40.9524 |      22.8571 |      36.1905 |
| not_spacified |         37 |         16 |          26 |      79 |      46.8354 |      20.2532 |      32.9114 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          6 |          7 |          10 |      23 |      26.087  |      30.4348 |      43.4783 |
| nationality | positive      | female        |         11 |          4 |           7 |      22 |      50      |      18.1818 |      31.8182 |
| nationality | positive      | not_spacified |          6 |          7 |           7 |      20 |      30      |      35      |      35      |
| ageism      | positive      | male          |          6 |         13 |          14 |      33 |      18.1818 |      39.3939 |      42.4242 |
| ageism      | positive      | female        |         13 |         18 |          12 |      43 |      30.2326 |      41.8605 |      27.907  |
| ageism      | positive      | not_spacified |          6 |         21 |          11 |      38 |      15.7895 |      55.2632 |      28.9474 |
| ableism     | positive      | male          |          7 |          4 |           3 |      14 |      50      |      28.5714 |      21.4286 |
| ableism     | positive      | female        |          4 |          4 |           1 |       9 |      44.4444 |      44.4444 |      11.1111 |
| ableism     | positive      | not_spacified |          4 |          5 |           2 |      11 |      36.3636 |      45.4545 |      18.1818 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         19 |         24 |          27 |      70 |      27.1429 |      34.2857 |      38.5714 |
| female        |         28 |         26 |          20 |      74 |      37.8378 |      35.1351 |      27.027  |
| not_spacified |         16 |         33 |          20 |      69 |      23.1884 |      47.8261 |      28.9855 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          4 |          9 |          12 |      25 |      16      |      36      |      48      |
| nationality | negative      | female        |          7 |          8 |           6 |      21 |      33.3333 |      38.0952 |      28.5714 |
| nationality | negative      | not_spacified |          9 |         11 |           9 |      29 |      31.0345 |      37.931  |      31.0345 |
| ageism      | negative      | male          |         11 |         10 |          14 |      35 |      31.4286 |      28.5714 |      40      |
| ageism      | negative      | female        |         16 |         14 |          13 |      43 |      37.2093 |      32.5581 |      30.2326 |
| ageism      | negative      | not_spacified |         14 |         17 |          11 |      42 |      33.3333 |      40.4762 |      26.1905 |
| ableism     | negative      | male          |          3 |          8 |           4 |      15 |      20      |      53.3333 |      26.6667 |
| ableism     | negative      | female        |          8 |          5 |           3 |      16 |      50      |      31.25   |      18.75   |
| ableism     | negative      | not_spacified |          7 |          1 |           0 |       8 |      87.5    |      12.5    |       0      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         18 |         27 |          30 |      75 |      24      |      36      |      40      |
| female        |         31 |         27 |          22 |      80 |      38.75   |      33.75   |      27.5    |
| not_spacified |         30 |         29 |          20 |      79 |      37.9747 |      36.7089 |      25.3165 |



## Kendall Tau Calculation

Total data: 553

Kendall's Tau Correlation for type 1: 0.11677877367899571

P-Value: 0.010154936077027447

Total data: 447

Kendall's Tau Correlation for type 2: -0.050047795644840826

P-Value: 0.33047291726312167

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 553

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.0025309915666314594

P-Value: 0.9456033276078826

Total data: 447

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.05720463042205306

P-Value: 0.17353809393657837

