# Report for Model: norallm/normistral-7b-warm-instruct

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        361 |        207 |          80 |     648 |      55.7099 |      31.9444 |     12.3457  |
| ageism      | positive      |        222 |        149 |          38 |     409 |      54.2787 |      36.4303 |      9.29095 |
| ableism     | positive      |        128 |         86 |          83 |     297 |      43.0976 |      28.9562 |     27.9461  |



### Type 1, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        299 |        264 |          81 |     644 |      46.4286 |      40.9938 |      12.5776 |
| ageism      | negative      |        189 |        172 |          44 |     405 |      46.6667 |      42.4691 |      10.8642 |
| ableism     | negative      |        143 |        131 |          37 |     311 |      45.9807 |      42.1222 |      11.8971 |



### Type 1, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        660 |        471 |         161 |    1292 | 51.0836 | 36.4551 | 12.4613 |
| ageism      |        411 |        321 |          82 |     814 | 50.4914 | 39.4349 | 10.0737 |
| ableism     |        271 |        217 |         120 |     608 | 44.5724 | 35.6908 | 19.7368 |



### Type 2, Positive Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      |        118 |        119 |         107 |     344 |      34.3023 |      34.593  |      31.1047 |
| ageism      | positive      |        148 |        123 |         377 |     648 |      22.8395 |      18.9815 |      58.179  |
| ableism     | positive      |         63 |         38 |          60 |     161 |      39.1304 |      23.6025 |      37.2671 |



### Type 2, Negative Attribute

| bias_type   | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      |        104 |        166 |          92 |     362 |      28.7293 |      45.8564 |      25.4144 |
| ageism      | negative      |        187 |        119 |         342 |     648 |      28.858  |      18.3642 |      52.7778 |
| ableism     | negative      |         52 |         63 |          70 |     185 |      28.1081 |      34.0541 |      37.8378 |



### Type 2, Combined Attribute

| bias_type   |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| nationality |        222 |        285 |         199 |     706 | 31.4448 | 40.3683 | 28.187  |
| ageism      |        335 |        242 |         719 |    1296 | 25.8488 | 18.6728 | 55.4784 |
| ableism     |        115 |        101 |         130 |     346 | 33.237  | 29.1908 | 37.5723 |



### Type 1, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |        104 |         71 |          32 |     207 |      50.2415 |      34.2995 |     15.4589  |
| nationality | positive      | female        |        122 |         60 |          27 |     209 |      58.3732 |      28.7081 |     12.9187  |
| nationality | positive      | not_spacified |        135 |         76 |          21 |     232 |      58.1897 |      32.7586 |      9.05172 |
| ageism      | positive      | male          |         80 |         48 |          10 |     138 |      57.971  |      34.7826 |      7.24638 |
| ageism      | positive      | female        |         70 |         49 |          16 |     135 |      51.8519 |      36.2963 |     11.8519  |
| ageism      | positive      | not_spacified |         72 |         52 |          12 |     136 |      52.9412 |      38.2353 |      8.82353 |
| ableism     | positive      | male          |         43 |         29 |          25 |      97 |      44.3299 |      29.8969 |     25.7732  |
| ableism     | positive      | female        |         44 |         28 |          28 |     100 |      44      |      28      |     28       |
| ableism     | positive      | not_spacified |         41 |         29 |          30 |     100 |      41      |      29      |     30       |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        227 |        148 |          67 |     442 |      51.3575 |      33.4842 |      15.1584 |
| female        |        236 |        137 |          71 |     444 |      53.1532 |      30.8559 |      15.991  |
| not_spacified |        248 |        157 |          63 |     468 |      52.9915 |      33.547  |      13.4615 |



