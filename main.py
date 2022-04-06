from habr_parser import pars


def main():
    pars('https://habr.com/ru/post/547472/',{'title', 'span', 'p'})


if __name__ == '__main__':
    main()

