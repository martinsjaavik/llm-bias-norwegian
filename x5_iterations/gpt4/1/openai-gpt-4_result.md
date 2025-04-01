# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        111 |          3 |          24 |     138 |      80.4348 |      2.17391 |      17.3913 |
| ageism      | positive      |         59 |          1 |          11 |      71 |      83.0986 |      1.40845 |      15.493  |
| ableism     | positive      |         44 |          6 |          14 |      64 |      68.75   |      9.375   |      21.875  |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         91 |          9 |          22 |     122 |      74.5902 |      7.37705 |      18.0328 |
| ageism      | negative      |         44 |         11 |          15 |      70 |      62.8571 |     15.7143  |      21.4286 |
| ableism     | negative      |         43 |          4 |          18 |      65 |      66.1538 |      6.15385 |      27.6923 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        202 |         12 |          46 |     260 | 77.6923 | 4.61538 | 17.6923 |
| ageism      |        103 |         12 |          26 |     141 | 73.0496 | 8.51064 | 18.4397 |
| ableism     |         87 |         10 |          32 |     129 | 67.4419 | 7.75194 | 24.8062 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         44 |          4 |          15 |      63 |      69.8413 |      6.34921 |      23.8095 |
| ageism      | positive      |         46 |         13 |          51 |     110 |      41.8182 |     11.8182  |      46.3636 |
| ableism     | positive      |          4 |          7 |          22 |      33 |      12.1212 |     21.2121  |      66.6667 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         30 |         10 |           5 |      45 |      66.6667 |      22.2222 |      11.1111 |
| ageism      | negative      |         23 |         42 |          43 |     108 |      21.2963 |      38.8889 |      39.8148 |
| ableism     | negative      |          1 |         13 |          18 |      32 |       3.125  |      40.625  |      56.25   |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |       pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|---------:|--------:|--------:|
| nationality |         74 |         14 |          20 |     108 | 68.5185  | 12.963  | 18.5185 |
| ageism      |         69 |         55 |          94 |     218 | 31.6514  | 25.2294 | 43.1193 |
| ableism     |          5 |         20 |          40 |      65 |  7.69231 | 30.7692 | 61.5385 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         30 |          1 |           5 |      36 |      83.3333 |      2.77778 |     13.8889  |
| nationality | positive      | female        |         41 |          1 |          10 |      52 |      78.8462 |      1.92308 |     19.2308  |
| nationality | positive      | not_spacified |         40 |          1 |           9 |      50 |      80      |      2       |     18       |
| ageism      | positive      | male          |         24 |          1 |           5 |      30 |      80      |      3.33333 |     16.6667  |
| ageism      | positive      | female        |         11 |          0 |           1 |      12 |      91.6667 |      0       |      8.33333 |
| ageism      | positive      | not_spacified |         24 |          0 |           5 |      29 |      82.7586 |      0       |     17.2414  |
| ableism     | positive      | male          |         12 |          3 |           4 |      19 |      63.1579 |     15.7895  |     21.0526  |
| ableism     | positive      | female        |         15 |          0 |           6 |      21 |      71.4286 |      0       |     28.5714  |
| ableism     | positive      | not_spacified |         17 |          3 |           4 |      24 |      70.8333 |     12.5     |     16.6667  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         66 |          5 |          14 |      85 |      77.6471 |      5.88235 |      16.4706 |
| female        |         67 |          1 |          17 |      85 |      78.8235 |      1.17647 |      20      |
| not_spacified |         81 |          4 |          18 |     103 |      78.6408 |      3.8835  |      17.4757 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         25 |          3 |           7 |      35 |      71.4286 |      8.57143 |     20       |
| nationality | negative      | female        |         39 |          2 |           8 |      49 |      79.5918 |      4.08163 |     16.3265  |
| nationality | negative      | not_spacified |         27 |          4 |           7 |      38 |      71.0526 |     10.5263  |     18.4211  |
| ageism      | negative      | male          |         17 |          5 |           5 |      27 |      62.963  |     18.5185  |     18.5185  |
| ageism      | negative      | female        |         15 |          4 |           5 |      24 |      62.5    |     16.6667  |     20.8333  |
| ageism      | negative      | not_spacified |         12 |          2 |           5 |      19 |      63.1579 |     10.5263  |     26.3158  |
| ableism     | negative      | male          |          8 |          2 |           9 |      19 |      42.1053 |     10.5263  |     47.3684  |
| ableism     | negative      | female        |         19 |          1 |           8 |      28 |      67.8571 |      3.57143 |     28.5714  |
| ableism     | negative      | not_spacified |         16 |          1 |           1 |      18 |      88.8889 |      5.55556 |      5.55556 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         50 |         10 |          21 |      81 |      61.7284 |     12.3457  |      25.9259 |
| female        |         73 |          7 |          21 |     101 |      72.2772 |      6.93069 |      20.7921 |
| not_spacified |         55 |          7 |          13 |      75 |      73.3333 |      9.33333 |      17.3333 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         15 |          1 |           6 |      22 |      68.1818 |      4.54545 |     27.2727  |
| nationality | positive      | female        |         18 |          1 |           2 |      21 |      85.7143 |      4.7619  |      9.52381 |
| nationality | positive      | not_spacified |         11 |          2 |           7 |      20 |      55      |     10       |     35       |
| ageism      | positive      | male          |         11 |          4 |          18 |      33 |      33.3333 |     12.1212  |     54.5455  |
| ageism      | positive      | female        |         19 |          4 |          19 |      42 |      45.2381 |      9.52381 |     45.2381  |
| ageism      | positive      | not_spacified |         16 |          5 |          14 |      35 |      45.7143 |     14.2857  |     40       |
| ableism     | positive      | male          |          2 |          0 |          12 |      14 |      14.2857 |      0       |     85.7143  |
| ableism     | positive      | female        |          1 |          4 |           4 |       9 |      11.1111 |     44.4444  |     44.4444  |
| ableism     | positive      | not_spacified |          1 |          3 |           6 |      10 |      10      |     30       |     60       |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         28 |          5 |          36 |      69 |      40.5797 |      7.24638 |      52.1739 |
| female        |         38 |          9 |          25 |      72 |      52.7778 |     12.5     |      34.7222 |
| not_spacified |         28 |         10 |          27 |      65 |      43.0769 |     15.3846  |      41.5385 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          6 |          4 |           3 |      13 |     46.1538  |      30.7692 |     23.0769  |
| nationality | negative      | female        |          5 |          3 |           1 |       9 |     55.5556  |      33.3333 |     11.1111  |
| nationality | negative      | not_spacified |         19 |          3 |           1 |      23 |     82.6087  |      13.0435 |      4.34783 |
| ageism      | negative      | male          |          6 |         10 |          13 |      29 |     20.6897  |      34.4828 |     44.8276  |
| ageism      | negative      | female        |          6 |         19 |          13 |      38 |     15.7895  |      50      |     34.2105  |
| ageism      | negative      | not_spacified |         11 |         13 |          17 |      41 |     26.8293  |      31.7073 |     41.4634  |
| ableism     | negative      | male          |          0 |          3 |          10 |      13 |      0       |      23.0769 |     76.9231  |
| ableism     | negative      | female        |          1 |          7 |           5 |      13 |      7.69231 |      53.8462 |     38.4615  |
| ableism     | negative      | not_spacified |          0 |          3 |           3 |       6 |      0       |      50      |     50       |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         12 |         17 |          26 |      55 |      21.8182 |      30.9091 |      47.2727 |
| female        |         12 |         29 |          19 |      60 |      20      |      48.3333 |      31.6667 |
| not_spacified |         30 |         19 |          21 |      70 |      42.8571 |      27.1429 |      30      |



## Kendall Tau Calculation

Total data: 530

Kendall's Tau Correlation for type 1: 0.1001067995728017

P-Value: 0.009255119591982518

Total data: 391

Kendall's Tau Correlation for type 2: 0.27215939194536926

P-Value: 6.060691746206311e-07

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 530

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.04011391954432182

P-Value: 0.2015533641907531

Total data: 391

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.017111348041941116

P-Value: 0.701193465852787

