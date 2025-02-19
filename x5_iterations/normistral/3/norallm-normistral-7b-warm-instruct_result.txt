# Report for Model: norallm/normistral-7b-warm-instruct

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         65 |         37 |          24 |     126 |      51.5873 |      29.3651 |      19.0476 |
| ageism      | positive      |         53 |         12 |           9 |      74 |      71.6216 |      16.2162 |      12.1622 |
| ableism     | positive      |         25 |         21 |          10 |      56 |      44.6429 |      37.5    |      17.8571 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         59 |         39 |          14 |     112 |      52.6786 |      34.8214 |     12.5     |
| ageism      | negative      |         47 |         16 |           3 |      66 |      71.2121 |      24.2424 |      4.54545 |
| ableism     | negative      |         28 |         17 |          13 |      58 |      48.2759 |      29.3103 |     22.4138  |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |      nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|---------:|
| nationality |        124 |         76 |          38 |     238 | 52.1008 | 31.9328 | 15.9664  |
| ageism      |        100 |         28 |          12 |     140 | 71.4286 | 20      |  8.57143 |
| ableism     |         53 |         38 |          23 |     114 | 46.4912 | 33.3333 | 20.1754  |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |         25 |          6 |          28 |      59 |      42.3729 |      10.1695 |      47.4576 |
| ageism      | positive      |         31 |         40 |          41 |     112 |      27.6786 |      35.7143 |      36.6071 |
| ableism     | positive      |          6 |          8 |          13 |      27 |      22.2222 |      29.6296 |      48.1481 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |         33 |          9 |          25 |      67 |      49.2537 |      13.4328 |      37.3134 |
| ageism      | negative      |         57 |         36 |          26 |     119 |      47.8992 |      30.2521 |      21.8487 |
| ableism     | negative      |          4 |         17 |          12 |      33 |      12.1212 |      51.5152 |      36.3636 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |         58 |         15 |          53 |     126 | 46.0317 | 11.9048 | 42.0635 |
| ageism      |         88 |         76 |          67 |     231 | 38.0952 | 32.9004 | 29.0043 |
| ableism     |         10 |         25 |          25 |      60 | 16.6667 | 41.6667 | 41.6667 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         16 |         10 |           6 |      32 |      50      |      31.25   |     18.75    |
| nationality | positive      | female        |         28 |         14 |           7 |      49 |      57.1429 |      28.5714 |     14.2857  |
| nationality | positive      | not_spacified |         21 |         13 |          11 |      45 |      46.6667 |      28.8889 |     24.4444  |
| ageism      | positive      | male          |         23 |          5 |           4 |      32 |      71.875  |      15.625  |     12.5     |
| ageism      | positive      | female        |          9 |          4 |           1 |      14 |      64.2857 |      28.5714 |      7.14286 |
| ageism      | positive      | not_spacified |         21 |          3 |           4 |      28 |      75      |      10.7143 |     14.2857  |
| ableism     | positive      | male          |          8 |          5 |           2 |      15 |      53.3333 |      33.3333 |     13.3333  |
| ableism     | positive      | female        |          8 |          5 |           5 |      18 |      44.4444 |      27.7778 |     27.7778  |
| ableism     | positive      | not_spacified |          9 |         11 |           3 |      23 |      39.1304 |      47.8261 |     13.0435  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         47 |         20 |          12 |      79 |      59.4937 |      25.3165 |      15.1899 |
| female        |         45 |         23 |          13 |      81 |      55.5556 |      28.3951 |      16.0494 |
| not_spacified |         51 |         27 |          18 |      96 |      53.125  |      28.125  |      18.75   |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         15 |         14 |           6 |      35 |      42.8571 |      40      |     17.1429  |
| nationality | negative      | female        |         21 |         17 |           5 |      43 |      48.8372 |      39.5349 |     11.6279  |
| nationality | negative      | not_spacified |         23 |          8 |           3 |      34 |      67.6471 |      23.5294 |      8.82353 |
| ageism      | negative      | male          |         16 |          6 |           1 |      23 |      69.5652 |      26.087  |      4.34783 |
| ageism      | negative      | female        |         16 |          6 |           1 |      23 |      69.5652 |      26.087  |      4.34783 |
| ageism      | negative      | not_spacified |         15 |          4 |           1 |      20 |      75      |      20      |      5       |
| ableism     | negative      | male          |          4 |          6 |           6 |      16 |      25      |      37.5    |     37.5     |
| ableism     | negative      | female        |         16 |          5 |           5 |      26 |      61.5385 |      19.2308 |     19.2308  |
| ableism     | negative      | not_spacified |          8 |          6 |           2 |      16 |      50      |      37.5    |     12.5     |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         35 |         26 |          13 |      74 |      47.2973 |      35.1351 |     17.5676  |
| female        |         53 |         28 |          11 |      92 |      57.6087 |      30.4348 |     11.9565  |
| not_spacified |         46 |         18 |           6 |      70 |      65.7143 |      25.7143 |      8.57143 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |          9 |          3 |           9 |      21 |      42.8571 |      14.2857 |      42.8571 |
| nationality | positive      | female        |          8 |          0 |          12 |      20 |      40      |       0      |      60      |
| nationality | positive      | not_spacified |          8 |          3 |           7 |      18 |      44.4444 |      16.6667 |      38.8889 |
| ageism      | positive      | male          |          8 |         12 |          13 |      33 |      24.2424 |      36.3636 |      39.3939 |
| ageism      | positive      | female        |         12 |         15 |          15 |      42 |      28.5714 |      35.7143 |      35.7143 |
| ageism      | positive      | not_spacified |         11 |         13 |          13 |      37 |      29.7297 |      35.1351 |      35.1351 |
| ableism     | positive      | male          |          2 |          5 |           4 |      11 |      18.1818 |      45.4545 |      36.3636 |
| ableism     | positive      | female        |          0 |          1 |           7 |       8 |       0      |      12.5    |      87.5    |
| ableism     | positive      | not_spacified |          4 |          2 |           2 |       8 |      50      |      25      |      25      |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         19 |         20 |          26 |      65 |      29.2308 |      30.7692 |      40      |
| female        |         20 |         16 |          34 |      70 |      28.5714 |      22.8571 |      48.5714 |
| not_spacified |         23 |         18 |          22 |      63 |      36.5079 |      28.5714 |      34.9206 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |          8 |          3 |          11 |      22 |     36.3636  |     13.6364  |      50      |
| nationality | negative      | female        |          8 |          5 |           8 |      21 |     38.0952  |     23.8095  |      38.0952 |
| nationality | negative      | not_spacified |         17 |          1 |           6 |      24 |     70.8333  |      4.16667 |      25      |
| ageism      | negative      | male          |         20 |          9 |           6 |      35 |     57.1429  |     25.7143  |      17.1429 |
| ageism      | negative      | female        |         18 |         16 |           9 |      43 |     41.8605  |     37.2093  |      20.9302 |
| ageism      | negative      | not_spacified |         19 |         11 |          11 |      41 |     46.3415  |     26.8293  |      26.8293 |
| ableism     | negative      | male          |          1 |          6 |           4 |      11 |      9.09091 |     54.5455  |      36.3636 |
| ableism     | negative      | female        |          3 |          7 |           5 |      15 |     20       |     46.6667  |      33.3333 |
| ableism     | negative      | not_spacified |          0 |          4 |           3 |       7 |      0       |     57.1429  |      42.8571 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         29 |         18 |          21 |      68 |      42.6471 |      26.4706 |      30.8824 |
| female        |         29 |         28 |          22 |      79 |      36.7089 |      35.443  |      27.8481 |
| not_spacified |         36 |         16 |          20 |      72 |      50      |      22.2222 |      27.7778 |



## Kendall Tau Calculation

Total data: 492

Kendall's Tau Correlation for type 1: 0.007270804415361227

P-Value: 0.8754896105718784

Total data: 417

Kendall's Tau Correlation for type 2: -0.07710665999574441

P-Value: 0.14695789196362793

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 492

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.014723378941106485

P-Value: 0.6976745447978249

Total data: 417

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: -0.022945672239187066

P-Value: 0.5973766731223913

