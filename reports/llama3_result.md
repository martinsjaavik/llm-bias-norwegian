# Report for Model: llama3

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        297 |        223 |         124 |     644 |      46.118  |      34.6273 |      19.2547 |
| ageism      | positive      |        115 |        129 |          58 |     302 |      38.0795 |      42.7152 |      19.2053 |
| ableism     | positive      |         87 |        151 |          76 |     314 |      27.707  |      48.0892 |      24.2038 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        124 |        454 |         140 |     718 |      17.2702 |      63.2312 |      19.4986 |
| ageism      | negative      |         93 |        180 |          58 |     331 |      28.0967 |      54.3807 |      17.5227 |
| ableism     | negative      |         52 |        180 |          75 |     307 |      16.9381 |      58.6319 |      24.43   |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        421 |        677 |         264 |    1362 | 30.9104 | 49.7063 | 19.3833 |
| ageism      |        208 |        309 |         116 |     633 | 32.8594 | 48.8152 | 18.3254 |
| ableism     |        139 |        331 |         151 |     621 | 22.3833 | 53.3011 | 24.3156 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        195 |         31 |          35 |     261 |      74.7126 |      11.8774 |      13.41   |
| ageism      | positive      |         91 |        219 |         113 |     423 |      21.513  |      51.773  |      26.7139 |
| ableism     | positive      |         40 |         56 |          58 |     154 |      25.974  |      36.3636 |      37.6623 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        124 |        108 |          49 |     281 |      44.1281 |      38.4342 |      17.4377 |
| ageism      | negative      |         99 |        225 |          81 |     405 |      24.4444 |      55.5556 |      20      |
| ableism     | negative      |         17 |        114 |          36 |     167 |      10.1796 |      68.2635 |      21.5569 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        319 |        139 |          84 |     542 | 58.8561 | 25.6458 | 15.4982 |
| ageism      |        190 |        444 |         194 |     828 | 22.9469 | 53.6232 | 23.43   |
| ableism     |         57 |        170 |          94 |     321 | 17.757  | 52.9595 | 29.2835 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         78 |         92 |          44 |     214 |      36.4486 |      42.9907 |      20.5607 |
| nationality | positive      | female        |        113 |         62 |          42 |     217 |      52.0737 |      28.5714 |      19.3548 |
| nationality | positive      | not_spacified |        106 |         69 |          38 |     213 |      49.7653 |      32.3944 |      17.8404 |
| ageism      | positive      | male          |         49 |         34 |          16 |      99 |      49.4949 |      34.3434 |      16.1616 |
| ageism      | positive      | female        |         42 |         47 |          19 |     108 |      38.8889 |      43.5185 |      17.5926 |
| ageism      | positive      | not_spacified |         24 |         48 |          23 |      95 |      25.2632 |      50.5263 |      24.2105 |
| ableism     | positive      | male          |         24 |         56 |          28 |     108 |      22.2222 |      51.8519 |      25.9259 |
| ableism     | positive      | female        |         37 |         44 |          26 |     107 |      34.5794 |      41.1215 |      24.2991 |
| ableism     | positive      | not_spacified |         26 |         51 |          22 |      99 |      26.2626 |      51.5152 |      22.2222 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        151 |        182 |          88 |     421 |      35.867  |      43.2304 |      20.9026 |
| female        |        192 |        153 |          87 |     432 |      44.4444 |      35.4167 |      20.1389 |
| not_spacified |        156 |        168 |          83 |     407 |      38.3292 |      41.2776 |      20.3931 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         31 |        177 |          40 |     248 |      12.5    |      71.371  |      16.129  |
| nationality | negative      | female        |         51 |        137 |          52 |     240 |      21.25   |      57.0833 |      21.6667 |
| nationality | negative      | not_spacified |         42 |        140 |          48 |     230 |      18.2609 |      60.8696 |      20.8696 |
| ageism      | negative      | male          |         35 |         63 |          20 |     118 |      29.661  |      53.3898 |      16.9492 |
| ageism      | negative      | female        |         27 |         57 |          27 |     111 |      24.3243 |      51.3514 |      24.3243 |
| ageism      | negative      | not_spacified |         31 |         60 |          11 |     102 |      30.3922 |      58.8235 |      10.7843 |
| ableism     | negative      | male          |         11 |         60 |          30 |     101 |      10.8911 |      59.4059 |      29.703  |
| ableism     | negative      | female        |         19 |         62 |          23 |     104 |      18.2692 |      59.6154 |      22.1154 |
| ableism     | negative      | not_spacified |         22 |         58 |          22 |     102 |      21.5686 |      56.8627 |      21.5686 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         77 |        300 |          90 |     467 |      16.4882 |      64.2398 |      19.2719 |
| female        |         97 |        256 |         102 |     455 |      21.3187 |      56.2637 |      22.4176 |
| not_spacified |         95 |        258 |          81 |     434 |      21.8894 |      59.447  |      18.6636 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         66 |         12 |          12 |      90 |      73.3333 |     13.3333  |      13.3333 |
| nationality | positive      | female        |         69 |          8 |          13 |      90 |      76.6667 |      8.88889 |      14.4444 |
| nationality | positive      | not_spacified |         60 |         11 |          10 |      81 |      74.0741 |     13.5802  |      12.3457 |
| ageism      | positive      | male          |         26 |         80 |          39 |     145 |      17.931  |     55.1724  |      26.8966 |
| ageism      | positive      | female        |         38 |         67 |          43 |     148 |      25.6757 |     45.2703  |      29.0541 |
| ageism      | positive      | not_spacified |         27 |         72 |          31 |     130 |      20.7692 |     55.3846  |      23.8462 |
| ableism     | positive      | male          |         10 |         23 |          21 |      54 |      18.5185 |     42.5926  |      38.8889 |
| ableism     | positive      | female        |         16 |         17 |          20 |      53 |      30.1887 |     32.0755  |      37.7358 |
| ableism     | positive      | not_spacified |         14 |         16 |          17 |      47 |      29.7872 |     34.0426  |      36.1702 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        102 |        115 |          72 |     289 |      35.2941 |      39.7924 |      24.9135 |
| female        |        123 |         92 |          76 |     291 |      42.268  |      31.6151 |      26.1168 |
| not_spacified |        101 |         99 |          58 |     258 |      39.1473 |      38.3721 |      22.4806 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         47 |         31 |          16 |      94 |     50       |      32.9787 |      17.0213 |
| nationality | negative      | female        |         43 |         42 |          21 |     106 |     40.566   |      39.6226 |      19.8113 |
| nationality | negative      | not_spacified |         34 |         35 |          12 |      81 |     41.9753  |      43.2099 |      14.8148 |
| ageism      | negative      | male          |         29 |         82 |          26 |     137 |     21.1679  |      59.854  |      18.9781 |
| ageism      | negative      | female        |         39 |         68 |          34 |     141 |     27.6596  |      48.227  |      24.1135 |
| ageism      | negative      | not_spacified |         31 |         75 |          21 |     127 |     24.4094  |      59.0551 |      16.5354 |
| ableism     | negative      | male          |          6 |         36 |          15 |      57 |     10.5263  |      63.1579 |      26.3158 |
| ableism     | negative      | female        |          7 |         33 |          14 |      54 |     12.963   |      61.1111 |      25.9259 |
| ableism     | negative      | not_spacified |          4 |         45 |           7 |      56 |      7.14286 |      80.3571 |      12.5    |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         82 |        149 |          57 |     288 |      28.4722 |      51.7361 |      19.7917 |
| female        |         89 |        143 |          69 |     301 |      29.5681 |      47.5083 |      22.9236 |
| not_spacified |         69 |        155 |          40 |     264 |      26.1364 |      58.7121 |      15.1515 |



## Kendall Tau Calculation

Total data: 2633

Kendall's Tau Correlation for type 1: 0.24023463334356987

P-Value: 2.414536592741138e-31

Total data: 1950

Kendall's Tau Correlation for type 2: 0.1540302432610125

P-Value: 3.755954320379722e-10

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 2633

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.061924023997037794

P-Value: 0.00023811146072176624

Total data: 1950

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.03704615384615385

P-Value: 0.06499110298758103

