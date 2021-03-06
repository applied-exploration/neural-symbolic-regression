from typing import Counter, List
from torchtext.vocab import Vocab
from torch.nn.utils.rnn import pad_sequence
import torch.nn.functional as F
import torch

def build_vocab(data: List[str]) -> Vocab:
    counter = Counter(data)
    return Vocab(counter, specials=['<pad>', '<bos>', '<eos>'])

def one_hot_encode_program(tokens: List[str], vocab: Vocab) -> torch.Tensor:
    indices = [vocab.stoi[str(t)] for t in tokens]
    return F.one_hot(torch.LongTensor(indices), len(vocab))

def one_hot_decode_program(tensor: torch.Tensor, vocab: Vocab) -> List[str]:
    indices = tensor.argmax(dim=-1)
    return [vocab.itos[i] for i in indices]

# PAD_IDX = de_vocab['<pad>']
# BOS_IDX = de_vocab['<bos>']
# EOS_IDX = de_vocab['<eos>']

# def generate_batch(data_batch):
#   de_batch, en_batch = [], []
#   for (de_item, en_item) in data_batch:
#     de_batch.append(torch.cat([torch.tensor([BOS_IDX]), de_item, torch.tensor([EOS_IDX])], dim=0))
#     en_batch.append(torch.cat([torch.tensor([BOS_IDX]), en_item, torch.tensor([EOS_IDX])], dim=0))
#   de_batch = pad_sequence(de_batch, padding_value=PAD_IDX)
#   en_batch = pad_sequence(en_batch, padding_value=PAD_IDX)
#   return de_batch, en_batch



# raw_de_iter = iter(io.open(filepaths[0], encoding="utf8"))
# raw_en_iter = iter(io.open(filepaths[1], encoding="utf8"))
# data = []
# for (raw_de, raw_en) in zip(raw_de_iter, raw_en_iter):
#     de_tensor_ = torch.tensor([de_vocab[token] for token in de_tokenizer(raw_de)],
#                             dtype=torch.long)
#     en_tensor_ = torch.tensor([en_vocab[token] for token in en_tokenizer(raw_en)],
#                             dtype=torch.long)
#     data.append((de_tensor_, en_tensor_))
# return data