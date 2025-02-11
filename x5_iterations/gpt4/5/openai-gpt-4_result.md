# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        118 |          2 |          19 |     139 |      84.8921 |      1.43885 |      13.6691 |
| ageism      | positive      |         71 |          1 |           9 |      81 |      87.6543 |      1.23457 |      11.1111 |
| ableism     | positive      |         51 |          5 |           9 |      65 |      78.4615 |      7.69231 |      13.8462 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         92 |          9 |          23 |     124 |      74.1935 |      7.25806 |      18.5484 |
| ageism      | negative      |         43 |         18 |          11 |      72 |      59.7222 |     25       |      15.2778 |
| ableism     | negative      |         46 |          8 |          14 |      68 |      67.6471 |     11.7647  |      20.5882 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |        210 |         11 |          42 |     263 | 79.8479 |  4.18251 | 15.9696 |
| ageism      |        114 |         19 |          20 |     153 | 74.5098 | 12.4183  | 13.0719 |
| ableism     |         97 |         13 |          23 |     133 | 72.9323 |  9.77444 | 17.2932 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         45 |          6 |          14 |      65 |      69.2308 |      9.23077 |      21.5385 |
| ageism      | positive      |         50 |         22 |          40 |     112 |      44.6429 |     19.6429  |      35.7143 |
| ableism     | positive      |          4 |         12 |          18 |      34 |      11.7647 |     35.2941  |      52.9412 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         41 |         18 |          11 |      70 |      58.5714 |      25.7143 |      15.7143 |
| ageism      | negative      |         33 |         50 |          37 |     120 |      27.5    |      41.6667 |      30.8333 |
| ableism     | negative      |          5 |         16 |          18 |      39 |      12.8205 |      41.0256 |      46.1538 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         86 |         24 |          25 |     135 | 63.7037 | 17.7778 | 18.5185 |
| ageism      |         83 |         72 |          77 |     232 | 35.7759 | 31.0345 | 33.1897 |
| ableism     |          9 |         28 |          36 |      73 | 12.3288 | 38.3562 | 49.3151 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         31 |          1 |           5 |      37 |      83.7838 |       2.7027 |     13.5135  |
| nationality | positive      | female        |         46 |          0 |           6 |      52 |      88.4615 |       0      |     11.5385  |
| nationality | positive      | not_spacified |         41 |          1 |           8 |      50 |      82      |       2      |     16       |
| ageism      | positive      | male          |         28 |          1 |           4 |      33 |      84.8485 |       3.0303 |     12.1212  |
| ageism      | positive      | female        |         15 |          0 |           2 |      17 |      88.2353 |       0      |     11.7647  |
| ageism      | positive      | not_spacified |         28 |          0 |           3 |      31 |      90.3226 |       0      |      9.67742 |
| ableism     | positive      | male          |         14 |          3 |           2 |      19 |      73.6842 |      15.7895 |     10.5263  |
| ableism     | positive      | female        |         17 |          1 |           3 |      21 |      80.9524 |       4.7619 |     14.2857  |
| ableism     | positive      | not_spacified |         20 |          1 |           4 |      25 |      80      |       4      |     16       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         73 |          5 |          11 |      89 |      82.0225 |      5.61798 |      12.3596 |
| female        |         78 |          1 |          11 |      90 |      86.6667 |      1.11111 |      12.2222 |
| not_spacified |         89 |          2 |          15 |     106 |      83.9623 |      1.88679 |      14.1509 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         27 |          2 |           8 |      37 |      72.973  |      5.40541 |     21.6216  |
| nationality | negative      | female        |         36 |          4 |           9 |      49 |      73.4694 |      8.16327 |     18.3673  |
| nationality | negative      | not_spacified |         29 |          3 |           6 |      38 |      76.3158 |      7.89474 |     15.7895  |
| ageism      | negative      | male          |         18 |          6 |           3 |      27 |      66.6667 |     22.2222  |     11.1111  |
| ageism      | negative      | female        |         16 |          5 |           2 |      23 |      69.5652 |     21.7391  |      8.69565 |
| ageism      | negative      | not_spacified |          9 |          7 |           6 |      22 |      40.9091 |     31.8182  |     27.2727  |
| ableism     | negative      | male          |         11 |          3 |           5 |      19 |      57.8947 |     15.7895  |     26.3158  |
| ableism     | negative      | female        |         20 |          3 |           7 |      30 |      66.6667 |     10       |     23.3333  |
| ableism     | negative      | not_spacified |         15 |          2 |           2 |      19 |      78.9474 |     10.5263  |     10.5263  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         56 |         11 |          16 |      83 |      67.4699 |      13.253  |      19.2771 |
| female        |         72 |         12 |          18 |     102 |      70.5882 |      11.7647 |      17.6471 |
| not_spacified |         53 |         12 |          14 |      79 |      67.0886 |      15.1899 |      17.7215 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         14 |          2 |           7 |      23 |     60.8696  |      8.69565 |      30.4348 |
| nationality | positive      | female        |         18 |          1 |           3 |      22 |     81.8182  |      4.54545 |      13.6364 |
| nationality | positive      | not_spacified |         13 |          3 |           4 |      20 |     65       |     15       |      20      |
| ageism      | positive      | male          |         16 |          4 |          13 |      33 |     48.4848  |     12.1212  |      39.3939 |
| ageism      | positive      | female        |         18 |         11 |          14 |      43 |     41.8605  |     25.5814  |      32.5581 |
| ageism      | positive      | not_spacified |         16 |          7 |          13 |      36 |     44.4444  |     19.4444  |      36.1111 |
| ableism     | positive      | male          |          2 |          3 |           9 |      14 |     14.2857  |     21.4286  |      64.2857 |
| ableism     | positive      | female        |          1 |          4 |           4 |       9 |     11.1111  |     44.4444  |      44.4444 |
| ableism     | positive      | not_spacified |          1 |          5 |           5 |      11 |      9.09091 |     45.4545  |      45.4545 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         32 |          9 |          29 |      70 |      45.7143 |      12.8571 |      41.4286 |
| female        |         37 |         16 |          21 |      74 |      50      |      21.6216 |      28.3784 |
| not_spacified |         30 |         15 |          22 |      67 |      44.7761 |      22.3881 |      32.8358 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         11 |          6 |           7 |      24 |      45.8333 |      25      |     29.1667  |
| nationality | negative      | female        |         11 |          6 |           1 |      18 |      61.1111 |      33.3333 |      5.55556 |
| nationality | negative      | not_spacified |         19 |          6 |           3 |      28 |      67.8571 |      21.4286 |     10.7143  |
| ageism      | negative      | male          |          6 |         15 |          14 |      35 |      17.1429 |      42.8571 |     40       |
| ageism      | negative      | female        |         12 |         20 |          11 |      43 |      27.907  |      46.5116 |     25.5814  |
| ageism      | negative      | not_spacified |         15 |         15 |          12 |      42 |      35.7143 |      35.7143 |     28.5714  |
| ableism     | negative      | male          |          2 |          6 |           7 |      15 |      13.3333 |      40      |     46.6667  |
| ableism     | negative      | female        |          0 |          8 |           8 |      16 |       0      |      50      |     50       |
| ableism     | negative      | not_spacified |          3 |          2 |           3 |       8 |      37.5    |      25      |     37.5     |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         19 |         27 |          28 |      74 |      25.6757 |      36.4865 |      37.8378 |
| female        |         23 |         34 |          20 |      77 |      29.8701 |      44.1558 |      25.974  |
| not_spacified |         37 |         23 |          18 |      78 |      47.4359 |      29.4872 |      23.0769 |



## Kendall Tau Calculation

Total data: 549

Kendall's Tau Correlation for type 1: 0.16836042348897315

P-Value: 3.702756046685881e-06

Total data: 440

Kendall's Tau Correlation for type 2: 0.1944214876033058

P-Value: 0.00016813538985453993

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 549

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.02294285685847094

P-Value: 0.4400970820703676

Total data: 440

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.011885330578512395

P-Value: 0.7783351958398133

