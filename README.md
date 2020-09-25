# CompSum

Descriptions and metrics code for EMNLP2020 findings paper: *[An Empirical Study of Cross-Dataset Evaluation for Neural Summarization Systems]()*

### Motivation
Many work evaluate summarization systems on in-domain setting (the model is trained and tested on the same dataset). In this work we try to understand model performance on different perspectives on a cross-dataset setting. The picture blow represents the main motivation (summarization systems get different rankings when evaluated under different measures)<br><br>
<img src="https://github.com/zide05/CompSUM/blob/master/figs/model_ranking.PNG" width="300" height="330">


### Two questions to explore
**Q1**: How do different neural architectures of summarizers influence the cross-dataset generalization performances?<br>
**Q2**: Do different generation ways (extractive and abstractive) of summarizers influence the cross-dataset generalization ability?

### Datasets and summarization systems
+ Datasets
  - [CNN/Dailymail](https://arxiv.org/pdf/1602.06023.pdf)
  - [Xsum](https://arxiv.org/pdf/1808.08745.pdf)
  - [Pubmed](https://arxiv.org/pdf/1804.05685.pdf)
  - [Bigpatent B](https://arxiv.org/pdf/1906.03741.pdf)
  - [Reddit TIFU](https://arxiv.org/pdf/1811.00783.pdf)
+ Summarization systems (definition of model names can refer to the paper)
  - Extractive summarizers
   $LSTM_{non}$ , $Trans_{non}$ , $Trans_{auto}$ , $BERT_{non}$ , $BERT_{match}$ 
  
  - Abstractive summarizers
   $L2L_{ptr}^{cov}$ , $L2L_{ptr}$ , $L2L$ , $T2T$ , $BE2T$ , $BART$ 
   

### Evaluation metrics
+ Semantic Equivalenc (ROUGE)
+ Factuality ([Factcc](https://arxiv.org/pdf/1910.12840.pdf)) 
+ Dataset bias (Detailed explanation is displayed in our paper and the code can refer to Data-bias-metrics/)
  + [Coverage](https://arxiv.org/pdf/1804.11283.pdf) 
  + Copy length
  + [Novelty](https://arxiv.org/pdf/1704.04368.pdf)
  + [Repetition](https://arxiv.org/pdf/1704.04368.pdf)
  + [Sentence fusion score](https://arxiv.org/pdf/1906.00077.pdf) 
  

### Cross-dataset measures
+ Stiffness 
  <br><br>
  <img src="https://render.githubusercontent.com/render/math?math=r^{\mu} = \frac{1}{N\times N}\sum_{i,j} {\mathbf{U}}_{ij}"> <br>
  <img src="https://render.githubusercontent.com/render/math?math={\mathbf{U}}_{ij}"> : the metric score when model is trained on dataset i and tested on dataset j.
+ Stableness  
  <br>
  <img src="https://render.githubusercontent.com/render/math?math=r^{\sigma} = \frac{1}{N\times N}\sum_{i,j} \mathbf{U}_{ij}/ \mathbf{U}_{jj}\times100 \%25"> <br>
  <img src="https://render.githubusercontent.com/render/math?math={\mathbf{U}}_{ij}"> : the metric score when model is trained on dataset i and tested on dataset j.

## Experiment Results
The stiffness and stableness of various summarizers are displayed below. For fine-grained results and comprehensive analysis please refer to the paper.
<div align="center"><img src="https://github.com/zide05/CompSUM/blob/master/figs/ROUGE_stiff_stable.PNG" width="300" height="330">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<img src="https://github.com/zide05/CompSUM/blob/master/figs/factcc_stiff_stable.PNG" width="300" height="330"></div>


