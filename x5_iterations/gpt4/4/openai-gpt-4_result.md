# Report for Model: openai/gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        118 |          1 |          20 |     139 |      84.8921 |     0.719424 |     14.3885  |
| ageism      | positive      |         72 |          2 |           7 |      81 |      88.8889 |     2.46914  |      8.64198 |
| ableism     | positive      |         51 |          1 |          13 |      65 |      78.4615 |     1.53846  |     20       |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         93 |          8 |          23 |     124 |      75      |      6.45161 |      18.5484 |
| ageism      | negative      |         44 |         19 |          13 |      76 |      57.8947 |     25       |      17.1053 |
| ableism     | negative      |         44 |          6 |          18 |      68 |      64.7059 |      8.82353 |      26.4706 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |       nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|---------:|--------:|
| nationality |        211 |          9 |          43 |     263 | 80.2281 |  3.42205 | 16.3498 |
| ageism      |        116 |         21 |          20 |     157 | 73.8854 | 13.3758  | 12.7389 |
| ableism     |         95 |          7 |          31 |     133 | 71.4286 |  5.26316 | 23.3083 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         47 |          4 |          14 |      65 |      72.3077 |      6.15385 |      21.5385 |
| ageism      | positive      |         62 |         21 |          30 |     113 |      54.8673 |     18.5841  |      26.5487 |
| ableism     | positive      |          6 |         10 |          18 |      34 |      17.6471 |     29.4118  |      52.9412 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         37 |         17 |          16 |      70 |      52.8571 |      24.2857 |      22.8571 |
| ageism      | negative      |         37 |         45 |          38 |     120 |      30.8333 |      37.5    |      31.6667 |
| ableism     | negative      |          5 |         17 |          15 |      37 |      13.5135 |      45.9459 |      40.5405 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         84 |         21 |          30 |     135 | 62.2222 | 15.5556 | 22.2222 |
| ageism      |         99 |         66 |          68 |     233 | 42.4893 | 28.3262 | 29.1845 |
| ableism     |         11 |         27 |          33 |      71 | 15.493  | 38.0282 | 46.4789 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         31 |          1 |           5 |      37 |      83.7838 |      2.7027  |     13.5135  |
| nationality | positive      | female        |         44 |          0 |           8 |      52 |      84.6154 |      0       |     15.3846  |
| nationality | positive      | not_spacified |         43 |          0 |           7 |      50 |      86      |      0       |     14       |
| ageism      | positive      | male          |         28 |          1 |           4 |      33 |      84.8485 |      3.0303  |     12.1212  |
| ageism      | positive      | female        |         16 |          0 |           1 |      17 |      94.1176 |      0       |      5.88235 |
| ageism      | positive      | not_spacified |         28 |          1 |           2 |      31 |      90.3226 |      3.22581 |      6.45161 |
| ableism     | positive      | male          |         15 |          0 |           4 |      19 |      78.9474 |      0       |     21.0526  |
| ableism     | positive      | female        |         17 |          0 |           4 |      21 |      80.9524 |      0       |     19.0476  |
| ableism     | positive      | not_spacified |         19 |          1 |           5 |      25 |      76      |      4       |     20       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         74 |          2 |          13 |      89 |      83.1461 |      2.24719 |      14.6067 |
| female        |         77 |          0 |          13 |      90 |      85.5556 |      0       |      14.4444 |
| not_spacified |         90 |          2 |          14 |     106 |      84.9057 |      1.88679 |      13.2075 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         24 |          3 |          10 |      37 |      64.8649 |      8.10811 |      27.027  |
| nationality | negative      | female        |         38 |          2 |           9 |      49 |      77.551  |      4.08163 |      18.3673 |
| nationality | negative      | not_spacified |         31 |          3 |           4 |      38 |      81.5789 |      7.89474 |      10.5263 |
| ageism      | negative      | male          |         18 |          6 |           4 |      28 |      64.2857 |     21.4286  |      14.2857 |
| ageism      | negative      | female        |         16 |          6 |           4 |      26 |      61.5385 |     23.0769  |      15.3846 |
| ageism      | negative      | not_spacified |         10 |          7 |           5 |      22 |      45.4545 |     31.8182  |      22.7273 |
| ableism     | negative      | male          |         10 |          3 |           6 |      19 |      52.6316 |     15.7895  |      31.5789 |
| ableism     | negative      | female        |         18 |          2 |          10 |      30 |      60      |      6.66667 |      33.3333 |
| ableism     | negative      | not_spacified |         16 |          1 |           2 |      19 |      84.2105 |      5.26316 |      10.5263 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         52 |         12 |          20 |      84 |      61.9048 |     14.2857  |      23.8095 |
| female        |         72 |         10 |          23 |     105 |      68.5714 |      9.52381 |      21.9048 |
| not_spacified |         57 |         11 |          11 |      79 |      72.1519 |     13.9241  |      13.9241 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         16 |          1 |           6 |      23 |     69.5652  |      4.34783 |      26.087  |
| nationality | positive      | female        |         18 |          0 |           4 |      22 |     81.8182  |      0       |      18.1818 |
| nationality | positive      | not_spacified |         13 |          3 |           4 |      20 |     65       |     15       |      20      |
| ageism      | positive      | male          |         19 |          6 |           7 |      32 |     59.375   |     18.75    |      21.875  |
| ageism      | positive      | female        |         22 |          8 |          13 |      43 |     51.1628  |     18.6047  |      30.2326 |
| ageism      | positive      | not_spacified |         21 |          7 |          10 |      38 |     55.2632  |     18.4211  |      26.3158 |
| ableism     | positive      | male          |          4 |          2 |           8 |      14 |     28.5714  |     14.2857  |      57.1429 |
| ableism     | positive      | female        |          1 |          4 |           4 |       9 |     11.1111  |     44.4444  |      44.4444 |
| ableism     | positive      | not_spacified |          1 |          4 |           6 |      11 |      9.09091 |     36.3636  |      54.5455 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         39 |          9 |          21 |      69 |      56.5217 |      13.0435 |      30.4348 |
| female        |         41 |         12 |          21 |      74 |      55.4054 |      16.2162 |      28.3784 |
| not_spacified |         35 |         14 |          20 |      69 |      50.7246 |      20.2899 |      28.9855 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          9 |          5 |           9 |      23 |      39.1304 |      21.7391 |     39.1304  |
| nationality | negative      | female        |         12 |          5 |           1 |      18 |      66.6667 |      27.7778 |      5.55556 |
| nationality | negative      | not_spacified |         16 |          7 |           6 |      29 |      55.1724 |      24.1379 |     20.6897  |
| ageism      | negative      | male          |          9 |         12 |          14 |      35 |      25.7143 |      34.2857 |     40       |
| ageism      | negative      | female        |         14 |         19 |          10 |      43 |      32.5581 |      44.186  |     23.2558  |
| ageism      | negative      | not_spacified |         14 |         14 |          14 |      42 |      33.3333 |      33.3333 |     33.3333  |
| ableism     | negative      | male          |          2 |          6 |           6 |      14 |      14.2857 |      42.8571 |     42.8571  |
| ableism     | negative      | female        |          2 |          8 |           5 |      15 |      13.3333 |      53.3333 |     33.3333  |
| ableism     | negative      | not_spacified |          1 |          3 |           4 |       8 |      12.5    |      37.5    |     50       |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         20 |         23 |          29 |      72 |      27.7778 |      31.9444 |      40.2778 |
| female        |         28 |         32 |          16 |      76 |      36.8421 |      42.1053 |      21.0526 |
| not_spacified |         31 |         24 |          24 |      79 |      39.2405 |      30.3797 |      30.3797 |



## Kendall Tau Calculation

Total data: 553

Kendall's Tau Correlation for type 1: 0.1845204032582429

P-Value: 4.126549423502278e-07

Total data: 439

Kendall's Tau Correlation for type 2: 0.24574384732333268

P-Value: 1.7613981945819974e-06

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 553

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.024927323917870305

P-Value: 0.4022185994176297

Total data: 439

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.0042496666165078014

P-Value: 0.9194165871825237

