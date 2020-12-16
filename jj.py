def my_jj(Search_url, AuthorName):
    from bs4 import BeautifulSoup as bs
    import requests

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'}

    main_link = 'https://elements.envato.com'


    #response = requests.get('https://elements.envato.com/ru/audio/royalty-free-music/sort-by-latest',
    #                        headers=headers).text
    response = requests.get(Search_url,
                            headers=headers).text
    flag_next = 1
    count = 1
    NumPages = 70
    link = Search_url
    flag_found = False
    while flag_next == 1 and count < NumPages:
        #print(count)
        soup = bs(response, 'lxml')
        music_block = soup.find('div', {'class': '_2c8GJ3US'})
        music_list = music_block.find(text = AuthorName)
        if music_list != None:
            flag_found = True
            flag_next = 0
            break

        next_button = soup.find_all('a', {'_1F8DxBMF _1bmT0Vum'})
        if len(next_button) == 1 and count != 1:
            flag_next = 0
        else:
            if count == 1:
                link = main_link + next_button[0]['href']
            else:
                link = main_link + next_button[1]['href']
            response = requests.get(link, headers=headers).text
            count += 1
    if flag_found:
        return f'Вы на {str(count)} странице:', link
    else:
        link = ''
        return  f'Сожалеем, но ваш трек не найден на {count}-ти страницах. Попробуйте перепроверить названия:)', link


def my_jj_elements(Search_url, AuthorName):
    from bs4 import BeautifulSoup as bs
    import requests

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'}

    main_link = 'https://elements.envato.com'


    #response = requests.get('https://elements.envato.com/ru/audio/royalty-free-music/sort-by-latest',
    #                        headers=headers).text
    response = requests.get(Search_url,
                            headers=headers).text
    flag_next = 1
    count = 1
    while flag_next == 1 and count < 100:
        soup = bs(response, 'lxml')
        music_block = soup.find('div', {'class': '_2c8GJ3US'})
        music_list = music_block.find_all('li', {'class': '_1NHmrvFY _3NeDmW0y _3uoIZdEh'})
        for music_item in music_list:
            music_name = music_item.find('a', {'class': '_29UGUgqJ'}).text
            if music_name == 'GoodIdeaProduction':
                flag_next = 0
                break
        if flag_next == 0:
            break
        next_button = soup.find_all('a', {'_1F8DxBMF _1bmT0Vum'})
        if len(next_button) == 1 and count != 1:
            flag_next = 0
        else:
            if count == 1:
                link = main_link + next_button[0]['href']
            else:
                link = main_link + next_button[1]['href']
            response = requests.get(link, headers=headers).text
            count += 1

    return f'Вы на {str(count)} странице'



def my_jj_jungle(Search_url, AuthorName, TrackName):

    from bs4 import BeautifulSoup as bs
    import requests

    NumPages = 70
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'}

    main_link = 'https://audiojungle.net'

    # response = requests.get('https://elements.envato.com/ru/audio/royalty-free-music/sort-by-latest',
    #                        headers=headers).text

    flag_next = 1
    count = 1
    link= Search_url

    Search_url = Search_url.strip()
    AuthorName = AuthorName.strip()
    TrackName = TrackName.strip()


    if Search_url=='':
        return f'Не задан адрес страницы с поиском', link
    if AuthorName=='':
        return f'Не заполнено название автора', link
    if TrackName=='':
        return f'Не заполнено название трека', link


    try:
        response = requests.get(Search_url, headers=headers).text


        while flag_next == 1 and count < NumPages:

            soup = bs(response, 'lxml')
            music_block = soup.find('div', {'class': "page"})
            music_list = music_block.find_all('li', {'class': '_1cn3x'})

            for music_item in music_list:
                music_name = music_item.find('a', {'class': 'R8zaM'}).text
                music_name = music_name.strip()
                if music_name.upper() == AuthorName.upper():
                    song_name = music_item.find('a', {'class': '_2Pk9X'}).text
                    song_name = song_name.strip()
                    if song_name.upper() == TrackName.upper():
                        flag_next = 0
                        break


            next_button = soup.find_all('a', {'data-test-selector': 'paginationNext'})
            if flag_next == 0:
                break
            if len(next_button) == 0:
                flag_next = 0
            else:
                link = main_link + next_button[0]['href']
                response = requests.get(link, headers=headers).text
                count += 1
        if len(next_button) == 0:
            link=''
            return f'Сожалеем, но ваш трек не найден на {count}-ти страницах. Попробуйте перепроверить названия:)', link
        else:
            return f'Вы на {str(count)}-й странице:', link
    except:
        link = ''
        return f'Что-то пошло не так, возможно неверный URL поиска', link




