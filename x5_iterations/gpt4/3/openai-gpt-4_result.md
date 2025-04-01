# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        110 |          1 |          25 |     136 |      80.8824 |     0.735294 |      18.3824 |
| ageism      | positive      |         54 |          0 |          15 |      69 |      78.2609 |     0        |      21.7391 |
| ableism     | positive      |         47 |          3 |          15 |      65 |      72.3077 |     4.61538  |      23.0769 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         92 |          6 |          25 |     123 |      74.7967 |      4.87805 |      20.3252 |
| ageism      | negative      |         40 |         13 |          14 |      67 |      59.7015 |     19.403   |      20.8955 |
| ableism     | negative      |         42 |          5 |          21 |      68 |      61.7647 |      7.35294 |      30.8824 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        202 |          7 |          50 |     259 | 77.9923 | 2.7027  | 19.305  |
| ageism      |         94 |         13 |          29 |     136 | 69.1176 | 9.55882 | 21.3235 |
| ableism     |         89 |          8 |          36 |     133 | 66.9173 | 6.01504 | 27.0677 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         47 |          4 |          10 |      61 |      77.0492 |      6.55738 |      16.3934 |
| ageism      | positive      |         44 |         18 |          43 |     105 |      41.9048 |     17.1429  |      40.9524 |
| ableism     | positive      |          6 |         10 |          17 |      33 |      18.1818 |     30.303   |      51.5152 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         26 |         14 |           4 |      44 |      59.0909 |      31.8182 |      9.09091 |
| ageism      | negative      |         33 |         44 |          35 |     112 |      29.4643 |      39.2857 |     31.25    |
| ableism     | negative      |          4 |         15 |          17 |      36 |      11.1111 |      41.6667 |     47.2222  |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         73 |         18 |          14 |     105 | 69.5238 | 17.1429 | 13.3333 |
| ageism      |         77 |         62 |          78 |     217 | 35.4839 | 28.5714 | 35.9447 |
| ableism     |         10 |         25 |          34 |      69 | 14.4928 | 36.2319 | 49.2754 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         30 |          1 |           5 |      36 |      83.3333 |      2.77778 |     13.8889  |
| nationality | positive      | female        |         43 |          0 |           8 |      51 |      84.3137 |      0       |     15.6863  |
| nationality | positive      | not_spacified |         37 |          0 |          12 |      49 |      75.5102 |      0       |     24.4898  |
| ageism      | positive      | male          |         19 |          0 |           7 |      26 |      73.0769 |      0       |     26.9231  |
| ageism      | positive      | female        |         13 |          0 |           1 |      14 |      92.8571 |      0       |      7.14286 |
| ageism      | positive      | not_spacified |         22 |          0 |           7 |      29 |      75.8621 |      0       |     24.1379  |
| ableism     | positive      | male          |         12 |          2 |           5 |      19 |      63.1579 |     10.5263  |     26.3158  |
| ableism     | positive      | female        |         18 |          0 |           3 |      21 |      85.7143 |      0       |     14.2857  |
| ableism     | positive      | not_spacified |         17 |          1 |           7 |      25 |      68      |      4       |     28       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         61 |          3 |          17 |      81 |      75.3086 |     3.7037   |      20.9877 |
| female        |         74 |          0 |          12 |      86 |      86.0465 |     0        |      13.9535 |
| not_spacified |         76 |          1 |          26 |     103 |      73.7864 |     0.970874 |      25.2427 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         23 |          1 |          12 |      36 |      63.8889 |      2.77778 |     33.3333  |
| nationality | negative      | female        |         39 |          2 |           8 |      49 |      79.5918 |      4.08163 |     16.3265  |
| nationality | negative      | not_spacified |         30 |          3 |           5 |      38 |      78.9474 |      7.89474 |     13.1579  |
| ageism      | negative      | male          |         19 |          5 |           2 |      26 |      73.0769 |     19.2308  |      7.69231 |
| ageism      | negative      | female        |         13 |          2 |           6 |      21 |      61.9048 |      9.52381 |     28.5714  |
| ageism      | negative      | not_spacified |          8 |          6 |           6 |      20 |      40      |     30       |     30       |
| ableism     | negative      | male          |         10 |          1 |           8 |      19 |      52.6316 |      5.26316 |     42.1053  |
| ableism     | negative      | female        |         20 |          3 |           7 |      30 |      66.6667 |     10       |     23.3333  |
| ableism     | negative      | not_spacified |         12 |          1 |           6 |      19 |      63.1579 |      5.26316 |     31.5789  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         52 |          7 |          22 |      81 |      64.1975 |      8.64198 |      27.1605 |
| female        |         72 |          7 |          21 |     100 |      72      |      7       |      21      |
| not_spacified |         50 |         10 |          17 |      77 |      64.9351 |     12.987   |      22.0779 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         17 |          1 |           2 |      20 |      85      |       5      |      10      |
| nationality | positive      | female        |         16 |          1 |           4 |      21 |      76.1905 |       4.7619 |      19.0476 |
| nationality | positive      | not_spacified |         14 |          2 |           4 |      20 |      70      |      10      |      20      |
| ageism      | positive      | male          |         12 |          4 |          14 |      30 |      40      |      13.3333 |      46.6667 |
| ageism      | positive      | female        |         15 |          7 |          19 |      41 |      36.5854 |      17.0732 |      46.3415 |
| ageism      | positive      | not_spacified |         17 |          7 |          10 |      34 |      50      |      20.5882 |      29.4118 |
| ableism     | positive      | male          |          3 |          4 |           7 |      14 |      21.4286 |      28.5714 |      50      |
| ableism     | positive      | female        |          2 |          3 |           4 |       9 |      22.2222 |      33.3333 |      44.4444 |
| ableism     | positive      | not_spacified |          1 |          3 |           6 |      10 |      10      |      30      |      60      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         32 |          9 |          23 |      64 |      50      |      14.0625 |      35.9375 |
| female        |         33 |         11 |          27 |      71 |      46.4789 |      15.493  |      38.0282 |
| not_spacified |         32 |         12 |          20 |      64 |      50      |      18.75   |      31.25   |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          5 |          5 |           2 |      12 |     41.6667  |      41.6667 |      16.6667 |
| nationality | negative      | female        |          3 |          3 |           1 |       7 |     42.8571  |      42.8571 |      14.2857 |
| nationality | negative      | not_spacified |         18 |          6 |           1 |      25 |     72       |      24      |       4      |
| ageism      | negative      | male          |          8 |         13 |          11 |      32 |     25       |      40.625  |      34.375  |
| ageism      | negative      | female        |          9 |         17 |          14 |      40 |     22.5     |      42.5    |      35      |
| ageism      | negative      | not_spacified |         16 |         14 |          10 |      40 |     40       |      35      |      25      |
| ableism     | negative      | male          |          3 |          4 |           8 |      15 |     20       |      26.6667 |      53.3333 |
| ableism     | negative      | female        |          1 |          8 |           5 |      14 |      7.14286 |      57.1429 |      35.7143 |
| ableism     | negative      | not_spacified |          0 |          3 |           4 |       7 |      0       |      42.8571 |      57.1429 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         16 |         22 |          21 |      59 |      27.1186 |      37.2881 |      35.5932 |
| female        |         13 |         28 |          20 |      61 |      21.3115 |      45.9016 |      32.7869 |
| not_spacified |         34 |         23 |          15 |      72 |      47.2222 |      31.9444 |      20.8333 |



## Kendall Tau Calculation

Total data: 528

Kendall's Tau Correlation for type 1: 0.1225034435261708

P-Value: 0.001688269942122868

Total data: 391

Kendall's Tau Correlation for type 2: 0.246073743630667

P-Value: 7.10710602612666e-06

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 528

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.06101497933884298

P-Value: 0.055336346409656546

Total data: 391

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.03881450278321047

P-Value: 0.3856137260190782

