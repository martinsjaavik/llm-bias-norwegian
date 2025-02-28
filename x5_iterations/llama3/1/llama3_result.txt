# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         57 |         32 |          21 |     110 |      51.8182 |      29.0909 |      19.0909 |
| ageism      | positive      |         26 |         12 |          12 |      50 |      52      |      24      |      24      |
| ableism     | positive      |         22 |         23 |          11 |      56 |      39.2857 |      41.0714 |      19.6429 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         31 |         59 |          19 |     109 |      28.4404 |      54.1284 |      17.4312 |
| ageism      | negative      |         21 |         35 |           9 |      65 |      32.3077 |      53.8462 |      13.8462 |
| ableism     | negative      |         13 |         27 |          17 |      57 |      22.807  |      47.3684 |      29.8246 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         88 |         91 |          40 |     219 | 40.1826 | 41.5525 | 18.2648 |
| ageism      |         47 |         47 |          21 |     115 | 40.8696 | 40.8696 | 18.2609 |
| ableism     |         35 |         50 |          28 |     113 | 30.9735 | 44.2478 | 24.7788 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         31 |          8 |           8 |      47 |      65.9574 |      17.0213 |      17.0213 |
| ageism      | positive      |         25 |         52 |          30 |     107 |      23.3645 |      48.5981 |      28.0374 |
| ableism     | positive      |          9 |          6 |           9 |      24 |      37.5    |      25      |      37.5    |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         23 |         14 |          11 |      48 |     47.9167  |      29.1667 |      22.9167 |
| ageism      | negative      |         30 |         58 |          24 |     112 |     26.7857  |      51.7857 |      21.4286 |
| ableism     | negative      |          1 |         20 |           5 |      26 |      3.84615 |      76.9231 |      19.2308 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         54 |         22 |          19 |      95 | 56.8421 | 23.1579 | 20      |
| ageism      |         55 |        110 |          54 |     219 | 25.1142 | 50.2283 | 24.6575 |
| ableism     |         10 |         26 |          14 |      50 | 20      | 52      | 28      |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         14 |          9 |           9 |      32 |      43.75   |      28.125  |      28.125  |
| nationality | positive      | female        |         22 |         11 |           7 |      40 |      55      |      27.5    |      17.5    |
| nationality | positive      | not_spacified |         21 |         12 |           5 |      38 |      55.2632 |      31.5789 |      13.1579 |
| ageism      | positive      | male          |         12 |          5 |           4 |      21 |      57.1429 |      23.8095 |      19.0476 |
| ageism      | positive      | female        |          4 |          1 |           0 |       5 |      80      |      20      |       0      |
| ageism      | positive      | not_spacified |         10 |          6 |           8 |      24 |      41.6667 |      25      |      33.3333 |
| ableism     | positive      | male          |          3 |         10 |           3 |      16 |      18.75   |      62.5    |      18.75   |
| ableism     | positive      | female        |          9 |          6 |           4 |      19 |      47.3684 |      31.5789 |      21.0526 |
| ableism     | positive      | not_spacified |         10 |          7 |           4 |      21 |      47.619  |      33.3333 |      19.0476 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         29 |         24 |          16 |      69 |      42.029  |      34.7826 |      23.1884 |
| female        |         35 |         18 |          11 |      64 |      54.6875 |      28.125  |      17.1875 |
| not_spacified |         41 |         25 |          17 |      83 |      49.3976 |      30.1205 |      20.4819 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          4 |         23 |           6 |      33 |      12.1212 |      69.697  |      18.1818 |
| nationality | negative      | female        |         14 |         23 |           7 |      44 |      31.8182 |      52.2727 |      15.9091 |
| nationality | negative      | not_spacified |         13 |         13 |           6 |      32 |      40.625  |      40.625  |      18.75   |
| ageism      | negative      | male          |          8 |          9 |           4 |      21 |      38.0952 |      42.8571 |      19.0476 |
| ageism      | negative      | female        |          8 |         11 |           4 |      23 |      34.7826 |      47.8261 |      17.3913 |
| ageism      | negative      | not_spacified |          5 |         15 |           1 |      21 |      23.8095 |      71.4286 |       4.7619 |
| ableism     | negative      | male          |          3 |          8 |           6 |      17 |      17.6471 |      47.0588 |      35.2941 |
| ableism     | negative      | female        |         10 |          8 |           7 |      25 |      40      |      32      |      28      |
| ableism     | negative      | not_spacified |          0 |         11 |           4 |      15 |       0      |      73.3333 |      26.6667 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         15 |         40 |          16 |      71 |      21.1268 |      56.338  |      22.5352 |
| female        |         32 |         42 |          18 |      92 |      34.7826 |      45.6522 |      19.5652 |
| not_spacified |         18 |         39 |          11 |      68 |      26.4706 |      57.3529 |      16.1765 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         11 |          3 |           3 |      17 |      64.7059 |      17.6471 |     17.6471  |
| nationality | positive      | female        |         10 |          3 |           4 |      17 |      58.8235 |      17.6471 |     23.5294  |
| nationality | positive      | not_spacified |         10 |          2 |           1 |      13 |      76.9231 |      15.3846 |      7.69231 |
| ageism      | positive      | male          |          3 |         20 |           7 |      30 |      10      |      66.6667 |     23.3333  |
| ageism      | positive      | female        |         11 |         15 |          16 |      42 |      26.1905 |      35.7143 |     38.0952  |
| ageism      | positive      | not_spacified |         11 |         17 |           7 |      35 |      31.4286 |      48.5714 |     20       |
| ableism     | positive      | male          |          3 |          3 |           4 |      10 |      30      |      30      |     40       |
| ableism     | positive      | female        |          2 |          1 |           2 |       5 |      40      |      20      |     40       |
| ableism     | positive      | not_spacified |          4 |          2 |           3 |       9 |      44.4444 |      22.2222 |     33.3333  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         17 |         26 |          14 |      57 |      29.8246 |      45.614  |      24.5614 |
| female        |         23 |         19 |          22 |      64 |      35.9375 |      29.6875 |      34.375  |
| not_spacified |         25 |         21 |          11 |      57 |      43.8596 |      36.8421 |      19.2982 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          7 |          5 |           4 |      16 |      43.75   |      31.25   |      25      |
| nationality | negative      | female        |          4 |          6 |           5 |      15 |      26.6667 |      40      |      33.3333 |
| nationality | negative      | not_spacified |         12 |          3 |           2 |      17 |      70.5882 |      17.6471 |      11.7647 |
| ageism      | negative      | male          |          8 |         18 |           7 |      33 |      24.2424 |      54.5455 |      21.2121 |
| ageism      | negative      | female        |         13 |         21 |           7 |      41 |      31.7073 |      51.2195 |      17.0732 |
| ageism      | negative      | not_spacified |          9 |         19 |          10 |      38 |      23.6842 |      50      |      26.3158 |
| ableism     | negative      | male          |          0 |          8 |           3 |      11 |       0      |      72.7273 |      27.2727 |
| ableism     | negative      | female        |          0 |          8 |           1 |       9 |       0      |      88.8889 |      11.1111 |
| ableism     | negative      | not_spacified |          1 |          4 |           1 |       6 |      16.6667 |      66.6667 |      16.6667 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         15 |         31 |          14 |      60 |      25      |      51.6667 |      23.3333 |
| female        |         17 |         35 |          13 |      65 |      26.1538 |      53.8462 |      20      |
| not_spacified |         22 |         26 |          13 |      61 |      36.0656 |      42.623  |      21.3115 |



## Kendall Tau Calculation

Total data: 447

Kendall's Tau Correlation for type 1: 0.2507194370623946

P-Value: 7.824499789713268e-07

Total data: 364

Kendall's Tau Correlation for type 2: 0.12564907619852675

P-Value: 0.026166265675661972

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 447

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.07358527393660946

P-Value: 0.07586077494855058

Total data: 364

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.04111822243690375

P-Value: 0.3727433415622504

