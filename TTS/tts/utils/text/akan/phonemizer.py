import re
from transformers import T5ForConditionalGeneration, AutoTokenizer

from TTS.tts.utils.text.phonemizers.akan_phonemizer import _DEF_AKA_PUNCS

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



def aka_text_to_phonemes(text: str) -> str:
    sentenceEnders = re.compile("!'(),-.:;?’")
    sentences = sentenceEnders.split(str(text))
    ph = ""
    for sentence in sentences:
        words = sentence.split(" ")
        for word in words:
            aka_text = _transformer_phonemize(word)
            aka_text+=" "
            ph+=aka_text
    print("phone sentence: "+ph)
    return ph


