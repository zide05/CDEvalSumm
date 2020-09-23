# CompSum

Descriptions and metrics code for EMNLP2020 findings paper: *[An Empirical Study of Cross-Dataset Evaluation for Neural Summarization Systems]()*

### Two questions to explore
**Q1**: How do different neural architectures of summarizers influence the cross-dataset generalization performances?<br>
**Q2**: Do different generation ways (extractive and abstractive) of summarizers influence the cross-dataset generalization ability?

### Datasets and summarization systems
+ Datasets
  - CNN/Dailymail
  - Xsum
  - Pubmed
  - Bigpatent B
  - Reddit TIFU
+ Summarization systems
  - Extractive summarizers
    1. $$LSTM_{non}$$
    2. $Trans_{non}$![Trans_{non}](http://www.sciweavers.org/tex2img.php?eq=1%2Bsin%28mc%5E2%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)
    3. $Trans_{auto}$
    4. $BERT_{non}$
    5. $BERT_{match}$
  - Abstractive summarizers
    1. $L2L_{ptr}^{cov}$
    2. $L2L_{ptr}$
    3. $L2L$
    4. $T2T$
    5. $BE2T$
    6. $BART$

### Evaluation metrics
+ Semantic Equivalenc (ROUGE)
+ Factuality (Factcc)
+ Dataset bias (Detailed explanation is displayed in our paper and the code can refer to xxx)
  + Coverage
  + Copy length
  + Novelty
  + Sentence fusion score
  + Repetition

### Cross-dataset measures
+ Stiffness
+ Stableness

## Experiment Results

