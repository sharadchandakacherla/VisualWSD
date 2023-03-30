# bert_encoder.py
#
# Created by Vaibhav Bhargava on 20-03-2023
# 
# Copyright © 2023 Vaibhav Bhargava
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import torch.nn as nn
from transformers import BertModel


class BERTEncoder(nn.Module):
    def __init__(self, embedding_dim: int, model_path: str, tokenizer_len):
        super(BERTEncoder, self).__init__()

        self.bert_model = BertModel.from_pretrained(model_path)
        self.bert_model.resize_token_embeddings(tokenizer_len)
        in_dim = list(self.bert_model.modules())[-2].weight.shape[0]
        self.embedding_dim = nn.Linear(in_dim, embedding_dim)

    def forward(self, x):
        x = self.bert_model(x)
        x = self.embedding_dim(x)
        return x
