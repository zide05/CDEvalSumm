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
+ Summarization systems (definition of model names can be referred to the paper)
  - Extractive summarizers
   $LSTM_{non}$ , $Trans_{non}$ , $Trans_{auto}$ , $BERT_{non}$ , $BERT_{match}$ 
  
  - Abstractive summarizers
   $L2L_{ptr}^{cov}$ , $L2L_{ptr}$ , $L2L$ , $T2T$ , $BE2T$ , $BART$ 
   

### Evaluation metrics
+ Semantic Equivalenc (ROUGE)
+ Factuality (Factcc) ([Evaluating the Factual Consistency of Abstractive Text Summarization](https://arxiv.org/pdf/1910.12840.pdf))
+ Dataset bias (Detailed explanation is displayed in our paper and the code can refer to Data-bias-metrics/)
  + Coverage ([NEWSROOM: A Dataset of 1.3 Million Summaries with Diverse Extractive Strategies](https://arxiv.org/pdf/1804.11283.pdf))
  + Copy length
  + Novelty ([Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/pdf/1704.04368.pdf))
  + Repetition ([Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/pdf/1704.04368.pdf))
  + Sentence fusion score ([Scoring Sentence Singletons and Pairs for Abstractive Summarization](https://arxiv.org/pdf/1906.00077.pdf))
  

### Cross-dataset measures
+ Stiffness
+ Stableness

## Experiment Results

