# Data-bias-metrics
Data bias metrics:

* Novelty
* Repetition
* Coverage
* Copy length
* Sentence fusion score 

Calling get_metrics in all_metrics.py to calculate the scores, the input of get_metrics are document samples list and prediction samples list, every sample has to be one list of sentences.

```python
from all_metrics import get_metrics

doc_samples = [["marseille , france -lrb- cnn -rrb- the french prosecutor leading an investigation into the crash of germanwings flight 9525 insisted wednesday that he was not aware of any video footage from on board the plane .", "marseille prosecutor brice robin told cnn that `` so far no videos were used in the crash investigation . ''"]]
pred_samples = [["marseille prosecutor says `` so far no videos were used in the crash investigation '' despite media reports .", "journalists at bild and paris match are `` very confident '' the video clip is real , an editor says .", "andreas lubitz had informed his lufthansa training school of an episode of severe depression , airline says ."]]

print(get_metrics(doc_samples, pred_samples))
```

The [code](https://github.com/Alex-Fabbri/Multi-News) of Coverage (metrics/fragment.py) is from passage [Multi-News: a Large-Scale Multi-Document Summarization Dataset and Abstractive Hierarchical Model](https://arxiv.org/pdf/1906.01749.pdf).

We change the [code](https://github.com/ucfnlp/summarization-sing-pair-mix) of sentence fusion (metrics/ssi_functions.py and metrics/sent_fusion.py) (from passage: [Scoring Sentence Singletons and Pairs for Abstractive Summarization](https://arxiv.org/pdf/1906.00077.pdf).) partly to get the sentence fusion score. 

