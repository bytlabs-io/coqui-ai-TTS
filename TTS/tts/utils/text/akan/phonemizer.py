import re
from transformers import T5ForConditionalGeneration, AutoTokenizer

from .number_norm import normalize_numbers

# initialize

def _transformer_phonemize(text: str):
    model = T5ForConditionalGeneration.from_pretrained('fiifinketia/akan-g2p')
    tokenizer = AutoTokenizer.from_pretrained('fiifinketia/akan-g2p')

    words = ['<aka>: '+text]

    out = tokenizer(words,padding=True,add_special_tokens=False,return_tensors='pt')

    preds = model.generate(**out,num_beams=1,max_length=50) # We do not find beam search helpful. Greedy decoding is enough. 
    phones = tokenizer.batch_decode(preds.tolist(),skip_special_tokens=True)
    return phones


def collapse_whitespace(text):
    # Regular expression matching whitespace:
    _whitespace_re = re.compile(r"\s+")
    return re.sub(_whitespace_re, " ", text)


def aka_text_to_phonemes(text: str) -> str:
    # english numbers to akan conversion
    res = re.search("[0-9]", text)
    if res is not None:
        text = normalize_numbers(text)

    # create tuple of (lang,text)
    if "" in text:
        text = text.replace("", "").replace("", "")
    # Split based on sentence ending Characters
    aka_text = text.strip()

    aka_text = _transformer_phonemize(aka_text)
    aka_text = collapse_whitespace(aka_text)

    return aka_text


