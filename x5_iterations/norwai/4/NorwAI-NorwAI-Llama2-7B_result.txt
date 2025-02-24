# Report for Model: NorwAI/NorwAI-Llama2-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         57 |         38 |          33 |     128 |      44.5312 |     29.6875  |      25.7812 |
| ageism      | positive      |         54 |          7 |          10 |      71 |      76.0563 |      9.85915 |      14.0845 |
| ableism     | positive      |         28 |         19 |          12 |      59 |      47.4576 |     32.2034  |      20.339  |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         57 |         34 |          25 |     116 |      49.1379 |      29.3103 |      21.5517 |
| ageism      | negative      |         45 |          7 |          12 |      64 |      70.3125 |      10.9375 |      18.75   |
| ableism     | negative      |         34 |         12 |           8 |      54 |      62.963  |      22.2222 |      14.8148 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        114 |         72 |          58 |     244 | 46.7213 | 29.5082 | 23.7705 |
| ageism      |         99 |         14 |          22 |     135 | 73.3333 | 10.3704 | 16.2963 |
| ableism     |         62 |         31 |          20 |     113 | 54.8673 | 27.4336 | 17.6991 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         37 |          9 |           5 |      51 |      72.549  |      17.6471 |      9.80392 |
| ageism      | positive      |         21 |         48 |          45 |     114 |      18.4211 |      42.1053 |     39.4737  |
| ableism     | positive      |          8 |          7 |          16 |      31 |      25.8065 |      22.5806 |     51.6129  |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         31 |         15 |          12 |      58 |      53.4483 |      25.8621 |      20.6897 |
| ageism      | negative      |         30 |         39 |          51 |     120 |      25      |      32.5    |      42.5    |
| ableism     | negative      |          8 |          7 |          16 |      31 |      25.8065 |      22.5806 |      51.6129 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         68 |         24 |          17 |     109 | 62.3853 | 22.0183 | 15.5963 |
| ageism      |         51 |         87 |          96 |     234 | 21.7949 | 37.1795 | 41.0256 |
| ableism     |         16 |         14 |          32 |      62 | 25.8065 | 22.5806 | 51.6129 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         21 |         10 |           3 |      34 |      61.7647 |     29.4118  |      8.82353 |
| nationality | positive      | female        |         19 |         15 |          13 |      47 |      40.4255 |     31.9149  |     27.6596  |
| nationality | positive      | not_spacified |         17 |         13 |          17 |      47 |      36.1702 |     27.6596  |     36.1702  |
| ageism      | positive      | male          |         23 |          2 |           5 |      30 |      76.6667 |      6.66667 |     16.6667  |
| ageism      | positive      | female        |         12 |          1 |           2 |      15 |      80      |      6.66667 |     13.3333  |
| ageism      | positive      | not_spacified |         19 |          4 |           3 |      26 |      73.0769 |     15.3846  |     11.5385  |
| ableism     | positive      | male          |          8 |          5 |           3 |      16 |      50      |     31.25    |     18.75    |
| ableism     | positive      | female        |         10 |          7 |           3 |      20 |      50      |     35       |     15       |
| ableism     | positive      | not_spacified |         10 |          7 |           6 |      23 |      43.4783 |     30.4348  |     26.087   |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         52 |         17 |          11 |      80 |      65      |      21.25   |      13.75   |
| female        |         41 |         23 |          18 |      82 |      50      |      28.0488 |      21.9512 |
| not_spacified |         46 |         24 |          26 |      96 |      47.9167 |      25      |      27.0833 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         15 |         10 |           8 |      33 |      45.4545 |     30.303   |     24.2424  |
| nationality | negative      | female        |         22 |         12 |          11 |      45 |      48.8889 |     26.6667  |     24.4444  |
| nationality | negative      | not_spacified |         20 |         12 |           6 |      38 |      52.6316 |     31.5789  |     15.7895  |
| ageism      | negative      | male          |         17 |          2 |           5 |      24 |      70.8333 |      8.33333 |     20.8333  |
| ageism      | negative      | female        |         18 |          2 |           3 |      23 |      78.2609 |      8.69565 |     13.0435  |
| ageism      | negative      | not_spacified |         10 |          3 |           4 |      17 |      58.8235 |     17.6471  |     23.5294  |
| ableism     | negative      | male          |          9 |          6 |           3 |      18 |      50      |     33.3333  |     16.6667  |
| ableism     | negative      | female        |         16 |          3 |           2 |      21 |      76.1905 |     14.2857  |      9.52381 |
| ableism     | negative      | not_spacified |          9 |          3 |           3 |      15 |      60      |     20       |     20       |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         41 |         18 |          16 |      75 |      54.6667 |      24      |      21.3333 |
| female        |         56 |         17 |          16 |      89 |      62.9213 |      19.1011 |      17.9775 |
| not_spacified |         39 |         18 |          13 |      70 |      55.7143 |      25.7143 |      18.5714 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         14 |          3 |           1 |      18 |     77.7778  |      16.6667 |      5.55556 |
| nationality | positive      | female        |         13 |          2 |           3 |      18 |     72.2222  |      11.1111 |     16.6667  |
| nationality | positive      | not_spacified |         10 |          4 |           1 |      15 |     66.6667  |      26.6667 |      6.66667 |
| ageism      | positive      | male          |          2 |         19 |          12 |      33 |      6.06061 |      57.5758 |     36.3636  |
| ageism      | positive      | female        |         12 |         16 |          15 |      43 |     27.907   |      37.2093 |     34.8837  |
| ageism      | positive      | not_spacified |          7 |         13 |          18 |      38 |     18.4211  |      34.2105 |     47.3684  |
| ableism     | positive      | male          |          4 |          4 |           5 |      13 |     30.7692  |      30.7692 |     38.4615  |
| ableism     | positive      | female        |          1 |          1 |           6 |       8 |     12.5     |      12.5    |     75       |
| ableism     | positive      | not_spacified |          3 |          2 |           5 |      10 |     30       |      20      |     50       |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         20 |         26 |          18 |      64 |      31.25   |      40.625  |      28.125  |
| female        |         26 |         19 |          24 |      69 |      37.6812 |      27.5362 |      34.7826 |
| not_spacified |         20 |         19 |          24 |      63 |      31.746  |      30.1587 |      38.0952 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         15 |          2 |           5 |      22 |      68.1818 |      9.09091 |      22.7273 |
| nationality | negative      | female        |          5 |          6 |           3 |      14 |      35.7143 |     42.8571  |      21.4286 |
| nationality | negative      | not_spacified |         11 |          7 |           4 |      22 |      50      |     31.8182  |      18.1818 |
| ageism      | negative      | male          |          8 |         11 |          16 |      35 |      22.8571 |     31.4286  |      45.7143 |
| ageism      | negative      | female        |          8 |         13 |          22 |      43 |      18.6047 |     30.2326  |      51.1628 |
| ageism      | negative      | not_spacified |         14 |         15 |          13 |      42 |      33.3333 |     35.7143  |      30.9524 |
| ableism     | negative      | male          |          3 |          3 |           6 |      12 |      25      |     25       |      50      |
| ableism     | negative      | female        |          3 |          3 |           7 |      13 |      23.0769 |     23.0769  |      53.8462 |
| ableism     | negative      | not_spacified |          2 |          1 |           3 |       6 |      33.3333 |     16.6667  |      50      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         26 |         16 |          27 |      69 |      37.6812 |      23.1884 |      39.1304 |
| female        |         16 |         22 |          32 |      70 |      22.8571 |      31.4286 |      45.7143 |
| not_spacified |         27 |         23 |          20 |      70 |      38.5714 |      32.8571 |      28.5714 |



## Kendall Tau Calculation

Total data: 492

Kendall's Tau Correlation for type 1: -0.04175755172185868

P-Value: 0.3707879824350212

Total data: 405

Kendall's Tau Correlation for type 2: -0.018533760097546106

P-Value: 0.7319019677594435

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 492

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: -0.016793079516161016

P-Value: 0.6596313579738399

Total data: 405

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.011138545953360768

P-Value: 0.8010014107248917

