# Report for Model: norallm/normistral-7b-warm-instruct

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         69 |         34 |          21 |     124 |      55.6452 |      27.4194 |      16.9355 |
| ageism      | positive      |         49 |         11 |           9 |      69 |      71.0145 |      15.942  |      13.0435 |
| ableism     | positive      |         25 |         18 |          12 |      55 |      45.4545 |      32.7273 |      21.8182 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         50 |         44 |          13 |     107 |      46.729  |      41.1215 |     12.1495  |
| ageism      | negative      |         43 |         22 |           3 |      68 |      63.2353 |      32.3529 |      4.41176 |
| ableism     | negative      |         30 |         18 |           9 |      57 |      52.6316 |      31.5789 |     15.7895  |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |      nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|---------:|
| nationality |        119 |         78 |          34 |     231 | 51.5152 | 33.7662 | 14.7186  |
| ageism      |         92 |         33 |          12 |     137 | 67.1533 | 24.0876 |  8.75912 |
| ableism     |         55 |         36 |          21 |     112 | 49.1071 | 32.1429 | 18.75    |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         30 |          8 |          18 |      56 |      53.5714 |      14.2857 |      32.1429 |
| ageism      | positive      |         46 |         38 |          30 |     114 |      40.3509 |      33.3333 |      26.3158 |
| ableism     | positive      |          9 |          8 |          12 |      29 |      31.0345 |      27.5862 |      41.3793 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         27 |         11 |          28 |      66 |      40.9091 |      16.6667 |      42.4242 |
| ageism      | negative      |         50 |         40 |          29 |     119 |      42.0168 |      33.6134 |      24.3697 |
| ableism     | negative      |          7 |         19 |           7 |      33 |      21.2121 |      57.5758 |      21.2121 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         57 |         19 |          46 |     122 | 46.7213 | 15.5738 | 37.7049 |
| ageism      |         96 |         78 |          59 |     233 | 41.2017 | 33.4764 | 25.3219 |
| ableism     |         16 |         27 |          19 |      62 | 25.8065 | 43.5484 | 30.6452 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         17 |          9 |           6 |      32 |      53.125  |      28.125  |     18.75    |
| nationality | positive      | female        |         28 |         12 |           7 |      47 |      59.5745 |      25.5319 |     14.8936  |
| nationality | positive      | not_spacified |         24 |         13 |           8 |      45 |      53.3333 |      28.8889 |     17.7778  |
| ageism      | positive      | male          |         22 |          3 |           5 |      30 |      73.3333 |      10      |     16.6667  |
| ageism      | positive      | female        |          6 |          6 |           2 |      14 |      42.8571 |      42.8571 |     14.2857  |
| ageism      | positive      | not_spacified |         21 |          2 |           2 |      25 |      84      |       8      |      8       |
| ableism     | positive      | male          |          5 |          4 |           5 |      14 |      35.7143 |      28.5714 |     35.7143  |
| ableism     | positive      | female        |          9 |          4 |           5 |      18 |      50      |      22.2222 |     27.7778  |
| ableism     | positive      | not_spacified |         11 |         10 |           2 |      23 |      47.8261 |      43.4783 |      8.69565 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         44 |         16 |          16 |      76 |      57.8947 |      21.0526 |      21.0526 |
| female        |         43 |         22 |          14 |      79 |      54.4304 |      27.8481 |      17.7215 |
| not_spacified |         56 |         25 |          12 |      93 |      60.2151 |      26.8817 |      12.9032 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         12 |         15 |           6 |      33 |      36.3636 |      45.4545 |     18.1818  |
| nationality | negative      | female        |         16 |         22 |           4 |      42 |      38.0952 |      52.381  |      9.52381 |
| nationality | negative      | not_spacified |         22 |          7 |           3 |      32 |      68.75   |      21.875  |      9.375   |
| ageism      | negative      | male          |         15 |          6 |           2 |      23 |      65.2174 |      26.087  |      8.69565 |
| ageism      | negative      | female        |         16 |          8 |           1 |      25 |      64      |      32      |      4       |
| ageism      | negative      | not_spacified |         12 |          8 |           0 |      20 |      60      |      40      |      0       |
| ableism     | negative      | male          |          6 |          6 |           5 |      17 |      35.2941 |      35.2941 |     29.4118  |
| ableism     | negative      | female        |         15 |          6 |           2 |      23 |      65.2174 |      26.087  |      8.69565 |
| ableism     | negative      | not_spacified |          9 |          6 |           2 |      17 |      52.9412 |      35.2941 |     11.7647  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         33 |         27 |          13 |      73 |      45.2055 |      36.9863 |     17.8082  |
| female        |         47 |         36 |           7 |      90 |      52.2222 |      40      |      7.77778 |
| not_spacified |         43 |         21 |           5 |      69 |      62.3188 |      30.4348 |      7.24638 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          9 |          4 |           3 |      16 |      56.25   |      25      |      18.75   |
| nationality | positive      | female        |         13 |          0 |           9 |      22 |      59.0909 |       0      |      40.9091 |
| nationality | positive      | not_spacified |          8 |          4 |           6 |      18 |      44.4444 |      22.2222 |      33.3333 |
| ageism      | positive      | male          |         12 |         13 |           8 |      33 |      36.3636 |      39.3939 |      24.2424 |
| ageism      | positive      | female        |         17 |         12 |          14 |      43 |      39.5349 |      27.907  |      32.5581 |
| ageism      | positive      | not_spacified |         17 |         13 |           8 |      38 |      44.7368 |      34.2105 |      21.0526 |
| ableism     | positive      | male          |          4 |          3 |           4 |      11 |      36.3636 |      27.2727 |      36.3636 |
| ableism     | positive      | female        |          1 |          2 |           5 |       8 |      12.5    |      25      |      62.5    |
| ableism     | positive      | not_spacified |          4 |          3 |           3 |      10 |      40      |      30      |      30      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         25 |         20 |          15 |      60 |      41.6667 |      33.3333 |      25      |
| female        |         31 |         14 |          28 |      73 |      42.4658 |      19.1781 |      38.3562 |
| not_spacified |         29 |         20 |          17 |      66 |      43.9394 |      30.303  |      25.7576 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          7 |          4 |          10 |      21 |      33.3333 |     19.0476  |      47.619  |
| nationality | negative      | female        |          8 |          5 |           5 |      18 |      44.4444 |     27.7778  |      27.7778 |
| nationality | negative      | not_spacified |         12 |          2 |          13 |      27 |      44.4444 |      7.40741 |      48.1481 |
| ageism      | negative      | male          |         14 |         14 |           7 |      35 |      40      |     40       |      20      |
| ageism      | negative      | female        |         18 |         14 |          10 |      42 |      42.8571 |     33.3333  |      23.8095 |
| ageism      | negative      | not_spacified |         18 |         12 |          12 |      42 |      42.8571 |     28.5714  |      28.5714 |
| ableism     | negative      | male          |          0 |          8 |           3 |      11 |       0      |     72.7273  |      27.2727 |
| ableism     | negative      | female        |          6 |          5 |           3 |      14 |      42.8571 |     35.7143  |      21.4286 |
| ableism     | negative      | not_spacified |          1 |          6 |           1 |       8 |      12.5    |     75       |      12.5    |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         21 |         26 |          20 |      67 |      31.3433 |      38.806  |      29.8507 |
| female        |         32 |         24 |          18 |      74 |      43.2432 |      32.4324 |      24.3243 |
| not_spacified |         31 |         20 |          26 |      77 |      40.2597 |      25.974  |      33.7662 |



## Kendall Tau Calculation

Total data: 480

Kendall's Tau Correlation for type 1: 0.0802951388888889

P-Value: 0.08833955979697598

Total data: 417

Kendall's Tau Correlation for type 2: 0.0588421349251534

P-Value: 0.26761146725018115

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 480

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.0114453125

P-Value: 0.7660905388715431

Total data: 417

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.0696996359746735

P-Value: 0.10790612459914053

