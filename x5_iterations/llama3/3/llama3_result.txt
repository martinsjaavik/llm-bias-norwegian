# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         58 |         36 |          25 |     119 |      48.7395 |      30.2521 |      21.0084 |
| ageism      | positive      |         31 |         18 |           9 |      58 |      53.4483 |      31.0345 |      15.5172 |
| ableism     | positive      |         17 |         22 |          17 |      56 |      30.3571 |      39.2857 |      30.3571 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         30 |         60 |          20 |     110 |      27.2727 |      54.5455 |     18.1818  |
| ageism      | negative      |         17 |         35 |           4 |      56 |      30.3571 |      62.5    |      7.14286 |
| ableism     | negative      |         10 |         34 |          12 |      56 |      17.8571 |      60.7143 |     21.4286  |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         88 |         96 |          45 |     229 | 38.4279 | 41.9214 | 19.6507 |
| ageism      |         48 |         53 |          13 |     114 | 42.1053 | 46.4912 | 11.4035 |
| ableism     |         27 |         56 |          29 |     112 | 24.1071 | 50      | 25.8929 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         34 |          9 |           8 |      51 |      66.6667 |      17.6471 |      15.6863 |
| ageism      | positive      |         23 |         53 |          32 |     108 |      21.2963 |      49.0741 |      29.6296 |
| ableism     | positive      |          3 |         13 |          10 |      26 |      11.5385 |      50      |      38.4615 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         24 |         25 |          10 |      59 |     40.678   |      42.3729 |      16.9492 |
| ageism      | negative      |         27 |         65 |          25 |     117 |     23.0769  |      55.5556 |      21.3675 |
| ableism     | negative      |          2 |         15 |           7 |      24 |      8.33333 |      62.5    |      29.1667 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         58 |         34 |          18 |     110 | 52.7273 | 30.9091 | 16.3636 |
| ageism      |         50 |        118 |          57 |     225 | 22.2222 | 52.4444 | 25.3333 |
| ableism     |          5 |         28 |          17 |      50 | 10      | 56      | 34      |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         12 |         12 |           9 |      33 |      36.3636 |      36.3636 |     27.2727  |
| nationality | positive      | female        |         26 |          9 |           8 |      43 |      60.4651 |      20.9302 |     18.6047  |
| nationality | positive      | not_spacified |         20 |         15 |           8 |      43 |      46.5116 |      34.8837 |     18.6047  |
| ageism      | positive      | male          |         13 |          6 |           3 |      22 |      59.0909 |      27.2727 |     13.6364  |
| ageism      | positive      | female        |          7 |          5 |           1 |      13 |      53.8462 |      38.4615 |      7.69231 |
| ageism      | positive      | not_spacified |         11 |          7 |           5 |      23 |      47.8261 |      30.4348 |     21.7391  |
| ableism     | positive      | male          |          3 |          8 |           7 |      18 |      16.6667 |      44.4444 |     38.8889  |
| ableism     | positive      | female        |          6 |          6 |           5 |      17 |      35.2941 |      35.2941 |     29.4118  |
| ableism     | positive      | not_spacified |          8 |          8 |           5 |      21 |      38.0952 |      38.0952 |     23.8095  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         28 |         26 |          19 |      73 |      38.3562 |      35.6164 |      26.0274 |
| female        |         39 |         20 |          14 |      73 |      53.4247 |      27.3973 |      19.1781 |
| not_spacified |         39 |         30 |          18 |      87 |      44.8276 |      34.4828 |      20.6897 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          6 |         22 |           7 |      35 |      17.1429 |      62.8571 |     20       |
| nationality | negative      | female        |         15 |         22 |           6 |      43 |      34.8837 |      51.1628 |     13.9535  |
| nationality | negative      | not_spacified |          9 |         16 |           7 |      32 |      28.125  |      50      |     21.875   |
| ageism      | negative      | male          |          6 |         12 |           3 |      21 |      28.5714 |      57.1429 |     14.2857  |
| ageism      | negative      | female        |          8 |         13 |           0 |      21 |      38.0952 |      61.9048 |      0       |
| ageism      | negative      | not_spacified |          3 |         10 |           1 |      14 |      21.4286 |      71.4286 |      7.14286 |
| ableism     | negative      | male          |          5 |         10 |           1 |      16 |      31.25   |      62.5    |      6.25    |
| ableism     | negative      | female        |          3 |         13 |           7 |      23 |      13.0435 |      56.5217 |     30.4348  |
| ableism     | negative      | not_spacified |          2 |         11 |           4 |      17 |      11.7647 |      64.7059 |     23.5294  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         17 |         44 |          11 |      72 |      23.6111 |      61.1111 |      15.2778 |
| female        |         26 |         48 |          13 |      87 |      29.8851 |      55.1724 |      14.9425 |
| not_spacified |         14 |         37 |          12 |      63 |      22.2222 |      58.7302 |      19.0476 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         11 |          2 |           3 |      16 |     68.75    |      12.5    |     18.75    |
| nationality | positive      | female        |         11 |          3 |           4 |      18 |     61.1111  |      16.6667 |     22.2222  |
| nationality | positive      | not_spacified |         12 |          4 |           1 |      17 |     70.5882  |      23.5294 |      5.88235 |
| ageism      | positive      | male          |          2 |         20 |          10 |      32 |      6.25    |      62.5    |     31.25    |
| ageism      | positive      | female        |          9 |         16 |          16 |      41 |     21.9512  |      39.0244 |     39.0244  |
| ageism      | positive      | not_spacified |         12 |         17 |           6 |      35 |     34.2857  |      48.5714 |     17.1429  |
| ableism     | positive      | male          |          1 |          6 |           4 |      11 |      9.09091 |      54.5455 |     36.3636  |
| ableism     | positive      | female        |          0 |          4 |           3 |       7 |      0       |      57.1429 |     42.8571  |
| ableism     | positive      | not_spacified |          2 |          3 |           3 |       8 |     25       |      37.5    |     37.5     |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         14 |         28 |          17 |      59 |      23.7288 |      47.4576 |      28.8136 |
| female        |         20 |         23 |          23 |      66 |      30.303  |      34.8485 |      34.8485 |
| not_spacified |         26 |         24 |          10 |      60 |      43.3333 |      40      |      16.6667 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          6 |          8 |           4 |      18 |      33.3333 |      44.4444 |      22.2222 |
| nationality | negative      | female        |          8 |          8 |           3 |      19 |      42.1053 |      42.1053 |      15.7895 |
| nationality | negative      | not_spacified |         10 |          9 |           3 |      22 |      45.4545 |      40.9091 |      13.6364 |
| ageism      | negative      | male          |          5 |         20 |           8 |      33 |      15.1515 |      60.6061 |      24.2424 |
| ageism      | negative      | female        |         11 |         22 |           9 |      42 |      26.1905 |      52.381  |      21.4286 |
| ageism      | negative      | not_spacified |         11 |         23 |           8 |      42 |      26.1905 |      54.7619 |      19.0476 |
| ableism     | negative      | male          |          0 |          5 |           2 |       7 |       0      |      71.4286 |      28.5714 |
| ableism     | negative      | female        |          1 |          5 |           3 |       9 |      11.1111 |      55.5556 |      33.3333 |
| ableism     | negative      | not_spacified |          1 |          5 |           2 |       8 |      12.5    |      62.5    |      25      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         11 |         33 |          14 |      58 |      18.9655 |      56.8966 |      24.1379 |
| female        |         20 |         35 |          15 |      70 |      28.5714 |      50      |      21.4286 |
| not_spacified |         22 |         37 |          13 |      72 |      30.5556 |      51.3889 |      18.0556 |



## Kendall Tau Calculation

Total data: 455

Kendall's Tau Correlation for type 1: 0.2723149378094433

P-Value: 5.507184100234729e-08

Total data: 385

Kendall's Tau Correlation for type 2: 0.11590487434643279

P-Value: 0.0336666356882146

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 455

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.05997826349474702

P-Value: 0.14268440987339753

Total data: 385

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.06808568055321301

P-Value: 0.1264948110008616

