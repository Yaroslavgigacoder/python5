import datetime
def log_cash (reshim):
    with open ('homework7\log.txt', 'a', encoding='utf-8') as file:
        file.write(f'Тип операции:{reshim}. Время операции: {str(datetime.datetime.now())}\n')
