import torch
import numpy as np
from torch.utils.data import Dataset
from pathlib import Path

class EncodingDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

    
def get_stopwords():



    '''
    :return: a set of 266 stop words from nltk. eg. {'someone', 'anyhow', 'almost', 'none', 'mostly', 'around', 'being', 'fifteen', 'moreover', 'whoever', 'further', 'not', 'side', 'keep', 'does', 'regarding', 'until', 'across', 'during', 'nothing', 'of', 'we', 'eleven', 'say', 'between', 'upon', 'whole', 'in', 'nowhere', 'show', 'forty', 'hers', 'may', 'who', 'onto', 'amount', 'you', 'yours', 'his', 'than', 'it', 'last', 'up', 'ca', 'should', 'hereafter', 'others', 'would', 'an', 'all', 'if', 'otherwise', 'somehow', 'due', 'my', 'as', 'since', 'they', 'therein', 'together', 'hereupon', 'go', 'throughout', 'well', 'first', 'thence', 'yet', 'were', 'neither', 'too', 'whether', 'call', 'a', 'without', 'anyway', 'me', 'made', 'the', 'whom', 'but', 'and', 'nor', 'although', 'nine', 'whose', 'becomes', 'everywhere', 'front', 'thereby', 'both', 'will', 'move', 'every', 'whence', 'used', 'therefore', 'anyone', 'into', 'meanwhile', 'perhaps', 'became', 'same', 'something', 'very', 'where', 'besides', 'own', 'whereby', 'whither', 'quite', 'wherever', 'why', 'latter', 'down', 'she', 'sometimes', 'about', 'sometime', 'eight', 'ever', 'towards', 'however', 'noone', 'three', 'top', 'can', 'or', 'did', 'seemed', 'that', 'because', 'please', 'whereafter', 'mine', 'one', 'us', 'within', 'themselves', 'only', 'must', 'whereas', 'namely', 'really', 'yourselves', 'against', 'thus', 'thru', 'over', 'some', 'four', 'her', 'just', 'two', 'whenever', 'seeming', 'five', 'him', 'using', 'while', 'already', 'alone', 'been', 'done', 'is', 'our', 'rather', 'afterwards', 'for', 'back', 'third', 'himself', 'put', 'there', 'under', 'hereby', 'among', 'anywhere', 'at', 'twelve', 'was', 'more', 'doing', 'become', 'name', 'see', 'cannot', 'once', 'thereafter', 'ours', 'part', 'below', 'various', 'next', 'herein', 'also', 'above', 'beside', 'another', 'had', 'has', 'to', 'could', 'least', 'though', 'your', 'ten', 'many', 'other', 'from', 'get', 'which', 'with', 'latterly', 'now', 'never', 'most', 'so', 'yourself', 'amongst', 'whatever', 'whereupon', 'their', 'serious', 'make', 'seem', 'often', 'on', 'seems', 'any', 'hence', 'herself', 'myself', 'be', 'either', 'somewhere', 'before', 'twenty', 'here', 'beyond', 'this', 'else', 'nevertheless', 'its', 'he', 'except', 'when', 'again', 'thereupon', 'after', 'through', 'ourselves', 'along', 'former', 'give', 'enough', 'them', 'behind', 'itself', 'wherein', 'always', 'such', 'several', 'these', 'everyone', 'toward', 'have', 'nobody', 'elsewhere', 'empty', 'few', 'six', 'formerly', 'do', 'no', 'then', 'unless', 'what', 'how', 'even', 'i', 'indeed', 'still', 'might', 'off', 'those', 'via', 'fifty', 'each', 'out', 'less', 're', 'take', 'by', 'hundred', 'much', 'anything', 'becoming', 'am', 'everything', 'per', 'full', 'sixty', 'are', 'bottom', 'beforehand'}
    '''
    stop_words = ['a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'ain', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'am', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'aren', "aren't", 'around', 'as', 'at', 'back', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'both',  'but', 'by', 'can', 'cannot', 'could', 'couldn', "couldn't", 'd', 'didn', "didn't", 'doesn', "doesn't", 'don', "don't", 'down', 'due', 'during', 'either', 'else', 'elsewhere', 'empty', 'enough', 'even', 'ever', 'everyone', 'everything', 'everywhere', 'except',  'first', 'for', 'former', 'formerly', 'from', 'hadn', "hadn't",  'hasn', "hasn't",  'haven', "haven't", 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i', 'if', 'in', 'indeed', 'into', 'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'latter', 'latterly', 'least', 'll', 'may', 'me', 'meanwhile', 'mightn', "mightn't", 'mine', 'more', 'moreover', 'most', 'mostly',  'must', 'mustn', "mustn't", 'my', 'myself', 'namely', 'needn', "needn't", 'neither', 'never', 'nevertheless', 'next', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'o', 'of', 'off', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'per', 'please','s', 'same', 'shan', "shan't", 'she', "she's", "should've", 'shouldn', "shouldn't", 'somehow', 'something', 'sometime', 'somewhere', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they','this', 'those', 'through', 'throughout', 'thru', 'thus', 'to', 'too','toward', 'towards', 'under', 'unless', 'until', 'up', 'upon', 'used',  've', 'was', 'wasn', "wasn't", 'we',  'were', 'weren', "weren't", 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'with', 'within', 'without', 'won', "won't", 'would', 'wouldn', "wouldn't", 'y', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']
    stop_words = set(stop_words)
    return stop_words


def read_imdb_split(split_dir):
    split_dir = Path(split_dir)
    texts = []
    labels = []
    for label_dir in ["pos", "neg"]:
        for text_file in (split_dir/label_dir).iterdir():
            texts.append(text_file.read_text())
            labels.append(0 if label_dir == "neg" else 1)

    return texts, labels