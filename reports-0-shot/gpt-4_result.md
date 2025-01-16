# Report for Model: gpt-4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        687 |         19 |         141 |     847 |      81.1098 |      2.24321 |      16.647  |
| ageism      | positive      |        340 |          5 |          79 |     424 |      80.1887 |      1.17925 |      18.6321 |
| ableism     | positive      |        251 |         35 |         110 |     396 |      63.3838 |      8.83838 |      27.7778 |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        641 |         48 |         154 |     843 |      76.038  |      5.69395 |      18.2681 |
| ageism      | negative      |        280 |         52 |          80 |     412 |      67.9612 |     12.6214  |      19.4175 |
| ableism     | negative      |        241 |         27 |         125 |     393 |      61.3232 |      6.87023 |      31.8066 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |       1328 |         67 |         295 |    1690 | 78.5799 | 3.9645  | 17.4556 |
| ageism      |        620 |         57 |         159 |     836 | 74.1627 | 6.81818 | 19.0191 |
| ableism     |        492 |         62 |         235 |     789 | 62.3574 | 7.85805 | 29.7845 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        276 |         29 |          89 |     394 |      70.0508 |      7.36041 |      22.5888 |
| ageism      | positive      |        259 |        120 |         269 |     648 |      39.9691 |     18.5185  |      41.5123 |
| ableism     | positive      |         25 |         39 |         128 |     192 |      13.0208 |     20.3125  |      66.6667 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        178 |        110 |          72 |     360 |      49.4444 |      30.5556 |      20      |
| ageism      | negative      |        143 |        307 |         185 |     635 |      22.5197 |      48.3465 |      29.1339 |
| ableism     | negative      |         17 |         81 |         119 |     217 |       7.8341 |      37.3272 |      54.8387 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        454 |        139 |         161 |     754 | 60.2122 | 18.435  | 21.3528 |
| ageism      |        402 |        427 |         454 |    1283 | 31.3328 | 33.2814 | 35.3858 |
| ableism     |         42 |        120 |         247 |     409 | 10.2689 | 29.3399 | 60.3912 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        225 |          8 |          48 |     281 |      80.0712 |     2.84698  |      17.0819 |
| nationality | positive      | female        |        239 |          4 |          39 |     282 |      84.7518 |     1.41844  |      13.8298 |
| nationality | positive      | not_spacified |        223 |          7 |          54 |     284 |      78.5211 |     2.46479  |      19.0141 |
| ageism      | positive      | male          |        110 |          1 |          29 |     140 |      78.5714 |     0.714286 |      20.7143 |
| ageism      | positive      | female        |        120 |          1 |          21 |     142 |      84.507  |     0.704225 |      14.7887 |
| ageism      | positive      | not_spacified |        110 |          3 |          29 |     142 |      77.4648 |     2.11268  |      20.4225 |
| ableism     | positive      | male          |         77 |         16 |          39 |     132 |      58.3333 |    12.1212   |      29.5455 |
| ableism     | positive      | female        |         91 |          5 |          36 |     132 |      68.9394 |     3.78788  |      27.2727 |
| ableism     | positive      | not_spacified |         83 |         14 |          35 |     132 |      62.8788 |    10.6061   |      26.5152 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        412 |         25 |         116 |     553 |      74.5027 |      4.5208  |      20.9765 |
| female        |        450 |         10 |          96 |     556 |      80.9353 |      1.79856 |      17.2662 |
| not_spacified |        416 |         24 |         118 |     558 |      74.552  |      4.30108 |      21.147  |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |        197 |         20 |          64 |     281 |      70.1068 |      7.11744 |      22.7758 |
| nationality | negative      | female        |        233 |         10 |          39 |     282 |      82.6241 |      3.5461  |      13.8298 |
| nationality | negative      | not_spacified |        211 |         18 |          51 |     280 |      75.3571 |      6.42857 |      18.2143 |
| ageism      | negative      | male          |         94 |         21 |          24 |     139 |      67.6259 |     15.1079  |      17.2662 |
| ageism      | negative      | female        |         95 |         14 |          29 |     138 |      68.8406 |     10.1449  |      21.0145 |
| ageism      | negative      | not_spacified |         91 |         17 |          27 |     135 |      67.4074 |     12.5926  |      20      |
| ableism     | negative      | male          |         64 |         12 |          55 |     131 |      48.855  |      9.16031 |      41.9847 |
| ableism     | negative      | female        |         88 |          5 |          39 |     132 |      66.6667 |      3.78788 |      29.5455 |
| ableism     | negative      | not_spacified |         89 |         10 |          31 |     130 |      68.4615 |      7.69231 |      23.8462 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        355 |         53 |         143 |     551 |      64.4283 |      9.61887 |      25.9528 |
| female        |        416 |         29 |         107 |     552 |      75.3623 |      5.25362 |      19.3841 |
| not_spacified |        391 |         45 |         109 |     545 |      71.7431 |      8.25688 |      20      |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         94 |         10 |          28 |     132 |      71.2121 |      7.57576 |      21.2121 |
| nationality | positive      | female        |         94 |          8 |          29 |     131 |      71.7557 |      6.10687 |      22.1374 |
| nationality | positive      | not_spacified |         88 |         11 |          32 |     131 |      67.1756 |      8.39695 |      24.4275 |
| ageism      | positive      | male          |         70 |         38 |         108 |     216 |      32.4074 |     17.5926  |      50      |
| ageism      | positive      | female        |         90 |         35 |          91 |     216 |      41.6667 |     16.2037  |      42.1296 |
| ageism      | positive      | not_spacified |         99 |         47 |          70 |     216 |      45.8333 |     21.7593  |      32.4074 |
| ableism     | positive      | male          |          7 |         15 |          43 |      65 |      10.7692 |     23.0769  |      66.1538 |
| ableism     | positive      | female        |          7 |         17 |          41 |      65 |      10.7692 |     26.1538  |      63.0769 |
| ableism     | positive      | not_spacified |         11 |          7 |          44 |      62 |      17.7419 |     11.2903  |      70.9677 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        171 |         63 |         179 |     413 |      41.4044 |      15.2542 |      43.3414 |
| female        |        191 |         60 |         161 |     412 |      46.3592 |      14.5631 |      39.0777 |
| not_spacified |        198 |         65 |         146 |     409 |      48.4108 |      15.8924 |      35.6968 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         59 |         37 |          26 |     122 |     48.3607  |      30.3279 |      21.3115 |
| nationality | negative      | female        |         60 |         38 |          17 |     115 |     52.1739  |      33.0435 |      14.7826 |
| nationality | negative      | not_spacified |         59 |         35 |          29 |     123 |     47.9675  |      28.4553 |      23.5772 |
| ageism      | negative      | male          |         37 |        110 |          66 |     213 |     17.3709  |      51.6432 |      30.9859 |
| ageism      | negative      | female        |         48 |         92 |          69 |     209 |     22.9665  |      44.0191 |      33.0144 |
| ageism      | negative      | not_spacified |         58 |        105 |          50 |     213 |     27.23    |      49.2958 |      23.4742 |
| ableism     | negative      | male          |          6 |         27 |          43 |      76 |      7.89474 |      35.5263 |      56.5789 |
| ableism     | negative      | female        |          1 |         29 |          42 |      72 |      1.38889 |      40.2778 |      58.3333 |
| ableism     | negative      | not_spacified |         10 |         25 |          34 |      69 |     14.4928  |      36.2319 |      49.2754 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        102 |        174 |         135 |     411 |      24.8175 |      42.3358 |      32.8467 |
| female        |        109 |        159 |         128 |     396 |      27.5253 |      40.1515 |      32.3232 |
| not_spacified |        127 |        165 |         113 |     405 |      31.358  |      40.7407 |      27.9012 |



## Kendall Tau Calculation

Total data: 3317

Kendall's Tau Correlation for type 1: 0.0690763699013923

P-Value: 7.659438842738196e-06

Total data: 2447

Kendall's Tau Correlation for type 2: 0.2893398904340469

P-Value: 1.201287609857158e-39

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 3317

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.060819965373289625

P-Value: 1.399957448428666e-06

Total data: 2447

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.02629242181906604

P-Value: 0.14254624331286442

