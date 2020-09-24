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
  | $LSTM_{non}$ | $Trans_{non}$ | $Trans_{auto}$ | $BERT_{non}$ | $BERT_{match}$ |
  | ------ | ------ | ------ | ------ | ------ | ------ |
  | $L2L_{ptr}^{cov}$ | $L2L_{ptr}$ | $L2L$ | $T2T$ | $BE2T$ | $BART$ |
     
  - Abstractive summarizers
    

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

