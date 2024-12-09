# Report for Model: gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         27 |          0 |           4 |      31 |      87.0968 |      0       |      12.9032 |
| ageism      | positive      |         20 |          0 |           3 |      23 |      86.9565 |      0       |      13.0435 |
| ableism     | positive      |         12 |          1 |           4 |      17 |      70.5882 |      5.88235 |      23.5294 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         30 |          1 |           8 |      39 |      76.9231 |      2.5641  |      20.5128 |
| ageism      | negative      |          7 |          3 |           4 |      14 |      50      |     21.4286  |      28.5714 |
| ableism     | negative      |         12 |          1 |           4 |      17 |      70.5882 |      5.88235 |      23.5294 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         57 |          1 |          12 |      70 | 81.4286 | 1.42857 | 17.1429 |
| ageism      |         27 |          3 |           7 |      37 | 72.973  | 8.10811 | 18.9189 |
| ableism     |         24 |          2 |           8 |      34 | 70.5882 | 5.88235 | 23.5294 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         10 |          1 |           3 |      14 |      71.4286 |      7.14286 |      21.4286 |
| ageism      | positive      |         12 |          2 |          16 |      30 |      40      |      6.66667 |      53.3333 |
| ableism     | positive      |          1 |          1 |           7 |       9 |      11.1111 |     11.1111  |      77.7778 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |          6 |          6 |           2 |      14 |      42.8571 |      42.8571 |      14.2857 |
| ageism      | negative      |          5 |         12 |          15 |      32 |      15.625  |      37.5    |      46.875  |
| ableism     | negative      |          1 |          1 |           7 |       9 |      11.1111 |      11.1111 |      77.7778 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         16 |          7 |           5 |      28 | 57.1429 | 25      | 17.8571 |
| ageism      |         17 |         14 |          31 |      62 | 27.4194 | 22.5806 | 50      |
| ableism     |          2 |          2 |          14 |      18 | 11.1111 | 11.1111 | 77.7778 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          6 |          0 |           0 |       6 |     100      |       0      |       0      |
| nationality | positive      | female        |          9 |          0 |           1 |      10 |      90      |       0      |      10      |
| nationality | positive      | not_spacified |         12 |          0 |           3 |      15 |      80      |       0      |      20      |
| ageism      | positive      | male          |         10 |          0 |           3 |      13 |      76.9231 |       0      |      23.0769 |
| ageism      | positive      | female        |          5 |          0 |           0 |       5 |     100      |       0      |       0      |
| ageism      | positive      | not_spacified |          5 |          0 |           0 |       5 |     100      |       0      |       0      |
| ableism     | positive      | male          |          1 |          0 |           0 |       1 |     100      |       0      |       0      |
| ableism     | positive      | female        |          6 |          0 |           1 |       7 |      85.7143 |       0      |      14.2857 |
| ableism     | positive      | not_spacified |          5 |          1 |           3 |       9 |      55.5556 |      11.1111 |      33.3333 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         17 |          0 |           3 |      20 |      85      |      0       |     15       |
| female        |         20 |          0 |           2 |      22 |      90.9091 |      0       |      9.09091 |
| not_spacified |         22 |          1 |           6 |      29 |      75.8621 |      3.44828 |     20.6897  |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          9 |          0 |           4 |      13 |      69.2308 |      0       |     30.7692  |
| nationality | negative      | female        |          9 |          1 |           3 |      13 |      69.2308 |      7.69231 |     23.0769  |
| nationality | negative      | not_spacified |         12 |          0 |           1 |      13 |      92.3077 |      0       |      7.69231 |
| ageism      | negative      | male          |          1 |          1 |           1 |       3 |      33.3333 |     33.3333  |     33.3333  |
| ageism      | negative      | female        |          2 |          0 |           2 |       4 |      50      |      0       |     50       |
| ageism      | negative      | not_spacified |          4 |          2 |           1 |       7 |      57.1429 |     28.5714  |     14.2857  |
| ableism     | negative      | male          |          2 |          1 |           2 |       5 |      40      |     20       |     40       |
| ableism     | negative      | female        |          3 |          0 |           2 |       5 |      60      |      0       |     40       |
| ableism     | negative      | not_spacified |          4 |          0 |           1 |       5 |      80      |      0       |     20       |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         12 |          2 |           7 |      21 |      57.1429 |      9.52381 |      33.3333 |
| female        |         14 |          1 |           7 |      22 |      63.6364 |      4.54545 |      31.8182 |
| not_spacified |         20 |          2 |           3 |      25 |      80      |      8       |      12      |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          2 |          0 |           0 |       2 |     100      |      0       |       0      |
| nationality | positive      | female        |          5 |          1 |           2 |       8 |      62.5    |     12.5     |      25      |
| nationality | positive      | not_spacified |          3 |          0 |           1 |       4 |      75      |      0       |      25      |
| ageism      | positive      | male          |          2 |          0 |           5 |       7 |      28.5714 |      0       |      71.4286 |
| ageism      | positive      | female        |          5 |          1 |           7 |      13 |      38.4615 |      7.69231 |      53.8462 |
| ageism      | positive      | not_spacified |          5 |          1 |           4 |      10 |      50      |     10       |      40      |
| ableism     | positive      | male          |          0 |          1 |           1 |       2 |       0      |     50       |      50      |
| ableism     | positive      | female        |          1 |          0 |           4 |       5 |      20      |      0       |      80      |
| ableism     | positive      | not_spacified |          0 |          0 |           2 |       2 |       0      |      0       |     100      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          4 |          1 |           6 |      11 |      36.3636 |      9.09091 |      54.5455 |
| female        |         11 |          2 |          13 |      26 |      42.3077 |      7.69231 |      50      |
| not_spacified |          8 |          1 |           7 |      16 |      50      |      6.25    |      43.75   |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          0 |          3 |           0 |       3 |      0       |     100      |       0      |
| nationality | negative      | female        |          1 |          1 |           2 |       4 |     25       |      25      |      50      |
| nationality | negative      | not_spacified |          5 |          2 |           0 |       7 |     71.4286  |      28.5714 |       0      |
| ageism      | negative      | male          |          1 |          4 |           7 |      12 |      8.33333 |      33.3333 |      58.3333 |
| ageism      | negative      | female        |          1 |          6 |           5 |      12 |      8.33333 |      50      |      41.6667 |
| ageism      | negative      | not_spacified |          3 |          2 |           3 |       8 |     37.5     |      25      |      37.5    |
| ableism     | negative      | male          |          0 |          3 |           3 |       6 |      0       |      50      |      50      |
| ableism     | negative      | female        |          0 |          2 |           2 |       4 |      0       |      50      |      50      |
| ableism     | negative      | not_spacified |          0 |          1 |           1 |       2 |      0       |      50      |      50      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          1 |         10 |          10 |      21 |       4.7619 |      47.619  |      47.619  |
| female        |          2 |          9 |           9 |      20 |      10      |      45      |      45      |
| not_spacified |          8 |          5 |           4 |      17 |      47.0588 |      29.4118 |      23.5294 |



## Kendall Tau Calculation

Total data: 139

Kendall's Tau Correlation for type 1: 0.16231043941824957

P-Value: 0.027402818680993712

Total data: 111

Kendall's Tau Correlation for type 2: 0.41652463274084894

P-Value: 4.862993526289756e-05

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 139

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.042854924693338854

P-Value: 0.47457588039028065

Total data: 111

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.079863647431215

P-Value: 0.33787032658814764

