# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         46 |         36 |          27 |     109 |      42.2018 |      33.0275 |      24.7706 |
| ageism      | positive      |         31 |         14 |           6 |      51 |      60.7843 |      27.451  |      11.7647 |
| ableism     | positive      |         18 |         21 |          16 |      55 |      32.7273 |      38.1818 |      29.0909 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         28 |         67 |          18 |     113 |      24.7788 |      59.292  |     15.9292  |
| ageism      | negative      |         21 |         37 |           3 |      61 |      34.4262 |      60.6557 |      4.91803 |
| ableism     | negative      |         11 |         35 |          13 |      59 |      18.6441 |      59.322  |     22.0339  |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |      nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|---------:|
| nationality |         74 |        103 |          45 |     222 | 33.3333 | 46.3964 | 20.2703  |
| ageism      |         52 |         51 |           9 |     112 | 46.4286 | 45.5357 |  8.03571 |
| ableism     |         29 |         56 |          29 |     114 | 25.4386 | 49.1228 | 25.4386  |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         29 |          8 |          10 |      47 |      61.7021 |      17.0213 |      21.2766 |
| ageism      | positive      |         23 |         50 |          35 |     108 |      21.2963 |      46.2963 |      32.4074 |
| ableism     | positive      |          8 |          7 |          13 |      28 |      28.5714 |      25      |      46.4286 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         25 |         16 |           7 |      48 |     52.0833  |      33.3333 |      14.5833 |
| ageism      | negative      |         24 |         57 |          29 |     110 |     21.8182  |      51.8182 |      26.3636 |
| ableism     | negative      |          1 |         14 |           7 |      22 |      4.54545 |      63.6364 |      31.8182 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         54 |         24 |          17 |      95 | 56.8421 | 25.2632 | 17.8947 |
| ageism      |         47 |        107 |          64 |     218 | 21.5596 | 49.0826 | 29.3578 |
| ableism     |          9 |         21 |          20 |      50 | 18      | 42      | 40      |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          6 |         12 |          10 |      28 |      21.4286 |      42.8571 |     35.7143  |
| nationality | positive      | female        |         20 |         11 |          10 |      41 |      48.7805 |      26.8293 |     24.3902  |
| nationality | positive      | not_spacified |         20 |         13 |           7 |      40 |      50      |      32.5    |     17.5     |
| ageism      | positive      | male          |         13 |          6 |           2 |      21 |      61.9048 |      28.5714 |      9.52381 |
| ageism      | positive      | female        |          8 |          3 |           1 |      12 |      66.6667 |      25      |      8.33333 |
| ageism      | positive      | not_spacified |         10 |          5 |           3 |      18 |      55.5556 |      27.7778 |     16.6667  |
| ableism     | positive      | male          |          1 |         10 |           5 |      16 |       6.25   |      62.5    |     31.25    |
| ableism     | positive      | female        |          7 |          6 |           3 |      16 |      43.75   |      37.5    |     18.75    |
| ableism     | positive      | not_spacified |         10 |          5 |           8 |      23 |      43.4783 |      21.7391 |     34.7826  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         20 |         28 |          17 |      65 |      30.7692 |      43.0769 |      26.1538 |
| female        |         35 |         20 |          14 |      69 |      50.7246 |      28.9855 |      20.2899 |
| not_spacified |         40 |         23 |          18 |      81 |      49.3827 |      28.3951 |      22.2222 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          3 |         24 |           7 |      34 |      8.82353 |      70.5882 |     20.5882  |
| nationality | negative      | female        |         12 |         24 |           7 |      43 |     27.907   |      55.814  |     16.2791  |
| nationality | negative      | not_spacified |         13 |         19 |           4 |      36 |     36.1111  |      52.7778 |     11.1111  |
| ageism      | negative      | male          |          7 |         14 |           1 |      22 |     31.8182  |      63.6364 |      4.54545 |
| ageism      | negative      | female        |          8 |         13 |           0 |      21 |     38.0952  |      61.9048 |      0       |
| ageism      | negative      | not_spacified |          6 |         10 |           2 |      18 |     33.3333  |      55.5556 |     11.1111  |
| ableism     | negative      | male          |          2 |         12 |           2 |      16 |     12.5     |      75      |     12.5     |
| ableism     | negative      | female        |          8 |         11 |           7 |      26 |     30.7692  |      42.3077 |     26.9231  |
| ableism     | negative      | not_spacified |          1 |         12 |           4 |      17 |      5.88235 |      70.5882 |     23.5294  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         12 |         50 |          10 |      72 |      16.6667 |      69.4444 |      13.8889 |
| female        |         28 |         48 |          14 |      90 |      31.1111 |      53.3333 |      15.5556 |
| not_spacified |         20 |         41 |          10 |      71 |      28.169  |      57.7465 |      14.0845 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          7 |          4 |           5 |      16 |      43.75   |      25      |     31.25    |
| nationality | positive      | female        |         10 |          2 |           4 |      16 |      62.5    |      12.5    |     25       |
| nationality | positive      | not_spacified |         12 |          2 |           1 |      15 |      80      |      13.3333 |      6.66667 |
| ageism      | positive      | male          |          2 |         20 |          10 |      32 |       6.25   |      62.5    |     31.25    |
| ageism      | positive      | female        |         11 |         17 |          14 |      42 |      26.1905 |      40.4762 |     33.3333  |
| ageism      | positive      | not_spacified |         10 |         13 |          11 |      34 |      29.4118 |      38.2353 |     32.3529  |
| ableism     | positive      | male          |          3 |          4 |           4 |      11 |      27.2727 |      36.3636 |     36.3636  |
| ableism     | positive      | female        |          2 |          0 |           6 |       8 |      25      |       0      |     75       |
| ableism     | positive      | not_spacified |          3 |          3 |           3 |       9 |      33.3333 |      33.3333 |     33.3333  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         12 |         28 |          19 |      59 |      20.339  |      47.4576 |      32.2034 |
| female        |         23 |         19 |          24 |      66 |      34.8485 |      28.7879 |      36.3636 |
| not_spacified |         25 |         18 |          15 |      58 |      43.1034 |      31.0345 |      25.8621 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          6 |          5 |           4 |      15 |     40       |      33.3333 |     26.6667  |
| nationality | negative      | female        |         11 |          3 |           2 |      16 |     68.75    |      18.75   |     12.5     |
| nationality | negative      | not_spacified |          8 |          8 |           1 |      17 |     47.0588  |      47.0588 |      5.88235 |
| ageism      | negative      | male          |          3 |         22 |           8 |      33 |      9.09091 |      66.6667 |     24.2424  |
| ageism      | negative      | female        |          7 |         21 |          13 |      41 |     17.0732  |      51.2195 |     31.7073  |
| ageism      | negative      | not_spacified |         14 |         14 |           8 |      36 |     38.8889  |      38.8889 |     22.2222  |
| ableism     | negative      | male          |          0 |          5 |           2 |       7 |      0       |      71.4286 |     28.5714  |
| ableism     | negative      | female        |          0 |          7 |           2 |       9 |      0       |      77.7778 |     22.2222  |
| ableism     | negative      | not_spacified |          1 |          2 |           3 |       6 |     16.6667  |      33.3333 |     50       |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          9 |         32 |          14 |      55 |      16.3636 |      58.1818 |      25.4545 |
| female        |         18 |         31 |          17 |      66 |      27.2727 |      46.9697 |      25.7576 |
| not_spacified |         23 |         24 |          12 |      59 |      38.9831 |      40.678  |      20.339  |



## Kendall Tau Calculation

Total data: 448

Kendall's Tau Correlation for type 1: 0.27168367346938777

P-Value: 6.575649454209043e-08

Total data: 363

Kendall's Tau Correlation for type 2: 0.11841935508351736

P-Value: 0.03721610781577378

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 448

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.11400370695153061

P-Value: 0.00550219255564896

Total data: 363

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.10914555016733829

P-Value: 0.01859725183599835

