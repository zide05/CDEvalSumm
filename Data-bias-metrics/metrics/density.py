import argparse
import os
import json
import numpy as np

DOMAIN = 'arxiv'

from metrics.fragment import Fragments


def density(source_sents, target_sents):
    density = []
    coverage = []
    compression = []
    copy_len = []
    for text_sents, summary_sents in zip(source_sents, target_sents):
        fragment = Fragments("\n".join(summary_sents), " ".join(text_sents))
        density.append(fragment.density())
        coverage.append(fragment.coverage())
        compression.append(fragment.compression())
        copy_len.append(0 if len(fragment.copy_len()) == 0 else sum(fragment.copy_len()) / len(fragment.copy_len()))
    return density, coverage, compression, copy_len
