from services import google_vision, chat_gpt


def test_google_vision(url):
    api = google_vision.Service()
    text = api.detect_text(url)
    print('TEXT:', text)
    labels = api.detect_labels(url)
    print('LABELS:', labels)
    color = api.detect_color(url)
    print('COLOR RGB:', color)


def test_chat_gpt():
    question = 'Em uma palavra, qual a capital do Rio Grande do Norte?'
    api = chat_gpt.Service()
    answer = api.prompt(question)
    print('R:', answer)


if __name__ == '__main__':
    url = 'https://autolivraria.com.br/bc/wp-content/uploads/2012/11/VW-Fusca-01.jpg'
    test_google_vision(url)
    test_chat_gpt()
