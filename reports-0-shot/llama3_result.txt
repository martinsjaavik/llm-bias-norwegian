# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         17 |         19 |           3 |      39 |      43.5897 |      48.7179 |      7.69231 |
| ageism      | positive      |         15 |          5 |           7 |      27 |      55.5556 |      18.5185 |     25.9259  |
| ableism     | positive      |          4 |         10 |           8 |      22 |      18.1818 |      45.4545 |     36.3636  |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |          8 |         25 |          12 |      45 |      17.7778 |      55.5556 |      26.6667 |
| ageism      | negative      |          3 |         10 |           5 |      18 |      16.6667 |      55.5556 |      27.7778 |
| ableism     | negative      |          4 |         10 |           8 |      22 |      18.1818 |      45.4545 |      36.3636 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         25 |         44 |          15 |      84 | 29.7619 | 52.381  | 17.8571 |
| ageism      |         18 |         15 |          12 |      45 | 40      | 33.3333 | 26.6667 |
| ableism     |          8 |         20 |          16 |      44 | 18.1818 | 45.4545 | 36.3636 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         13 |          2 |           1 |      16 |      81.25   |      12.5    |       6.25   |
| ageism      | positive      |          6 |         23 |           8 |      37 |      16.2162 |      62.1622 |      21.6216 |
| ableism     | positive      |          3 |          2 |           5 |      10 |      30      |      20      |      50      |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |          5 |         11 |           4 |      20 |     25       |      55      |      20      |
| ageism      | negative      |          3 |         25 |           9 |      37 |      8.10811 |      67.5676 |      24.3243 |
| ableism     | negative      |          3 |          2 |           5 |      10 |     30       |      20      |      50      |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         18 |         13 |           5 |      36 | 50      | 36.1111 | 13.8889 |
| ageism      |          9 |         48 |          17 |      74 | 12.1622 | 64.8649 | 22.973  |
| ableism     |          6 |          4 |          10 |      20 | 30      | 20      | 50      |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          2 |          6 |           0 |       8 |      25      |      75      |      0       |
| nationality | positive      | female        |          7 |          5 |           2 |      14 |      50      |      35.7143 |     14.2857  |
| nationality | positive      | not_spacified |          8 |          8 |           1 |      17 |      47.0588 |      47.0588 |      5.88235 |
| ageism      | positive      | male          |          9 |          3 |           3 |      15 |      60      |      20      |     20       |
| ageism      | positive      | female        |          1 |          1 |           3 |       5 |      20      |      20      |     60       |
| ageism      | positive      | not_spacified |          5 |          1 |           1 |       7 |      71.4286 |      14.2857 |     14.2857  |
| ableism     | positive      | male          |          1 |          1 |           2 |       4 |      25      |      25      |     50       |
| ableism     | positive      | female        |          2 |          3 |           3 |       8 |      25      |      37.5    |     37.5     |
| ableism     | positive      | not_spacified |          1 |          6 |           3 |      10 |      10      |      60      |     30       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         12 |         10 |           5 |      27 |      44.4444 |      37.037  |      18.5185 |
| female        |         10 |          9 |           8 |      27 |      37.037  |      33.3333 |      29.6296 |
| not_spacified |         14 |         15 |           5 |      34 |      41.1765 |      44.1176 |      14.7059 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          3 |          8 |           4 |      15 |      20      |      53.3333 |      26.6667 |
| nationality | negative      | female        |          2 |         10 |           3 |      15 |      13.3333 |      66.6667 |      20      |
| nationality | negative      | not_spacified |          3 |          7 |           5 |      15 |      20      |      46.6667 |      33.3333 |
| ageism      | negative      | male          |          1 |          3 |           1 |       5 |      20      |      60      |      20      |
| ageism      | negative      | female        |          1 |          2 |           2 |       5 |      20      |      40      |      40      |
| ageism      | negative      | not_spacified |          1 |          5 |           2 |       8 |      12.5    |      62.5    |      25      |
| ableism     | negative      | male          |          3 |          2 |           2 |       7 |      42.8571 |      28.5714 |      28.5714 |
| ableism     | negative      | female        |          1 |          3 |           2 |       6 |      16.6667 |      50      |      33.3333 |
| ableism     | negative      | not_spacified |          2 |          3 |           1 |       6 |      33.3333 |      50      |      16.6667 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          7 |         13 |           7 |      27 |      25.9259 |      48.1481 |      25.9259 |
| female        |          4 |         15 |           7 |      26 |      15.3846 |      57.6923 |      26.9231 |
| not_spacified |          6 |         15 |           8 |      29 |      20.6897 |      51.7241 |      27.5862 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          4 |          0 |           0 |       4 |    100       |       0      |       0      |
| nationality | positive      | female        |          6 |          0 |           1 |       7 |     85.7143  |       0      |      14.2857 |
| nationality | positive      | not_spacified |          3 |          2 |           0 |       5 |     60       |      40      |       0      |
| ageism      | positive      | male          |          1 |          6 |           1 |       8 |     12.5     |      75      |      12.5    |
| ageism      | positive      | female        |          4 |         10 |           3 |      17 |     23.5294  |      58.8235 |      17.6471 |
| ageism      | positive      | not_spacified |          1 |          7 |           4 |      12 |      8.33333 |      58.3333 |      33.3333 |
| ableism     | positive      | male          |          0 |          1 |           2 |       3 |      0       |      33.3333 |      66.6667 |
| ableism     | positive      | female        |          2 |          1 |           1 |       4 |     50       |      25      |      25      |
| ableism     | positive      | not_spacified |          1 |          0 |           2 |       3 |     33.3333  |       0      |      66.6667 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          5 |          7 |           3 |      15 |      33.3333 |      46.6667 |      20      |
| female        |         12 |         11 |           5 |      28 |      42.8571 |      39.2857 |      17.8571 |
| not_spacified |          5 |          9 |           6 |      20 |      25      |      45      |      30      |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          1 |          4 |           2 |       7 |     14.2857  |      57.1429 |      28.5714 |
| nationality | negative      | female        |          0 |          4 |           2 |       6 |      0       |      66.6667 |      33.3333 |
| nationality | negative      | not_spacified |          4 |          3 |           0 |       7 |     57.1429  |      42.8571 |       0      |
| ageism      | negative      | male          |          2 |          9 |           2 |      13 |     15.3846  |      69.2308 |      15.3846 |
| ageism      | negative      | female        |          1 |          8 |           5 |      14 |      7.14286 |      57.1429 |      35.7143 |
| ageism      | negative      | not_spacified |          0 |          8 |           2 |      10 |      0       |      80      |      20      |
| ableism     | negative      | male          |          0 |          4 |           1 |       5 |      0       |      80      |      20      |
| ableism     | negative      | female        |          1 |          2 |           1 |       4 |     25       |      50      |      25      |
| ableism     | negative      | not_spacified |          0 |          2 |           0 |       2 |      0       |     100      |       0      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          3 |         17 |           5 |      25 |     12       |      68      |      20      |
| female        |          2 |         14 |           8 |      24 |      8.33333 |      58.3333 |      33.3333 |
| not_spacified |          4 |         13 |           2 |      19 |     21.0526  |      68.4211 |      10.5263 |



## Kendall Tau Calculation

Total data: 178

Kendall's Tau Correlation for type 1: 0.20123721752304002

P-Value: 0.013032767532368743

Total data: 136

Kendall's Tau Correlation for type 2: 0.2584342560553633

P-Value: 0.004280494438910563

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 178

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.0386314859234945

P-Value: 0.5592943750692888

Total data: 136

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.08482915224913495

P-Value: 0.24913710025043956

