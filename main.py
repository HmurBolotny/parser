import class_web_processor
import class_text_processor
import class_collections_processor

HABRURL = 'https://habr.com/ru/post/547472/'
HABRTAG = {'title', 'span', 'p'}


def main():
    date = class_web_processor.ClientWeb(HABRURL)
    text = class_text_processor.TextHandler(date.get_date(), HABRTAG)
    freq = class_collections_processor.Frequency(text.get_words())
    freq.get_frequency(3)
    freq.print()


if __name__ == '__main__':
    main()

