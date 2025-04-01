# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        113 |          2 |          23 |     138 |      81.8841 |      1.44928 |      16.6667 |
| ageism      | positive      |         57 |          1 |          12 |      70 |      81.4286 |      1.42857 |      17.1429 |
| ableism     | positive      |         46 |          3 |          16 |      65 |      70.7692 |      4.61538 |      24.6154 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         92 |          9 |          21 |     122 |      75.4098 |      7.37705 |      17.2131 |
| ageism      | negative      |         41 |         12 |          14 |      67 |      61.194  |     17.9104  |      20.8955 |
| ableism     | negative      |         47 |          6 |          14 |      67 |      70.1493 |      8.95522 |      20.8955 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        205 |         11 |          44 |     260 | 78.8462 | 4.23077 | 16.9231 |
| ageism      |         98 |         13 |          26 |     137 | 71.5328 | 9.48905 | 18.9781 |
| ableism     |         93 |          9 |          30 |     132 | 70.4545 | 6.81818 | 22.7273 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         45 |          3 |          14 |      62 |      72.5806 |      4.83871 |      22.5806 |
| ageism      | positive      |         48 |         15 |          48 |     111 |      43.2432 |     13.5135  |      43.2432 |
| ableism     | positive      |          5 |          9 |          19 |      33 |      15.1515 |     27.2727  |      57.5758 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         27 |         13 |           7 |      47 |     57.4468  |      27.6596 |      14.8936 |
| ageism      | negative      |         32 |         35 |          42 |     109 |     29.3578  |      32.1101 |      38.5321 |
| ableism     | negative      |          2 |         13 |          19 |      34 |      5.88235 |      38.2353 |      55.8824 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         72 |         16 |          21 |     109 | 66.055  | 14.6789 | 19.2661 |
| ageism      |         80 |         50 |          90 |     220 | 36.3636 | 22.7273 | 40.9091 |
| ableism     |          7 |         22 |          38 |      67 | 10.4478 | 32.8358 | 56.7164 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         29 |          1 |           6 |      36 |      80.5556 |      2.77778 |      16.6667 |
| nationality | positive      | female        |         42 |          1 |           9 |      52 |      80.7692 |      1.92308 |      17.3077 |
| nationality | positive      | not_spacified |         42 |          0 |           8 |      50 |      84      |      0       |      16      |
| ageism      | positive      | male          |         25 |          0 |           6 |      31 |      80.6452 |      0       |      19.3548 |
| ageism      | positive      | female        |         11 |          0 |           2 |      13 |      84.6154 |      0       |      15.3846 |
| ageism      | positive      | not_spacified |         21 |          1 |           4 |      26 |      80.7692 |      3.84615 |      15.3846 |
| ableism     | positive      | male          |         10 |          1 |           8 |      19 |      52.6316 |      5.26316 |      42.1053 |
| ableism     | positive      | female        |         17 |          0 |           4 |      21 |      80.9524 |      0       |      19.0476 |
| ableism     | positive      | not_spacified |         19 |          2 |           4 |      25 |      76      |      8       |      16      |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         64 |          2 |          20 |      86 |      74.4186 |      2.32558 |      23.2558 |
| female        |         70 |          1 |          15 |      86 |      81.3953 |      1.16279 |      17.4419 |
| not_spacified |         82 |          3 |          16 |     101 |      81.1881 |      2.9703  |      15.8416 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         24 |          2 |           9 |      35 |      68.5714 |      5.71429 |      25.7143 |
| nationality | negative      | female        |         38 |          3 |           8 |      49 |      77.551  |      6.12245 |      16.3265 |
| nationality | negative      | not_spacified |         30 |          4 |           4 |      38 |      78.9474 |     10.5263  |      10.5263 |
| ageism      | negative      | male          |         18 |          4 |           5 |      27 |      66.6667 |     14.8148  |      18.5185 |
| ageism      | negative      | female        |         14 |          3 |           6 |      23 |      60.8696 |     13.0435  |      26.087  |
| ageism      | negative      | not_spacified |          9 |          5 |           3 |      17 |      52.9412 |     29.4118  |      17.6471 |
| ableism     | negative      | male          |         11 |          2 |           6 |      19 |      57.8947 |     10.5263  |      31.5789 |
| ableism     | negative      | female        |         20 |          3 |           6 |      29 |      68.9655 |     10.3448  |      20.6897 |
| ableism     | negative      | not_spacified |         16 |          1 |           2 |      19 |      84.2105 |      5.26316 |      10.5263 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         53 |          8 |          20 |      81 |      65.4321 |      9.87654 |      24.6914 |
| female        |         72 |          9 |          20 |     101 |      71.2871 |      8.91089 |      19.802  |
| not_spacified |         55 |         10 |           9 |      74 |      74.3243 |     13.5135  |      12.1622 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         14 |          1 |           7 |      22 |     63.6364  |      4.54545 |      31.8182 |
| nationality | positive      | female        |         17 |          1 |           2 |      20 |     85       |      5       |      10      |
| nationality | positive      | not_spacified |         14 |          1 |           5 |      20 |     70       |      5       |      25      |
| ageism      | positive      | male          |         13 |          4 |          15 |      32 |     40.625   |     12.5     |      46.875  |
| ageism      | positive      | female        |         18 |          6 |          18 |      42 |     42.8571  |     14.2857  |      42.8571 |
| ageism      | positive      | not_spacified |         17 |          5 |          15 |      37 |     45.9459  |     13.5135  |      40.5405 |
| ableism     | positive      | male          |          3 |          2 |           9 |      14 |     21.4286  |     14.2857  |      64.2857 |
| ableism     | positive      | female        |          1 |          3 |           4 |       8 |     12.5     |     37.5     |      50      |
| ableism     | positive      | not_spacified |          1 |          4 |           6 |      11 |      9.09091 |     36.3636  |      54.5455 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         30 |          7 |          31 |      68 |      44.1176 |      10.2941 |      45.5882 |
| female        |         36 |         10 |          24 |      70 |      51.4286 |      14.2857 |      34.2857 |
| not_spacified |         32 |         10 |          26 |      68 |      47.0588 |      14.7059 |      38.2353 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          8 |          3 |           4 |      15 |     53.3333  |      20      |     26.6667  |
| nationality | negative      | female        |          2 |          5 |           2 |       9 |     22.2222  |      55.5556 |     22.2222  |
| nationality | negative      | not_spacified |         17 |          5 |           1 |      23 |     73.913   |      21.7391 |      4.34783 |
| ageism      | negative      | male          |          8 |         10 |          14 |      32 |     25       |      31.25   |     43.75    |
| ageism      | negative      | female        |         10 |         17 |          12 |      39 |     25.641   |      43.5897 |     30.7692  |
| ageism      | negative      | not_spacified |         14 |          8 |          16 |      38 |     36.8421  |      21.0526 |     42.1053  |
| ableism     | negative      | male          |          1 |          3 |          10 |      14 |      7.14286 |      21.4286 |     71.4286  |
| ableism     | negative      | female        |          1 |          6 |           7 |      14 |      7.14286 |      42.8571 |     50       |
| ableism     | negative      | not_spacified |          0 |          4 |           2 |       6 |      0       |      66.6667 |     33.3333  |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         17 |         16 |          28 |      61 |      27.8689 |      26.2295 |      45.9016 |
| female        |         13 |         28 |          21 |      62 |      20.9677 |      45.1613 |      33.871  |
| not_spacified |         31 |         17 |          19 |      67 |      46.2687 |      25.3731 |      28.3582 |



## Kendall Tau Calculation

Total data: 529

Kendall's Tau Correlation for type 1: 0.10347304362119918

P-Value: 0.006521040621012089

Total data: 396

Kendall's Tau Correlation for type 2: 0.23362411998775634

P-Value: 1.617333626639482e-05

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 529

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.03596685260558675

P-Value: 0.24687755184586935

Total data: 396

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.03944750535659627

P-Value: 0.37291496116332734

