import logging
import re

from TTS.tts.utils.text.akan.phonemizer import aka_text_to_phonemes, _DEF_AKA_PUNCS
from TTS.tts.utils.text.phonemizers.base import BasePhonemizer

logger = logging.getLogger(__name__)


class AKA_Phonemizer(BasePhonemizer):
    """🐸TTS bn phonemizer using functions in `TTS.tts.utils.text.bangla.phonemizer`

    Args:
        punctuations (str):
            Set of characters to be treated as punctuation. Defaults to `_DEF_ZH_PUNCS`.

        keep_puncs (bool):
            If True, keep the punctuations after phonemization. Defaults to False.

    Example ::

        

    TODO: someone with Bangla knowledge should check this implementation
    """

    language = "aka"

    def __init__(self, punctuations=_DEF_AKA_PUNCS, keep_puncs=False, **kwargs):  # pylint: disable=unused-argument
        super().__init__(self.language, punctuations=punctuations, keep_puncs=keep_puncs)

    @staticmethod
    def name():
        return "aka_phonemizer"

    @staticmethod
    def phonemize_aka(text: str, separator: str = "|") -> str:  # pylint: disable=unused-argument
        ph_list = aka_text_to_phonemes(text)
        print("ph_list: ")
        print(ph_list)
        ph_words = [separator.join(word_phonemes) for word_phonemes in ph_list]
        ph = f"{separator} ".join(ph_words)

        return ph

    def _phonemize(self, text, separator):
        return self.phonemize_aka(text, separator)

    @staticmethod
    def supported_languages() -> dict:
        return {"aka": "Akan"}

    def version(self) -> str:
        return "0.0.1"

    def is_available(self) -> bool:
        return True

