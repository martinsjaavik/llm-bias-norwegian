# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        111 |          2 |          24 |     137 |      81.0219 |      1.45985 |      17.5182 |
| ageism      | positive      |         67 |          1 |          13 |      81 |      82.716  |      1.23457 |      16.0494 |
| ableism     | positive      |         51 |          4 |          10 |      65 |      78.4615 |      6.15385 |      15.3846 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         88 |         11 |          25 |     124 |      70.9677 |      8.87097 |      20.1613 |
| ageism      | negative      |         40 |         19 |          15 |      74 |      54.0541 |     25.6757  |      20.2703 |
| ableism     | negative      |         43 |          6 |          19 |      68 |      63.2353 |      8.82353 |      27.9412 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |        199 |         13 |          49 |     261 | 76.2452 |  4.98084 | 18.7739 |
| ageism      |        107 |         20 |          28 |     155 | 69.0323 | 12.9032  | 18.0645 |
| ableism     |         94 |         10 |          29 |     133 | 70.6767 |  7.5188  | 21.8045 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         42 |          7 |          15 |      64 |     65.625   |      10.9375 |      23.4375 |
| ageism      | positive      |         53 |         13 |          48 |     114 |     46.4912  |      11.4035 |      42.1053 |
| ableism     | positive      |          3 |         10 |          21 |      34 |      8.82353 |      29.4118 |      61.7647 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         41 |         16 |          11 |      68 |      60.2941 |      23.5294 |      16.1765 |
| ageism      | negative      |         36 |         40 |          44 |     120 |      30      |      33.3333 |      36.6667 |
| ableism     | negative      |          8 |         15 |          16 |      39 |      20.5128 |      38.4615 |      41.0256 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         83 |         23 |          26 |     132 | 62.8788 | 17.4242 | 19.697  |
| ageism      |         89 |         53 |          92 |     234 | 38.0342 | 22.6496 | 39.3162 |
| ableism     |         11 |         25 |          37 |      73 | 15.0685 | 34.2466 | 50.6849 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         28 |          1 |           7 |      36 |      77.7778 |      2.77778 |     19.4444  |
| nationality | positive      | female        |         40 |          0 |          11 |      51 |      78.4314 |      0       |     21.5686  |
| nationality | positive      | not_spacified |         43 |          1 |           6 |      50 |      86      |      2       |     12       |
| ageism      | positive      | male          |         24 |          1 |           8 |      33 |      72.7273 |      3.0303  |     24.2424  |
| ageism      | positive      | female        |         16 |          0 |           1 |      17 |      94.1176 |      0       |      5.88235 |
| ageism      | positive      | not_spacified |         27 |          0 |           4 |      31 |      87.0968 |      0       |     12.9032  |
| ableism     | positive      | male          |         15 |          2 |           2 |      19 |      78.9474 |     10.5263  |     10.5263  |
| ableism     | positive      | female        |         17 |          1 |           3 |      21 |      80.9524 |      4.7619  |     14.2857  |
| ableism     | positive      | not_spacified |         19 |          1 |           5 |      25 |      76      |      4       |     20       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         67 |          4 |          17 |      88 |      76.1364 |      4.54545 |      19.3182 |
| female        |         73 |          1 |          15 |      89 |      82.0225 |      1.1236  |      16.8539 |
| not_spacified |         89 |          2 |          15 |     106 |      83.9623 |      1.88679 |      14.1509 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         24 |          4 |           9 |      37 |      64.8649 |     10.8108  |      24.3243 |
| nationality | negative      | female        |         35 |          3 |          11 |      49 |      71.4286 |      6.12245 |      22.449  |
| nationality | negative      | not_spacified |         29 |          4 |           5 |      38 |      76.3158 |     10.5263  |      13.1579 |
| ageism      | negative      | male          |         16 |          5 |           6 |      27 |      59.2593 |     18.5185  |      22.2222 |
| ageism      | negative      | female        |         14 |          6 |           6 |      26 |      53.8462 |     23.0769  |      23.0769 |
| ageism      | negative      | not_spacified |         10 |          8 |           3 |      21 |      47.619  |     38.0952  |      14.2857 |
| ableism     | negative      | male          |         10 |          2 |           7 |      19 |      52.6316 |     10.5263  |      36.8421 |
| ableism     | negative      | female        |         18 |          3 |           9 |      30 |      60      |     10       |      30      |
| ableism     | negative      | not_spacified |         15 |          1 |           3 |      19 |      78.9474 |      5.26316 |      15.7895 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         50 |         11 |          22 |      83 |      60.241  |      13.253  |      26.506  |
| female        |         67 |         12 |          26 |     105 |      63.8095 |      11.4286 |      24.7619 |
| not_spacified |         54 |         13 |          11 |      78 |      69.2308 |      16.6667 |      14.1026 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         15 |          1 |           7 |      23 |      65.2174 |      4.34783 |      30.4348 |
| nationality | positive      | female        |         16 |          1 |           5 |      22 |      72.7273 |      4.54545 |      22.7273 |
| nationality | positive      | not_spacified |         11 |          5 |           3 |      19 |      57.8947 |     26.3158  |      15.7895 |
| ageism      | positive      | male          |         12 |          3 |          18 |      33 |      36.3636 |      9.09091 |      54.5455 |
| ageism      | positive      | female        |         21 |          7 |          15 |      43 |      48.8372 |     16.2791  |      34.8837 |
| ageism      | positive      | not_spacified |         20 |          3 |          15 |      38 |      52.6316 |      7.89474 |      39.4737 |
| ableism     | positive      | male          |          2 |          3 |           9 |      14 |      14.2857 |     21.4286  |      64.2857 |
| ableism     | positive      | female        |          1 |          4 |           4 |       9 |      11.1111 |     44.4444  |      44.4444 |
| ableism     | positive      | not_spacified |          0 |          3 |           8 |      11 |       0      |     27.2727  |      72.7273 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         29 |          7 |          34 |      70 |      41.4286 |      10      |      48.5714 |
| female        |         38 |         12 |          24 |      74 |      51.3514 |      16.2162 |      32.4324 |
| not_spacified |         31 |         11 |          26 |      68 |      45.5882 |      16.1765 |      38.2353 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         12 |          6 |           5 |      23 |      52.1739 |      26.087  |     21.7391  |
| nationality | negative      | female        |         11 |          5 |           1 |      17 |      64.7059 |      29.4118 |      5.88235 |
| nationality | negative      | not_spacified |         18 |          5 |           5 |      28 |      64.2857 |      17.8571 |     17.8571  |
| ageism      | negative      | male          |          9 |         11 |          15 |      35 |      25.7143 |      31.4286 |     42.8571  |
| ageism      | negative      | female        |         11 |         19 |          13 |      43 |      25.5814 |      44.186  |     30.2326  |
| ageism      | negative      | not_spacified |         16 |         10 |          16 |      42 |      38.0952 |      23.8095 |     38.0952  |
| ableism     | negative      | male          |          3 |          5 |           7 |      15 |      20      |      33.3333 |     46.6667  |
| ableism     | negative      | female        |          3 |          6 |           7 |      16 |      18.75   |      37.5    |     43.75    |
| ableism     | negative      | not_spacified |          2 |          4 |           2 |       8 |      25      |      50      |     25       |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         24 |         22 |          27 |      73 |      32.8767 |      30.137  |      36.9863 |
| female        |         25 |         30 |          21 |      76 |      32.8947 |      39.4737 |      27.6316 |
| not_spacified |         36 |         19 |          23 |      78 |      46.1538 |      24.359  |      29.4872 |



## Kendall Tau Calculation

Total data: 549

Kendall's Tau Correlation for type 1: 0.1831447141847572

P-Value: 1.8091004446059272e-06

Total data: 439

Kendall's Tau Correlation for type 2: 0.16728846363395788

P-Value: 0.0011539700871126494

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 549

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.02363960305373904

P-Value: 0.45046058336167283

Total data: 439

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.005043560380031236

P-Value: 0.9045302455520269

