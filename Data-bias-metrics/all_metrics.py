from metrics.density import density as Density
from metrics.novelty_repetition_unk import novelty as Novelty
from metrics.novelty_repetition_unk import repetition as Repetition
from metrics.sent_fusion import sent_fusion, funsion_score
from metrics.Len import getlen as Getlen


def list_minus(a, b):
    return [tmpa - tmpb for tmpa, tmpb in zip(a, b)]


def get_avg(res):
    result = {}
    for key, value in res.items():
        if isinstance(value, list):
            result[key] = sum(value) / len(value)
        else:
            result[key] = value
    return result


def get_metrics(raws, preds):
    '''
    :param raws: every sample of raws are list of source document sentences
    :param preds: every sample of preds are list of model prediction sentences
    :return:
    '''
    result = {}

    # save len
    result['pred_len'] = Getlen(preds)
    print('length done!')

    # save density coverage compression copylen
    result['pred_density'], result['pred_coverage'], result['pred_compression'], result['pred_copylen'] = Density(raws,
                                                                                                                  preds)
    print('density coverage compression copylen done!')

    # save novlty repetition
    result['pred_novelty1'] = Novelty(raws, preds, 1)
    result['pred_novelty2'] = Novelty(raws, preds, 2)
    result['pred_novelty3'] = Novelty(raws, preds, 3)
    result['pred_novelty4'] = Novelty(raws, preds, 4)
    result['pred_noveltysent'] = Novelty(raws, preds, -1)

    result['pred_repetition1'] = Repetition(preds, 1)
    result['pred_repetition2'] = Repetition(preds, 2)
    result['pred_repetition3'] = Repetition(preds, 3)
    result['pred_repetition4'] = Repetition(preds, 4)
    result['pred_repetitionsent'] = Repetition(preds, -1)
    print('novelty repetition done!')

    # save sentence fusion
    result['pred_fusion'] = funsion_score(sent_fusion(raws, preds))

    result = get_avg(result)
    print("get metrics done!")

    return result


# print(get_metrics([["marseille , france -lrb- cnn -rrb- the french prosecutor leading an investigation into the crash of germanwings flight 9525 insisted wednesday that he was not aware of any video footage from on board the plane .", "marseille prosecutor brice robin told cnn that `` so far no videos were used in the crash investigation . ''", "he added , `` a person who has such a video needs to immediately give it to the investigators . ''", "robin 's comments follow claims by two magazines , german daily bild and french paris match , of a cell phone video showing the harrowing final seconds from on board germanwings flight 9525 as it crashed into the french alps . all 150 on board were killed .", "paris match and bild reported that the video was recovered from a phone at the wreckage site ."]],[["marseille prosecutor says `` so far no videos were used in the crash investigation '' despite media reports .", "journalists at bild and paris match are `` very confident '' the video clip is real , an editor says .", "andreas lubitz had informed his lufthansa training school of an episode of severe depression , airline says ."]]))
