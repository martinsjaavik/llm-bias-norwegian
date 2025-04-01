# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         47 |         62 |          24 |     133 |      35.3383 |      46.6165 |      18.0451 |
| ageism      | positive      |         34 |         23 |          14 |      71 |      47.8873 |      32.3944 |      19.7183 |
| ableism     | positive      |         20 |         28 |          14 |      62 |      32.2581 |      45.1613 |      22.5806 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         22 |         73 |          24 |     119 |      18.4874 |      61.3445 |      20.1681 |
| ageism      | negative      |         21 |         39 |          12 |      72 |      29.1667 |      54.1667 |      16.6667 |
| ableism     | negative      |          7 |         39 |          20 |      66 |      10.6061 |      59.0909 |      30.303  |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         69 |        135 |          48 |     252 | 27.381  | 53.5714 | 19.0476 |
| ageism      |         55 |         62 |          26 |     143 | 38.4615 | 43.3566 | 18.1818 |
| ableism     |         27 |         67 |          34 |     128 | 21.0938 | 52.3438 | 26.5625 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         46 |          6 |          12 |      64 |      71.875  |       9.375  |      18.75   |
| ageism      | positive      |         24 |         53 |          37 |     114 |      21.0526 |      46.4912 |      32.4561 |
| ableism     | positive      |          8 |         13 |           7 |      28 |      28.5714 |      46.4286 |      25      |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         24 |         36 |          14 |      74 |      32.4324 |      48.6486 |     18.9189  |
| ageism      | negative      |         22 |         75 |          23 |     120 |      18.3333 |      62.5    |     19.1667  |
| ableism     | negative      |          9 |         17 |           2 |      28 |      32.1429 |      60.7143 |      7.14286 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         70 |         42 |          26 |     138 | 50.7246 | 30.4348 | 18.8406 |
| ageism      |         46 |        128 |          60 |     234 | 19.6581 | 54.7009 | 25.641  |
| ableism     |         17 |         30 |           9 |      56 | 30.3571 | 53.5714 | 16.0714 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          9 |         20 |           7 |      36 |      25      |      55.5556 |      19.4444 |
| nationality | positive      | female        |         21 |         20 |           8 |      49 |      42.8571 |      40.8163 |      16.3265 |
| nationality | positive      | not_spacified |         17 |         22 |           9 |      48 |      35.4167 |      45.8333 |      18.75   |
| ageism      | positive      | male          |         17 |          7 |           5 |      29 |      58.6207 |      24.1379 |      17.2414 |
| ageism      | positive      | female        |          7 |          4 |           5 |      16 |      43.75   |      25      |      31.25   |
| ageism      | positive      | not_spacified |         10 |         12 |           4 |      26 |      38.4615 |      46.1538 |      15.3846 |
| ableism     | positive      | male          |          7 |          9 |           3 |      19 |      36.8421 |      47.3684 |      15.7895 |
| ableism     | positive      | female        |          7 |          6 |           7 |      20 |      35      |      30      |      35      |
| ableism     | positive      | not_spacified |          6 |         13 |           4 |      23 |      26.087  |      56.5217 |      17.3913 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         33 |         36 |          15 |      84 |      39.2857 |      42.8571 |      17.8571 |
| female        |         35 |         30 |          20 |      85 |      41.1765 |      35.2941 |      23.5294 |
| not_spacified |         33 |         47 |          17 |      97 |      34.0206 |      48.4536 |      17.5258 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          8 |         24 |           4 |      36 |     22.2222  |      66.6667 |      11.1111 |
| nationality | negative      | female        |          6 |         28 |          13 |      47 |     12.766   |      59.5745 |      27.6596 |
| nationality | negative      | not_spacified |          8 |         21 |           7 |      36 |     22.2222  |      58.3333 |      19.4444 |
| ageism      | negative      | male          |         10 |         10 |           6 |      26 |     38.4615  |      38.4615 |      23.0769 |
| ageism      | negative      | female        |          5 |         15 |           5 |      25 |     20       |      60      |      20      |
| ageism      | negative      | not_spacified |          6 |         14 |           1 |      21 |     28.5714  |      66.6667 |       4.7619 |
| ableism     | negative      | male          |          3 |         11 |           5 |      19 |     15.7895  |      57.8947 |      26.3158 |
| ableism     | negative      | female        |          2 |         17 |          10 |      29 |      6.89655 |      58.6207 |      34.4828 |
| ableism     | negative      | not_spacified |          2 |         11 |           5 |      18 |     11.1111  |      61.1111 |      27.7778 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         21 |         45 |          15 |      81 |      25.9259 |      55.5556 |      18.5185 |
| female        |         13 |         60 |          28 |     101 |      12.8713 |      59.4059 |      27.7228 |
| not_spacified |         16 |         46 |          13 |      75 |      21.3333 |      61.3333 |      17.3333 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         14 |          1 |           7 |      22 |      63.6364 |      4.54545 |      31.8182 |
| nationality | positive      | female        |         17 |          2 |           3 |      22 |      77.2727 |      9.09091 |      13.6364 |
| nationality | positive      | not_spacified |         15 |          3 |           2 |      20 |      75      |     15       |      10      |
| ageism      | positive      | male          |          6 |         17 |          10 |      33 |      18.1818 |     51.5152  |      30.303  |
| ageism      | positive      | female        |          8 |         18 |          17 |      43 |      18.6047 |     41.8605  |      39.5349 |
| ageism      | positive      | not_spacified |         10 |         18 |          10 |      38 |      26.3158 |     47.3684  |      26.3158 |
| ableism     | positive      | male          |          4 |          6 |           2 |      12 |      33.3333 |     50       |      16.6667 |
| ableism     | positive      | female        |          3 |          3 |           1 |       7 |      42.8571 |     42.8571  |      14.2857 |
| ableism     | positive      | not_spacified |          1 |          4 |           4 |       9 |      11.1111 |     44.4444  |      44.4444 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         24 |         24 |          19 |      67 |      35.8209 |      35.8209 |      28.3582 |
| female        |         28 |         23 |          21 |      72 |      38.8889 |      31.9444 |      29.1667 |
| not_spacified |         26 |         25 |          16 |      67 |      38.806  |      37.3134 |      23.8806 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          8 |         13 |           4 |      25 |      32      |      52      |     16       |
| nationality | negative      | female        |          6 |         10 |           4 |      20 |      30      |      50      |     20       |
| nationality | negative      | not_spacified |         10 |         13 |           6 |      29 |      34.4828 |      44.8276 |     20.6897  |
| ageism      | negative      | male          |          5 |         24 |           6 |      35 |      14.2857 |      68.5714 |     17.1429  |
| ageism      | negative      | female        |          7 |         26 |          10 |      43 |      16.2791 |      60.4651 |     23.2558  |
| ageism      | negative      | not_spacified |         10 |         25 |           7 |      42 |      23.8095 |      59.5238 |     16.6667  |
| ableism     | negative      | male          |          4 |          6 |           1 |      11 |      36.3636 |      54.5455 |      9.09091 |
| ableism     | negative      | female        |          4 |          8 |           0 |      12 |      33.3333 |      66.6667 |      0       |
| ableism     | negative      | not_spacified |          1 |          3 |           1 |       5 |      20      |      60      |     20       |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         17 |         43 |          11 |      71 |      23.9437 |      60.5634 |      15.493  |
| female        |         17 |         44 |          14 |      75 |      22.6667 |      58.6667 |      18.6667 |
| not_spacified |         21 |         41 |          14 |      76 |      27.6316 |      53.9474 |      18.4211 |



## Kendall Tau Calculation

Total data: 523

Kendall's Tau Correlation for type 1: 0.2073783766986316

P-Value: 7.406013636959681e-06

Total data: 428

Kendall's Tau Correlation for type 2: 0.2259149270678662

P-Value: 1.2415374095715894e-05

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 523

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.01747163920461816

P-Value: 0.6436660167778874

Total data: 428

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.01632784522665735

P-Value: 0.6990513616236249

