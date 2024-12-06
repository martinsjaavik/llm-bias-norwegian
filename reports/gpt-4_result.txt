# Report for Model: gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         35 |          0 |           5 |      40 |      87.5    |      0       |      12.5    |
| ageism      | positive      |         22 |          0 |           7 |      29 |      75.8621 |      0       |      24.1379 |
| ableism     | positive      |         16 |          2 |           5 |      23 |      69.5652 |      8.69565 |      21.7391 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         33 |          3 |          11 |      47 |      70.2128 |      6.38298 |      23.4043 |
| ageism      | negative      |         11 |          3 |           4 |      18 |      61.1111 |     16.6667  |      22.2222 |
| ableism     | negative      |         16 |          2 |           5 |      23 |      69.5652 |      8.69565 |      21.7391 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         68 |          3 |          16 |      87 | 78.1609 | 3.44828 | 18.3908 |
| ageism      |         33 |          3 |          11 |      47 | 70.2128 | 6.38298 | 23.4043 |
| ableism     |         32 |          4 |          10 |      46 | 69.5652 | 8.69565 | 21.7391 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         12 |          2 |           3 |      17 |     70.5882  |     11.7647  |      17.6471 |
| ageism      | positive      |         13 |          4 |          20 |      37 |     35.1351  |     10.8108  |      54.0541 |
| ableism     | positive      |          1 |          1 |           9 |      11 |      9.09091 |      9.09091 |      81.8182 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         10 |          6 |           3 |      19 |     52.6316  |     31.5789  |      15.7895 |
| ageism      | negative      |         10 |         15 |          12 |      37 |     27.027   |     40.5405  |      32.4324 |
| ableism     | negative      |          1 |          1 |           9 |      11 |      9.09091 |      9.09091 |      81.8182 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |       pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|---------:|---------:|--------:|
| nationality |         22 |          8 |           6 |      36 | 61.1111  | 22.2222  | 16.6667 |
| ageism      |         23 |         19 |          32 |      74 | 31.0811  | 25.6757  | 43.2432 |
| ableism     |          2 |          2 |          18 |      22 |  9.09091 |  9.09091 | 81.8182 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          8 |          0 |           1 |       9 |      88.8889 |          0   |     11.1111  |
| nationality | positive      | female        |         13 |          0 |           1 |      14 |      92.8571 |          0   |      7.14286 |
| nationality | positive      | not_spacified |         14 |          0 |           3 |      17 |      82.3529 |          0   |     17.6471  |
| ageism      | positive      | male          |         10 |          0 |           6 |      16 |      62.5    |          0   |     37.5     |
| ageism      | positive      | female        |          5 |          0 |           0 |       5 |     100      |          0   |      0       |
| ageism      | positive      | not_spacified |          7 |          0 |           1 |       8 |      87.5    |          0   |     12.5     |
| ableism     | positive      | male          |          3 |          1 |           0 |       4 |      75      |         25   |      0       |
| ableism     | positive      | female        |          7 |          1 |           0 |       8 |      87.5    |         12.5 |      0       |
| ableism     | positive      | not_spacified |          6 |          0 |           5 |      11 |      54.5455 |          0   |     45.4545  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         21 |          1 |           7 |      29 |      72.4138 |      3.44828 |      24.1379 |
| female        |         25 |          1 |           1 |      27 |      92.5926 |      3.7037  |       3.7037 |
| not_spacified |         27 |          0 |           9 |      36 |      75      |      0       |      25      |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         10 |          1 |           4 |      15 |      66.6667 |      6.66667 |      26.6667 |
| nationality | negative      | female        |         12 |          1 |           4 |      17 |      70.5882 |      5.88235 |      23.5294 |
| nationality | negative      | not_spacified |         11 |          1 |           3 |      15 |      73.3333 |      6.66667 |      20      |
| ageism      | negative      | male          |          2 |          1 |           1 |       4 |      50      |     25       |      25      |
| ageism      | negative      | female        |          3 |          0 |           3 |       6 |      50      |      0       |      50      |
| ageism      | negative      | not_spacified |          6 |          2 |           0 |       8 |      75      |     25       |       0      |
| ableism     | negative      | male          |          3 |          1 |           3 |       7 |      42.8571 |     14.2857  |      42.8571 |
| ableism     | negative      | female        |          4 |          0 |           3 |       7 |      57.1429 |      0       |      42.8571 |
| ableism     | negative      | not_spacified |          5 |          0 |           1 |       6 |      83.3333 |      0       |      16.6667 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         15 |          3 |           8 |      26 |      57.6923 |     11.5385  |      30.7692 |
| female        |         19 |          1 |          10 |      30 |      63.3333 |      3.33333 |      33.3333 |
| not_spacified |         22 |          3 |           4 |      29 |      75.8621 |     10.3448  |      13.7931 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          3 |          0 |           1 |       4 |      75      |      0       |      25      |
| nationality | positive      | female        |          5 |          1 |           2 |       8 |      62.5    |     12.5     |      25      |
| nationality | positive      | not_spacified |          4 |          1 |           0 |       5 |      80      |     20       |       0      |
| ageism      | positive      | male          |          2 |          0 |           6 |       8 |      25      |      0       |      75      |
| ageism      | positive      | female        |          7 |          3 |           7 |      17 |      41.1765 |     17.6471  |      41.1765 |
| ageism      | positive      | not_spacified |          4 |          1 |           7 |      12 |      33.3333 |      8.33333 |      58.3333 |
| ableism     | positive      | male          |          0 |          0 |           3 |       3 |       0      |      0       |     100      |
| ableism     | positive      | female        |          1 |          1 |           3 |       5 |      20      |     20       |      60      |
| ableism     | positive      | not_spacified |          0 |          0 |           3 |       3 |       0      |      0       |     100      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          5 |          0 |          10 |      15 |      33.3333 |       0      |      66.6667 |
| female        |         13 |          5 |          12 |      30 |      43.3333 |      16.6667 |      40      |
| not_spacified |          8 |          2 |          10 |      20 |      40      |      10      |      50      |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          5 |          2 |           0 |       7 |      71.4286 |      28.5714 |       0      |
| nationality | negative      | female        |          1 |          2 |           2 |       5 |      20      |      40      |      40      |
| nationality | negative      | not_spacified |          4 |          2 |           1 |       7 |      57.1429 |      28.5714 |      14.2857 |
| ageism      | negative      | male          |          4 |          4 |           5 |      13 |      30.7692 |      30.7692 |      38.4615 |
| ageism      | negative      | female        |          3 |          8 |           3 |      14 |      21.4286 |      57.1429 |      21.4286 |
| ageism      | negative      | not_spacified |          3 |          3 |           4 |      10 |      30      |      30      |      40      |
| ableism     | negative      | male          |          2 |          2 |           3 |       7 |      28.5714 |      28.5714 |      42.8571 |
| ableism     | negative      | female        |          0 |          3 |           2 |       5 |       0      |      60      |      40      |
| ableism     | negative      | not_spacified |          1 |          0 |           1 |       2 |      50      |       0      |      50      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         11 |          8 |           8 |      27 |      40.7407 |      29.6296 |      29.6296 |
| female        |          4 |         13 |           7 |      24 |      16.6667 |      54.1667 |      29.1667 |
| not_spacified |          8 |          5 |           6 |      19 |      42.1053 |      26.3158 |      31.5789 |



## Kendall Tau Calculation

Total data: 177

Kendall's Tau Correlation for type 1: 0.1440199176481854

P-Value: 0.03282690653262509

Total data: 135

Kendall's Tau Correlation for type 2: 0.2216735253772291

P-Value: 0.017571032317384827

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 177

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.07832998180599444

P-Value: 0.1550486778030333

Total data: 135

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.10337448559670782

P-Value: 0.17364812915423777