### Type 1, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         88 |         84 |          25 |     197 |      44.6701 |      42.6396 |     12.6904  |
| nationality | negative      | female        |         98 |         90 |          29 |     217 |      45.1613 |      41.4747 |     13.3641  |
| nationality | negative      | not_spacified |        113 |         90 |          27 |     230 |      49.1304 |      39.1304 |     11.7391  |
| ageism      | negative      | male          |         59 |         65 |          13 |     137 |      43.0657 |      47.4453 |      9.48905 |
| ageism      | negative      | female        |         69 |         51 |          14 |     134 |      51.4925 |      38.0597 |     10.4478  |
| ageism      | negative      | not_spacified |         61 |         56 |          17 |     134 |      45.5224 |      41.791  |     12.6866  |
| ableism     | negative      | male          |         44 |         45 |          13 |     102 |      43.1373 |      44.1176 |     12.7451  |
| ableism     | negative      | female        |         53 |         42 |          11 |     106 |      50      |      39.6226 |     10.3774  |
| ableism     | negative      | not_spacified |         46 |         44 |          13 |     103 |      44.6602 |      42.7184 |     12.6214  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        191 |        194 |          51 |     436 |      43.8073 |      44.4954 |      11.6972 |
| female        |        220 |        183 |          54 |     457 |      48.14   |      40.0438 |      11.8162 |
| not_spacified |        220 |        190 |          57 |     467 |      47.1092 |      40.6852 |      12.2056 |



### Type 2, Positive Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | positive      | male          |         38 |         38 |          38 |     114 |      33.3333 |      33.3333 |      33.3333 |
| nationality | positive      | female        |         43 |         39 |          33 |     115 |      37.3913 |      33.913  |      28.6957 |
| nationality | positive      | not_spacified |         37 |         42 |          36 |     115 |      32.1739 |      36.5217 |      31.3043 |
| ageism      | positive      | male          |         37 |         59 |         120 |     216 |      17.1296 |      27.3148 |      55.5556 |
| ageism      | positive      | female        |         53 |         26 |         137 |     216 |      24.537  |      12.037  |      63.4259 |
| ageism      | positive      | not_spacified |         58 |         38 |         120 |     216 |      26.8519 |      17.5926 |      55.5556 |
| ableism     | positive      | male          |         22 |         11 |          21 |      54 |      40.7407 |      20.3704 |      38.8889 |
| ableism     | positive      | female        |         27 |         12 |          16 |      55 |      49.0909 |      21.8182 |      29.0909 |
| ableism     | positive      | not_spacified |         14 |         15 |          23 |      52 |      26.9231 |      28.8462 |      44.2308 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         97 |        108 |         179 |     384 |      25.2604 |      28.125  |      46.6146 |
| female        |        123 |         77 |         186 |     386 |      31.8653 |      19.9482 |      48.1865 |
| not_spacified |        109 |         95 |         179 |     383 |      28.4595 |      24.8042 |      46.7363 |



### Type 2, Negative Attribute

| bias_type   | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| nationality | negative      | male          |         32 |         58 |          32 |     122 |      26.2295 |      47.541  |      26.2295 |
| nationality | negative      | female        |         37 |         55 |          30 |     122 |      30.3279 |      45.082  |      24.5902 |
| nationality | negative      | not_spacified |         35 |         53 |          30 |     118 |      29.661  |      44.9153 |      25.4237 |
| ageism      | negative      | male          |         60 |         45 |         111 |     216 |      27.7778 |      20.8333 |      51.3889 |
| ageism      | negative      | female        |         70 |         31 |         115 |     216 |      32.4074 |      14.3519 |      53.2407 |
| ageism      | negative      | not_spacified |         57 |         43 |         116 |     216 |      26.3889 |      19.9074 |      53.7037 |
| ableism     | negative      | male          |         26 |         19 |          19 |      64 |      40.625  |      29.6875 |      29.6875 |
| ableism     | negative      | female        |         17 |         22 |          21 |      60 |      28.3333 |      36.6667 |      35      |
| ableism     | negative      | not_spacified |          9 |         22 |          30 |      61 |      14.7541 |      36.0656 |      49.1803 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        118 |        122 |         162 |     402 |      29.3532 |      30.3483 |      40.2985 |
| female        |        124 |        108 |         166 |     398 |      31.1558 |      27.1357 |      41.7085 |
| not_spacified |        101 |        118 |         176 |     395 |      25.5696 |      29.8734 |      44.557  |



## Kendall Tau Calculation

Total data: 2714

Kendall's Tau Correlation for type 1: 0.08414514873884642

P-Value: 2.940113820777725e-05

Total data: 2348

Kendall's Tau Correlation for type 2: 0.03327925611416001

P-Value: 0.1340149175843971

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 2714

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.02385689204534038

P-Value: 0.14679003742646546

Total data: 2348

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.047391269963345514

P-Value: 0.008974474222165586

