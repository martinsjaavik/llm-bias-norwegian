# Report for Model: norallm/normistral-7b-warm-instruct

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         16 |         12 |           4 |      32 |      50      |       37.5   |      12.5    |
| ageism      | positive      |         15 |         11 |           3 |      29 |      51.7241 |       37.931 |      10.3448 |
| ableism     | positive      |          5 |          6 |           5 |      16 |      31.25   |       37.5   |      31.25   |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         15 |         10 |          11 |      36 |      41.6667 |      27.7778 |      30.5556 |
| ageism      | negative      |          8 |          9 |           2 |      19 |      42.1053 |      47.3684 |      10.5263 |
| ableism     | negative      |          5 |          6 |           5 |      16 |      31.25   |      37.5    |      31.25   |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         31 |         22 |          15 |      68 | 45.5882 | 32.3529 | 22.0588 |
| ageism      |         23 |         20 |           5 |      48 | 47.9167 | 41.6667 | 10.4167 |
| ableism     |         10 |         12 |          10 |      32 | 31.25   | 37.5    | 31.25   |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |          2 |          7 |           3 |      12 |      16.6667 |      58.3333 |      25      |
| ageism      | positive      |         17 |          4 |          16 |      37 |      45.9459 |      10.8108 |      43.2432 |
| ableism     | positive      |          3 |          2 |           5 |      10 |      30      |      20      |      50      |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |          6 |          7 |           3 |      16 |      37.5    |      43.75   |      18.75   |
| ageism      | negative      |          8 |          6 |          23 |      37 |      21.6216 |      16.2162 |      62.1622 |
| ableism     | negative      |          3 |          2 |           5 |      10 |      30      |      20      |      50      |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |          8 |         14 |           6 |      28 | 28.5714 | 50      | 21.4286 |
| ageism      |         25 |         10 |          39 |      74 | 33.7838 | 13.5135 | 52.7027 |
| ableism     |          6 |          4 |          10 |      20 | 30      | 20      | 50      |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          3 |          4 |           1 |       8 |      37.5    |      50      |     12.5     |
| nationality | positive      | female        |          5 |          5 |           1 |      11 |      45.4545 |      45.4545 |      9.09091 |
| nationality | positive      | not_spacified |          8 |          3 |           2 |      13 |      61.5385 |      23.0769 |     15.3846  |
| ageism      | positive      | male          |          6 |          9 |           1 |      16 |      37.5    |      56.25   |      6.25    |
| ageism      | positive      | female        |          2 |          1 |           2 |       5 |      40      |      20      |     40       |
| ageism      | positive      | not_spacified |          7 |          1 |           0 |       8 |      87.5    |      12.5    |      0       |
| ableism     | positive      | male          |          1 |          2 |           0 |       3 |      33.3333 |      66.6667 |      0       |
| ableism     | positive      | female        |          3 |          2 |           2 |       7 |      42.8571 |      28.5714 |     28.5714  |
| ableism     | positive      | not_spacified |          1 |          2 |           3 |       6 |      16.6667 |      33.3333 |     50       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         10 |         15 |           2 |      27 |      37.037  |      55.5556 |      7.40741 |
| female        |         10 |          8 |           5 |      23 |      43.4783 |      34.7826 |     21.7391  |
| not_spacified |         16 |          6 |           5 |      27 |      59.2593 |      22.2222 |     18.5185  |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          2 |          5 |           4 |      11 |      18.1818 |      45.4545 |      36.3636 |
| nationality | negative      | female        |          8 |          2 |           3 |      13 |      61.5385 |      15.3846 |      23.0769 |
| nationality | negative      | not_spacified |          5 |          3 |           4 |      12 |      41.6667 |      25      |      33.3333 |
| ageism      | negative      | male          |          1 |          3 |           1 |       5 |      20      |      60      |      20      |
| ageism      | negative      | female        |          4 |          2 |           0 |       6 |      66.6667 |      33.3333 |       0      |
| ageism      | negative      | not_spacified |          3 |          4 |           1 |       8 |      37.5    |      50      |      12.5    |
| ableism     | negative      | male          |          1 |          5 |           0 |       6 |      16.6667 |      83.3333 |       0      |
| ableism     | negative      | female        |          3 |          2 |           0 |       5 |      60      |      40      |       0      |
| ableism     | negative      | not_spacified |          2 |          2 |           0 |       4 |      50      |      50      |       0      |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          4 |         13 |           5 |      22 |      18.1818 |      59.0909 |      22.7273 |
| female        |         15 |          6 |           3 |      24 |      62.5    |      25      |      12.5    |
| not_spacified |         10 |          9 |           5 |      24 |      41.6667 |      37.5    |      20.8333 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          0 |          2 |           1 |       3 |       0      |      66.6667 |      33.3333 |
| nationality | positive      | female        |          0 |          4 |           2 |       6 |       0      |      66.6667 |      33.3333 |
| nationality | positive      | not_spacified |          2 |          1 |           0 |       3 |      66.6667 |      33.3333 |       0      |
| ageism      | positive      | male          |          6 |          0 |           2 |       8 |      75      |       0      |      25      |
| ageism      | positive      | female        |          6 |          2 |           9 |      17 |      35.2941 |      11.7647 |      52.9412 |
| ageism      | positive      | not_spacified |          5 |          2 |           5 |      12 |      41.6667 |      16.6667 |      41.6667 |
| ableism     | positive      | male          |          0 |          1 |           2 |       3 |       0      |      33.3333 |      66.6667 |
| ableism     | positive      | female        |          2 |          1 |           1 |       4 |      50      |      25      |      25      |
| ableism     | positive      | not_spacified |          1 |          0 |           2 |       3 |      33.3333 |       0      |      66.6667 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |          6 |          3 |           5 |      14 |      42.8571 |      21.4286 |      35.7143 |
| female        |          8 |          7 |          12 |      27 |      29.6296 |      25.9259 |      44.4444 |
| not_spacified |          8 |          3 |           7 |      18 |      44.4444 |      16.6667 |      38.8889 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          4 |          0 |           1 |       5 |      80      |      0       |      20      |
| nationality | negative      | female        |          1 |          3 |           1 |       5 |      20      |     60       |      20      |
| nationality | negative      | not_spacified |          1 |          4 |           1 |       6 |      16.6667 |     66.6667  |      16.6667 |
| ageism      | negative      | male          |          5 |          3 |           5 |      13 |      38.4615 |     23.0769  |      38.4615 |
| ageism      | negative      | female        |          2 |          1 |          11 |      14 |      14.2857 |      7.14286 |      78.5714 |
| ageism      | negative      | not_spacified |          1 |          2 |           7 |      10 |      10      |     20       |      70      |
| ableism     | negative      | male          |          1 |          1 |           2 |       4 |      25      |     25       |      50      |
| ableism     | negative      | female        |          1 |          2 |           2 |       5 |      20      |     40       |      40      |
| ableism     | negative      | not_spacified |          0 |          0 |           1 |       1 |       0      |      0       |     100      |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         10 |          4 |           8 |      22 |      45.4545 |      18.1818 |      36.3636 |
| female        |          4 |          6 |          14 |      24 |      16.6667 |      25      |      58.3333 |
| not_spacified |          2 |          6 |           9 |      17 |      11.7647 |      35.2941 |      52.9412 |



## Kendall Tau Calculation

Total data: 166

Kendall's Tau Correlation for type 1: 0.04224125417331979

P-Value: 0.6159578671654987

Total data: 127

Kendall's Tau Correlation for type 2: 0.11383222766445533

P-Value: 0.23093362870703016

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 166

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.1978153578168094

P-Value: 0.0040358803005665165

Total data: 127

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.12276024552049104

P-Value: 0.11228919691906886

