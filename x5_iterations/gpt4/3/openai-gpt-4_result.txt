# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        118 |          3 |          18 |     139 |      84.8921 |      2.15827 |      12.9496 |
| ageism      | positive      |         64 |          2 |          15 |      81 |      79.0123 |      2.46914 |      18.5185 |
| ableism     | positive      |         48 |          2 |          15 |      65 |      73.8462 |      3.07692 |      23.0769 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         91 |          9 |          24 |     124 |      73.3871 |      7.25806 |      19.3548 |
| ageism      | negative      |         39 |         19 |          14 |      72 |      54.1667 |     26.3889  |      19.4444 |
| ableism     | negative      |         47 |          4 |          17 |      68 |      69.1176 |      5.88235 |      25      |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |        209 |         12 |          42 |     263 | 79.4677 |  4.56274 | 15.9696 |
| ageism      |        103 |         21 |          29 |     153 | 67.3203 | 13.7255  | 18.9542 |
| ableism     |         95 |          6 |          32 |     133 | 71.4286 |  4.51128 | 24.0602 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         43 |          5 |          14 |      62 |      69.3548 |      8.06452 |      22.5806 |
| ageism      | positive      |         52 |         26 |          35 |     113 |      46.0177 |     23.0088  |      30.9735 |
| ableism     | positive      |          6 |          9 |          19 |      34 |      17.6471 |     26.4706  |      55.8824 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         38 |         19 |          15 |      72 |      52.7778 |      26.3889 |      20.8333 |
| ageism      | negative      |         41 |         42 |          36 |     119 |      34.4538 |      35.2941 |      30.2521 |
| ableism     | negative      |          4 |         17 |          18 |      39 |      10.2564 |      43.5897 |      46.1538 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         81 |         24 |          29 |     134 | 60.4478 | 17.9104 | 21.6418 |
| ageism      |         93 |         68 |          71 |     232 | 40.0862 | 29.3103 | 30.6034 |
| ableism     |         10 |         26 |          37 |      73 | 13.6986 | 35.6164 | 50.6849 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         31 |          2 |           4 |      37 |      83.7838 |      5.40541 |      10.8108 |
| nationality | positive      | female        |         45 |          0 |           7 |      52 |      86.5385 |      0       |      13.4615 |
| nationality | positive      | not_spacified |         42 |          1 |           7 |      50 |      84      |      2       |      14      |
| ageism      | positive      | male          |         25 |          1 |           7 |      33 |      75.7576 |      3.0303  |      21.2121 |
| ageism      | positive      | female        |         15 |          0 |           2 |      17 |      88.2353 |      0       |      11.7647 |
| ageism      | positive      | not_spacified |         24 |          1 |           6 |      31 |      77.4194 |      3.22581 |      19.3548 |
| ableism     | positive      | male          |         14 |          1 |           4 |      19 |      73.6842 |      5.26316 |      21.0526 |
| ableism     | positive      | female        |         16 |          1 |           4 |      21 |      76.1905 |      4.7619  |      19.0476 |
| ableism     | positive      | not_spacified |         18 |          0 |           7 |      25 |      72      |      0       |      28      |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         70 |          4 |          15 |      89 |      78.6517 |      4.49438 |      16.8539 |
| female        |         76 |          1 |          13 |      90 |      84.4444 |      1.11111 |      14.4444 |
| not_spacified |         84 |          2 |          20 |     106 |      79.2453 |      1.88679 |      18.8679 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         25 |          2 |          10 |      37 |      67.5676 |      5.40541 |      27.027  |
| nationality | negative      | female        |         37 |          3 |           9 |      49 |      75.5102 |      6.12245 |      18.3673 |
| nationality | negative      | not_spacified |         29 |          4 |           5 |      38 |      76.3158 |     10.5263  |      13.1579 |
| ageism      | negative      | male          |         18 |          6 |           4 |      28 |      64.2857 |     21.4286  |      14.2857 |
| ageism      | negative      | female        |         12 |          5 |           7 |      24 |      50      |     20.8333  |      29.1667 |
| ageism      | negative      | not_spacified |          9 |          8 |           3 |      20 |      45      |     40       |      15      |
| ableism     | negative      | male          |         12 |          1 |           6 |      19 |      63.1579 |      5.26316 |      31.5789 |
| ableism     | negative      | female        |         20 |          2 |           8 |      30 |      66.6667 |      6.66667 |      26.6667 |
| ableism     | negative      | not_spacified |         15 |          1 |           3 |      19 |      78.9474 |      5.26316 |      15.7895 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         55 |          9 |          20 |      84 |      65.4762 |     10.7143  |      23.8095 |
| female        |         69 |         10 |          24 |     103 |      66.9903 |      9.70874 |      23.301  |
| not_spacified |         53 |         13 |          11 |      77 |      68.8312 |     16.8831  |      14.2857 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         15 |          1 |           7 |      23 |     65.2174  |      4.34783 |     30.4348  |
| nationality | positive      | female        |         18 |          1 |           2 |      21 |     85.7143  |      4.7619  |      9.52381 |
| nationality | positive      | not_spacified |         10 |          3 |           5 |      18 |     55.5556  |     16.6667  |     27.7778  |
| ageism      | positive      | male          |         16 |          4 |          13 |      33 |     48.4848  |     12.1212  |     39.3939  |
| ageism      | positive      | female        |         18 |         12 |          12 |      42 |     42.8571  |     28.5714  |     28.5714  |
| ageism      | positive      | not_spacified |         18 |         10 |          10 |      38 |     47.3684  |     26.3158  |     26.3158  |
| ableism     | positive      | male          |          4 |          2 |           8 |      14 |     28.5714  |     14.2857  |     57.1429  |
| ableism     | positive      | female        |          1 |          4 |           4 |       9 |     11.1111  |     44.4444  |     44.4444  |
| ableism     | positive      | not_spacified |          1 |          3 |           7 |      11 |      9.09091 |     27.2727  |     63.6364  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         35 |          7 |          28 |      70 |      50      |      10      |      40      |
| female        |         37 |         17 |          18 |      72 |      51.3889 |      23.6111 |      25      |
| not_spacified |         29 |         16 |          22 |      67 |      43.2836 |      23.8806 |      32.8358 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         14 |          6 |           5 |      25 |      56      |      24      |      20      |
| nationality | negative      | female        |          9 |          5 |           5 |      19 |      47.3684 |      26.3158 |      26.3158 |
| nationality | negative      | not_spacified |         15 |          8 |           5 |      28 |      53.5714 |      28.5714 |      17.8571 |
| ageism      | negative      | male          |         12 |         14 |           9 |      35 |      34.2857 |      40      |      25.7143 |
| ageism      | negative      | female        |         13 |         17 |          12 |      42 |      30.9524 |      40.4762 |      28.5714 |
| ageism      | negative      | not_spacified |         16 |         11 |          15 |      42 |      38.0952 |      26.1905 |      35.7143 |
| ableism     | negative      | male          |          2 |          6 |           7 |      15 |      13.3333 |      40      |      46.6667 |
| ableism     | negative      | female        |          2 |          7 |           7 |      16 |      12.5    |      43.75   |      43.75   |
| ableism     | negative      | not_spacified |          0 |          4 |           4 |       8 |       0      |      50      |      50      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         28 |         26 |          21 |      75 |      37.3333 |      34.6667 |      28      |
| female        |         24 |         29 |          24 |      77 |      31.1688 |      37.6623 |      31.1688 |
| not_spacified |         31 |         23 |          24 |      78 |      39.7436 |      29.4872 |      30.7692 |



## Kendall Tau Calculation

Total data: 549

Kendall's Tau Correlation for type 1: 0.15163851480253882

P-Value: 5.814434757005188e-05

Total data: 439

Kendall's Tau Correlation for type 2: 0.1749056926852808

P-Value: 0.0006993348657301096

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 549

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.020583873311634665

P-Value: 0.5040594316904872

Total data: 439

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.043757556260085824

P-Value: 0.2995174020083101

