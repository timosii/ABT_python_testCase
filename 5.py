import os
import re 
import time
import multiprocessing

def task1():
    # в папке test найти все файлы filenames вывести количество
    test_path = os.path.join(os.getcwd(), 'test')
    result = os.walk(test_path)
    files_count = 0
    for _, _, files in result:
        for file in files:
            if 'filenames' in file:
                files_count += 1
    print(files_count)



def find_emails(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        emails = re.findall(email_pattern, text)
        return emails

def task2():
    # в папке test найти все email адреса записанные в файлы
    start = time.time()
    test_path = os.path.join(os.getcwd(), 'test')
    emails = []
    for root, _, files in os.walk(test_path):
        for file in files:
            file_path = os.path.join(root, file)
            emails_in_file = find_emails(file_path)
            emails.extend(emails_in_file)
    
    elapsed_time = time.time() - start
    print(emails, elapsed_time)


def task2_parallel():
    start = time.time()
    test_path = os.path.join(os.getcwd(), 'test')
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    files = []
    for root, _, file_list in os.walk(test_path):
        for file in file_list:
            file_path = os.path.join(root, file)
            files.append(file_path)
    results = pool.map(find_emails, files)
    all_emails = [email for emails in results for email in emails]
    elapsed_time = time.time() - start
    print(all_emails, elapsed_time)

def main():
    task1()
    task2()
    task2_parallel()
    # дополнительно: придумать над механизмом оптимизации 2-й задачи (параллелизация)
    # реализовал параллельную функцию, но время её выполнения больше, чем последовательной т.к. при последовательном выполнении для каждого файла при однократном проходе сразу вызывается функция find_emails, а при параллельном сначала формируется список файлов, а затем для него параллельно проводится поиск, что более ресурсозатратно


if __name__ == '__main__':
    main()
