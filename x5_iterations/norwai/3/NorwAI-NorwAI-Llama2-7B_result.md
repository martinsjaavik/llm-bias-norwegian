# Report for Model: NorwAI/NorwAI-Llama2-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         63 |         31 |          35 |     129 |      48.8372 |      24.031  |     27.1318  |
| ageism      | positive      |         59 |          9 |           7 |      75 |      78.6667 |      12      |      9.33333 |
| ableism     | positive      |         33 |         13 |           9 |      55 |      60      |      23.6364 |     16.3636  |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         49 |         30 |          31 |     110 |      44.5455 |      27.2727 |      28.1818 |
| ageism      | negative      |         42 |         13 |          13 |      68 |      61.7647 |      19.1176 |      19.1176 |
| ableism     | negative      |         33 |         14 |           9 |      56 |      58.9286 |      25      |      16.0714 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        112 |         61 |          66 |     239 | 46.8619 | 25.523  | 27.6151 |
| ageism      |        101 |         22 |          20 |     143 | 70.6294 | 15.3846 | 13.986  |
| ableism     |         66 |         27 |          18 |     111 | 59.4595 | 24.3243 | 16.2162 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         34 |         16 |           6 |      56 |      60.7143 |      28.5714 |      10.7143 |
| ageism      | positive      |         19 |         44 |          51 |     114 |      16.6667 |      38.5965 |      44.7368 |
| ableism     | positive      |         10 |          4 |          15 |      29 |      34.4828 |      13.7931 |      51.7241 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         25 |         21 |          14 |      60 |      41.6667 |      35      |      23.3333 |
| ageism      | negative      |         22 |         40 |          58 |     120 |      18.3333 |      33.3333 |      48.3333 |
| ableism     | negative      |         10 |          8 |          11 |      29 |      34.4828 |      27.5862 |      37.931  |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         59 |         37 |          20 |     116 | 50.8621 | 31.8966 | 17.2414 |
| ageism      |         41 |         84 |         109 |     234 | 17.5214 | 35.8974 | 46.5812 |
| ableism     |         20 |         12 |          26 |      58 | 34.4828 | 20.6897 | 44.8276 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         23 |          5 |           7 |      35 |      65.7143 |     14.2857  |     20       |
| nationality | positive      | female        |         23 |         11 |          12 |      46 |      50      |     23.913   |     26.087   |
| nationality | positive      | not_spacified |         17 |         15 |          16 |      48 |      35.4167 |     31.25    |     33.3333  |
| ageism      | positive      | male          |         22 |          5 |           3 |      30 |      73.3333 |     16.6667  |     10       |
| ageism      | positive      | female        |         12 |          2 |           1 |      15 |      80      |     13.3333  |      6.66667 |
| ageism      | positive      | not_spacified |         25 |          2 |           3 |      30 |      83.3333 |      6.66667 |     10       |
| ableism     | positive      | male          |         10 |          4 |           2 |      16 |      62.5    |     25       |     12.5     |
| ableism     | positive      | female        |         11 |          5 |           2 |      18 |      61.1111 |     27.7778  |     11.1111  |
| ableism     | positive      | not_spacified |         12 |          4 |           5 |      21 |      57.1429 |     19.0476  |     23.8095  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         55 |         14 |          12 |      81 |      67.9012 |      17.284  |      14.8148 |
| female        |         46 |         18 |          15 |      79 |      58.2278 |      22.7848 |      18.9873 |
| not_spacified |         54 |         21 |          24 |      99 |      54.5455 |      21.2121 |      24.2424 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         14 |         10 |          10 |      34 |      41.1765 |      29.4118 |     29.4118  |
| nationality | negative      | female        |         20 |         11 |          10 |      41 |      48.7805 |      26.8293 |     24.3902  |
| nationality | negative      | not_spacified |         15 |          9 |          11 |      35 |      42.8571 |      25.7143 |     31.4286  |
| ageism      | negative      | male          |         16 |          3 |           6 |      25 |      64      |      12      |     24       |
| ageism      | negative      | female        |         15 |          5 |           3 |      23 |      65.2174 |      21.7391 |     13.0435  |
| ageism      | negative      | not_spacified |         11 |          5 |           4 |      20 |      55      |      25      |     20       |
| ableism     | negative      | male          |         12 |          3 |           4 |      19 |      63.1579 |      15.7895 |     21.0526  |
| ableism     | negative      | female        |         12 |          7 |           2 |      21 |      57.1429 |      33.3333 |      9.52381 |
| ableism     | negative      | not_spacified |          9 |          4 |           3 |      16 |      56.25   |      25      |     18.75    |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         42 |         16 |          20 |      78 |      53.8462 |      20.5128 |      25.641  |
| female        |         47 |         23 |          15 |      85 |      55.2941 |      27.0588 |      17.6471 |
| not_spacified |         35 |         18 |          18 |      71 |      49.2958 |      25.3521 |      25.3521 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         10 |          8 |           2 |      20 |      50      |      40      |      10      |
| nationality | positive      | female        |         13 |          4 |           2 |      19 |      68.4211 |      21.0526 |      10.5263 |
| nationality | positive      | not_spacified |         11 |          4 |           2 |      17 |      64.7059 |      23.5294 |      11.7647 |
| ageism      | positive      | male          |          5 |         14 |          14 |      33 |      15.1515 |      42.4242 |      42.4242 |
| ageism      | positive      | female        |          8 |         13 |          22 |      43 |      18.6047 |      30.2326 |      51.1628 |
| ageism      | positive      | not_spacified |          6 |         17 |          15 |      38 |      15.7895 |      44.7368 |      39.4737 |
| ableism     | positive      | male          |          7 |          2 |           4 |      13 |      53.8462 |      15.3846 |      30.7692 |
| ableism     | positive      | female        |          1 |          1 |           5 |       7 |      14.2857 |      14.2857 |      71.4286 |
| ableism     | positive      | not_spacified |          2 |          1 |           6 |       9 |      22.2222 |      11.1111 |      66.6667 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         22 |         24 |          20 |      66 |      33.3333 |      36.3636 |      30.303  |
| female        |         22 |         18 |          29 |      69 |      31.8841 |      26.087  |      42.029  |
| not_spacified |         19 |         22 |          23 |      64 |      29.6875 |      34.375  |      35.9375 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          8 |          8 |           6 |      22 |      36.3636 |      36.3636 |     27.2727  |
| nationality | negative      | female        |          6 |          3 |           6 |      15 |      40      |      20      |     40       |
| nationality | negative      | not_spacified |         11 |         10 |           2 |      23 |      47.8261 |      43.4783 |      8.69565 |
| ageism      | negative      | male          |          7 |         12 |          16 |      35 |      20      |      34.2857 |     45.7143  |
| ageism      | negative      | female        |          8 |         13 |          22 |      43 |      18.6047 |      30.2326 |     51.1628  |
| ageism      | negative      | not_spacified |          7 |         15 |          20 |      42 |      16.6667 |      35.7143 |     47.619   |
| ableism     | negative      | male          |          5 |          4 |           3 |      12 |      41.6667 |      33.3333 |     25       |
| ableism     | negative      | female        |          3 |          3 |           6 |      12 |      25      |      25      |     50       |
| ableism     | negative      | not_spacified |          2 |          1 |           2 |       5 |      40      |      20      |     40       |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         20 |         24 |          25 |      69 |      28.9855 |      34.7826 |      36.2319 |
| female        |         17 |         19 |          34 |      70 |      24.2857 |      27.1429 |      48.5714 |
| not_spacified |         20 |         26 |          24 |      70 |      28.5714 |      37.1429 |      34.2857 |



## Kendall Tau Calculation

Total data: 493

Kendall's Tau Correlation for type 1: 0.06997765882599805

P-Value: 0.13194665685672952

Total data: 408

Kendall's Tau Correlation for type 2: 0.03556324490580546

P-Value: 0.5088416458990843

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 493

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.03947352180013084

P-Value: 0.2985512746454897

Total data: 408

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.02899726066897347

P-Value: 0.5095489000836082

