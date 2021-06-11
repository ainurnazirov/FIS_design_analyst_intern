-- Запрос, который возвращает самого популярного писателя за год
SELECT
library_author.last_name, library_author.first_name, library_author.patronymic, count_by_author.count_id
FROM
  (SELECT
   COUNT(library_book_issue.id) AS count_id,
   library_book.id_author_id AS id_author

   FROM library_book_issue
   INNER JOIN library_book ON library_book.id = library_book_issue.id_book_id
   WHERE library_book_issue.issue_date > DATE('now', '-1 year')
   GROUP BY library_book.id_author_id) AS count_by_author

INNER JOIN library_author ON library_author.id = count_by_author.id_author
ORDER BY count_by_author.count_id DESC LIMIT 1
