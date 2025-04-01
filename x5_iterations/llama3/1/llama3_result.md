# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         49 |         58 |          23 |     130 |      37.6923 |      44.6154 |      17.6923 |
| ageism      | positive      |         31 |         29 |          10 |      70 |      44.2857 |      41.4286 |      14.2857 |
| ableism     | positive      |         11 |         36 |          13 |      60 |      18.3333 |      60      |      21.6667 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         26 |         65 |          24 |     115 |      22.6087 |      56.5217 |      20.8696 |
| ageism      | negative      |         18 |         40 |          15 |      73 |      24.6575 |      54.7945 |      20.5479 |
| ableism     | negative      |          8 |         39 |          19 |      66 |      12.1212 |      59.0909 |      28.7879 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         75 |        123 |          47 |     245 | 30.6122 | 50.2041 | 19.1837 |
| ageism      |         49 |         69 |          25 |     143 | 34.2657 | 48.2517 | 17.4825 |
| ableism     |         19 |         75 |          32 |     126 | 15.0794 | 59.5238 | 25.3968 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         43 |          7 |          15 |      65 |      66.1538 |      10.7692 |      23.0769 |
| ageism      | positive      |         28 |         52 |          34 |     114 |      24.5614 |      45.614  |      29.8246 |
| ableism     | positive      |         10 |          9 |           9 |      28 |      35.7143 |      32.1429 |      32.1429 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         22 |         39 |          11 |      72 |      30.5556 |      54.1667 |     15.2778  |
| ageism      | negative      |         20 |         70 |          29 |     119 |      16.8067 |      58.8235 |     24.3697  |
| ableism     | negative      |          9 |         16 |           2 |      27 |      33.3333 |      59.2593 |      7.40741 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         65 |         46 |          26 |     137 | 47.4453 | 33.5766 | 18.9781 |
| ageism      |         48 |        122 |          63 |     233 | 20.6009 | 52.3605 | 27.0386 |
| ableism     |         19 |         25 |          11 |      55 | 34.5455 | 45.4545 | 20      |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         10 |         20 |           5 |      35 |      28.5714 |      57.1429 |      14.2857 |
| nationality | positive      | female        |         20 |         21 |          11 |      52 |      38.4615 |      40.3846 |      21.1538 |
| nationality | positive      | not_spacified |         19 |         17 |           7 |      43 |      44.186  |      39.5349 |      16.2791 |
| ageism      | positive      | male          |         16 |         11 |           3 |      30 |      53.3333 |      36.6667 |      10      |
| ageism      | positive      | female        |          6 |          5 |           3 |      14 |      42.8571 |      35.7143 |      21.4286 |
| ageism      | positive      | not_spacified |          9 |         13 |           4 |      26 |      34.6154 |      50      |      15.3846 |
| ableism     | positive      | male          |          5 |         10 |           3 |      18 |      27.7778 |      55.5556 |      16.6667 |
| ableism     | positive      | female        |          2 |         11 |           7 |      20 |      10      |      55      |      35      |
| ableism     | positive      | not_spacified |          4 |         15 |           3 |      22 |      18.1818 |      68.1818 |      13.6364 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         31 |         41 |          11 |      83 |      37.3494 |      49.3976 |      13.253  |
| female        |         28 |         37 |          21 |      86 |      32.5581 |      43.0233 |      24.4186 |
| not_spacified |         32 |         45 |          14 |      91 |      35.1648 |      49.4505 |      15.3846 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          8 |         24 |           5 |      37 |     21.6216  |      64.8649 |      13.5135 |
| nationality | negative      | female        |         12 |         23 |           9 |      44 |     27.2727  |      52.2727 |      20.4545 |
| nationality | negative      | not_spacified |          6 |         18 |          10 |      34 |     17.6471  |      52.9412 |      29.4118 |
| ageism      | negative      | male          |          5 |         15 |           6 |      26 |     19.2308  |      57.6923 |      23.0769 |
| ageism      | negative      | female        |          7 |         12 |           6 |      25 |     28       |      48      |      24      |
| ageism      | negative      | not_spacified |          6 |         13 |           3 |      22 |     27.2727  |      59.0909 |      13.6364 |
| ableism     | negative      | male          |          3 |         12 |           4 |      19 |     15.7895  |      63.1579 |      21.0526 |
| ableism     | negative      | female        |          4 |         13 |          11 |      28 |     14.2857  |      46.4286 |      39.2857 |
| ableism     | negative      | not_spacified |          1 |         14 |           4 |      19 |      5.26316 |      73.6842 |      21.0526 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         16 |         51 |          15 |      82 |      19.5122 |      62.1951 |      18.2927 |
| female        |         23 |         48 |          26 |      97 |      23.7113 |      49.4845 |      26.8041 |
| not_spacified |         13 |         45 |          17 |      75 |      17.3333 |      60      |      22.6667 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         13 |          3 |           7 |      23 |      56.5217 |     13.0435  |      30.4348 |
| nationality | positive      | female        |         16 |          1 |           5 |      22 |      72.7273 |      4.54545 |      22.7273 |
| nationality | positive      | not_spacified |         14 |          3 |           3 |      20 |      70      |     15       |      15      |
| ageism      | positive      | male          |          5 |         20 |           8 |      33 |      15.1515 |     60.6061  |      24.2424 |
| ageism      | positive      | female        |         12 |         14 |          17 |      43 |      27.907  |     32.5581  |      39.5349 |
| ageism      | positive      | not_spacified |         11 |         18 |           9 |      38 |      28.9474 |     47.3684  |      23.6842 |
| ableism     | positive      | male          |          6 |          3 |           4 |      13 |      46.1538 |     23.0769  |      30.7692 |
| ableism     | positive      | female        |          2 |          3 |           1 |       6 |      33.3333 |     50       |      16.6667 |
| ableism     | positive      | not_spacified |          2 |          3 |           4 |       9 |      22.2222 |     33.3333  |      44.4444 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         24 |         26 |          19 |      69 |      34.7826 |      37.6812 |      27.5362 |
| female        |         30 |         18 |          23 |      71 |      42.2535 |      25.3521 |      32.3944 |
| not_spacified |         27 |         24 |          16 |      67 |      40.2985 |      35.8209 |      23.8806 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          8 |         12 |           5 |      25 |     32       |      48      |     20       |
| nationality | negative      | female        |          5 |         11 |           4 |      20 |     25       |      55      |     20       |
| nationality | negative      | not_spacified |          9 |         16 |           2 |      27 |     33.3333  |      59.2593 |      7.40741 |
| ageism      | negative      | male          |          3 |         26 |           6 |      35 |      8.57143 |      74.2857 |     17.1429  |
| ageism      | negative      | female        |          8 |         23 |          12 |      43 |     18.6047  |      53.4884 |     27.907   |
| ageism      | negative      | not_spacified |          9 |         21 |          11 |      41 |     21.9512  |      51.2195 |     26.8293  |
| ableism     | negative      | male          |          4 |          7 |           2 |      13 |     30.7692  |      53.8462 |     15.3846  |
| ableism     | negative      | female        |          3 |          6 |           0 |       9 |     33.3333  |      66.6667 |      0       |
| ableism     | negative      | not_spacified |          2 |          3 |           0 |       5 |     40       |      60      |      0       |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         15 |         45 |          13 |      73 |      20.5479 |      61.6438 |      17.8082 |
| female        |         16 |         40 |          16 |      72 |      22.2222 |      55.5556 |      22.2222 |
| not_spacified |         20 |         40 |          13 |      73 |      27.3973 |      54.7945 |      17.8082 |



## Kendall Tau Calculation

Total data: 514

Kendall's Tau Correlation for type 1: 0.13753425487138338

P-Value: 0.0030631578594048393

Total data: 425

Kendall's Tau Correlation for type 2: 0.254560553633218

P-Value: 1.0231902381245873e-06

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 514

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.044160396069584704

P-Value: 0.24404185005599188

Total data: 425

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.060224221453287194

P-Value: 0.15690733631165432

