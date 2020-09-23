import numpy as np
from metrics import ssi_functions
import os
from metrics import util
from tqdm import tqdm
import glob
import multiprocessing as mp
import sys
import json
import datetime
import shutil
from metrics.utils.utils import ranstr


np.random.seed(123)

FLAGS = {"dataset_name": "cnn_dm", "sentence_limit": 3, "top_n_sents": -1, "num_instances": -1, "min_matched_tokens": 2,
         "abstract_idx": 0}


def process_one_example(example):
    raw_article_sents, groundtruth_summ_sents, example_idx, pretty_html_path, out_full_dir = example
    article_sent_tokens = [util.process_sent(sent, whitespace=True) for sent in raw_article_sents]
    doc_indices = None
    if doc_indices is None or (FLAGS['dataset_name'] != 'duc_2004' and len(doc_indices) != len(
            util.flatten_list_of_lists(article_sent_tokens))):
        doc_indices = [0] * len(util.flatten_list_of_lists(article_sent_tokens))
    doc_indices = [int(doc_idx) for doc_idx in doc_indices]
    summary_sent_tokens = [util.process_sent(sent, whitespace=True) for sent in groundtruth_summ_sents]

    writer = open(os.path.join(out_full_dir, '%06d_ssi.tsv' % example_idx), 'wb')

    if len(article_sent_tokens) == 0:
        print('Skipping because empty')
        writer.write('\n'.encode(encoding='utf-8'))
        return

    ''' This is the main function that finds the article sentences that were fused to create the given summary sentence'''
    simple_similar_source_indices, lcs_paths_list, smooth_article_paths_list = ssi_functions.get_simple_source_indices_list(
        summary_sent_tokens, article_sent_tokens, vocab=None,
        sentence_limit=FLAGS['sentence_limit'], min_matched_tokens=FLAGS['min_matched_tokens'])

    highlight_line = '\t'.join([','.join([str(src_idx) for src_idx in source_indices]) for source_indices in
                                simple_similar_source_indices]) + '\n'
    writer.write(highlight_line.encode())

    # if example_idx < 1:
    #     f_pretty_html = open(pretty_html_path, 'wb')
    # extracted_sents_in_article_html = ssi_functions.html_highlight_sents_in_article(summary_sent_tokens,
    #                                                                                 simple_similar_source_indices,
    #                                                                                 article_sent_tokens,
    #                                                                                 doc_indices,
    #                                                                                 lcs_paths_list,
    #                                                                                 smooth_article_paths_list)
    # f_pretty_html.write(extracted_sents_in_article_html.encode())


def create_example_list(source_sents, target_sents, pretty_html_path, out_full_dir, total):
    ex_list = []
    for example_idx in tqdm(range(total)):
        if FLAGS['num_instances'] != -1 and example_idx >= FLAGS['num_instances']:
            break
        src = source_sents[example_idx]  # text
        tgt = target_sents[example_idx]  # summary

        raw_article_sents = src
        groundtruth_summ_sents = tgt

        example = (raw_article_sents, groundtruth_summ_sents, example_idx, pretty_html_path, out_full_dir)
        ex_list.append(example)
    return ex_list


def sent_fusion(source_sents, target_sents):
    # if len(unused_argv) != 1:  # prints a message if you've entered flags incorrectly
    #     raise Exception("Problem with flags: %s" % unused_argv)
    result = []
    total = len(source_sents)

    save_path = "./sentence_fusion"
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    time1 = datetime.datetime.now()
    name = datetime.datetime.strftime(time1, '%Y-%m-%d %H:%M:%S')
    name = name + "_" + ranstr(6)

    out_full_dir = os.path.join(save_path, name + '_temp_highlight')
    pretty_html_path = os.path.join(save_path, name + '_pretty_html.html')

    # util.create_dirs(os.path.dirname(pretty_html_path))
    util.create_dirs(out_full_dir)
    # f_pretty_html = open(pretty_html_path, 'wb')

    ex_list = create_example_list(source_sents, target_sents, pretty_html_path, out_full_dir, total)

    pool = mp.Pool(mp.cpu_count())
    _ = list(tqdm(pool.imap(process_one_example, ex_list), total=total))
    pool.close()

    # f_pretty_html.close()
    file_list = sorted(glob.glob(os.path.join(out_full_dir, '*')))
    for file_name in tqdm(file_list):
        with open(file_name) as f_single_file_hl:
            highlights = f_single_file_hl.read()
        result.append(highlights.encode())

    # os.removedirs(out_full_dir)
    shutil.rmtree(out_full_dir)
    # os.remove(pretty_html_path)
    return result


def funsion_score(data):
    result = [0, 0, 0, 0]

    for line in data:
        line = line.decode()
        line = line.strip("\n")
        line = line.split("\t")
        num_sent = len(line)
        for sent in line:
            result[len(sent.split(","))] += 1
    fusion_score1 = (result[2] + result[3]) / (result[1] + result[2] + result[3])
    return fusion_score1

