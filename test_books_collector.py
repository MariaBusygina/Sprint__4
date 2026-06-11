import pytest


class TestBooksCollector:

    # Добавление новой книги
    def test_add_new_book(self, collector):
        collector.add_new_book('Ребекка')

        assert 'Ребекка' in collector.books_genre

    # У новой книги жанр пустой
    def test_new_book_has_empty_genre(self, collector):
        collector.add_new_book('Ребекка')

        assert collector.get_book_genre('Ребекка') == ''

    # Книга длиннее 40 символов не добавляется
    def test_add_new_book_with_long_name(self, collector):
        collector.add_new_book('А' * 41)

        assert len(collector.books_genre) == 0

    # Повторно книга не добавляется
    def test_add_duplicate_book(self, collector):
        collector.add_new_book('Ребекка')
        collector.add_new_book('Ребекка')

        assert len(collector.books_genre) == 1

    # Установка жанра
    @pytest.mark.parametrize(
        'genre',
        ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    )
    def test_set_book_genre(self, collector, genre):
        collector.add_new_book('Тестовая книга')

        collector.set_book_genre('Тестовая книга', genre)

        assert collector.get_book_genre('Тестовая книга') == genre

    # Нельзя установить несуществующий жанр
    def test_set_invalid_genre(self, collector):
        collector.add_new_book('Ребекка')

        collector.set_book_genre('Ребекка', 'Роман')

        assert collector.get_book_genre('Ребекка') == ''

    # Проверка метода get_book_genre
    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book('Ребекка')
        collector.set_book_genre('Ребекка', 'Комедии')

        assert collector.get_book_genre('Ребекка') == 'Комедии'

    # Получение книг определённого жанра
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Солярис']

    # Проверка метода get_books_genre
    def test_get_books_genre_returns_dictionary(self, collector):
        collector.add_new_book('Ребекка')

        expected = {'Ребекка': ''}

        assert collector.get_books_genre() == expected

    # Книги с возрастным рейтингом не попадают в детские
    @pytest.mark.parametrize(
        'genre',
        ['Ужасы', 'Детективы']
    )
    def test_books_with_age_rating_not_for_children(self, collector, genre):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', genre)

        assert 'Оно' not in collector.get_books_for_children()

    # Добавление книги в избранное
    def test_add_book_to_favorites(self, collector):
        collector.add_new_book('Ребекка')

        collector.add_book_in_favorites('Ребекка')

        assert 'Ребекка' in collector.get_list_of_favorites_books()

    # Книга не добавляется в избранное дважды
    def test_add_book_to_favorites_only_once(self, collector):
        collector.add_new_book('Ребекка')

        collector.add_book_in_favorites('Ребекка')
        collector.add_book_in_favorites('Ребекка')

        assert len(collector.get_list_of_favorites_books()) == 1

    # Удаление книги из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Ребекка')
        collector.add_book_in_favorites('Ребекка')

        collector.delete_book_from_favorites('Ребекка')

        assert 'Ребекка' not in collector.get_list_of_favorites_books()