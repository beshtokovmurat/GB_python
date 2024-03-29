main_menu = '''\nГлавное меню:
		1. Открыть записную книгу • 
		2. Сохранить данное состояние записной книги •
		3. Показать все заметки •
		4. Добавить заметку в записную книгу •
		5. Найти заметку •
		6. Изменить заметку •
		7. Удалить заметку •
		8. Выход •\n '''

input_choice = 'Выберите пункт меню: '
note_file_name = 'note.txt'

load_successful = 'Записная книга успешно открыта'
save_successful = 'Записная книга успешно сохранена'

load_error = 'Записная книга пустая или она не прочитана'

input_new_note = 'Введите новую запись (заметку): '
new_notes = {'title': 'Введите заголовок заметки: ',
               'note': 'Введите текст заметки: '}

def new_note_successful(title: str):
		return f'Заметка {title} успешно добавлена.'

cancel_input = 'Отмена ввода'

index_del_note = 'Введите индекс (номер) заметки, которую хотите удалить: '
def del_note(title: str):
		return f'Заметка {title} успешно удалёна!'

input_change = 'Введите индекс (номер) заметки, которую хотите изменить: '
input_index = 'Введите индекс (номер) заметки: '

change_note = 'Введите новые данные или оставьте поле пустым, чтобы не менять: '

def change_successful(title: str | dict) -> str:
    return f'Заметка {title} успешно изменена!'

input_search = 'Введите индекс (номер) заметки, которую хотите найти: '
def empty_search(word) -> str:
    return f'Заметки содержащие слово "{word}" не найдены!'