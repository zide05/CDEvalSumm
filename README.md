# CDEvalSumm: Cross-Dataset Evaluation for Summarization

Descriptions and metrics code for EMNLP2020 findings paper: *[CDEvalSumm: An Empirical Study of Cross-Dataset Evaluation for Neural Summarization Systems]()*<br>
([Yiran Chen](https://scholar.google.com/citations?hl=zh-CN&user=ZEnShlcAAAAJ), [Pengfei Liu](https://scholar.google.com/citations?hl=zh-CN&user=oIz_CYEAAAAJ), [Ming Zhong](https://scholar.google.com/citations?hl=zh-CN&user=mnifqeUAAAAJ), [Zi-Yi Dou](https://scholar.google.com/citations?hl=zh-CN&user=RWogNsEAAAAJ), [Danqing Wang](https://scholar.google.com/citations?hl=zh-CN&user=mAo_lUwAAAAJ), [Xipeng Qiu](https://scholar.google.com/citations?hl=zh-CN&user=Pq4Yp_kAAAAJ), [Xuanjing Huang](https://scholar.google.com/citations?hl=zh-CN&user=RGsMgZA4H78C))

## Motivation
Many work evaluate summarization systems on in-domain setting (the model is trained and tested on the same dataset). In this work we try to understand model performance on different perspectives on a cross-dataset setting. The picture blow represents the main motivation (summarization systems get different rankings when evaluated under different measures where abstractive models are red while extractive ones are blue): <br><br>

<img src="https://github.com/zide05/CompSUM/blob/master/figs/ranking6.png" width="300" height="180">



## Two Research Questions
**Q1**: How do different neural architectures of summarizers influence the cross-dataset generalization performances?<br>
**Q2**: Do different generation ways (extractive and abstractive) of summarizers influence the cross-dataset generalization ability?

## Datasets and Summarization Systems
+ Datasets
  - [CNN/Dailymail](https://arxiv.org/pdf/1602.06023.pdf)
  - [Xsum](https://arxiv.org/pdf/1808.08745.pdf)
  - [Pubmed](https://arxiv.org/pdf/1804.05685.pdf)
  - [Bigpatent B](https://arxiv.org/pdf/1906.03741.pdf)
  - [Reddit TIFU](https://arxiv.org/pdf/1811.00783.pdf)
+ Summarization systems (definition of model names can refer to the paper)
  - Extractive summarizers: <img src="https://render.githubusercontent.com/render/math?math=LSTM_{non}, Trans_{non}, Trans_{auto}, BERT_{non}, BERT_{match}">
  <!--$LSTM_{non}$ , $Trans_{non}$ , $Trans_{auto}$ , $BERT_{non}$ , $BERT_{match}$-->
  
  - Abstractive summarizers: <img src="https://render.githubusercontent.com/render/math?math=L2L_{ptr}^{cov}, L2L_{ptr}, L2L, T2T, BE2T, BART">
  <!--$L2L_{ptr}^{cov}$ , $L2L_{ptr}$ , $L2L$ , $T2T$ , $BE2T$ , $BART$-->
   

## Evaluation Metrics
+ Semantic Equivalenc (ROUGE)
+ Factuality ([Factcc](https://arxiv.org/pdf/1910.12840.pdf)) 
+ Dataset bias (Detailed explanation is displayed in our paper and the code can refer to Data-bias-metrics/)
  + [Coverage](https://arxiv.org/pdf/1804.11283.pdf) 
  + Copy length
  + [Novelty](https://arxiv.org/pdf/1704.04368.pdf)
  + [Repetition](https://arxiv.org/pdf/1704.04368.pdf)
  + [Sentence fusion score](https://arxiv.org/pdf/1906.00077.pdf) 
  

## Cross-dataset Measures
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
<div align="center"><img src="https://github.com/zide05/CompSUM/blob/master/figs/rouge_all.PNG" width="310" height="330">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<img src="https://github.com/zide05/CompSUM/blob/master/figs/factcc_all.PNG" width="320" height="330"></div>


