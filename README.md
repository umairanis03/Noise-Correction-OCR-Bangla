# Bangla OCR Correction

#### Project aim:
- Correcting OCR output on Bangla language

### Workflow:
1. Creating Bangla Corpus
2. Pre-processing corpus, converting articles to lines
3. Convert text-lines to Images
4. Running OCR on these Images
5. Calculating Word Error Rate of OCR output using ground truth text-lines

## Project tree

 * [seq2seq_OCR_Correction](./tree-md)
 * [OCR](./dir2)
   * [ReadMe.md](./dir2/file21.ext)
   * [ocr_paralell.py](./dir2/file22.ext)
 * [Preprocessing](./dir1)
   * [preprocessing.py](./dir1/file11.ext)
   * [preprocessing_2.py](./dir1/file12.ext)
 * [Text2Images-Pillow](./file_in_root.ext)
 * [README.md](./README.md)
 * [OCR_Evaluation](./dir3)
     * [compare.py]()

## Preparing Text Dataset
- Bangla Text corpus not availaible
- Wikipedia Article Scrapped for corpus preparation
- Find Scrapped Corpus [here](https://github.com/Rajan-sust/WikiTextCorpusDownloader/blob/master/bn_corpus.zip)
- 

## Conversion Text2Images


## Using pytesseract to convert images2text


## Spell Checker for correcting noisy output for OCR

## Relevant Link to blogs/repositories
