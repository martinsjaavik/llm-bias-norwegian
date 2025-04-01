# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        110 |          1 |          25 |     136 |      80.8824 |     0.735294 |      18.3824 |
| ageism      | positive      |         58 |          1 |          10 |      69 |      84.058  |     1.44928  |      14.4928 |
| ableism     | positive      |         48 |          3 |          14 |      65 |      73.8462 |     4.61538  |      21.5385 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         92 |         11 |          20 |     123 |      74.7967 |      8.94309 |      16.2602 |
| ageism      | negative      |         42 |         14 |          11 |      67 |      62.6866 |     20.8955  |      16.4179 |
| ableism     | negative      |         43 |          5 |          19 |      67 |      64.1791 |      7.46269 |      28.3582 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |        202 |         12 |          45 |     259 | 77.9923 |  4.6332  | 17.3745 |
| ageism      |        100 |         15 |          21 |     136 | 73.5294 | 11.0294  | 15.4412 |
| ableism     |         91 |          8 |          33 |     132 | 68.9394 |  6.06061 | 25      |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         45 |          6 |          13 |      64 |      70.3125 |       9.375  |      20.3125 |
| ageism      | positive      |         52 |         12 |          48 |     112 |      46.4286 |      10.7143 |      42.8571 |
| ableism     | positive      |          6 |         11 |          17 |      34 |      17.6471 |      32.3529 |      50      |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         29 |         12 |           8 |      49 |     59.1837  |      24.4898 |      16.3265 |
| ageism      | negative      |         33 |         35 |          43 |     111 |     29.7297  |      31.5315 |      38.7387 |
| ableism     | negative      |          3 |         17 |          14 |      34 |      8.82353 |      50      |      41.1765 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         74 |         18 |          21 |     113 | 65.4867 | 15.9292 | 18.5841 |
| ageism      |         85 |         47 |          91 |     223 | 38.1166 | 21.0762 | 40.8072 |
| ableism     |          9 |         28 |          31 |      68 | 13.2353 | 41.1765 | 45.5882 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         28 |          1 |           7 |      36 |      77.7778 |      2.77778 |     19.4444  |
| nationality | positive      | female        |         42 |          0 |           8 |      50 |      84      |      0       |     16       |
| nationality | positive      | not_spacified |         40 |          0 |          10 |      50 |      80      |      0       |     20       |
| ageism      | positive      | male          |         23 |          0 |           6 |      29 |      79.3103 |      0       |     20.6897  |
| ageism      | positive      | female        |         11 |          0 |           2 |      13 |      84.6154 |      0       |     15.3846  |
| ageism      | positive      | not_spacified |         24 |          1 |           2 |      27 |      88.8889 |      3.7037  |      7.40741 |
| ableism     | positive      | male          |         12 |          2 |           5 |      19 |      63.1579 |     10.5263  |     26.3158  |
| ableism     | positive      | female        |         17 |          0 |           4 |      21 |      80.9524 |      0       |     19.0476  |
| ableism     | positive      | not_spacified |         19 |          1 |           5 |      25 |      76      |      4       |     20       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         63 |          3 |          18 |      84 |      75      |      3.57143 |      21.4286 |
| female        |         70 |          0 |          14 |      84 |      83.3333 |      0       |      16.6667 |
| not_spacified |         83 |          2 |          17 |     102 |      81.3725 |      1.96078 |      16.6667 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         26 |          3 |           8 |      37 |      70.2703 |      8.10811 |      21.6216 |
| nationality | negative      | female        |         39 |          2 |           8 |      49 |      79.5918 |      4.08163 |      16.3265 |
| nationality | negative      | not_spacified |         27 |          6 |           4 |      37 |      72.973  |     16.2162  |      10.8108 |
| ageism      | negative      | male          |         19 |          4 |           3 |      26 |      73.0769 |     15.3846  |      11.5385 |
| ageism      | negative      | female        |         15 |          3 |           4 |      22 |      68.1818 |     13.6364  |      18.1818 |
| ageism      | negative      | not_spacified |          8 |          7 |           4 |      19 |      42.1053 |     36.8421  |      21.0526 |
| ableism     | negative      | male          |          9 |          3 |           7 |      19 |      47.3684 |     15.7895  |      36.8421 |
| ableism     | negative      | female        |         19 |          1 |           9 |      29 |      65.5172 |      3.44828 |      31.0345 |
| ableism     | negative      | not_spacified |         15 |          1 |           3 |      19 |      78.9474 |      5.26316 |      15.7895 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         54 |         10 |          18 |      82 |      65.8537 |      12.1951 |      21.9512 |
| female        |         73 |          6 |          21 |     100 |      73      |       6      |      21      |
| not_spacified |         50 |         14 |          11 |      75 |      66.6667 |      18.6667 |      14.6667 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         15 |          2 |           6 |      23 |     65.2174  |      8.69565 |      26.087  |
| nationality | positive      | female        |         17 |          1 |           3 |      21 |     80.9524  |      4.7619  |      14.2857 |
| nationality | positive      | not_spacified |         13 |          3 |           4 |      20 |     65       |     15       |      20      |
| ageism      | positive      | male          |         11 |          3 |          19 |      33 |     33.3333  |      9.09091 |      57.5758 |
| ageism      | positive      | female        |         20 |          5 |          16 |      41 |     48.7805  |     12.1951  |      39.0244 |
| ageism      | positive      | not_spacified |         21 |          4 |          13 |      38 |     55.2632  |     10.5263  |      34.2105 |
| ableism     | positive      | male          |          3 |          3 |           8 |      14 |     21.4286  |     21.4286  |      57.1429 |
| ableism     | positive      | female        |          2 |          4 |           3 |       9 |     22.2222  |     44.4444  |      33.3333 |
| ableism     | positive      | not_spacified |          1 |          4 |           6 |      11 |      9.09091 |     36.3636  |      54.5455 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         29 |          8 |          33 |      70 |      41.4286 |      11.4286 |      47.1429 |
| female        |         39 |         10 |          22 |      71 |      54.9296 |      14.0845 |      30.9859 |
| not_spacified |         35 |         11 |          23 |      69 |      50.7246 |      15.942  |      33.3333 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          5 |          4 |           5 |      14 |      35.7143 |      28.5714 |      35.7143 |
| nationality | negative      | female        |          8 |          2 |           0 |      10 |      80      |      20      |       0      |
| nationality | negative      | not_spacified |         16 |          6 |           3 |      25 |      64      |      24      |      12      |
| ageism      | negative      | male          |         11 |          9 |          13 |      33 |      33.3333 |      27.2727 |      39.3939 |
| ageism      | negative      | female        |         11 |         11 |          16 |      38 |      28.9474 |      28.9474 |      42.1053 |
| ageism      | negative      | not_spacified |         11 |         15 |          14 |      40 |      27.5    |      37.5    |      35      |
| ableism     | negative      | male          |          2 |          7 |           6 |      15 |      13.3333 |      46.6667 |      40      |
| ableism     | negative      | female        |          0 |          7 |           6 |      13 |       0      |      53.8462 |      46.1538 |
| ableism     | negative      | not_spacified |          1 |          3 |           2 |       6 |      16.6667 |      50      |      33.3333 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         18 |         20 |          24 |      62 |      29.0323 |      32.2581 |      38.7097 |
| female        |         19 |         20 |          22 |      61 |      31.1475 |      32.7869 |      36.0656 |
| not_spacified |         28 |         24 |          19 |      71 |      39.4366 |      33.8028 |      26.7606 |



## Kendall Tau Calculation

Total data: 527

Kendall's Tau Correlation for type 1: 0.12878741507008631

P-Value: 0.0007666734339195216

Total data: 404

Kendall's Tau Correlation for type 2: 0.23132536025879816

P-Value: 1.623413674709453e-05

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 527

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.052248774884869786

P-Value: 0.09456471180134017

Total data: 404

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.03630158807960004

P-Value: 0.4076407009995766

