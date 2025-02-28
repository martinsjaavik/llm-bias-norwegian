# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         57 |         36 |          22 |     115 |      49.5652 |      31.3043 |      19.1304 |
| ageism      | positive      |         23 |         23 |           8 |      54 |      42.5926 |      42.5926 |      14.8148 |
| ableism     | positive      |         25 |         23 |          11 |      59 |      42.3729 |      38.9831 |      18.6441 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         32 |         55 |          17 |     104 |      30.7692 |      52.8846 |      16.3462 |
| ageism      | negative      |         13 |         31 |          10 |      54 |      24.0741 |      57.4074 |      18.5185 |
| ableism     | negative      |         13 |         33 |          12 |      58 |      22.4138 |      56.8966 |      20.6897 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         89 |         91 |          39 |     219 | 40.6393 | 41.5525 | 17.8082 |
| ageism      |         36 |         54 |          18 |     108 | 33.3333 | 50      | 16.6667 |
| ableism     |         38 |         56 |          23 |     117 | 32.4786 | 47.8632 | 19.6581 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         35 |          1 |           9 |      45 |      77.7778 |      2.22222 |      20      |
| ageism      | positive      |         25 |         51 |          36 |     112 |      22.3214 |     45.5357  |      32.1429 |
| ableism     | positive      |          5 |         12 |           8 |      25 |      20      |     48       |      32      |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         19 |         20 |          15 |      54 |      35.1852 |      37.037  |      27.7778 |
| ageism      | negative      |         25 |         63 |          25 |     113 |      22.1239 |      55.7522 |      22.1239 |
| ableism     | negative      |          0 |         14 |          10 |      24 |       0      |      58.3333 |      41.6667 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         54 |         21 |          24 |      99 | 54.5455 | 21.2121 | 24.2424 |
| ageism      |         50 |        114 |          61 |     225 | 22.2222 | 50.6667 | 27.1111 |
| ableism     |          5 |         26 |          18 |      49 | 10.2041 | 53.0612 | 36.7347 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         11 |         12 |           4 |      27 |      40.7407 |      44.4444 |      14.8148 |
| nationality | positive      | female        |         23 |         11 |          11 |      45 |      51.1111 |      24.4444 |      24.4444 |
| nationality | positive      | not_spacified |         23 |         13 |           7 |      43 |      53.4884 |      30.2326 |      16.2791 |
| ageism      | positive      | male          |         15 |          8 |           3 |      26 |      57.6923 |      30.7692 |      11.5385 |
| ageism      | positive      | female        |          4 |          4 |           1 |       9 |      44.4444 |      44.4444 |      11.1111 |
| ageism      | positive      | not_spacified |          4 |         11 |           4 |      19 |      21.0526 |      57.8947 |      21.0526 |
| ableism     | positive      | male          |          3 |          9 |           4 |      16 |      18.75   |      56.25   |      25      |
| ableism     | positive      | female        |          9 |          6 |           3 |      18 |      50      |      33.3333 |      16.6667 |
| ableism     | positive      | not_spacified |         13 |          8 |           4 |      25 |      52      |      32      |      16      |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         29 |         29 |          11 |      69 |       42.029 |      42.029  |      15.942  |
| female        |         36 |         21 |          15 |      72 |       50     |      29.1667 |      20.8333 |
| not_spacified |         40 |         32 |          15 |      87 |       45.977 |      36.7816 |      17.2414 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          6 |         19 |           5 |      30 |      20      |      63.3333 |      16.6667 |
| nationality | negative      | female        |         13 |         22 |           8 |      43 |      30.2326 |      51.1628 |      18.6047 |
| nationality | negative      | not_spacified |         13 |         14 |           4 |      31 |      41.9355 |      45.1613 |      12.9032 |
| ageism      | negative      | male          |          7 |          7 |           4 |      18 |      38.8889 |      38.8889 |      22.2222 |
| ageism      | negative      | female        |          4 |         11 |           4 |      19 |      21.0526 |      57.8947 |      21.0526 |
| ageism      | negative      | not_spacified |          2 |         13 |           2 |      17 |      11.7647 |      76.4706 |      11.7647 |
| ableism     | negative      | male          |          4 |          9 |           2 |      15 |      26.6667 |      60      |      13.3333 |
| ableism     | negative      | female        |          9 |         10 |           6 |      25 |      36      |      40      |      24      |
| ableism     | negative      | not_spacified |          0 |         14 |           4 |      18 |       0      |      77.7778 |      22.2222 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         17 |         35 |          11 |      63 |      26.9841 |      55.5556 |      17.4603 |
| female        |         26 |         43 |          18 |      87 |      29.8851 |      49.4253 |      20.6897 |
| not_spacified |         15 |         41 |          10 |      66 |      22.7273 |      62.1212 |      15.1515 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         12 |          0 |           4 |      16 |      75      |       0      |      25      |
| nationality | positive      | female        |         12 |          1 |           3 |      16 |      75      |       6.25   |      18.75   |
| nationality | positive      | not_spacified |         11 |          0 |           2 |      13 |      84.6154 |       0      |      15.3846 |
| ageism      | positive      | male          |          6 |         19 |           8 |      33 |      18.1818 |      57.5758 |      24.2424 |
| ageism      | positive      | female        |          8 |         17 |          18 |      43 |      18.6047 |      39.5349 |      41.8605 |
| ageism      | positive      | not_spacified |         11 |         15 |          10 |      36 |      30.5556 |      41.6667 |      27.7778 |
| ableism     | positive      | male          |          3 |          6 |           2 |      11 |      27.2727 |      54.5455 |      18.1818 |
| ableism     | positive      | female        |          0 |          3 |           2 |       5 |       0      |      60      |      40      |
| ableism     | positive      | not_spacified |          2 |          3 |           4 |       9 |      22.2222 |      33.3333 |      44.4444 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         21 |         25 |          14 |      60 |      35      |      41.6667 |      23.3333 |
| female        |         20 |         21 |          23 |      64 |      31.25   |      32.8125 |      35.9375 |
| not_spacified |         24 |         18 |          16 |      58 |      41.3793 |      31.0345 |      27.5862 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          6 |          9 |           6 |      21 |      28.5714 |      42.8571 |      28.5714 |
| nationality | negative      | female        |          4 |          4 |           5 |      13 |      30.7692 |      30.7692 |      38.4615 |
| nationality | negative      | not_spacified |          9 |          7 |           4 |      20 |      45      |      35      |      20      |
| ageism      | negative      | male          |          6 |         21 |           6 |      33 |      18.1818 |      63.6364 |      18.1818 |
| ageism      | negative      | female        |         11 |         21 |          11 |      43 |      25.5814 |      48.8372 |      25.5814 |
| ageism      | negative      | not_spacified |          8 |         21 |           8 |      37 |      21.6216 |      56.7568 |      21.6216 |
| ableism     | negative      | male          |          0 |          7 |           5 |      12 |       0      |      58.3333 |      41.6667 |
| ableism     | negative      | female        |          0 |          5 |           3 |       8 |       0      |      62.5    |      37.5    |
| ableism     | negative      | not_spacified |          0 |          2 |           2 |       4 |       0      |      50      |      50      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         12 |         37 |          17 |      66 |      18.1818 |      56.0606 |      25.7576 |
| female        |         15 |         30 |          19 |      64 |      23.4375 |      46.875  |      29.6875 |
| not_spacified |         17 |         30 |          14 |      61 |      27.8689 |      49.1803 |      22.9508 |



## Kendall Tau Calculation

Total data: 444

Kendall's Tau Correlation for type 1: 0.22597597597597596

P-Value: 8.030430630114534e-06

Total data: 373

Kendall's Tau Correlation for type 2: 0.18250688210222168

P-Value: 0.001104103791214894

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 444

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.050827854881908933

P-Value: 0.21842127176965365

Total data: 373

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.04793393181867188

P-Value: 0.2940373360956535

