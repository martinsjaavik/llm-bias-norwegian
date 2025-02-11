# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        117 |          2 |          20 |     139 |      84.1727 |      1.43885 |      14.3885 |
| ageism      | positive      |         70 |          3 |           7 |      80 |      87.5    |      3.75    |       8.75   |
| ableism     | positive      |         48 |          4 |          13 |      65 |      73.8462 |      6.15385 |      20      |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         91 |          8 |          25 |     124 |      73.3871 |      6.45161 |      20.1613 |
| ageism      | negative      |         39 |         21 |          14 |      74 |      52.7027 |     28.3784  |      18.9189 |
| ableism     | negative      |         45 |         11 |          12 |      68 |      66.1765 |     16.1765  |      17.6471 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |        208 |         10 |          45 |     263 | 79.0875 |  3.80228 | 17.1103 |
| ageism      |        109 |         24 |          21 |     154 | 70.7792 | 15.5844  | 13.6364 |
| ableism     |         93 |         15 |          25 |     133 | 69.9248 | 11.2782  | 18.797  |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         44 |          5 |          15 |      64 |      68.75   |       7.8125 |      23.4375 |
| ageism      | positive      |         50 |         19 |          45 |     114 |      43.8596 |      16.6667 |      39.4737 |
| ableism     | positive      |          5 |         11 |          18 |      34 |      14.7059 |      32.3529 |      52.9412 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         40 |         16 |          14 |      70 |      57.1429 |      22.8571 |      20      |
| ageism      | negative      |         40 |         45 |          35 |     120 |      33.3333 |      37.5    |      29.1667 |
| ableism     | negative      |          0 |         18 |          21 |      39 |       0      |      46.1538 |      53.8462 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |       pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|---------:|--------:|--------:|
| nationality |         84 |         21 |          29 |     134 | 62.6866  | 15.6716 | 21.6418 |
| ageism      |         90 |         64 |          80 |     234 | 38.4615  | 27.3504 | 34.188  |
| ableism     |          5 |         29 |          39 |      73 |  6.84932 | 39.726  | 53.4247 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         30 |          2 |           5 |      37 |      81.0811 |      5.40541 |     13.5135  |
| nationality | positive      | female        |         44 |          0 |           8 |      52 |      84.6154 |      0       |     15.3846  |
| nationality | positive      | not_spacified |         43 |          0 |           7 |      50 |      86      |      0       |     14       |
| ageism      | positive      | male          |         29 |          2 |           2 |      33 |      87.8788 |      6.06061 |      6.06061 |
| ageism      | positive      | female        |         15 |          0 |           2 |      17 |      88.2353 |      0       |     11.7647  |
| ageism      | positive      | not_spacified |         26 |          1 |           3 |      30 |      86.6667 |      3.33333 |     10       |
| ableism     | positive      | male          |         13 |          2 |           4 |      19 |      68.4211 |     10.5263  |     21.0526  |
| ableism     | positive      | female        |         16 |          1 |           4 |      21 |      76.1905 |      4.7619  |     19.0476  |
| ableism     | positive      | not_spacified |         19 |          1 |           5 |      25 |      76      |      4       |     20       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         72 |          6 |          11 |      89 |      80.8989 |      6.74157 |      12.3596 |
| female        |         75 |          1 |          14 |      90 |      83.3333 |      1.11111 |      15.5556 |
| not_spacified |         88 |          2 |          15 |     105 |      83.8095 |      1.90476 |      14.2857 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         24 |          2 |          11 |      37 |      64.8649 |      5.40541 |     29.7297  |
| nationality | negative      | female        |         36 |          3 |          10 |      49 |      73.4694 |      6.12245 |     20.4082  |
| nationality | negative      | not_spacified |         31 |          3 |           4 |      38 |      81.5789 |      7.89474 |     10.5263  |
| ageism      | negative      | male          |         16 |          7 |           4 |      27 |      59.2593 |     25.9259  |     14.8148  |
| ageism      | negative      | female        |         14 |          6 |           6 |      26 |      53.8462 |     23.0769  |     23.0769  |
| ageism      | negative      | not_spacified |          9 |          8 |           4 |      21 |      42.8571 |     38.0952  |     19.0476  |
| ableism     | negative      | male          |          9 |          6 |           4 |      19 |      47.3684 |     31.5789  |     21.0526  |
| ableism     | negative      | female        |         20 |          3 |           7 |      30 |      66.6667 |     10       |     23.3333  |
| ableism     | negative      | not_spacified |         16 |          2 |           1 |      19 |      84.2105 |     10.5263  |      5.26316 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         49 |         15 |          19 |      83 |      59.0361 |      18.0723 |      22.8916 |
| female        |         70 |         12 |          23 |     105 |      66.6667 |      11.4286 |      21.9048 |
| not_spacified |         56 |         13 |           9 |      78 |      71.7949 |      16.6667 |      11.5385 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         16 |          1 |           6 |      23 |     69.5652  |      4.34783 |     26.087   |
| nationality | positive      | female        |         18 |          1 |           2 |      21 |     85.7143  |      4.7619  |      9.52381 |
| nationality | positive      | not_spacified |         10 |          3 |           7 |      20 |     50       |     15       |     35       |
| ageism      | positive      | male          |         14 |          5 |          14 |      33 |     42.4242  |     15.1515  |     42.4242  |
| ageism      | positive      | female        |         16 |         11 |          16 |      43 |     37.2093  |     25.5814  |     37.2093  |
| ageism      | positive      | not_spacified |         20 |          3 |          15 |      38 |     52.6316  |      7.89474 |     39.4737  |
| ableism     | positive      | male          |          3 |          4 |           7 |      14 |     21.4286  |     28.5714  |     50       |
| ableism     | positive      | female        |          1 |          4 |           4 |       9 |     11.1111  |     44.4444  |     44.4444  |
| ableism     | positive      | not_spacified |          1 |          3 |           7 |      11 |      9.09091 |     27.2727  |     63.6364  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         33 |         10 |          27 |      70 |      47.1429 |      14.2857 |      38.5714 |
| female        |         35 |         16 |          22 |      73 |      47.9452 |      21.9178 |      30.137  |
| not_spacified |         31 |          9 |          29 |      69 |      44.9275 |      13.0435 |      42.029  |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         11 |          7 |           6 |      24 |      45.8333 |      29.1667 |      25      |
| nationality | negative      | female        |          9 |          4 |           5 |      18 |      50      |      22.2222 |      27.7778 |
| nationality | negative      | not_spacified |         20 |          5 |           3 |      28 |      71.4286 |      17.8571 |      10.7143 |
| ageism      | negative      | male          |         12 |         14 |           9 |      35 |      34.2857 |      40      |      25.7143 |
| ageism      | negative      | female        |         14 |         17 |          12 |      43 |      32.5581 |      39.5349 |      27.907  |
| ageism      | negative      | not_spacified |         14 |         14 |          14 |      42 |      33.3333 |      33.3333 |      33.3333 |
| ableism     | negative      | male          |          0 |          6 |           9 |      15 |       0      |      40      |      60      |
| ableism     | negative      | female        |          0 |          9 |           7 |      16 |       0      |      56.25   |      43.75   |
| ableism     | negative      | not_spacified |          0 |          3 |           5 |       8 |       0      |      37.5    |      62.5    |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         23 |         27 |          24 |      74 |      31.0811 |      36.4865 |      32.4324 |
| female        |         23 |         30 |          24 |      77 |      29.8701 |      38.961  |      31.1688 |
| not_spacified |         34 |         22 |          22 |      78 |      43.5897 |      28.2051 |      28.2051 |



## Kendall Tau Calculation

Total data: 550

Kendall's Tau Correlation for type 1: 0.18447603305785124

P-Value: 8.847460943353763e-07

Total data: 441

Kendall's Tau Correlation for type 2: 0.1938081354990976

P-Value: 0.00016989586160584923

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 550

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.03083305785123967

P-Value: 0.31432234742725873

Total data: 441

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.0216267913060916

P-Value: 0.6076008629301254

